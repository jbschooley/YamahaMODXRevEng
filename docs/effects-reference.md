# MONTAGE M effects reference (from the Data List PDF)

Source: `montage_m_dl_H0.pdf` (MONTAGE M Data List). Extracted tables live in
`data/effect_types.json`, `data/effect_params.json`, `data/effect_presets.json`,
`data/effect_data_assign.json`. PDF page indices used: Effect Type List 157–158,
Effect Parameter List 159–171, Effect Preset List 172–175, Effect Data Assign
Table 176–197 (these match the printed TOC numbers exactly, no offset).

## How effect types are numbered

There are 106 rows in the Effect Type List (NO EFFECT, THRU, and 104 real types
in 12 categories). Each row has **three different kinds of number**:

1. **Type (HEX) MSB / LSB** — the only identifier the MIDI parameter tables use.
   Stored as `type_hex` (e.g. `"01 03"`), `type_msb`, `type_lsb`, and
   `type_number = MSB*128 + LSB`. MSB is the category (01 reverb, 02 delay,
   03 chorus, 04 flanger, 05 phaser, 06 tremolo/rotary, 07 distortion,
   08 compressor, 0A wah, 0B lo-fi, 0C tech, 0D misc; 09 is unused). LSB is the
   type within the category. `00 00` is both NO EFFECT (reverb/variation) and
   THRU (insertion/rotary). LSBs are not contiguous (e.g. HD HALL = 01 03,
   REV-X HALL = 01 00, CONTROL FLANGER = 04 08) — do not assume list order = LSB.
2. **Per-block ordinal columns** REV / VAR / InsA / InsB / ADIns / VCM Rotary /
   Mas (`list_numbers.*`). These are the position of the type in the menu of that
   block. A blank cell means the type is not offered there (`available_in`).
   Reverb block has 13 types + OFF; Variation and Insertion A/B have 91 + THRU;
   A/D Insertion has 86 (no VINYL BREAK / BEAT REPEAT); VCM Rotary has 3 + THRU;
   Master has 28 (numbered 0–27 with DELAY LR = 0).
3. **Effect Parameter List `[n]`** — a *category-local* ordinal within each block
   (`[1] CROSS DELAY`, `[2] TEMPO CROSS DELAY`… under "Category — DELAY"). In the
   Reverb and Rotary blocks it equals the REV / VCM Rotary column. In the
   Variation/Insertion block it equals `VAR − (VAR of first type in the category) + 1`.
   This was checked programmatically for all 95 parameter tables (0 mismatches).
   These are stored as `list_number` in effect_params.json, and every set carries
   the resolved `effect_type` / `type_hex` / `type_number`.

## How a performance references effects (MIDI Parameter Change Table)

From the Performance Common / Part tables (`data/midi_param_tables.json`):

| Address | Parameter | Size | Default |
|---|---|---|---|
| 06 00 04 00 | Insertion-A Type (A/D part) | 2 | 00 00 |
| 06 00 05 00 | Insertion-B Type (A/D part) | 2 | 00 00 |
| 06 00 07 00 | Reverb Type | 2 | 01 00 (REV-X HALL) |
| 06 00 08 00 | Variation Type | 2 | 03 00 (G CHORUS) |
| 06 00 09 00 | VCM Rotary Speaker Type | 2 | range 06 40 – 06 42 |
| 06 00 0B 00 | Master Effect Type | 2 | 08 20 (MULTI BAND COMP) |
| 1p 00 04 00 | Part p Insertion-A Type | 2 | 00 00 |
| 1p 00 05 00 | Part p Insertion-B Type | 2 | 00 00 |

