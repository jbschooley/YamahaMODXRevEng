#!/usr/bin/env python3
"""Reader/writer for Yamaha MONTAGE M / MODX M `.pfm` performance files (ESP plugin format).

Container format (all integers big-endian):
  * a "block" is  u32 length + raw bytes; the bytes are the same parameter block the MIDI bulk
    dump carries (see data/midi_param_tables.json), except that 2-byte parameters are stored as
    16-bit little-endian words instead of MSB/LSB 7-bit pairs, and string blocks carry one extra
    NUL byte (20-char names -> 21-byte block, 16-char knob names -> 17).
  * an "array" is  u32 count  followed by that many items (blocks or groups).
  * Part records are  u32 (always 1 so far) + u8 engine type + blocks.

Run as a script to probe/validate files:  pfm.py probe <file>   |   pfm.py validate <dir>
"""
import struct
import sys

ENGINE = {0: "AWM2", 1: "DRUM", 2: "FM-X", 3: "AN-X", 255: "EMPTY"}


class Reader:
    def __init__(self, data):
        self.d = data
        self.i = 0

    def u32(self):
        v = struct.unpack(">I", self.d[self.i:self.i + 4])[0]
        self.i += 4
        return v

    def u8(self):
        v = self.d[self.i]
        self.i += 1
        return v

    def block(self, expect=None, label=""):
        n = self.u32()
        if expect is not None and n != expect:
            raise ValueError(f"{label}: expected block of {expect} bytes, got {n} at 0x{self.i - 4:x}")
        b = self.d[self.i:self.i + n]
        self.i += n
        return b

    def array(self, fn, expect=None, label=""):
        n = self.u32()
        if expect is not None and n != expect:
            raise ValueError(f"{label}: expected array of {expect}, got {n} at 0x{self.i - 4:x}")
        return [fn(k) for k in range(n)]


# ---- layout (block sizes from the Data List "Bulk Dump Block" table, strings +1) ----
COMMON_LAYOUT = [
    ("name", 21), ("c1", 29), ("c2", 86), ("ctrl", 86),
]


def read_lane(r, label):
    return {"l1": r.block(4, label + ".l1"), "l2": r.block(20, label + ".l2"),
            "seq": r.array(lambda k: r.block(102, label + ".seq"), 8, label + ".seq")}


def read_common(r):
    c = {}
    c["name"] = r.block(21, "name")
    c["c1"] = r.block(29, "common1")
    c["c2"] = r.block(86, "common2")
    c["ctrl"] = r.block(86, "ctrl")
    c["ins"] = r.array(lambda k: r.block(52, "ad_ins"), 2, "ad_ins")
    for key, n in (("arp", 14), ("reverb", 52), ("variation", 52), ("rotary", 68), ("meq", 34),
                   ("mfx", 52), ("msq", 12), ("superknob", 90), ("ad", 42), ("usb", 14), ("sklane", 20)):
        c[key] = r.block(n, key)
    c["skseq"] = r.array(lambda k: r.block(102, "skseq"), 8, "skseq")
    c["scenes"] = r.array(lambda k: {"s1": r.block(19, "scene1"), "s2": r.block(44, "scene2")}, 8, "scenes")
    c["knobnames"] = r.array(lambda k: r.block(17, "knobname"), 8, "knobnames")
    c["ctrlbox"] = r.array(lambda k: r.block(18, "ctrlbox"), 32, "ctrlbox")
    c["lanes"] = r.array(lambda k: read_lane(r, "adlane"), 4, "adlanes")
    return c


def read_part(r, k):
    """Part record: header + the per-part blocks common to every engine (engine data follows the array)."""
    p = {}
    p["hdr"] = r.u32()
    p["engine"] = r.u8()
    p["name"] = r.block(21, "pname")
    p["p1"] = r.block(81, "part1")
    p["p2"] = r.block(94, "part2")
    p["p3"] = r.block(62, "part3")
    p["ins"] = r.array(lambda k: r.block(52, "ins"), 2, "ins")
    p["arp"] = r.block(100, "arp")
    p["lfo"] = r.block(68, "lfo")
    p["zone"] = r.block(26, "zone")
    p["keyctrl"] = r.block(64, "keyctrl")
    p["scenes"] = r.array(lambda k: r.block(80, "scene"), 8, "scenes")
    p["knobnames"] = r.array(lambda k: r.block(17, "knobname"), 8, "knobnames")
    p["ctrlbox"] = r.array(lambda k: r.block(18, "ctrlbox"), None, "ctrlbox")
    p["lanes"] = r.array(lambda k: read_lane(r, "lane"), 4, "lanes")
    return p


