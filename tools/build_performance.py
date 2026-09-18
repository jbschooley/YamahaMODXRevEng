#!/usr/bin/env python3
"""Build a MONTAGE M / MODX M performance (.pfm and/or .syx) from a high-level JSON spec.

Usage:
  build_performance.py spec.json out.pfm            # plugin file (install with install.py)
  build_performance.py spec.json out.syx            # bulk dump for hardware (edit buffer)
  build_performance.py --dump-spec <file.pfm>       # print a spec-like view of an existing performance

Every part starts from the factory init template of its engine (Init Normal AWM2 / FM-X / AN-X / Init
Drum, shipped inside the ESP plugin bundle), so anything the spec does not mention keeps Yamaha's
init values. Values are the raw Data List values (see data/midi_param_tables.json: "desc" gives the
printed range, "default" the init) except where a helper accepts names:

  effect types      by name from data/effect_types.json   ("REV-X HALL", "VCM EQ 501", "TEMPO CROSS DELAY")
  controller source by name/short name from data/control_sources.json   ("Modulation Wheel", "AsgnKnob 1")
  controller dest   by name/short name from data/control_destinations.json ("Cutoff", "E.LFO PMD")
  waveforms         by exact name from data/waveforms.json ("Fat Saw St")
  arpeggios         by exact name from data/arpeggio_types.json
  notes             "C-2".."G8" (C3 = 60)
  categories        main/sub names from data/performance_categories.json

Spec (all keys optional except parts[].engine):
{
  "name": "My Sound", "category": ["Bass", "Synth"], "tempo": 120,
  "reverb":    {"type": "REV-X HALL", "params": {1: 40}},      # params keyed by effect parameter number
  "variation": {"type": "TEMPO CROSS DELAY", "params": {...}},
  "master_fx": {"type": "MULTI BAND COMP", "on": true, "params": {...}},
  "common": {"c1": {"Arpeggio Master Switch": 1}, "c2": {...}},   # raw block overrides by table key
  "superknob": {"knob_names": ["Cutoff", ...], "links": [1,1,0,0,0,0,0,0]},
  "parts": [{
    "engine": "AN-X" | "AWM2" | "FM-X" | "Drum",
    "name": "Bass", "category": ["Bass", "Synth"],
    "volume": 100, "pan": 64, "note_range": ["C-2", "G8"], "velocity_range": [1, 127],
    "mono": true, "legato": false, "portamento": {"switch": 1, "time": 20, "mode": 0},
    "keyboard_control": true, "reverb_send": 20, "variation_send": 0, "dry_level": 127,
    "ins_a": {"type": "VCM EQ 501", "params": {...}}, "ins_b": {...}, "ins_connect": 1,
    "controllers": [{"source": "Modulation Wheel", "dest": "Cutoff", "ratio": 32,
                     "polarity": 0, "curve": 0, "curve_p1": 5}],
    "arp": {"switch": 1, "hold": 2, "numbers": [7501, 0, 0, 0, 0, 0, 0, 0], "names": ["MA_..."]},
    "params": {"p1": {...}, "p2": {...}, "p3": {...}, "lfo": {...}, "arp": {...}},   # raw overrides
    "scenes": {"1": {"Keyboard Control Switch": 0}, "2": {"Keyboard Control Switch": 1}},   # per-scene part values
    # engine specific
    "anx": {"common": {...}, "osc": [{...},{...},{...}], "osc_sw": [{...}], "filter": [{...},{...}], "fold": {...}},
    "fmx": {"common": {...}, "filter": {...}, "op": [{...} x8], "op_sw": [{...} x8]},
    "elements": [{"wave": "Fat Saw St", "e1": {...}, "osc": {...}, "amp": {...}, "pitch": {...}, "filter": {...}}],
    "drum_keys": {"C1": {"wave": "...", ...}}
  }]
}
"""
import copy
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pfm  # noqa: E402
import syx  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data")
FACTORY = ("/Library/Audio/Plug-Ins/Components/Expanded Softsynth Plugin for MONTAGE M.component"
           "/Contents/Resources/contents/performance")
