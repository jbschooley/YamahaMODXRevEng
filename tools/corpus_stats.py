#!/usr/bin/env python3
"""Decode every performance in one or more directories and print sound-design statistics.

Usage: corpus_stats.py <dir> [<dir>...] [--json out.json]

Output covers: engine/part-count usage, category mix, effect type usage per slot, AWM2 element
counts/filters/waveform categories, FM-X algorithms, AN-X oscillator/filter choices, and the
controller-box (mod matrix) source→destination pairs that factory sounds use most.
"""
import glob
import json
import os
import sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pfm  # noqa: E402

DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")


def load_json(name):
    return json.load(open(os.path.join(DATA, name)))


def effect_names():
    return {r["type_number"]: r["name"] for r in load_json("effect_types.json")["effect_types"] if r["name"] != "THRU"}


def main():
    dirs = [a for a in sys.argv[1:] if not a.startswith("--")]
    files = [f for d in dirs for f in sorted(glob.glob(os.path.join(d, "*.pfm")))]
    fx = effect_names()
    dest_names = {r["number"]: r["short_name"] or r["name"]
                  for r in load_json("control_destinations.json")["tables"]["controller_box_destination"]["entries"]}
    src_names = {r["number"]: r["short_name"] or r["name"] for r in load_json("control_sources.json")["sources"]}
    waves = {w["number"]: w for w in load_json("waveforms.json")["waveforms"]}

    st = defaultdict(Counter)
    n = 0
    for f in files:
        try:
            raw = pfm.read_performance(open(f, "rb").read())
            perf = pfm.decode_performance(raw)
        except Exception as e:
            st["errors"][str(e)[:50]] += 1
            continue
        n += 1
        c = perf["common"]
        parts = [p for p in perf["parts"] if p["engine"] != "EMPTY"]
        st["nparts"][len(parts)] += 1
        st["engine_mix"][tuple(sorted(set(p["engine"] for p in parts)))] += 1
        st["main_category"][c["c2"]["Performance Main Category"]] += 1
        st["reverb_type"][fx.get(c["reverb"]["Reverb Type"], c["reverb"]["Reverb Type"])] += 1
        st["variation_type"][fx.get(c["variation"]["Variation Type"], c["variation"]["Variation Type"])] += 1
        st["master_fx_on"][c["c1"]["Master Effect Switch"]] += 1
        st["master_fx_type"][fx.get(c["mfx"]["Master Effect Type"], c["mfx"]["Master Effect Type"])] += 1
        st["arp_master_on"][c["c1"]["Arpeggio Master Switch"]] += 1
        st["motionseq_on"][c["c1"]["Motion Seq Master Switch"]] += 1
        for b in c["ctrlbox"]:
            if b["Controller Set Switch"]:
                st["common_ctrl"][(src_names.get(b["Controller Set Source"], b["Controller Set Source"]),
                                   dest_names.get(b["Controller Set Destination"], b["Controller Set Destination"]))] += 1
        for p in parts:
            st["part_engine"][p["engine"]] += 1
            for i in range(2):
                t = p["ins"][i][f"Insertion-{'AB'[i]} Type"]
                st[f"ins_{'AB'[i]}_type"][fx.get(t, t)] += 1
                st[f"ins_{'AB'[i]}_type_by_engine"][(p["engine"], fx.get(t, t))] += 1
            st["ins_connect"][p["p3"]["Insertion Connection Type"]] += 1
            st["mono_poly"][p["p1"]["Mono/Poly Mode"]] += 1
            st["portamento"][p["p1"]["Portamento Switch"]] += 1
            st["arp_on"][p["p1"]["Part Arp Switch"]] += 1
            for b in p["ctrlbox"]:
                if b["Controller Set Switch"]:
                    st["part_ctrl"][(p["engine"], src_names.get(b["Controller Set Source"], b["Controller Set Source"]),
                                     dest_names.get(b["Controller Set Destination"], b["Controller Set Destination"]))] += 1
            if "elements" in p:
                st["n_elements"][len(p["elements"])] += 1
                for e in p["elements"]:
                    if not e["e1"]["Element Switch"]:
                        continue
                    st["filter_type"][e["filter"]["Filter Type"]] += 1
                    st["xa_control"][e["osc"]["XA Control"]] += 1
                    w = e["osc"]["Wave Number"]
                    if e["osc"]["Wave Select"] == 0 and w in waves:
                        st["wave_category"][(waves[w]["main_category"], waves[w]["sub_category"])] += 1
                        st["wave_top"][waves[w]["name"]] += 1
            if "fmx" in p:
                st["fmx_algorithm"][p["fmx"]["common"].get("Algorithm Number", p["fmx"]["common"].get("Algorithm"))] += 1
                st["fmx_filter_type"][p["fmx"]["filter"]["Filter Type"]] += 1
                for o in p["fmx"]["op"]:
                    st["fmx_spectral_form"][o["op"]["Spectral Form"]] += 1
                    st["fmx_freq_mode"][o["op"]["Oscillator Frequency Mode"]] += 1
            if "anx" in p:
                a = p["anx"]
                for i, o in enumerate(a["osc"]):
                    st["anx_osc_wave"][(i + 1, o["osc"]["Oscillator Wave"])] += 1
                    st["anx_osc_octave"][(i + 1, o["osc"]["Oscillator Octave"])] += 1
                for i, fl in enumerate(a["filt"]):
                    st["anx_filter_type"][(i + 1, fl["filt"]["Filter Type"])] += 1
                st["anx_unison"][a["common"]["Unison"]] += 1
                st["anx_filter_connection"][a["common"].get("Filter Connection", a["common"].get("Filter Routing"))] += 1
    print(f"{n} performances decoded from {len(files)} files")
    for key in ("nparts", "engine_mix", "part_engine", "main_category", "n_elements", "reverb_type", "variation_type",
                "master_fx_on", "master_fx_type", "ins_A_type", "ins_B_type", "ins_connect", "mono_poly", "portamento",
                "arp_on", "arp_master_on", "motionseq_on", "filter_type", "xa_control", "wave_category", "wave_top",
                "fmx_algorithm", "fmx_filter_type", "fmx_spectral_form", "fmx_freq_mode", "anx_osc_wave",
                "anx_osc_octave", "anx_filter_type", "anx_unison", "anx_filter_connection", "common_ctrl", "part_ctrl",
                "ins_A_type_by_engine", "errors"):
        c = st[key]
        if not c:
            continue
        print(f"\n== {key} ({sum(c.values())})")
        for k, v in c.most_common(25):
            print(f"  {v:6d}  {k}")
    if "--json" in sys.argv:
        out = {k: [[str(kk), vv] for kk, vv in c.most_common()] for k, c in st.items()}
        json.dump(out, open(sys.argv[sys.argv.index("--json") + 1], "w"), indent=1)


if __name__ == "__main__":
    main()