def read_engine(r, p):
    """Engine-specific data for one part; stored after the parts array, one section per part in order."""
    eng = p["engine"]
    p["engine_offset"] = r.i
    if eng == 3:
        p["anx"] = read_anx(r)
    elif eng == 2:
        p["fmx"] = read_fmx(r)
    elif eng == 0:
        p["awm2"] = read_awm2(r)
    elif eng == 1:
        p["drum"] = read_drum(r)
    elif eng == 255:
        pass  # "Initialized Part" placeholder in multi-part factory performances: no engine data
    else:
        raise ValueError(f"unknown engine {eng} at 0x{r.i:x}")


def read_anx(r):
    a = {"common": r.block(110, "anx.common")}
    a["osc"] = r.array(lambda k: {"sw": r.block(39, "anx.oscsw"), "osc": r.block(78, "anx.osc")}, 3, "anx.osc")
    a["filt"] = r.array(lambda k: {"sw": r.block(39, "anx.filtsw"), "filt": r.block(30, "anx.filt")}, 2, "anx.filt")
    a["fold"] = r.block(34, "anx.fold")
    return a


def read_fmx(r):
    f = {"common": r.block(82, "fmx.common"), "filter": r.block(70, "fmx.filter")}
    f["op"] = r.array(lambda k: {"sw": r.block(39, "fmx.opsw"), "op": r.block(76, "fmx.op")}, 8, "fmx.op")
    return f


def read_awm2(r):
    def elem(k):
        return {"e1": r.block(43, "el1"), "osc": r.block(40, "el.osc"), "amp": r.block(54, "el.amp"),
                "pitch": r.block(48, "el.pitch"), "filter": r.block(108, "el.filter")}
    return {"elements": r.array(elem, None, "elements")}


def read_drum(r):
    return {"keys": r.array(lambda k: r.block(64, "drumkey"), 73, "keys")}


def read_performance(data):
    r = Reader(data)
    perf = {"common": read_common(r)}
    perf["parts"] = r.array(lambda k: read_part(r, k), None, "parts")
    for p in perf["parts"]:
        read_engine(r, p)
    perf["tail_offset"] = r.i
    perf["tail"] = data[r.i:]
    return perf


# ---- named-parameter decode/encode using the Data List tables ----
import json
import os
from collections import OrderedDict

_TABLES = None
TABLE_OF = {  # block key in the parsed tree -> MIDI table base address in data/midi_param_tables.json
    "common.name": "06 00 00 00", "common.c1": "06 00 01 00", "common.c2": "06 00 02 00",
    "common.ctrl": "06 00 03 00", "common.ins.0": "06 00 04 00", "common.ins.1": "06 00 05 00",
    "common.arp": "06 00 06 00", "common.reverb": "06 00 07 00", "common.variation": "06 00 08 00",
    "common.rotary": "06 00 09 00", "common.meq": "06 00 0A 00", "common.mfx": "06 00 0B 00",
    "common.msq": "06 00 0C 00", "common.superknob": "06 00 0D 00", "common.ad": "06 00 0E 00",
    "common.usb": "06 00 0F 00", "common.sklane": "06 00 12 00", "common.skseq": "06 01 0m 00",
    "common.scenes.s1": "06 02 0c 00", "common.scenes.s2": "06 03 0c 00", "common.knobnames": "06 04 0k 00",
    "common.ctrlbox": "06 05 bb 00", "common.lanes.l1": "06 06 L0 00", "common.lanes.l2": "06 07 L0 00",
    "common.lanes.seq": "06 08 L 00",
    "part.name": "1p 00 00 00", "part.p1": "1p 00 01 00", "part.p2": "1p 00 02 00", "part.p3": "1p 00 03 00",
    "part.ins.0": "1p 00 04 00", "part.ins.1": "1p 00 05 00", "part.arp": "1p 00 06 00", "part.lfo": "1p 00 07 00",
    "part.zone": "1p 00 08 00", "part.keyctrl": "1p 00 09 00", "part.scenes": "1p 03 0c 00",
    "part.knobnames": "1p 04 0k 00", "part.ctrlbox": "1p 05 bb 00", "part.lanes.l1": "1p 06 L0 00",
    "part.lanes.l2": "1p 07 L0 00", "part.lanes.seq": "1p 08 Lm 00",
    "el.e1": "2p 00 ee 00", "el.osc": "2p 01 ee 00", "el.amp": "2p 02 ee 00", "el.pitch": "2p 03 ee 00",
    "el.filter": "2p 04 ee 00", "drum.key": "2p 10 kk 00",
    "fmx.common": "3p 00 00 00", "fmx.filter": "3p 00 01 00", "fmx.opsw": "3p 01 0o 00", "fmx.op": "3p 02 0o 00",
    "anx.common": "4p 00 00 00", "anx.oscsw": "4p 01 0o 00", "anx.osc": "4p 02 0o 00", "anx.filtsw": "4p 03 0f 00",
    "anx.filt": "4p 04 0f 00", "anx.fold": "4p 05 00 00",
}
STRING_TABLES = {"06 00 00 00", "1p 00 00 00", "06 04 0k 00", "1p 04 0k 00"}
# Effect-type parameters are stored in .pfm as (MSB << 8) | LSB, i.e. the two 7-bit sysex bytes kept
# as two 8-bit bytes (REV-X HALL "01 00" -> 0x0100 = 256). Every other 2-byte parameter is the plain
# 14-bit value (MSB*128 + LSB). decode/encode expose the 14-bit form so values match the Data List.
PAIR_PARAMS = {"Reverb Type", "Variation Type", "VCM Rotary Speaker Type", "Master Effect Type",
               "Insertion-A Type", "Insertion-B Type"}