TEMPLATE = {"AN-X": "3F277B", "AWM2": "3F277C", "FM-X": "3F277D", "DRUM": "3F277E", "Drum": "3F277E"}
ENGINE_NUM = {"AWM2": 0, "DRUM": 1, "Drum": 1, "FM-X": 2, "AN-X": 3}
NOTE_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]


def _json(name):
    return json.load(open(os.path.join(DATA, name)))


class Names:
    """Name -> number lookups from the extracted Data List tables (lazy)."""

    def __init__(self):
        self._fx = self._src = self._dst = self._wave = self._arp = self._cat = None

    def effect(self, v):
        if isinstance(v, int):
            return v
        if self._fx is None:
            self._fx = {}
            for r in _json("effect_types.json")["effect_types"]:
                self._fx[r["name"].upper()] = r["type_number"]
                self._fx[r["short_name"].upper()] = r["type_number"]
        return _lookup(self._fx, v.upper(), "effect type")

    def source(self, v):
        if isinstance(v, int):
            return v
        if self._src is None:
            self._src = {}
            for r in _json("control_sources.json")["sources"]:
                if r.get("name"):
                    self._src[r["name"].lower()] = r["number"]
                if r.get("short_name"):
                    self._src[r["short_name"].lower()] = r["number"]
        return _lookup(self._src, v.lower(), "controller source")

    ENGINE_COL = {"AWM2": "awm_normal", "DRUM": "awm_drum", "Drum": "awm_drum", "FM-X": "fmx", "AN-X": "anx", None: "common_audio"}
    ENGINE_CAT = {"AWM2": "AWM", "DRUM": "AWM", "Drum": "AWM", "FM-X": "FM", "AN-X": "AN-X"}

    def dest(self, v, engine=None):
        """Destination number. Short names like "Cutoff" exist once per engine section, so the part's
        engine picks the right one (AWM 85 / FM-X 100 / AN-X 142); engine=None means a Common/AD box."""
        if isinstance(v, int):
            return v
        if self._dst is None:
            self._dst = {}
            for r in _json("control_destinations.json")["tables"]["controller_box_destination"]["entries"]:
                for key in (r.get("name"), r.get("short_name")):
                    if key:
                        self._dst.setdefault(key.lower(), []).append(r)
        cands = _lookup(self._dst, v.lower(), "controller destination")
        col = self.ENGINE_COL.get(engine, "common_audio")
        ok = [r for r in cands if r["available"].get(col)]
        cat = self.ENGINE_CAT.get(engine)
        if cat:
            pref = [r for r in ok if (r.get("category") or "").startswith(cat)]
            if pref:
                ok = pref
        if not ok:
            raise KeyError(f"destination {v!r} is not available for a {engine or 'Common/AD'} controller box")
        return ok[0]["number"]

    def wave(self, v):
        if isinstance(v, int):
            return v
        if self._wave is None:
            self._wave = {w["name"].lower(): w["number"] for w in _json("waveforms.json")["waveforms"]}
        return _lookup(self._wave, v.lower(), "waveform")

    def arp(self, v):
        if isinstance(v, int):
            return v
        if self._arp is None:
            self._arp = {}
            for a in _json("arpeggio_types.json")["arpeggio_types"]:
                self._arp.setdefault(a["name"].lower(), a["number"])
        return _lookup(self._arp, v.lower(), "arpeggio")

    def category(self, main, sub=None):
        if self._cat is None:
            self._cat = _json("performance_categories.json")["main_categories"]
        if isinstance(main, int):
            return main, (sub or 0)
        m = next(c for c in self._cat if c["name"].lower() == main.lower())
        s = 0
        if sub is not None:
            if isinstance(sub, int):
                s = sub
            else:
                s = next(x["number"] for x in m["sub_categories"] if x["name"].lower() == sub.lower())
        return m["number"], s


