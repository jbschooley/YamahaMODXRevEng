#!/usr/bin/env python3
"""Parse the MIDI Parameter Change Tables out of the Yamaha MONTAGE M Data List PDF.

Usage: parse_datalist_midi.py <MONTAGE-M_data_list_En_H0.pdf> <out.json> [--text-dump path]

The PDF pages 219–256 (1-based, in the H0 edition) hold two-column tables. Each column
is extracted separately with pdftotext -layout so rows stay intact. Rows are split into
cells (runs of >=2 spaces separate cells); the first cell after the range is the parameter
name, the last hex-looking cell is the default, cells in between are the description and
cells after the default are notes. Continuation (wrapped) lines are assigned to the column
whose x-position (learned from the table's own rows) is nearest.

Output JSON:
{
  "tables": [
     {"section": "PERFORMANCE COMMON", "base": "06 00 02 00", "total_size": 86,
      "params": [{"offset": 0, "size": 2, "range": "00 00 – 00 10", "name": "Performance Main Category",
                  "desc": "0 – 16 Refer to Performance Category List", "default": "00 10", "notes": ""}, ...],
      "footnotes": ["p = Part number 0–F Part 1 – 16 ..."]}
  ]
}
"""
import json
import re
import subprocess
import sys

FIRST_PAGE, LAST_PAGE = 219, 256

TOKEN = r"(?:[0-9A-Za-z]{2}|[A-Za-z])"
ROW_RE = re.compile(r"^(\s*)((?:" + TOKEN + r"\s+){0,3}" + TOKEN + r")\s+(\d+)\s")
RANGE_RE = re.compile(r"^\s*((?:[0-9A-F]{2}(?: [0-9A-F]{2})?)(?:, [0-9A-F]{2}(?: [0-9A-F]{2})?)?\s*(?:[–-]\s*(?:[0-9A-F]{2}(?: [0-9A-F]{2})?)?)?)(\s+|$)")
DEFAULT_RE = re.compile(r"^(?:[0-9A-F]{2}(?: [0-9A-F]{2})?|-)$")
CELL_RE = re.compile(r"\S+(?: \S+)*")
HDR_RE = re.compile(r"Parameter Name")
TOTAL_RE = re.compile(r"TOTAL SIZE\s*=\s*(\d+)")
SECTION_RE = re.compile(r"^\s*\(([A-Z0-9 \-/]+)\)")


def extract_text(pdf, first, last):
    """Return list of (page, column, text) with each column of each page extracted separately."""
    out = []
    for p in range(first, last + 1):
        for col, (x, w) in (("L", (0, 300)), ("R", (300, 295))):
            txt = subprocess.run(
                ["pdftotext", "-layout", "-f", str(p), "-l", str(p), "-x", str(x), "-y", "30",
                 "-W", str(w), "-H", "800", pdf, "-"],
                check=True, capture_output=True, text=True).stdout
            out.append((p, col, txt))
    return out


def cells(text, base=0):
    """Split a line into (start_x, text) cells separated by runs of >=2 spaces."""
    return [(base + m.start(), m.group()) for m in CELL_RE.finditer(text)]


def parse_row_cells(line, size_end):
    """Split a data row (text after the size field) into range/name/desc/default/notes with x positions."""
    rest = line[size_end:]
    m = RANGE_RE.match(rest)
    rng, rng_x = "", size_end
    if m:
        rng = m.group(1).strip()
        rng_x = size_end + m.start(1)
        rest_start = size_end + m.end()
    else:
        rest_start = size_end
    cs = cells(line[rest_start:], rest_start)
    out = {"range": (rng_x, rng), "name": (None, ""), "desc": (None, ""), "default": (None, ""), "notes": (None, "")}
    if not cs:
        return out
    # a description glued to the name by a single space: "Filter Cutoff Frequency 0 – 1023"
    nx, nt = cs[0]
    mg = re.search(r" (?=(?:[−\-+]?\d+(?:\.\d+)?[A-Za-z%]*\s*[–-]|\d+ = |Off, On|L\d+ – C|C-2 – ))", nt)
    if mg:
        cs = [(nx, nt[:mg.start()]), (nx + mg.start() + 1, nt[mg.start() + 1:])] + cs[1:]
    # a default glued to the end of the description ("Unipolar, Bipolar 00 00") or notes glued after
    # the default ("00 10 (NoAsg)")
    fixed = []
    for x, t in cs:
        md = re.match(r"^([0-9A-F]{2}(?: [0-9A-F]{2})?) (.+)$", t)
        if md and not DEFAULT_RE.match(t):
            fixed.append((x, md.group(1)))
            fixed.append((x + len(md.group(1)) + 1, md.group(2)))
            continue
        me = re.match(r"^(.+?) ([0-9A-F]{2}(?: [0-9A-F]{2})?)$", t)
        if me and not DEFAULT_RE.match(t) and not re.search(r"[–-]\s*$", me.group(1)):
            fixed.append((x, me.group(1)))
            fixed.append((x + len(me.group(1)) + 1, me.group(2)))
            continue
        fixed.append((x, t))
    cs = fixed
    out["name"] = cs[0]
    rest_cells = cs[1:]
    dflt = None
    for k in range(len(rest_cells) - 1, -1, -1):
        if DEFAULT_RE.match(rest_cells[k][1]):
            dflt = k
            break
    if dflt is None:
        if rest_cells:
            out["desc"] = (rest_cells[0][0], " ".join(c[1] for c in rest_cells))
    else:
        out["default"] = rest_cells[dflt]
        if dflt > 0:
            out["desc"] = (rest_cells[0][0], " ".join(c[1] for c in rest_cells[:dflt]))
        if dflt + 1 < len(rest_cells):
            out["notes"] = (rest_cells[dflt + 1][0], " ".join(c[1] for c in rest_cells[dflt + 1:]))
    return out