def is_pair(p):
    return p["size"] == 2 and p["key"] in PAIR_PARAMS


def pair_to_value(raw):
    return ((raw >> 8) << 7) | (raw & 0x7F)


def value_to_pair(v):
    return ((v >> 7) << 8) | (v & 0x7F)


def load_tables(path=None):
    """Load data/midi_param_tables.json into {base: [params with unique keys]}."""
    global _TABLES
    if _TABLES is not None and path is None:
        return _TABLES
    path = path or os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "midi_param_tables.json")
    raw = json.load(open(path))
    tables = {}
    for t in raw["tables"]:
        seen = {}
        params = []
        for p in t["params"]:
            key = p["name"] or f"param_{p['offset']}"
            if key in seen:
                key = f"{key} @{p['offset']}"
            seen[key] = True
            params.append({**p, "key": key})
        tables[t["base"]] = {"section": t["section"], "params": params, "size": t["calc_size"]}
    _TABLES = tables
    return tables


def decode_block(data, base):
    """bytes -> OrderedDict(param key -> raw int) using the table for `base` (strings -> str)."""
    tables = load_tables()
    if base in STRING_TABLES:
        return data.split(b"\0")[0].decode("latin1").rstrip()
    out = OrderedDict()
    for p in tables[base]["params"]:
        o, n = p["offset"], p["size"]
        if o + n > len(data):
            break
        if n == 1:
            out[p["key"]] = data[o]
        else:
            raw = struct.unpack("<H", data[o:o + 2])[0]
            out[p["key"]] = pair_to_value(raw) if is_pair(p) else raw
    return out


def encode_block(values, base, size, template=None):
    """OrderedDict/dict -> bytes. Unspecified params keep `template` bytes (or 0)."""
    tables = load_tables()
    if base in STRING_TABLES:
        s = values.encode("latin1")[:size - 1]
        return s.ljust(size - 1) + b"\0" if size in (17, 21) else s.ljust(size, b"\0")
    buf = bytearray(template if template is not None else bytes(size))
    for p in tables[base]["params"]:
        if p["key"] not in values:
            continue
        v = int(values[p["key"]])
        o, n = p["offset"], p["size"]
        if n == 1:
            buf[o] = v & 0xFF
        else:
            buf[o:o + 2] = struct.pack("<H", (value_to_pair(v) if is_pair(p) else v) & 0xFFFF)
    return bytes(buf)