def _lookup(table, key, what):
    try:
        return table[key]
    except KeyError:
        import difflib
        near = difflib.get_close_matches(key, table.keys(), n=6, cutoff=0.5)
        raise KeyError(f"unknown {what} {key!r}; close matches: {near}") from None


NAMES = Names()


def note(v):
    """'C3' -> 60 (Yamaha convention: C3 = middle C = 60, range C-2..G8)."""
    if isinstance(v, int):
        return v
    m = re.fullmatch(r"([A-G])(#?)(-?\d)", v.strip())
    if not m:
        raise ValueError(f"bad note {v!r}")
    n = NOTE_NAMES.index(m.group(1) + m.group(2))
    return (int(m.group(3)) + 2) * 12 + n


def load_template(engine):
    path = os.path.join(FACTORY, TEMPLATE[engine] + "-Performance.pfm")
    return pfm.read_performance(open(path, "rb").read())


def setp(block, base, values):
    """Return block bytes with the given {key: value} applied (keys as in data/midi_param_tables.json)."""
    if not values:
        return block
    tables = pfm.load_tables()
    keys = {p["key"] for p in tables[base]["params"]}
    for k in values:
        if k not in keys:
            raise KeyError(f"{k!r} is not a parameter of table {base} ({tables[base]['section']})")
    return pfm.encode_block(values, base, len(block), template=block)


def set_string(size, text):
    return text.encode("latin1")[:size - 1].ljust(size - 1) + b"\0"


_FX_DEFAULTS = None


def effect_defaults(type_number):
    global _FX_DEFAULTS
    if _FX_DEFAULTS is None:
        _FX_DEFAULTS = _json("effect_defaults.json")["defaults"]
    return _FX_DEFAULTS.get(str(type_number))


def apply_effect(block, base, spec, prefix):
    """spec = {"type": name|int, "preset": n, "params": {1: v, ...}}. Setting a type first loads the
    factory-typical parameter vector for that type (data/effect_defaults.json), then applies params."""
    if not spec:
        return block
    vals = {}
    if "type" in spec:
        t = NAMES.effect(spec["type"])
        vals[f"{prefix} Type"] = t
        d = effect_defaults(t)
        if d:
            keys = {p["key"] for p in pfm.load_tables()[base]["params"]}
            for i, v in enumerate(d["params"], 1):
                if f"{prefix} Parameter {i}" in keys:
                    vals[f"{prefix} Parameter {i}"] = v
            if f"{prefix} Preset Number" in keys:
                vals[f"{prefix} Preset Number"] = d["preset"]
    if "preset" in spec:
        vals[f"{prefix} Preset Number"] = spec["preset"]
    for n, v in (spec.get("params") or {}).items():
        vals[f"{prefix} Parameter {int(n)}"] = v
    return setp(block, base, vals)


def build_controller(template_block, c, engine=None):
    """Controller box from {"source", "dest", "ratio" (-128..+127, default +32), "polarity" (0 uni/1 bi),
    "curve" (0-31 preset type), "curve_p1", "curve_p2"}. Ratio raw = display + 128 (Data List: range
    00 00–01 7F printed as −128 – +127, default 01 40 = +64)."""
    vals = {"Controller Set Switch": 1,
            "Controller Set Source": NAMES.source(c["source"]),
            "Controller Set Destination": NAMES.dest(c["dest"], engine),
            "Controller Set Ratio": c.get("ratio", 32) + 128,
            "Controller Set Polarity": c.get("polarity", 0),
            "Controller Set Curve Type": c.get("curve", 0),
            "Controller Set Curve Parameter 1": c.get("curve_p1", 5),
            "Controller Set Curve Parameter 2": c.get("curve_p2", 0)}
    return setp(template_block, pfm.TABLE_OF["part.ctrlbox"], vals)


