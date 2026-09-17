# MONTAGE M / MODX M performance file format (`.pfm`) and bulk dump

Reverse-engineered from the Expanded Softsynth Plugin (ESP) for MONTAGE M v3.0 and the
official *MONTAGE M Data List* (MW-H0, OS 3.0). Verified by parsing and re-serialising
byte-exactly all 3631 factory performances shipped inside the plugin bundle and all 2020
user performances on this machine, and by importing all 185 MONTAGE M performance dumps
from Soundmondo (`tools/pfm.py validate|roundtrip`, `tools/syx.py`).

## Where the files live

| What | Path |
|---|---|
| Factory (preset) performances, 3631 files | `/Library/Audio/Plug-Ins/Components/Expanded Softsynth Plugin for MONTAGE M.component/Contents/Resources/contents/performance/3Fxxxx-Performance.pfm` (also `00xxxx` = GM bank, `7F0000` = GM drum kit, `FFxxxx` = internal single-element "voices" used by drum kits) |
| Factory index | same folder, `performance.cfg` |
| User performances | `/Library/Yamaha/Expanded Softsynth Plugin for MONTAGE M/contents/current/performance/40xxxx-Performance.pfm` (0x40 = User bank) |
| User index | `.../contents/current/performance.cfg` |
| Init templates | `3F277B` Init Normal (AN-X), `3F277C` Init Normal (AWM2), `3F277D` Init Normal (FM-X), `3F277E` Init Drum |

The file number is the bank (1 byte) + slot (2 bytes) in hex. The same parameter blocks
are what the instrument sends as a MIDI bulk dump, so a `.pfm` converts losslessly to a
`.syx` for a hardware MODX M / MONTAGE M and back.

## Container encoding

All integers in the container are **big-endian**.

* **Block** = `u32 length` + `length` bytes. The bytes are one parameter block of the
  Data List's *MIDI Parameter Change Table* (see `data/midi_param_tables.json`), with two
  differences from the sysex form:
  * 2-byte parameters are stored as **little-endian u16** holding the 14-bit value
    (`MSB*128 + LSB`); in sysex they are two 7-bit bytes.
  * string blocks (20-char names, 16-char knob names) carry one extra NUL: 21 / 17 bytes.
* **Array** = `u32 count` + `count` items (blocks or groups of blocks).
* **Part record** = `u32 1` + `u8 engine` + the part's common blocks. Engine byte:
  `0` AWM2 (normal), `1` Drum, `2` FM-X, `3` AN-X, `255` empty ("Initialized Part"
  placeholder used by some multi-part factory performances).
* There is no file header, checksum or trailer; the Performance Flag block (`06 09`) and
  the Soundmondo version block are not stored in `.pfm`.

## Block order

```
Performance common
  name(21) c1(29) c2(86) ctrl(86)
  [2] A/D-part insertion A(52), B(52)
  arp(14) reverb(52) variation(52) rotary(68) masterEQ(34) masterFX(52)
  motionseq(12) superknob(90) A/D-in(42) USB-in(14) superknob-lane(20)
  [8] superknob sequence(102)
  [8] scene { 1byte(19) 2byte(44) }
  [8] assignable knob name(17)
  [32] controller box(18)
  [4] A/D lane { 1byte(4) 2byte(20) [8] sequence(102) }
[n] part
  u32 1, u8 engine
  name(21) p1(81) p2(94) p3(62)
  [2] insertion A(52), B(52)
  arp(100) lfo(68) zone(26) keyctrl(64)
  [8] scene(80)   [8] knob name(17)   [32] controller box(18)
  [4] lane { 1byte(4) 2byte(20) [8] sequence(102) }
then, for each part in order, its engine data:
  AWM2 : [elements] { e1(43) osc(40) amp(54) pitch(48) filter(108) }      (1..128 elements)
  Drum : [73] key(64)                                                      (C0..C6)
  FM-X : common(82) filter(70) [8] { ctrl-switch(39) operator(76) }
  AN-X : common(110) [3] { ctrl-switch(39) oscillator(78) } [2] { ctrl-switch(39) filter(30) } wavefolder(34)
  empty: nothing
```

Block sizes are the *Bulk Dump Block* byte counts of the Data List except: the Data List
prints the AWM2 element 1-byte block as 36 and the element filter block as 106, while its
own row lists (and the files) have 43 and 108. `data/midi_param_tables.json` carries the
row-derived sizes.

## Mapping blocks to Data List tables