def decode_performance(perf):
    """Raw block tree -> nested dict of named values (a readable 'view'; raw bytes stay canonical)."""
    c = perf["common"]
    out = {"common": {}}
    oc = out["common"]
    for k in ("name", "c1", "c2", "ctrl", "arp", "reverb", "variation", "rotary", "meq", "mfx", "msq",
              "superknob", "ad", "usb", "sklane"):
        oc[k] = decode_block(c[k], TABLE_OF["common." + k])
    oc["ins"] = [decode_block(c["ins"][i], TABLE_OF[f"common.ins.{i}"]) for i in range(2)]
    oc["skseq"] = [decode_block(b, TABLE_OF["common.skseq"]) for b in c["skseq"]]
    oc["scenes"] = [{"s1": decode_block(sc["s1"], TABLE_OF["common.scenes.s1"]),
                     "s2": decode_block(sc["s2"], TABLE_OF["common.scenes.s2"])} for sc in c["scenes"]]
    oc["knobnames"] = [decode_block(b, TABLE_OF["common.knobnames"]) for b in c["knobnames"]]
    oc["ctrlbox"] = [decode_block(b, TABLE_OF["common.ctrlbox"]) for b in c["ctrlbox"]]
    oc["lanes"] = [{"l1": decode_block(l["l1"], TABLE_OF["common.lanes.l1"]),
                    "l2": decode_block(l["l2"], TABLE_OF["common.lanes.l2"]),
                    "seq": [decode_block(b, TABLE_OF["common.lanes.seq"]) for b in l["seq"]]} for l in c["lanes"]]
    out["parts"] = []
    for p in perf["parts"]:
        op = {"engine": ENGINE.get(p["engine"], p["engine"])}
        for k in ("name", "p1", "p2", "p3", "arp", "lfo", "zone", "keyctrl"):
            op[k] = decode_block(p[k], TABLE_OF["part." + k])
        op["ins"] = [decode_block(p["ins"][i], TABLE_OF[f"part.ins.{i}"]) for i in range(2)]
        op["scenes"] = [decode_block(b, TABLE_OF["part.scenes"]) for b in p["scenes"]]
        op["knobnames"] = [decode_block(b, TABLE_OF["part.knobnames"]) for b in p["knobnames"]]
        op["ctrlbox"] = [decode_block(b, TABLE_OF["part.ctrlbox"]) for b in p["ctrlbox"]]
        op["lanes"] = [{"l1": decode_block(l["l1"], TABLE_OF["part.lanes.l1"]),
                        "l2": decode_block(l["l2"], TABLE_OF["part.lanes.l2"]),
                        "seq": [decode_block(b, TABLE_OF["part.lanes.seq"]) for b in l["seq"]]} for l in p["lanes"]]
        if "awm2" in p:
            op["elements"] = [{k: decode_block(e[k], TABLE_OF["el." + k]) for k in ("e1", "osc", "amp", "pitch", "filter")}
                              for e in p["awm2"]["elements"]]
        if "drum" in p:
            op["keys"] = [decode_block(b, TABLE_OF["drum.key"]) for b in p["drum"]["keys"]]
        if "fmx" in p:
            f = p["fmx"]
            op["fmx"] = {"common": decode_block(f["common"], TABLE_OF["fmx.common"]),
                         "filter": decode_block(f["filter"], TABLE_OF["fmx.filter"]),
                         "op": [{"sw": decode_block(o["sw"], TABLE_OF["fmx.opsw"]),
                                 "op": decode_block(o["op"], TABLE_OF["fmx.op"])} for o in f["op"]]}
        if "anx" in p:
            a = p["anx"]
            op["anx"] = {"common": decode_block(a["common"], TABLE_OF["anx.common"]),
                         "osc": [{"sw": decode_block(o["sw"], TABLE_OF["anx.oscsw"]),
                                  "osc": decode_block(o["osc"], TABLE_OF["anx.osc"])} for o in a["osc"]],
                         "filt": [{"sw": decode_block(o["sw"], TABLE_OF["anx.filtsw"]),
                                   "filt": decode_block(o["filt"], TABLE_OF["anx.filt"])} for o in a["filt"]],
                         "fold": decode_block(a["fold"], TABLE_OF["anx.fold"])}
        out["parts"].append(op)
    return out


# ---- writer (raw block tree -> bytes) ----
def _blk(b):
    return struct.pack(">I", len(b)) + b


def _arr(items, fn):
    return struct.pack(">I", len(items)) + b"".join(fn(x) for x in items)


def _lane(l):
    return _blk(l["l1"]) + _blk(l["l2"]) + _arr(l["seq"], _blk)