def finish(table):
    """Turn the collected raw rows of a table into parameter dicts."""
    rows = table.pop("_rows")
    parsed = []
    xs = {"range": [], "name": [], "desc": [], "default": [], "notes": []}
    for row, lines in rows:
        f = parse_row_cells(lines[0], row.pop("_size_end"))
        for k, (x, t) in f.items():
            if x is not None and t:
                xs[k].append(x)
        parsed.append((row, f, lines[1:]))
    col_x = {}
    for k, v in xs.items():
        if v:
            col_x[k] = min(v) if k in ("name", "range") else sorted(v)[len(v) // 2]
    for row, f, more in parsed:
        fields = {k: t for k, (x, t) in f.items()}
        for line in more:
            cs = []
            for x, t in cells(line):
                # a range continuation glued to text by one space ("00 11, Part", "00 4C Gain")
                mh = re.match(r"^([0-9A-F]{2}( [0-9A-F]{2})?,?( ?[–-])?) (.+)$", t)
                if mh and x <= col_x.get("name", 0) + 1:
                    cs.append((x, mh.group(1)))
                    cs.append((x + len(mh.group(1)) + 1, mh.group(4)))
                else:
                    cs.append((x, t))
            for x, t in cs:
                is_hex = re.match(r"^[0-9A-F]{2}( [0-9A-F]{2})?,?( ?[–-])?$", t) is not None
                if x <= col_x.get("name", 0) + 1:
                    k = "range" if is_hex else "name"
                elif re.fullmatch(r"\d{1,2}", t) and x < col_x.get("desc", 10**9) - 2 and fields["name"] and not re.search(r"\d$", fields["name"]):
                    k = "name"  # a wrapped trailing index ("Reverb Parameter" / "1")
                else:
                    best = None
                    for k2, kx in col_x.items():
                        if k2 == "range":
                            continue
                        d = abs(x - kx)
                        if best is None or d < best[0]:
                            best = (d, k2)
                    if best is None:
                        continue
                    k = best[1]
                fields[k] = (fields[k] + " " + t).strip() if fields[k] else t
        for k, v in fields.items():
            v = re.sub(r"\s*MONTAGE M Data List(\s+\d+)?", "", v)
            v = re.sub(r"\s*MONTAGE M(\s+Data List)?\s*$", "", v)
            if k == "name":
                v = re.sub(r"\s*[–-]\s*$", "", v)
            fields[k] = v.strip()
        row.update(fields)
        table["params"].append(row)


def parse(pages):
    tables = []
    section = None
    cols_size = None
    cur = None
    last = None

    def close_table(total=None):
        nonlocal cur, last
        if cur is not None:
            cur["total_size"] = total
            finish(cur)
            tables.append(cur)
        cur = None
        last = None

    for page, col, txt in pages:
        lines = txt.split("\n")
        for i, raw in enumerate(lines):
            line = raw.rstrip()
            if not line.strip():
                continue
            if "MIDI PARAMETER CHANGE TABLE" in line:
                m = SECTION_RE.search(line.replace("MIDI PARAMETER CHANGE TABLE", ""))
                if m:
                    section = m.group(1).strip()
                continue
            m = SECTION_RE.match(line)
            if m and "Group Number" in line:
                section = m.group(1).strip()
                continue
            if HDR_RE.search(line):
                cols_size = line.index("Size")
                continue
            if cols_size is None:
                continue
            mt = TOTAL_RE.search(line)
            if mt:
                close_table(int(mt.group(1)))
                continue
            if line.strip().startswith("Group Number") or "MIDI Data Table" in line:
                continue
            if re.fullmatch(r"\s*(?:\(HEX\)|LSB|MSB/|Range|Data|Default|MSB/ LSB|Address|Size)(?:\s+(?:\(HEX\)|LSB|MSB/|Range|Data|Default))*\s*", line):
                continue
            if re.fullmatch(r"\s*[a-zA-Z]\s*", line) and len(line) - len(line.lstrip()) < cols_size - 2:
                continue
            mr = ROW_RE.match(line)
            is_row = False
            if mr:
                indent = len(mr.group(1))
                size_pos = line.index(mr.group(3), len(mr.group(1)) + len(mr.group(2)))
                if indent < cols_size - 2 and abs(size_pos - cols_size) <= 4:
                    is_row = True
            if is_row:
                addr_tokens = mr.group(2).split()
                size = int(mr.group(3))
                size_end = size_pos + len(mr.group(3))
                if len(addr_tokens) == 4:
                    if cur is not None and cur["_rows"]:
                        close_table(None)
                    if cur is None:
                        cur = {"section": section, "base": " ".join(addr_tokens), "params": [],
                               "footnotes": [], "page": page, "_rows": []}
                    offset = int(addr_tokens[3], 16)
                else:
                    if cur is None:
                        cur = {"section": section, "base": None, "params": [], "footnotes": [],
                               "page": page, "_rows": []}
                    offset = int(addr_tokens[-1], 16)
                row = {"offset": offset, "size": size, "_size_end": size_end}
                cur["_rows"].append((row, [line]))
                last = row
                continue
            ms = re.match(r"^\s*(\d+)\s", line)
            if ms and cur is not None and abs(line.index(ms.group(1)) - cols_size) <= 2 and line[cols_size + 2:].strip():
                prev = cur["_rows"][-1][0] if cur["_rows"] else None
                offset = prev["offset"] + prev["size"] if prev else 0
                row = {"offset": offset, "size": int(ms.group(1)), "offset_inferred": True,
                       "_size_end": line.index(ms.group(1)) + len(ms.group(1))}
                cur["_rows"].append((row, [line]))
                last = row
                continue
            if cur is None and tables and re.match(r"^\s*[a-zA-Z]{1,2}\s*=", line):
                tables[-1]["footnotes"].append(line.strip())
                continue
            if cur is None and tables and tables[-1]["footnotes"] and line.startswith("       "):
                tables[-1]["footnotes"].append(line.strip())
                continue
            if last is not None and cur is not None:
                cur["_rows"][-1][1].append(line)
    close_table(None)
    return tables


def main():
    pdf, out = sys.argv[1], sys.argv[2]
    pages = extract_text(pdf, FIRST_PAGE, LAST_PAGE)
    if "--text-dump" in sys.argv:
        with open(sys.argv[sys.argv.index("--text-dump") + 1], "w") as f:
            for p, c, t in pages:
                f.write(f"=====PAGE {p} {c}=====\n{t}")
    tables = parse(pages)
    for t in tables:
        # effect blocks: "<X> Parameter 1..24" rows wrap in the PDF; name them by position
        prm = [p for p in t["params"] if re.match(r"^(.+?) Parameter\b", p["name"])]
        if len(prm) >= 16:
            prefix = re.match(r"^(.+?) Parameter\b", prm[0]["name"]).group(1)
            for i, p in enumerate(prm):
                p["name"] = f"{prefix} Parameter {i + 1}"
                p["desc"] = "Refer to Effect Parameter List for the selected type"
    for t in tables:
        # offsets must increase monotonically; a printed offset that goes backwards is a typo in the
        # PDF (e.g. "Key Controller Set 2 Switch" printed at 00 instead of 10) -> infer from the previous row
        prev_end = 0
        for p in t["params"]:
            if p["offset"] < prev_end:
                p["offset_printed"] = p["offset"]
                p["offset"] = prev_end
                p["offset_corrected"] = True
            prev_end = p["offset"] + p["size"]
        calc = sum(p["size"] for p in t["params"])
        t["calc_size"] = calc
        t["size_ok"] = (t["total_size"] == calc) if t["total_size"] is not None else None
    with open(out, "w") as f:
        json.dump({"source": "MONTAGE M Data List (MW-H0), MIDI Data Table pages %d-%d" % (FIRST_PAGE, LAST_PAGE),
                   "tables": tables}, f, indent=1, ensure_ascii=False)
    bad = [t for t in tables if not t["size_ok"]]
    print(f"{len(tables)} tables, {sum(len(t['params']) for t in tables)} params, {len(bad)} size mismatches")
    for t in tables:
        flag = "" if t["size_ok"] else "  <-- MISMATCH" if t["size_ok"] is False else "  (no total)"
        print(f"  p{t['page']} {t['section']!s:24} {t['base']!s:12} n={len(t['params']):3d} total={t['total_size']} calc={t['calc_size']}{flag}")


if __name__ == "__main__":
    main()