The 2-byte value is exactly the Type (HEX) MSB/LSB pair. In every block the
Type is followed at +02 by a 2-byte **Preset Number** (or "Template Number" for
the A/D-part insertion) and then 2-byte Parameter 1, 2, 3… at +04, +06, +08….
The parameter index N in those MIDI tables is the `no` column of
effect_params.json for that type; the raw 2-byte value is the `value` range
(the parenthesised numbers), and when `table` is set the displayed value is
`effect_data_assign.json` table `values[raw − first_index]`.
Whether the MIDI Preset Number is the 0-based position in the Effect Preset List
is an assumption (marked unverified in effect_presets.json).

## Parameter tables

- 95 printed parameter tables cover all 106 types; many types share one table
  (HD HALL/HD ROOM; R3/SPX HALL/ROOM/PLATE/STAGE; GATED/REVERSE REVERB;
  SPIRALIZER P/F; TEMPO SPIRALIZER P/F; the four BEAT REPEATs; the three VCM
  ROTARY SPEAKERs). `types[]` lists every sharer.
- Most Variation/Insertion tables have 16 slots; ROTARY SPEAKER 2 has 18, UNI COMP
  DOWN/UP 17, M/S EQ COMPRESSOR / VOCODER / SHIMMER REVERB 24, BEAT REPEAT 21,
  VCM ROTARY SPEAKER 32 (18–32 unused).
- "—" rows are `unused: true`. The PDF's "N – M: Same as the parameters shaded in
  gray in CROSS DELAY" lines were expanded to the four gray rows verified on the
  rendered page (CROSS DELAY 13–16: EQ Low Frequency (4–40, tbl 3), EQ Low Gain
  (52–76), EQ High Frequency (28–58, tbl 3), EQ High Gain (52–76)); those rows
  carry `shared_eq_block: true`. Depending on the effect they land at 6–9, 11–14
  or 13–16.
- Part EQ (2-band) and Master EQ tables are included as blocks `part_eq` /
  `master_eq` with `effect_type: null` (they are not effect types).
- The Master Effect Block prints only a list of 23 type names (no THRU; bypass by
  switching the block off); it is stored under `master_effect_block` with a
  mapping to type-list names ("DOWNWARD COMP" = UNI COMP DOWN, "SPIRALIZER
  TYPE-P" = SPIRALIZER P, "BEAT REPEAT" = all four BEAT REPEAT types, etc.).
  That list covers 26 types; the Type List's Mas column has 28 — it omits
  M/S EQ COMPRESSOR (Mas 7) and CS RING MODULATOR (Mas 11).

## Lookup tables (Effect Data Assign Table, 74 tables)

Which table a parameter uses comes from its `Tbl No.` column; every table has a
`used_by_parameters` list. Rough map by parameter family:

- LFO / modulation speed: #1 LFO Frequency (0.00–39.7 Hz, 0–127; LFO Speed, AM
  Speed, Rotor/Horn Speed of ROTARY SPEAKER 1), #36 Multi FX LFO Speed, #60
  Reversible LFO (Spiral Speed, ±39.7 Hz), #62 Wave Folder LFO (1024 steps),
  #73 Shimmer AM Freq (1024 steps, starts at index 4), #74 GS1 Ensemble LFO Speed
  (1–200), #20/#21/#22 VCM Flanger/Phaser/Wah Speed (236/253/255 steps).
- Delay times: #2 Modulation Delay Offset (0–50 ms), #5 Delay/Initial Delay
  (0.1–200 ms), #7 (0.1–400 ms, PITCH CHANGE), #18 Classic Flanger Delay Offset,
  #41/#42 Analog Delay Retro/Modern times, #72 Shimmer Pre-Delay (966 steps).
- Tempo-synced values: #13 Tempo (32nd/3 … 4thx16, 30 entries; sub-ranges 0–19,
  5–29, 5–11 are used by different effects), #61 LFO Step Transitional Rate.
- Frequencies: #3 EQ Frequency (61 entries, THRU at both ends; used by every
  HPF/LPF/EQ Low/Mid/High Frequency with 0–60 sub-ranges), #39 fine EQ Frequency
  (256 entries; Part EQ, M/S EQ, Shimmer filters), #28/#29 VCM EQ Frequency/Q,
  #17 Ring Mod OSC, #12 Lo-Fi sampling frequency, #46 Beat Repeat Cutoff, #54/#55
  Downward Comp EQ Freq / Post HPF.