def write_performance(perf):
    c = perf["common"]
    out = _blk(c["name"]) + _blk(c["c1"]) + _blk(c["c2"]) + _blk(c["ctrl"]) + _arr(c["ins"], _blk)
    for k in ("arp", "reverb", "variation", "rotary", "meq", "mfx", "msq", "superknob", "ad", "usb", "sklane"):
        out += _blk(c[k])
    out += _arr(c["skseq"], _blk)
    out += _arr(c["scenes"], lambda sc: _blk(sc["s1"]) + _blk(sc["s2"]))
    out += _arr(c["knobnames"], _blk) + _arr(c["ctrlbox"], _blk) + _arr(c["lanes"], _lane)

    def part(p):
        b = struct.pack(">I", p["hdr"]) + bytes([p["engine"]]) + _blk(p["name"]) + _blk(p["p1"]) + _blk(p["p2"]) + _blk(p["p3"])
        b += _arr(p["ins"], _blk) + _blk(p["arp"]) + _blk(p["lfo"]) + _blk(p["zone"]) + _blk(p["keyctrl"])
        b += _arr(p["scenes"], _blk) + _arr(p["knobnames"], _blk) + _arr(p["ctrlbox"], _blk) + _arr(p["lanes"], _lane)
        return b
    out += _arr(perf["parts"], part)
    for p in perf["parts"]:
        if "anx" in p:
            a = p["anx"]
            out += _blk(a["common"]) + _arr(a["osc"], lambda o: _blk(o["sw"]) + _blk(o["osc"]))
            out += _arr(a["filt"], lambda o: _blk(o["sw"]) + _blk(o["filt"])) + _blk(a["fold"])
        elif "fmx" in p:
            f = p["fmx"]
            out += _blk(f["common"]) + _blk(f["filter"]) + _arr(f["op"], lambda o: _blk(o["sw"]) + _blk(o["op"]))
        elif "awm2" in p:
            out += _arr(p["awm2"]["elements"], lambda e: b"".join(_blk(e[k]) for k in ("e1", "osc", "amp", "pitch", "filter")))
        elif "drum" in p:
            out += _arr(p["drum"]["keys"], _blk)
    return out + perf.get("tail", b"")


def probe_chain(data, i, n=40):
    """Heuristic dump of u32-prefixed chain from offset i (for exploring unknown regions)."""
    out = []
    for _ in range(n):
        if i + 4 > len(data):
            out.append("EOF")
            break
        v = struct.unpack(">I", data[i:i + 4])[0]
        if 4 < v < 4096 and i + 4 + v <= len(data):
            out.append(f"B{v}")
            i += 4 + v
        elif v <= 256:
            out.append(f"[{v}]")
            i += 4
        else:
            out.append(f"??{v:x}@{i:x}")
            break
    return " ".join(out)


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "probe":
        data = open(sys.argv[2], "rb").read()
        try:
            perf = read_performance(data)
            print("parsed OK; parts:", [(ENGINE.get(p["engine"]), p["name"][:20].rstrip(b"\0 ")) for p in perf["parts"]],
                  "tail bytes:", len(perf["tail"]), perf["tail"][:64].hex(" "))
        except Exception as e:
            print("ERROR:", e)
            import re
            m = re.search(r"0x([0-9a-f]+)", str(e))
            if m:
                off = int(m.group(1), 16)
                print("chain from there:", probe_chain(data, off))
    elif cmd == "roundtrip":
        import glob, os
        files = sorted(glob.glob(os.path.join(sys.argv[2], "*.pfm")))
        bad = 0
        for f in files:
            data = open(f, "rb").read()
            if write_performance(read_performance(data)) != data:
                bad += 1
                print("MISMATCH", os.path.basename(f))
        print(f"{len(files) - bad}/{len(files)} byte-exact round trips")
    elif cmd == "dump":
        perf = decode_performance(read_performance(open(sys.argv[2], "rb").read()))
        print(json.dumps(perf, indent=1))
    elif cmd == "validate":
        import glob, os
        files = sorted(glob.glob(os.path.join(sys.argv[2], "*.pfm")))
        ok = 0
        errs = {}
        for f in files:
            data = open(f, "rb").read()
            try:
                perf = read_performance(data)
                if perf["tail"]:
                    errs.setdefault("tail:" + str(len(perf["tail"])), []).append(f)
                else:
                    ok += 1
            except Exception as e:
                errs.setdefault(str(e).split(" at ")[0], []).append(f)
        print(f"{ok}/{len(files)} parsed with no tail")
        for k, v in sorted(errs.items(), key=lambda kv: -len(kv[1]))[:15]:
            print(f"  {len(v):5d}  {k}   e.g. {os.path.basename(v[0])}")