| Block | Table base address |
|---|---|
| common name / c1 / c2 / ctrl | `06 00 00` / `06 00 01` / `06 00 02` / `06 00 03` |
| A/D ins A / B, arp, reverb, variation, rotary | `06 00 04` / `05` / `06` / `07` / `08` / `09` |
| master EQ, master FX, motionseq, superknob, A/D in, USB in, SK lane | `06 00 0A` / `0B` / `0C` / `0D` / `0E` / `0F` / `12` |
| superknob seq m, scene c 1byte / 2byte, knob name k, ctrl box bb | `06 01 0m` / `06 02 0c` / `06 03 0c` / `06 04 0k` / `06 05 bb` |
| A/D lane L 1byte / 2byte / sequence m | `06 06 L0` / `06 07 L0` / `06 08 Lm` |
| part name / p1 / p2 / p3 | `1p 00 00` / `01` / `02` / `03` |
| part ins A / B, arp, lfo, zone, keyctrl | `1p 00 04` / `05` / `06` / `07` / `08` / `09` |
| part scene c, knob name k, ctrl box bb, lane L | `1p 03 0c` / `1p 04 0k` / `1p 05 bb` / `1p 06 L0`, `1p 07 L0`, `1p 08 Lm` |
| element ee: e1 / osc / amp / pitch / filter | `2p 00 ee` / `01` / `02` / `03` / `04` |
| drum key kk | `2p 10 kk` |
| FM-X common / filter / op o switch / op o | `3p 00 00` / `3p 00 01` / `3p 01 0o` / `3p 02 0o` |
| AN-X common / osc o switch / osc o / filter f switch / filter f / wave folder | `4p 00 00` / `4p 01 0o` / `4p 02 0o` / `4p 03 0f` / `4p 04 0f` / `4p 05 00` |

`tools/pfm.py` implements exactly this (`TABLE_OF`), decodes every block into named
parameters (`decode_performance`) and writes it back (`write_performance`).

## Value conventions inside blocks

* Raw values are unsigned. Bipolar parameters are stored with an offset: a range printed
  as `−64 – +63` with default `00 40` means `raw − 64`; `−128 – +127` / `01 00` means
  `raw − 256`; `−255 – 0 – +255` / `02 00` means `raw − 256`; `−4800 – +4800 [cent]` on
  AN-X with default `01 77` means `(raw − 247) × 25` cents where the printed step is 25.
  The `desc` and `default` fields of each row in `data/midi_param_tables.json` give the
  printed range and centre.
* Effect types are the 14-bit value `MSB*128 + LSB` of the *Type (HEX)* column of the
  Effect Type List (`data/effect_types.json`, `type_number`). Example: `768` = `06 00`
  = AUTO PAN; `1 * 128 + 0` = REV-X HALL.
* Waveform: `Wave Select` (0 preset, 1 user, 2–17 library) + `Wave Number` (1-based, see
  `data/waveforms.json`).
* Arpeggio: per part `Arp 1–8 Number` (0 = off, 1–10922 preset; user arps 12032+).
* Names are ASCII, space padded to 20 (16 for knob names), NUL terminated in the file.

## `performance.cfg` (plugin index)

```
"PChd" u32 4 (version) u32 count
count × ( "Entr" u32 len  record )
record: u8[4] id (00 bank slot_hi slot_lo)   bank 0x40 user, 0x3F preset, 0x00 GM
        u8   flags1 (0/1, unknown)
        u8   flags2 (0/1/4, unknown; 4 on many factory entries)
        u8   engine mask: bit0 AWM2 or Drum, bit1 FM-X, bit2 AN-X   (same as Performance Flag block)
        u8   2 = single-part performance, 0 = multi-part (0x40/0x80 seen on a few)
        u8   0
        u16  little-endian part-present bitmask (part 1 = bit 0)
        u8[5] 0
        u16  0 for factory; user entries carry a nonzero value (looks like a save-time stamp)
        ASCII "<main*16+sub>:<display name>:<performance name>" NUL
```
`main`/`sub` are the performance's category numbers (Piano=0 … Ethnic=15, No Assign=16;
sub 0–8 in the printed column order of the category table). `tools/install.py` writes a
record like this when it adds a generated performance to the user bank.

## Sysex bulk dump

```
F0 43 0n 7F 1C  bh bl  0D  a1 a2 a3 a4  data…  cs  F7
```
`bh bl` = 7-bit byte count of (model id + address + data); checksum makes the 7-bit sum
of model id, address, data and checksum zero. A performance dump is wrapped in a header
`04 ll mm nn` / footer `05 ll mm nn` message (edit buffer = `04 04 00 00`, which is what
Soundmondo dumps use; user bank slots = `04 01 00 nn`). The Performance Flag block
`06 09 00 00` (8 bytes, second value = engine mask) and a Soundmondo version block
`00 00 7F 00` (`00 01 00 00 00 00`) accompany the performance blocks.

Dumps made on firmware 1.x carry shorter blocks (e.g. common 2-byte block 84 instead of
86 bytes); the importer zero-fills the parameters that were added later.