- Reverb: #4 Reverb Time (0.3–30 s, 70 entries), #23/#24 REV-X Hall/Room time,
  #6 Room Size, #11 Space Simulator Width/Depth/Height, #71 Shimmer Reverb Time.
- Dynamics: #8/#9/#10 classic compressor attack/release/ratio, #14 multi-band gain,
  #15/#16 Dyna attack/release, #25/#26/#27 VCM Comp level/attack/release,
  #45 Side Chain Input Level (−∞…+24 dB, also used for Mid/Side Gain and
  Modulator/Mic input), #47 Beat Repeat/Bit Crusher/Vinyl Break output level,
  #50–#55 Universal (Downward) Comp.
- Selectors printed as tables: #30/#31 Speaker Type, #33 Wah SW, #34 Dist SW,
  #35 Dist EQ, #37 Phaser SW, #38 Delay SW, #43/#44 Analog Delay type, #64 Wave
  Folder SEQ pattern, #19 Modulation Phase, #49 rotary accel/decel multiplier.
- Rotary: #56–#59 ROTARY SPEAKER 2 rpm tables, #65–#68 VCM Rotary rpm tables.
- Never referenced by any Tbl No.: #32 Distortion Type, #40 Beat Repeat Ratio,
  #69 Gain Table.

## Gotchas found while parsing

- The Side Chain/Modulator column is a Symbol-font bullet (U+F06C) that
  `pdftotext -layout` silently drops; it was recovered from `-bbox-layout` word
  positions. Marked types: DYNAMIC FLANGER, DYNAMIC PHASER, VCM COMPRESSOR 376,
  CLASSIC COMPRESSOR, MULTI BAND COMP, UNI COMP DOWN/UP, RING MODULATOR, DYNAMIC
  RING MODULATOR, DYNAMIC FILTER, VOCODER.
- The Data Assign pages are multi-column with tables stacked vertically inside a
  column (e.g. #8/#9/#10, #13/#14, #37/#38, #63/#64) and long tables continue
  across pages (#62, #72, #73). Columns were assigned by bounding boxes and
  continuation columns by data-index continuity; all 74 tables verified to have
  contiguous in-order indices. #47, #67, #68 start at 1; #49 at 14; #73 at 4.
- Likely misprints, kept as printed and noted in `_meta.notes`:
  GS1 ENSEMBLE & TREMOLO has Tbl 74 on "Tremolo LFO Depth" instead of "Tremolo
  LFO Speed"; US HIGH GAIN "Type" cites Tbl 35 (Distortion EQ) although its
  values are Tbl 32 (Distortion Type). Two "Feedback High Dump" spellings and
  "Beat Repert" table names are the PDF's own.
- "(Ins17)" second ranges on GATED/REVERSE REVERB and EARLY REFLECTION (Room Size,
  Initial Delay) are stored as `alternates`; the PDF never defines "Ins17".
- REV-X HALL/ROOM Reverb Time prints "23/24" in Tbl No.; stored as
  `table_by_type`. BEAT REPEAT "Length" prints four value ranges (Even 0–8,
  Triplet 0–8, Even+Triplet 0–16, Free 0–127) in one cell; kept as one string.
- Names differ between lists: Type List "DELAY LR" / "UNI COMP DOWN" /
  "PARALLEL COMP" vs Parameter List "DELAY L, R" / "UNIVERSAL COMPRESSOR DOWN" /
  "PARALLEL COMPRESSOR" vs Preset List "U.S. Combo" / "Multi-band Comp" /
  "Beat Repeat (even)". JSON files keep the printed spelling and add the resolved
  Type List name.
- Effect presets: only names are printed (657 across 104 types); no parameter
  values exist in the Data List.
