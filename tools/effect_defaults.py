#!/usr/bin/env python3
"""Mine the factory bank for a sensible default parameter set per effect type.

Writes data/effect_defaults.json: {type_number: {"name":..., "count": n, "params": [p1..p24], "preset": n}}
where params is the most frequently used complete parameter vector for that type across every
reverb / variation / insertion / master / rotary block of the 3631 factory performances.
Used by build_performance.py so that choosing an effect type also gives it Yamaha-like settings.
"""
import glob
import json
import os
import sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pfm  # noqa: E402

FACTORY = ("/Library/Audio/Plug-Ins/Components/Expanded Softsynth Plugin for MONTAGE M.component"
           "/Contents/Resources/contents/performance")
DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")


def main():
    names = {r["type_number"]: r["name"] for r in json.load(open(os.path.join(DATA, "effect_types.json")))["effect_types"]}
    votes = defaultdict(Counter)
    for f in sorted(glob.glob(os.path.join(FACTORY, "3F*.pfm"))):
        perf = pfm.decode_performance(pfm.read_performance(open(f, "rb").read()))
        c = perf["common"]
        blocks = [(c["reverb"], "Reverb"), (c["variation"], "Variation"), (c["mfx"], "Master Effect"),
                  (c["rotary"], "VCM Rotary Speaker")]
        for p in perf["parts"]:
            if p["engine"] == "EMPTY":
                continue
            blocks += [(p["ins"][0], "Insertion-A"), (p["ins"][1], "Insertion-B")]
        for blk, prefix in blocks:
            t = blk[f"{prefix} Type"]
            if t == 0:
                continue
            n = 32 if prefix == "VCM Rotary Speaker" else 24
            params = tuple(blk[f"{prefix} Parameter {i}"] for i in range(1, n + 1))
            preset = blk.get(f"{prefix} Preset Number", 0)
            votes[t][(preset, params)] += 1
    out = {}
    for t, cnt in votes.items():
        (preset, params), n = cnt.most_common(1)[0]
        out[str(t)] = {"name": names.get(t), "count": sum(cnt.values()), "preset": preset, "params": list(params)}
    json.dump({"_meta": {"source": "most common (preset, parameter vector) per effect type over the factory bank",
                         "types": len(out)}, "defaults": out},
              open(os.path.join(DATA, "effect_defaults.json"), "w"), indent=1)
    print(len(out), "effect types with defaults")


if __name__ == "__main__":
    main()