def build_part(spec, part_index):
    engine = spec["engine"]
    tpl = load_template(engine)
    part = tpl["parts"][0]
    T = pfm.TABLE_OF
    part["engine"] = ENGINE_NUM[engine]
    part["name"] = set_string(21, spec.get("name", f"Part {part_index + 1}"))
    p1, p2, p3 = {}, {}, {}
    p1["Part Switch"] = 1
    p1["Keyboard Control Switch"] = 1 if spec.get("keyboard_control", part_index < 8) else 0
    if "mono" in spec:
        p1["Mono/Poly Mode"] = 0 if spec["mono"] else 1
    if "legato" in spec:
        p1["Key Assign Mode"] = 0 if spec["legato"] else 1  # 0 Single (legato-capable), 1 Multi
    if "portamento" in spec:
        po = spec["portamento"]
        if "switch" in po:
            p1["Portamento Switch"] = po["switch"]
        if "time" in po:
            p3["Portamento Time"] = po["time"]
        if "mode" in po:
            p3["Portamento Mode"] = po["mode"]
    if "arp" in spec and "switch" in spec["arp"]:
        p1["Part Arp Switch"] = spec["arp"]["switch"]
    if "category" in spec:
        m, s = NAMES.category(*spec["category"]) if isinstance(spec["category"], (list, tuple)) else NAMES.category(spec["category"])
        p2["Part Main Category"], p2["Part Sub Category"] = m, s
    if "volume" in spec:
        p2["Volume"] = spec["volume"]
    if "pan" in spec:
        p2["Pan"] = spec["pan"]
    if "note_range" in spec:
        p2["Note Limit Low"], p2["Note Limit High"] = note(spec["note_range"][0]), note(spec["note_range"][1])
    if "velocity_range" in spec:
        p2["Velocity Limit Low"], p2["Velocity Limit High"] = spec["velocity_range"]
    for key, name in (("reverb_send", "Reverb Send"), ("variation_send", "Variation Send"), ("dry_level", "Dry Level")):
        if key in spec:
            p2[name] = spec[key]
    if "ins_connect" in spec:
        p3["Insertion Connection Type"] = spec["ins_connect"]
    raw = spec.get("params", {})
    p1.update(raw.get("p1", {}))
    p2.update(raw.get("p2", {}))
    p3.update(raw.get("p3", {}))
    part["p1"] = setp(part["p1"], T["part.p1"], p1)
    part["p2"] = setp(part["p2"], T["part.p2"], p2)
    part["p3"] = setp(part["p3"], T["part.p3"], p3)
    for k in ("arp", "lfo", "zone", "keyctrl"):
        if k in raw:
            part[k] = setp(part[k], T["part." + k], raw[k])
    if "arp" in spec:
        a = dict(spec["arp"])
        vals = {}
        if "hold" in a:
            vals["Arp Hold"] = a["hold"]
        nums = a.get("numbers") or [NAMES.arp(n) if n else 0 for n in a.get("names", [])]
        for i, n in enumerate(nums[:8]):
            vals[f"Arp {i + 1} Number"] = n
        for k, v in a.items():
            if k.startswith("Arp "):
                vals[k] = v
        part["arp"] = setp(part["arp"], T["part.arp"], vals)
    part["ins"][0] = apply_effect(part["ins"][0], T["part.ins.0"], spec.get("ins_a"), "Insertion-A")
    part["ins"][1] = apply_effect(part["ins"][1], T["part.ins.1"], spec.get("ins_b"), "Insertion-B")
    if "controllers" in spec:
        boxes = part["ctrlbox"]
        # switch every template box off, then fill from the spec
        boxes = [setp(b, T["part.ctrlbox"], {"Controller Set Switch": 0}) for b in boxes]
        for i, c in enumerate(spec["controllers"][:32]):
            boxes[i] = build_controller(boxes[i], c, engine)
        part["ctrlbox"] = boxes
    if "knob_names" in spec:
        for i, n in enumerate(spec["knob_names"][:8]):
            part["knobnames"][i] = set_string(17, n)
    for idx, vals in (spec.get("scenes") or {}).items():  # {"1": {"Keyboard Control Switch": 0, ...}} (1-based)
        i = int(idx) - 1
        part["scenes"][i] = setp(part["scenes"][i], T["part.scenes"], vals)
    # engine data
    if engine == "AN-X":
        a = part["anx"]
        s = spec.get("anx", {})
        a["common"] = setp(a["common"], T["anx.common"], s.get("common"))
        for i in range(3):
            if i < len(s.get("osc", [])):
                a["osc"][i]["osc"] = setp(a["osc"][i]["osc"], T["anx.osc"], s["osc"][i])
            if i < len(s.get("osc_sw", [])):
                a["osc"][i]["sw"] = setp(a["osc"][i]["sw"], T["anx.oscsw"], s["osc_sw"][i])
        for i in range(2):
            if i < len(s.get("filter", [])):
                a["filt"][i]["filt"] = setp(a["filt"][i]["filt"], T["anx.filt"], s["filter"][i])
            if i < len(s.get("filter_sw", [])):
                a["filt"][i]["sw"] = setp(a["filt"][i]["sw"], T["anx.filtsw"], s["filter_sw"][i])
        a["fold"] = setp(a["fold"], T["anx.fold"], s.get("fold"))
    elif engine == "FM-X":
        f = part["fmx"]
        s = spec.get("fmx", {})
        f["common"] = setp(f["common"], T["fmx.common"], s.get("common"))
        f["filter"] = setp(f["filter"], T["fmx.filter"], s.get("filter"))
        for i in range(8):
            if i < len(s.get("op", [])):
                f["op"][i]["op"] = setp(f["op"][i]["op"], T["fmx.op"], s["op"][i])
            if i < len(s.get("op_sw", [])):
                f["op"][i]["sw"] = setp(f["op"][i]["sw"], T["fmx.opsw"], s["op_sw"][i])
    elif engine == "AWM2":
        els = part["awm2"]["elements"]
        tpl_el = copy.deepcopy(els[0])
        specs = spec.get("elements")
        if specs is not None:
            new = []
            for i, es in enumerate(specs):
                e = copy.deepcopy(els[i] if i < len(els) else tpl_el)
                e1 = dict(es.get("e1", {}))
                e1.setdefault("Element Switch", 1)
                osc = dict(es.get("osc", {}))
                if "wave" in es:
                    osc["Wave Select"] = 0
                    osc["Wave Number"] = NAMES.wave(es["wave"])
                if "note_range" in es:
                    osc["Note Limit Low"], osc["Note Limit High"] = note(es["note_range"][0]), note(es["note_range"][1])
                if "velocity_range" in es:
                    osc["Velocity Limit Low"], osc["Velocity Limit High"] = es["velocity_range"]
                e["e1"] = setp(e["e1"], T["el.e1"], e1)
                e["osc"] = setp(e["osc"], T["el.osc"], osc)
                for k in ("amp", "pitch", "filter"):
                    e[k] = setp(e[k], T["el." + k], es.get(k))
                new.append(e)
            # the template has 8 elements; keep the remaining ones switched off
            for e in els[len(new):8]:
                e = copy.deepcopy(e)
                e["e1"] = setp(e["e1"], T["el.e1"], {"Element Switch": 0})
                new.append(e)
            part["awm2"]["elements"] = new
    elif engine in ("DRUM", "Drum"):
        keys = part["drum"]["keys"]
        for kname, ks in (spec.get("drum_keys") or {}).items():
            k = note(kname) - note("C0")
            vals = dict(ks)
            if "wave" in vals:
                vals["Wave Select"] = 0
                vals["Wave Number"] = NAMES.wave(vals.pop("wave"))
            keys[k] = setp(keys[k], T["drum.key"], vals)
    return part, tpl


