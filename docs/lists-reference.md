# MONTAGE M Data List — extracted reference tables

Source: Yamaha *MONTAGE M Data List* (`montage_m_dl_H0.pdf`, "For firmware version 3.01 and
later", 261 pages). PDF page indices equal the printed page numbers (checked on pp. 2, 27, 28,
66, 94, 156). Extraction used `pdftotext -bbox` word coordinates, assigning words to table
columns by x-position; every JSON file carries a `_meta` block with `source_pages` and notes.

| File | List | PDF pages | Entries |
|---|---|---|---|
| `data/performances.json` | Performance List | 2–26 | 3487 performances (1–3487, contiguous) |
| `data/performance_categories.json` | Performance Category List | 27 | 16 main categories + No Assign |
| `data/drum_kits.json` | Drum Kit Assign List | 28–65 | 153 kits, 10647 key assignments |
| `data/waveforms.json` | Waveform List | 66–90 | 7647 waveforms (1–7647, contiguous) |
| `data/arpeggio_types.json` | Arpeggio Type List | 94–156 | 10922 arpeggios (1–10922, contiguous) |

Not extracted: Live Set List (pp. 91–93) — it only maps slot positions to Performance names.

## Performance List (`performances.json`)

Fields: `number`, `name`, `main_category`, `sub_category`, `new_in_v3_0`, `page`.
`number` is the 1-based preset Performance number as printed. `new_in_v3_0` is true for the 60
rows marked `*1` ("new Performances added by firmware version 3.0 update", nos. 3428–3487).
Main/sub category strings are exactly the printed ones; every pair is valid against the
category table below. No factory Performance uses sub category "No Assign".

## Performance Category List (`performance_categories.json`)

The printed table has one row per main category; each row lists that category's sub
categories left to right. Numbering used in the JSON:

- `main_categories[].number` = row order 0–15 (Piano=0 … Ethnic=15) plus 16 = "No Assign".
  This matches the MIDI Data Table: *Performance Main Category* / *Part Main Category*
  range 0–16, default 0x10 shown as "NoAsg" (pp. 230, 240).
- `sub_categories[].number` = printed column order within the row, 0 = first column.
  Rows have 4 category-specific subs, then the 4 common subs Rock/Pop, R&B/Hip Hop,
  Electronic, Jazz/World, then "No Assign" (9 columns). Bass and Drum / Perc have only 3
  specific subs (8 columns), so the common subs sit at index 3–6 there instead of 4–7.
- Caveat: the MIDI Data Table gives *Performance Sub Category* / *Part Sub Category* a range of
  0–7 (default 0 shown as "--"), i.e. 8 values, while most rows print 9 columns. How the
  trailing "No Assign" column maps onto 0–7 (or whether the documented range is simply
  stale) cannot be settled from this document — treat sub index 8 as unverified.

## Drum Kit Assign List (`drum_kits.json`)

`drum_kits[]` = `{index, name, page, keys[]}` with `keys[] = {note, wave_number, wave_name}`.
`index` is just order of appearance (left→right, top→bottom, page by page); the list carries no
kit numbers and does not say which Performance/Part each kit belongs to. `wave_number` is the
preset waveform number (cross-reference `waveforms.json`). Most kits span C0–C6 (73 keys);
several are shorter (e.g. Trap Kit B0–A4, "Highland Snares" C2–G3, "Round Robin Timps" starts at
C#0). Kits can be stacked vertically in one column (p. 40 has "Highland Snares" under
"Bones&Spoons Kit"), and "Darbuka Sagat Riq" (p. 40) is one kit, not three. Kit 153 (p. 65,
4th column) has no name printed in the PDF (checked against a page render) → `name: null`.

## Waveform List (`waveforms.json`)

Fields: `number`, `name`, `main_category`, `sub_category`, `new_in_v3_0`, `page`.
`number` is the preset waveform number used by the MIDI Element parameter *Wave Number*
(p. 248/250: "1 – 7620 (USR, Library: 1 – 1024)"). The printed list runs to 7647: 7621–7635
(CFX 2022, CP80 Stage) are not flagged, 7636–7647 (ClavD6) carry the `*1` v3.0 mark — the
"1 – 7620" range text in the MIDI table is evidently stale. Categories use the on-screen
abbreviations (main: Piano, Keys, Organ, Guitr, Bass, Strng, Brass, SaxWW, SynLd, Pads,
SyCmp, CPerc, Dr/Pc, S.EFX, M.EFX, Ethnc; sub e.g. Rd, Wr, Clavi, TnWhl, Kick, Snare, HHat…).

## Arpeggio Type List (`arpeggio_types.json`)

Fields: `number`, `main_category`, `sub_category`, `name`, `time_signature`, `length_bars`,
`original_tempo`, `accent`, `random_sfx`, `sound_type`, `sound_type_ditto`, `page`.
`number` is the preset Arp number for the Part parameters *Arp 1–8 Number* (p. 242:
"Preset (0=Off, 1 – 10239), User, Library"); the list actually contains 10922 presets, so
the "10239" in the MIDI table is also stale. User/Library arps live at 12032+ (Arpeggio
Number Table, p. 243): User 12032–12287, Library1–16 in 256-blocks from 12288, and Library
17–24 via *Arp Number Extra* with number 16383.
Main categories are the abbreviated ones printed (Piano, Keys, Organ, Gtr, Bass, Str, Brass,
WW, SynLd, Pad, SynCp, CPerc, Dr/Pc, S.FX, M.FX, Ethnc, Ct/Hb); sub categories are e.g. Rock,
Pop Rock, Ballad, Classic R&B, Modern R&B, Hip Hop, Techno, House, D&B, Chill, Jazz, Latin,
World, General, and for Ct/Hb: Filter, Mod, Pan, PBend, Assign, Exprs, Zone, Z.Pad, Comb.
`accent` / `random_sfx` are true where the PDF prints a marker glyph (private-use char U+F0A1)
in that column: 3610 accent, 1817 random-SFX rows. `sound_type` is the recommended sound;
the PDF prints ":" for "same as the row above", which was resolved in reading order
(`sound_type_ditto: true` marks resolved rows). Controller arps show notes such as
"(CC#16)", "(PB, PB Range=12)", "(no event)" in this column and they are kept verbatim.

## Parsing caveats

- All tables are multi-column (2 columns for Performances, 4 for Waveforms and Drum Kits,
  2 for Arpeggios); the layout is identical on every page of a list, so fixed x-boundaries
  derived from the header words were used. Validation: every row has an integer number,
  numbers are contiguous with no duplicates, every time signature matches `\d+/\d+`,
  length/tempo are integers, every Performance category pair exists in the category table.
- Long centred Sound Type strings (e.g. "Mega1coilSlpPedalWah") overflow into the Random SFX
  column; non-marker words there were re-attached to `sound_type`.
- One Sound Type wraps onto a second line (arp 9067, "Dry Standard Kit (PB Range=24)");
  the continuation was appended.
- Names are stored exactly as printed, including oddities like Performance 3361
  "Rock Organ 2 +" and the "[Mg]" prefix on Mega Voice arps.
- The `*1` firmware-3.0 markers sit between the number and the name; they were removed
  from the name and recorded as `new_in_v3_0`.
- Nothing was inferred: any cell that was blank in the PDF is `null` (only the kit-153 name).