def build(spec):
    parts, tpls = [], []
    for i, ps in enumerate(spec["parts"]):
        p, t = build_part(ps, i)
        parts.append(p)
        tpls.append(t)
    perf = tpls[0]
    perf["parts"] = parts
    T = pfm.TABLE_OF
    c = perf["common"]
    c["name"] = set_string(21, spec.get("name", "New Performance"))
    c2 = {}
    if "category" in spec:
        m, s = NAMES.category(*spec["category"]) if isinstance(spec["category"], (list, tuple)) else NAMES.category(spec["category"])
        c2["Performance Main Category"], c2["Performance Sub Category"] = m, s
    if "tempo" in spec:
        c2["Tempo"] = spec["tempo"]
    c1 = {}
    if "master_fx" in spec and "on" in spec["master_fx"]:
        c1["Master Effect Switch"] = 1 if spec["master_fx"]["on"] else 0
    if any("arp" in p and p["arp"].get("switch") for p in spec["parts"]):
        c1.setdefault("Arpeggio Master Switch", 1)
    raw = spec.get("common", {})
    c1.update(raw.get("c1", {}))
    c2.update(raw.get("c2", {}))
    c["c1"] = setp(c["c1"], T["common.c1"], c1)
    c["c2"] = setp(c["c2"], T["common.c2"], c2)
    for k in ("ctrl", "arp", "meq", "msq", "superknob", "sklane"):
        if k in raw:
            c[k] = setp(c[k], T["common." + k], raw[k])
    c["reverb"] = apply_effect(c["reverb"], T["common.reverb"], spec.get("reverb"), "Reverb")
    c["variation"] = apply_effect(c["variation"], T["common.variation"], spec.get("variation"), "Variation")
    c["mfx"] = apply_effect(c["mfx"], T["common.mfx"], spec.get("master_fx"), "Master Effect")
    sk = spec.get("superknob", {})
    if "knob_names" in sk:
        for i, n in enumerate(sk["knob_names"][:8]):
            c["knobnames"][i] = set_string(17, n)
    if "links" in sk:
        c["c1"] = setp(c["c1"], T["common.c1"], {f"Assignable Knob{i + 1} Link Switch": v for i, v in enumerate(sk["links"][:8])})
    for idx, vals in (spec.get("scenes") or {}).items():  # {"1": {"s1": {...}, "s2": {...}}} (1-based)
        i = int(idx) - 1
        if "s1" in vals:
            c["scenes"][i]["s1"] = setp(c["scenes"][i]["s1"], T["common.scenes.s1"], vals["s1"])
        if "s2" in vals:
            c["scenes"][i]["s2"] = setp(c["scenes"][i]["s2"], T["common.scenes.s2"], vals["s2"])
    if "controllers" in spec:
        boxes = [setp(b, T["common.ctrlbox"], {"Controller Set Switch": 0}) for b in c["ctrlbox"]]
        for i, cs in enumerate(spec["controllers"][:32]):
            vals = {"Controller Set Switch": 1, "Controller Set Source": NAMES.source(cs["source"]),
                    "Controller Set Destination": NAMES.dest(cs["dest"]),
                    "Controller Set Ratio": cs.get("ratio", 32) + 128, "Controller Set Polarity": cs.get("polarity", 0),
                    "Controller Set Curve Type": cs.get("curve", 0), "Controller Set Curve Parameter 1": cs.get("curve_p1", 5)}
            boxes[i] = setp(boxes[i], T["common.ctrlbox"], vals)
        c["ctrlbox"] = boxes
    perf["tail"] = b""
    return perf


def main():
    if sys.argv[1] == "--dump-spec":
        perf = pfm.decode_performance(pfm.read_performance(open(sys.argv[2], "rb").read()))
        print(json.dumps(perf, indent=1))
        return
    spec = json.load(open(sys.argv[1]))
    perf = build(spec)
    out = sys.argv[2]
    if out.lower().endswith(".syx"):
        open(out, "wb").write(syx.performance_to_syx(perf))
    else:
        open(out, "wb").write(pfm.write_performance(perf))
    check = pfm.read_performance(pfm.write_performance(perf))
    nul = b"\0 "
    print(f"wrote {out}: {check['common']['name'][:20].rstrip(nul).decode()!r}, parts:",
          [(pfm.ENGINE[p['engine']], p['name'][:20].rstrip(nul).decode()) for p in check["parts"]])


if __name__ == "__main__":
    main()
