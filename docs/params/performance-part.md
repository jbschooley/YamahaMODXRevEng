# PERFORMANCE PART

## `1p 00 00 00` — 20 bytes
`.pfm` block: `part.name`
_p = Part number 0–F                      Part 1 – 16 (Normal, Drum, FM-X, AN-X)_

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 1 | Part Name 1 | 0, 32 – 126 (ASCII) Initialized |  |  |
| 1 | 1 | Part Name 2 | 0, 32 – 126 (ASCII) Part |  |  |
| 2 | 1 | Part Name 3 | 0, 32 – 126 (ASCII) |  |  |
| 3 | 1 | Part Name 4 | 0, 32 – 126 (ASCII) |  |  |
| 4 | 1 | Part Name 5 | 0, 32 – 126 (ASCII) |  |  |
| 5 | 1 | Part Name 6 | 0, 32 – 126 (ASCII) |  |  |
| 6 | 1 | Part Name 7 | 0, 32 – 126 (ASCII) |  |  |
| 7 | 1 | Part Name 8 | 0, 32 – 126 (ASCII) |  |  |
| 8 | 1 | Part Name 9 | 0, 32 – 126 (ASCII) |  |  |
| 9 | 1 | Part Name | 00, 20 – 7E | 10 | 0, 32 – 126 (ASCII) |
| 10 | 1 | Part Name @10 | 00, 20 – 7E | 11 | 0, 32 – 126 (ASCII) |
| 11 | 1 | Part Name @11 | 00, 20 – 7E | 12 | 0, 32 – 126 (ASCII) |
| 12 | 1 | Part Name @12 | 00, 20 – 7E | 13 | 0, 32 – 126 (ASCII) |
| 13 | 1 | Part Name @13 | 00, 20 – 7E | 14 | 0, 32 – 126 (ASCII) |
| 14 | 1 | Part Name @14 | 00, 20 – 7E | 15 | 0, 32 – 126 (ASCII) |
| 15 | 1 | Part Name @15 | 00, 20 – 7E | 16 | 0, 32 – 126 (ASCII) |
| 16 | 1 | Part Name @16 | 00, 20 – 7E | 17 | 0, 32 – 126 (ASCII) |
| 17 | 1 | Part Name @17 | 00, 20 – 7E | 18 | 0, 32 – 126 (ASCII) |
| 18 | 1 | Part Name @18 | 00, 20 – 7E | 19 | 0, 32 – 126 (ASCII) |
| 19 | 1 | Part Name @19 | 00, 20 – 7E | 20 | 0, 32 – 126 (ASCII) |

## `1p 00 01 00` — 81 bytes
`.pfm` block: `part.p1`
_p = Part number 0–F                   Part 1 – 16 (Normal, Drum, FM-X, AN-X)_

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 1 | Part Switch | Off, On | 01 |  |
| 1 | 1 | Part Mode | Internal, External | 00 |  |
| 2 | 1 | Keyboard Control Switch | Off, On | 01 | Fixed to “Off” for Part 9 or later. |
| 3 | 1 | Mute Switch | Off, On | 00 |  |
| 4 | 1 | Insertion FX A Switch | Off, On | 01 |  |
| 5 | 1 | Insertion FX B Switch | Off, On | 01 |  |
| 6 | 1 | Element Pan Switch | Off, On | 01 |  |
| 7 | 1 | Motion Seq Part Switch | Off, On | 01 |  |
| 8 | 1 | Key Assign Mode | Single, Multi | 01 | Not available for Drum Part |
| 9 | 1 | Mono/Poly Mode | Mono, Poly | 01 | Not available for Drum Part |
| 10 | 1 | Portamento Switch | Off, On | 01 | Not available for Drum Part |
| 11 | 1 | Receive Pitch Bend | Off, On | 01 |  |
| 12 | 1 | Receive After Touch | Off, On | 01 |  |
| 13 | 1 | Receive PAT | Off, On | 01 |  |
| 14 | 1 | Receive Program Change | Off, On | 01 |  |
| 15 | 1 | Receive Bank Select | Off, On | 01 |  |
| 16 | 1 | Receive Control Change | Off, On | 01 |  |
| 17 | 1 | Receive Assignable Knob 1 | Off, On | 01 |  |
| 18 | 1 | Receive Assignable Knob 2 | Off, On | 01 |  |
| 19 | 1 | Receive Assignable Knob 3 | Off, On | 01 |  |
| 20 | 1 | Receive Assignable Knob 4 | Off, On | 01 |  |
| 21 | 1 | Receive Assignable Knob 5 | Off, On | 01 |  |
| 22 | 1 | Receive Assignable Knob 6 | Off, On | 01 |  |
| 23 | 1 | Receive Assignable Knob 7 | Off, On | 01 |  |
| 24 | 1 | Receive Assignable Knob 8 | Off, On | 01 |  |
| 25 | 1 | Receive Foot Controller 1 | Off, On | 01 |  |
| 26 | 1 | Receive Foot Controller 2 | Off, On | 01 |  |
| 27 | 1 | Receive Modulation Wheel | Off, On | 01 |  |
| 28 | 1 | Receive Sustain / Sostenuto | Off, On | 01 |  |
| 29 | 1 | Receive Pan | Off, On | 01 |  |
| 30 | 1 | Receive Volume / Expression | Off, On | 01 |  |
| 31 | 1 | Receive Ribbon Controller | Off, On | 01 |  |
| 32 | 1 | Receive Breath Controller | Off, On | 01 |  |
| 33 | 1 | Receive Foot Switch | Off, On | 01 |  |
| 34 | 1 | Receive Assignable Function 1 | Off, On | 01 |  |
| 35 | 1 | Receive Assignable Function 2 | Off, On | 01 |  |
| 36 | 1 | reserved | 00 | 00 |  |
| 37 | 1 | Receive Motion Seq Trigger | Off, On | 01 |  |
| 38 | 1 | Receive Portamento Switch | Off, On | 01 |  |
| 39 | 1 | Receive Portamento Time | Off, On | 01 |  |
| 40 | 1 | LFO Tempo Sync | Off, On | 00 |  |
| 41 | 1 | LFO Loop Switch | On, Off | 00 | 239 |
| 42 | 1 | Transmit Pitch Bend | Off, On | 01 |  |
| 43 | 1 | Transmit After Touch | Off, On | 01 |  |
| 44 | 1 | Transmit PAT | Off, On | 01 |  |
| 45 | 1 | Transmit Program Change | Off, On | 01 |  |
| 46 | 1 | Transmit Bank Select | Off, On | 01 |  |
| 47 | 1 | Transmit Control Change | Off, On | 01 |  |
| 48 | 1 | Transmit Assignable Knob 1 | Off, On | 01 |  |
| 49 | 1 | Transmit Assignable Knob 2 | Off, On | 01 |  |
| 50 | 1 | Transmit Assignable Knob 3 | Off, On | 01 |  |
| 51 | 1 | Transmit Assignable Knob 4 | Off, On | 01 |  |
| 52 | 1 | Transmit Assignable Knob 5 | Off, On | 01 |  |
| 53 | 1 | Transmit Assignable Knob 6 | Off, On | 01 |  |
| 54 | 1 | Transmit Assignable Knob 7 | Off, On | 01 |  |
| 55 | 1 | Transmit Assignable Knob 8 | Off, On | 01 |  |
| 56 | 1 | Transmit Foot Controller 1 | Off, On | 01 |  |
| 57 | 1 | Transmit Foot Controller 2 | Off, On | 01 |  |
| 58 | 1 | Transmit Modulation Wheel | Off, On | 01 |  |
| 59 | 1 | Transmit Sustain/Sostenuto | Off, On | 01 |  |
| 60 | 1 | Transmit Pan | Off, On | 01 |  |
| 61 | 1 | Transmit Volume/Expression | Off, On | 01 |  |
| 62 | 1 | Transmit Ribbon Controller | Off, On | 01 |  |
| 63 | 1 | Transmit Breath Controller | Off, On | 01 |  |
| 64 | 1 | Transmit Foot Switch | Off, On | 01 |  |
| 65 | 1 | Transmit Assignable Function 1 | Off, On | 01 |  |
| 66 | 1 | Transmit Assignable Function 2 | Off, On | 01 |  |
| 67 | 1 | reserved @67 |  |  |  |
| 68 | 1 | Transmit Motion Seq Trigger | Off, On | 01 |  |
| 69 | 1 | Transmit Portamento Switch | Off, On | 01 |  |
| 70 | 1 | Transmit Portamento Time | Off, On | 01 |  |
| 71 | 1 | Part Arp Switch | Off, On | 01 |  |
| 72 | 1 | Arp Play Only | Off, On | 00 |  |
| 73 | 1 | Arp Fixed SD/BD | Off, On | 00 | Not available expect for Drum Part |
| 74 | 1 | Arp Loop | Off, On | 01 |  |
| 75 | 1 | Arp Accent Start Quantize | Off, On | 01 |  |
| 76 | 1 | Arp Random SFX | Off, On | 01 |  |
| 77 | 1 | Arp Random SFX Key On Control | Off, On | 01 |  |
| 78 | 1 | Slider Direction | Normal, Reverse | 00 |  |
| 79 | 1 | Expression Type | Normal, Pre FX | 00 |  |
| 80 | 1 | Extended Element Switch | Off, On | 00 |  |

## `1p 00 02 00` — 94 bytes
`.pfm` block: `part.p2`
_p = Part number MONTAGE M Data List               240_

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 2 | Part Main Category | 0 – 16 Refer to Performance Category List | 00 10 (NoAsg) formance | Refer to Per- Category List. |
| 2 | 2 | Part Sub Category | 0–7 Refer to Performance Category List | 00 00 (--) | Refer to Per- formance Category List. |
| 4 | 2 | Velocity Limit Low | 1 – 127 | 00 01 |  |
| 6 | 2 | Velocity Limit High | 1 – 127 | 00 7F |  |
| 8 | 2 | Note Limit Low | C-2 – G8 | 00 00 |  |
| 10 | 2 | Note Limit High | C-2 – G8 | 00 7F |  |
| 12 | 2 | Velocity Sensitivity Depth | 0 – 127 | 00 40 |  |
| 14 | 2 | Velocity Sensitivity Offset | 0 – 127 | 00 40 |  |
| 16 | 2 | Volume | 0 – 127 | 00 64 |  |
| 18 | 2 | Pan | L63 – C – R63 | 00 40 |  |
| 20 | 2 | Reverb Send | 0 – 127 | 00 00 |  |
| 22 | 2 | Variation Send | 0 – 127 | 00 00 |  |
| 24 | 2 | Dry Level | 0 – 127 | 00 7F |  |
| 26 | 2 | Envelope Follower Gain | −24dB – 0dB – +24dB | 00 40 |  |
| 28 | 2 | Envelope Follower Attack | 1ms – 40ms | 00 10 |  |
| 30 | 2 | Envelope Follower Release | 10ms – 680ms | 00 07 |  |
| 32 | 2 | Part Output Select | 0: MainL&R, 8: AsgnL&R, 9-23: USB1&2, – USB29&30, 64 – 95: AsgnL, AsgnR, USB1, – USB30, 125: Off, 127: Drum | 00 00 | For parts other than the Drum Part, “Drum” is displayed as “MainL&R.” |
| 34 | 2 | AEG Attack Time | −64 – +63 | 00 40 |  |
| 36 | 2 | AEG Decay Time | −64 – +63 | 00 40 |  |
| 38 | 2 | AEG Sustain Level | −64 – +63 | 00 40 | Not available for Drum Part |
| 40 | 2 | AEG Release Time | −64 – +63 | 00 40 | Not available for Drum Part |
| 42 | 2 | FEG Attack Time | −64 – +63 | 00 40 | Available only for AWM Normal Part |
| 44 | 2 | FEG Decay Time | −64 – +63 | 00 40 | Available only for AWM Normal Part |
| 46 | 2 | FEG Sustain Level | −64 – +63 | 00 40 | Available only for AWM Normal Part |
| 48 | 2 | FEG Release Time | −64 – +63 | 00 40 | Available only for AWM Normal Part |
| 50 | 2 | FEG Depth | −64 – +63 | 00 40 | Not available for Drum Part |
| 52 | 2 | Filter Cutoff Frequency | −64 – +63 | 00 40 |  |
| 54 | 2 | Filter Resonance/ Width | −64 – +63 | 00 40 |  |
| 56 | 2 | Assignable Knob 1 Value | 0 – 1023 | 04 00 |  |
| 58 | 2 | Assignable Knob 2 Value | 0 – 1023 | 04 00 |  |
| 60 | 2 | Assignable Knob 3 Value | 0 – 1023 | 04 00 |  |
| 62 | 2 | Assignable Knob 4 Value | 0 – 1023 | 04 00 |  |
| 64 | 2 | Assignable Knob 5 Value | 0 – 1023 | 04 00 |  |
| 66 | 2 | Assignable Knob 6 Value | 0 – 1023 | 04 00 |  |
| 68 | 2 | Assignable Knob 7 Value | 0 – 1023 | 04 00 |  |
| 70 | 2 | Assignable Knob 8 Value | 0 – 1023 | 04 00 |  |
| 72 | 2 | Swing | −120 – 0 – +120 | 01 00 |  |
| 74 | 2 | Motion Seq Amplitude | −127 – +127 | 01 00 |  |
| 76 | 2 | Motion Seq Pulse Shape | −100, −98, – 0, – +98, +100 | 00 40 |  |
| 78 | 2 | Motion Seq Smooth | −127 – +127 | 01 00 |  |
| 80 | 2 | Motion Seq Random | 0 – 127 | 00 00 |  |
| 82 | 2 | MotionSeq View Lane | 1–4 | 00 00 |  |
| 84 | 2 | Expression Curve | Normal, Organ | 00 00 |  |
| 86 | 2 | Element Count | 8 – 128 | 00 08 |  |
| 88 | 2 | Pitch Control Group | Off, A, B, – P | 00 00 |  |
| 90 | 2 | Arpeggio Group | Off, A, B, – P | 00 00 |  |
| 92 | 2 | Note Range Group | bit 3: OFF, ON Group D bit 2: OFF, ON Group C bit 1: OFF, ON Group B bit 0: OFF, ON Group A | 00 00 |  |

## `1p 00 03 00` — 62 bytes
`.pfm` block: `part.p3`
_p = Part number 0–F                   Part 1 – 16 (Normal, Drum, FM-X, AN-X)_

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 2 | Pitch Bend Range Upper | −48 – +24 | 00 42 |  |
| 2 | 2 | Pitch Bend Range Lower | −48 – +24 | 00 3E |  |
| 4 | 2 | Detune | −12.8 – +12.7 [Hz] | 01 00 |  |
| 6 | 2 | Note Shift | −48 – +48 [semitones] | 00 40 | Not available for Drum Part |
| 8 | 2 | Portamento Time | 0 – 127 | 00 40 | Not available for Drum Part |
| 10 | 2 | Portamento Mode | Fingered, Full-time | 00 01 | Not available for Drum Part |
| 12 | 2 | Portamento Time Mode | Rate 1, Time 1, Rate 2, Time 2 | 00 00 | Not available for Drum Part |
| 14 | 2 | Micro Tuning Scale | Equal Temperament, Pure Major, Pure Minor, Werckmeister, Kirnberger, Valloti&Young, 1/4 Shift, 1/4 tone, 1/8 tone, Indian, Arabic 1, Arabic 2, Arabic 3, User1 – 8, Library1-1 – 16-8, Library17-1 – Library24-8 | 00 00 | Not available for Drum Part |
| 16 | 2 | Micro Tuning Root | C–B | 00 00 | Not available for Drum Part |
| 18 | 2 | Legato Slope | 0–7 | 00 00 | Not available for Drum, FM-X and AN-X |
| 20 | 2 | Insertion Connection Type | Parallel, Ins AB, Ins BA | 00 01 | Parallel is not available for FM-X and AN-X |
| 22 | 2 | Insertion to Reverb Send Level | 0 – 127 | 00 00 | Drum Part only. |
| 24 | 2 | Insertion to Variation Send Level | 0 – 127 | 00 00 | Drum Part only. |
| 26 | 2 | 3-band EQ Low Frequency | 50.1 – 2.00k | 00 36 |  |
| 28 | 2 | 3-band EQ Low Gain | −12.00dB – +12.00dB | 00 40 |  |
| 30 | 2 | 3-band EQ Mid Frequency | 139.7 – 10.1k | 01 0D |  |
| 32 | 2 | 3-band EQ Mid Gain | −12.00dB – +12.00dB | 00 40 |  |
| 34 | 2 | 3-band EQ Mid Q | 0.7 – 10.3 | 00 00 |  |
| 36 | 2 | 3-band EQ High Frequency | 503.8 – 14.0k | 01 67 |  |
| 38 | 2 | 3-band EQ High Gain | −12.00dB – +12.00dB | 00 40 |  |
| 40 | 2 | 2-band EQ 1 Type | Thru, LPF, HPF, Low Shelf Hi Shelf, Peak/ Dip | 00 00 |  |
| 42 | 2 | 2-band EQ 1 Frequency | 63.0 – 18.0k | 00 30 |  |
| 44 | 2 | 2-band EQ 1 Gain | −12.00dB – +12.00dB | 00 40 |  |
| 46 | 2 | 2-band EQ 1 Q | 0.1 – 12.0 | 00 01 |  |
| 48 | 2 | 2-band EQ 2 Type | Thru, LPF, HPF, Low Shelf Hi Shelf, Peak/ Dip | 00 00 |  |
| 50 | 2 | 2-band EQ 2 Frequency | 63.0 – 18.0k | 00 30 |  |
| 52 | 2 | 2-band EQ 2 Gain | −12.00dB – +12.00dB | 00 40 |  |
| 54 | 2 | 2-band EQ 2 Q | 0.1 – 12.0 | 00 01 |  |
| 56 | 2 | 2-band EQ Output Level | −12.00dB – +12.00dB | 00 40 |  |
| 58 | 2 | Insertion-A Side Chain Part | 0: Part 1, 1: Part 2 – 00 7F 15: Part 16, 16: A/D, 17:Master 127: Off |  |  |
| 60 | 2 | Insertion-B Side Chain Part | 0: Part 1, 1: Part 2 – 00 7F 15: Part 16, 16: A/D, 17:Master 127: Off |  |  |

## `1p 00 04 00` — 52 bytes
`.pfm` block: `part.ins.0`
_p = Part number 00 – 0F               Part 1 – 16 (Normal, Drum, FM-X, AN-X)_

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 2 | Insertion-A Type | Refer to Effect Parameter List | 00 00 |  |
| 2 | 2 | Insertion-A Preset Number | 00 00 – 7F 7F | 00 00 |  |
| 4 | 2 | Insertion-A Parameter 1 | Refer to Effect Parameter List for the selected type | 00 00 |  |
| 6 | 2 | Insertion-A Parameter 2 | Refer to Effect Parameter List for the selected type | 00 00 |  |
| 8 | 2 | Insertion-A Parameter 3 | Refer to Effect Parameter List for the selected type | 00 00 |  |
| 10 | 2 | Insertion-A Parameter 4 | Refer to Effect Parameter List for the selected type | 00 00 |  |
| 12 | 2 | Insertion-A Parameter 5 | Refer to Effect Parameter List for the selected type | 00 00 |  |
| 14 | 2 | Insertion-A Parameter 6 | Refer to Effect Parameter List for the selected type | 00 00 |  |
| 16 | 2 | Insertion-A Parameter 7 | Refer to Effect Parameter List for the selected type | 00 00 |  |
| 18 | 2 | Insertion-A Parameter 8 | Refer to Effect Parameter List for the selected type | 00 00 |  |
| 20 | 2 | Insertion-A Parameter 9 | Refer to Effect Parameter List for the selected type | 00 00 |  |
| 22 | 2 | Insertion-A Parameter 10 | Refer to Effect Parameter List for the selected type | 00 00 |  |
| 24 | 2 | Insertion-A Parameter 11 | Refer to Effect Parameter List for the selected type | 00 00 |  |
| 26 | 2 | Insertion-A Parameter 12 | Refer to Effect Parameter List for the selected type | 00 00 |  |
| 28 | 2 | Insertion-A Parameter 13 | Refer to Effect Parameter List for the selected type | 00 00 |  |
| 30 | 2 | Insertion-A Parameter 14 | Refer to Effect Parameter List for the selected type | 00 00 |  |
| 32 | 2 | Insertion-A Parameter 15 | Refer to Effect Parameter List for the selected type | 00 00 |  |
| 34 | 2 | Insertion-A Parameter 16 | Refer to Effect Parameter List for the selected type | 00 00 |  |
| 36 | 2 | Insertion-A Parameter 17 | Refer to Effect Parameter List for the selected type | 00 00 |  |
| 38 | 2 | Insertion-A Parameter 18 | Refer to Effect Parameter List for the selected type | 00 00 |  |
| 40 | 2 | Insertion-A Parameter 19 | Refer to Effect Parameter List for the selected type | 00 00 |  |
| 42 | 2 | Insertion-A Parameter 20 | Refer to Effect Parameter List for the selected type | 00 00 |  |
| 44 | 2 | Insertion-A Parameter 21 | Refer to Effect Parameter List for the selected type | 00 00 |  |
| 46 | 2 | Insertion-A Parameter 22 | Refer to Effect Parameter List for the selected type | 00 00 |  |
| 48 | 2 | Insertion-A Parameter 23 | Refer to Effect Parameter List for the selected type | 00 00 |  |
| 50 | 2 | Insertion-A Parameter 24 | Refer to Effect Parameter List for the selected type | 00 00 |  |

## `1p 00 05 00` — 52 bytes
`.pfm` block: `part.ins.1`
_p = Part number 00 – 0F               Part 1 – 16 (Normal, Drum, FM-X, AN-X)_

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 2 | Insertion-B Type | Refer to Effect Parameter List | 00 00 |  |
| 2 | 2 | Insertion-B Preset Number | 00 00 – 7F 7F | 00 00 |  |
| 4 | 2 | Insertion-B Parameter 1 | Refer to Effect Parameter List for the selected type | 00 00 |  |
| 6 | 2 | Insertion-B Parameter 2 | Refer to Effect Parameter List for the selected type | 00 00 |  |
| 8 | 2 | Insertion-B Parameter 3 | Refer to Effect Parameter List for the selected type | 00 00 |  |
| 10 | 2 | Insertion-B Parameter 4 | Refer to Effect Parameter List for the selected type | 00 00 |  |
| 12 | 2 | Insertion-B Parameter 5 | Refer to Effect Parameter List for the selected type | 00 00 |  |
| 14 | 2 | Insertion-B Parameter 6 | Refer to Effect Parameter List for the selected type | 00 00 |  |
| 16 | 2 | Insertion-B Parameter 7 | Refer to Effect Parameter List for the selected type | 00 00 |  |
| 18 | 2 | Insertion-B Parameter 8 | Refer to Effect Parameter List for the selected type | 00 00 |  |
| 20 | 2 | Insertion-B Parameter 9 | Refer to Effect Parameter List for the selected type | 00 00 |  |
| 22 | 2 | Insertion-B Parameter 10 | Refer to Effect Parameter List for the selected type | 00 00 |  |
| 24 | 2 | Insertion-B Parameter 11 | Refer to Effect Parameter List for the selected type | 00 00 |  |
| 26 | 2 | Insertion-B Parameter 12 | Refer to Effect Parameter List for the selected type | 00 00 |  |
| 28 | 2 | Insertion-B Parameter 13 | Refer to Effect Parameter List for the selected type | 00 00 |  |
| 30 | 2 | Insertion-B Parameter 14 | Refer to Effect Parameter List for the selected type | 00 00 |  |
| 32 | 2 | Insertion-B Parameter 15 | Refer to Effect Parameter List for the selected type | 00 00 |  |
| 34 | 2 | Insertion-B Parameter 16 | Refer to Effect Parameter List for the selected type | 00 00 |  |
| 36 | 2 | Insertion-B Parameter 17 | Refer to Effect Parameter List for the selected type | 00 00 |  |
| 38 | 2 | Insertion-B Parameter 18 | Refer to Effect Parameter List for the selected type | 00 00 |  |
| 40 | 2 | Insertion-B Parameter 19 | Refer to Effect Parameter List for the selected type | 00 00 |  |
| 42 | 2 | Insertion-B Parameter 20 | Refer to Effect Parameter List for the selected type | 00 00 |  |
| 44 | 2 | Insertion-B Parameter 21 | Refer to Effect Parameter List for the selected type | 00 00 |  |
| 46 | 2 | Insertion-B Parameter 22 | Refer to Effect Parameter List for the selected type | 00 00 |  |
| 48 | 2 | Insertion-B Parameter 23 | Refer to Effect Parameter List for the selected type | 00 00 |  |
| 50 | 2 | Insertion-B Parameter 24 | Refer to Effect Parameter List for the selected type | 00 00 |  |

## `1p 00 06 00` — 100 bytes
`.pfm` block: `part.arp`
_p = Part number MONTAGE M Data List             242 Arp 1-8 Number      Arp 1-8 Number Extra Bank                                                        Description User            12032 – 12287                0               001 – 256 Library1          12288 – 12543                0               001 – 256 Library2          12544 – 12799                0               001 – 256 Library3          12800 – 13055                0               001 – 256 Library4          13056 – 13311                0               001 – 256 Library5          13312 – 13567                0               001 – 256 Library6          13568 – 13823                0               001 – 256 Library7          13824 – 14079                0               001 – 256 Library8          14080 – 14335                0               001 – 256 Library9          14336 – 14591                0               001 – 256 Library10         14592 – 14847                0               001 – 256 Library11         14848 – 15103                0               001 – 256 Library12         15104 – 15359                0               001 – 256 Library13         15360 – 15615                0               001 – 256 Library14         15616 – 15871                0               001 – 256 Library15         15872 – 16127                0               001 – 256 Library16         16128 – 16382                0               001 – 255 Library16              16383                   0                  256 Library17              16383                1 – 256            001 – 256 Library18              16383               257 – 512           001 – 256 Library19              16383               513 – 768           001 – 256 Library20              16383              769 – 1024           001 – 256 Library21              16383             1025 – 1280           001 – 256 Library22              16383             1281 – 1536           001 – 256 Library23              16383             1537 – 1792           001 – 256 Library24              16383             1793 – 2048           001 – 256_

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 2 | Arp Hold | Sync-Off, Off, On | 00 01 |  |
| 2 | 2 | Arp Unit Multiply | 50%, 66%, 75%, 100%, 133%, 150%, 200%, 266%, 300%, 400%, common | 00 03 |  |
| 4 | 2 | Arp Note Limit Low | C-2 – G8 | 00 00 |  |
| 6 | 2 | Arp Note Limit High | C-2 – G8 | 00 7F |  |
| 8 | 2 | Arp Velocity Limit Low | 1 – 127 | 00 01 |  |
| 10 | 2 | Arp Velocity Limit High | 1 – 127 | 00 7F |  |
| 12 | 2 | Arp Key Mode | Sort, Thru, Direct, Sort+Drct, Thru+Drct | 00 00 |  |
| 14 | 2 | Arp Velocity Mode | Original, Thru | 00 00 |  |
| 16 | 2 | Arp Change Timing | Real-time, Measure | 00 01 |  |
| 18 | 2 | Arp Quantize Value | 60, 80, 120, 160, 240, 320, 480 | 00 03 |  |
| 20 | 2 | Arp Quantize Strength | 0 – 100% | 00 00 |  |
| 22 | 2 | Arp Velocity Rate | 0 – 200% | 00 64 |  |
| 24 | 2 | Arp Gate Time Rate | 0 – 200% | 00 64 |  |
| 26 | 2 | Arp Accent Velocity Threshold | Off, 1 – 127 | 00 40 |  |
| 28 | 2 | Arp Octave Range | −3 – 0 – +3 | 00 40 |  |
| 30 | 2 | Arp Output Octave Shift | −10 – 0 – +10 | 00 40 |  |
| 32 | 2 | Arp Trigger Mode | Gate, Toggle | 00 00 |  |
| 34 | 2 | Arp Random SFX Velocity Offset | −64 – 0 – +63 | 00 40 |  |
| 36 | 2 | Arp 1 Velocity Rate Offset | −100 – 0 – +100 | 01 00 |  |
| 38 | 2 | Arp 1 Gate Time Rate Offset | 〃 | 01 00 |  |
| 40 | 2 | Arp 2 Velocity Rate Offset | 〃 | 01 00 |  |
| 42 | 2 | Arp 2 Gate Time Rate Offset | 〃 | 01 00 |  |
| 44 | 2 | Arp 3 Velocity Rate Offset | 〃 | 01 00 |  |
| 46 | 2 | Arp 3 Gate Time Rate Offset | 〃 | 01 00 |  |
| 48 | 2 | Arp 4 Velocity Rate Offset | 〃 | 01 00 |  |
| 50 | 2 | Arp 4 Gate Time Rate Offset | 〃 | 01 00 |  |
| 52 | 2 | Arp 5 Velocity Rate Offset | 〃 | 01 00 |  |
| 54 | 2 | Arp 5 Gate Time Rate Offset | 〃 | 01 00 |  |
| 56 | 2 | Arp 6 Velocity Rate Offset | 〃 | 01 00 |  |
| 58 | 2 | Arp 6 Gate Time Rate Offset | 〃 | 01 00 |  |
| 60 | 2 | Arp 7 Velocity Rate Offset | 〃 | 01 00 |  |
| 62 | 2 | Arp 7 Gate Time Rate Offset | 〃 | 01 00 |  |
| 64 | 2 | Arp 8 Velocity Rate Offset | 〃 | 01 00 |  |
| 66 | 2 | Arp 8 Gate Time Rate Offset | 〃 | 01 00 |  |
| 68 | 2 | Arp 1 Number | Preset (0=Off, 1 – 10239), User, Library (see the Arpeggio Number Table) | 00 00 |  |
| 70 | 2 | Arp 2 Number | Preset (0=Off, 1 – 10239), User, Library (see the Arpeggio Number Table) | 00 00 |  |
| 72 | 2 | Arp 3 Number | Preset (0=Off, 1 – 10239), User, Library (see the Arpeggio Number Table) | 00 00 |  |
| 74 | 2 | Arp 4 Number | Preset (0=Off, 1 – 10239), User, Library (see the Arpeggio Number Table) | 00 00 |  |
| 76 | 2 | Arp 5 Number | Preset (0=Off, 1 – 10239), User, Library (see the Arpeggio Number Table) | 00 00 |  |
| 78 | 2 | Arp 6 Number | Preset (0=Off, 1 – 10239), User, Library (see the Arpeggio Number Table | 00 00 |  |
| 80 | 2 | Arp 7 Number | Preset (0=Off, 1 – 10239), User, Library (see the Arpeggio Number Table) | 00 00 |  |
| 82 | 2 | Arp 8 Number | Preset (0=Off, 1 – 10239), User, Library (see the Arpeggio Number Table) | 00 00 |  |
| 84 | 2 | Arp 1 Number Extra | 0=Library16-256, 1 … 2048=Library17-1 … Library24-256 | 00 00 |  |
| 86 | 2 | Arp 2 Number Extra | 0=Library16-256, 1 … 2048=Library17-1 … Library24-256 | 00 00 |  |
| 88 | 2 | Arp 3 Number Extra | 0=Library16-256, 1 … 2048=Library17-1 … Library24-256 | 00 00 |  |
| 90 | 2 | Arp 4 Number Extra | 0=Library16-256, 1 … 2048=Library17-1 … Library24-256 | 00 00 |  |
| 92 | 2 | Arp 5 Number Extra | 0=Library16-256, 1 … 2048=Library17-1 … Library24-256 | 00 00 |  |
| 94 | 2 | Arp 6 Number Extra | 0=Library16-256, 1 … 2048=Library17-1 … Library24-256 | 00 00 |  |
| 96 | 2 | Arp 7 Number Extra | 0=Library16-256, 1 … 2048=Library17-1 … Library24-256 | 00 00 |  |
| 98 | 2 | Arp 8 Number Extra | 0=Library16-256, 1 … 2048=Library17-1 … Library24-256 | 00 00 |  |

## `1p 00 07 00` — 68 bytes
`.pfm` block: `part.lfo`
_p = Part number 00 – 0F               Part 1 – 16 (Normal, Drum, FM-X, AN-X)_

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 2 | LFO Phase | 0, 90, 120, 180, 240, 270 | 00 00 | LFO-related parameters hereinafter are not available for Drum Part. |
| 2 | 2 | LFO Wave | Triangle, Triangle+, Saw Up, Saw Down, Squ1/4, Squ1/3, Square, Squ2/3, Squ3/4, Trapezoid, S/H1, S/H2, User | 00 00 |  |
| 4 | 2 | LFO Speed | 0 – 63 | 00 20 | This is available only when Tempo Sync is set to Off. |
| 6 | 2 | LFO Tempo Speed | 5 – 24 (16th, 8th/3, 16th., 8th, 4th/3, 8th., 4th, 2th/3, 4th., 2nd, Whole/3, 2nd., 4thX4, 4thX5, 4thX6, 4thX7, 4thX8, 4thX16, 4thX32, 4thX64) | 00 0B | This is available only when Tempo Sync is set to On. |
| 8 | 2 | LFO Delay Time | 0 – 127 | 00 00 |  |
| 10 | 2 | LFO Fade In Time | 0 – 127 | 00 00 |  |
| 12 | 2 | LFO Hold Time | 0 – 126, Hold | 00 7F |  |
| 14 | 2 | LFO Fade Out Time | 0 – 127 | 00 40 |  |
| 16 | 2 | LFO Key On Reset | Off, Each-On,1st-On | 00 02 |  |
| 18 | 2 | LFO Destination 1 | 0 – 69 (Refer to LFO Box Destination of Control List) | 00 02 |  |
| 20 | 2 | LFO Depth 1 | 0 – 127 | 00 00 |  |
| 22 | 2 | LFO Destination 2 | 0 – 69 (Refer to LFO Box Destination of Control List) | 00 04 |  |
| 24 | 2 | LFO Depth 2 | 0 – 127 | 00 00 |  |
| 26 | 2 | LFO Destination 3 | 0 – 69 (Refer to LFO Box Destination of Control List) | 00 04 |  |
| 28 | 2 | LFO Depth 3 | 0 – 127 | 00 00 |  |
| 30 | 2 | User LFO Cycle | 2 steps, 3 steps, 4 steps, 6 steps, 8 steps, 12 steps, 16 steps | 00 06 |  |
| 32 | 2 | User LFO Slope | Off, Up, Down, Up&Down | 00 00 |  |
| 34 | 2 | User LFO Step Value 1 | −64 – +63 | 00 40 |  |
| 36 | 2 | User LFO Step Value 2 | −64 – +63 | 00 40 |  |
| 38 | 2 | User LFO Step Value 3 | −64 – +63 | 00 40 |  |
| 40 | 2 | User LFO Step Value 4 | −64 – +63 | 00 40 |  |
| 42 | 2 | User LFO Step Value 5 | −64 – +63 | 00 40 |  |
| 44 | 2 | User LFO Step Value 6 | −64 – +63 | 00 40 |  |
| 46 | 2 | User LFO Step Value 7 | −64 – +63 | 00 40 |  |
| 48 | 2 | User LFO Step Value 8 | −64 – +63 | 00 40 |  |
| 50 | 2 | User LFO Step Value 9 | −64 – +63 | 00 40 |  |
| 52 | 2 | User LFO Step Value 10 | −64 – +63 | 00 40 |  |
| 54 | 2 | User LFO Step Value 11 | −64 – +63 | 00 40 |  |
| 56 | 2 | User LFO Step Value 12 | −64 – +63 | 00 40 |  |
| 58 | 2 | User LFO Step Value 13 | −64 – +63 | 00 40 |  |
| 60 | 2 | User LFO Step Value 14 | −64 – +63 | 00 40 |  |
| 62 | 2 | User LFO Step Value 15 | −64 – +63 | 00 40 |  |
| 64 | 2 | User LFO Step Value 16 | −64 – +63 | 00 40 |  |
| 66 | 2 | Part LFO Random Speed Depth | 0 – 127 | 00 00 | This is available only when Tempo Sync is set to Off. |

## `1p 00 08 00` — 26 bytes
`.pfm` block: `part.zone`
_p = Part number 0–F                   Part 1 – 16 (Normal, Drum, FM-X, AN-X)_

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 2 | MIDI Transmit Channel | Ch1 – 16 | 00 | 0p This is available only when Part Mode is set to External. |
| 2 | 2 | MIDI Tx/Rx Channel Ch1 – 16, Off | 00 00 – 00 0F, 00 7F | 00 | 0p This is available only when Part Mode is set to Internal and Keyboard Control |
| 4 | 2 | Zone Octave Shift | −3 – +3 | 00 40 |  |
| 6 | 2 | Zone Transpose | −11 – +11 (semitones) | 00 40 |  |
| 8 | 2 | Zone Velocity Limit Low | 1 – 127 | 00 01 |  |
| 10 | 2 | Zone Velocity Limit High | 1 – 127 | 00 7F |  |
| 12 | 2 | Zone Note Limit Low | C-2 – G8 | 00 00 |  |
| 14 | 2 | Zone Note Limit High | C-2 – G8 | 00 7F |  |
| 16 | 2 | MIDI Volume | 0 – 127 | 00 64 |  |
| 18 | 2 | MIDI Pan | L64 – C – R63 | 00 40 |  |
| 20 | 2 | MIDI Bank | 0 – 127 | 00 00 |  |
| 22 | 2 | MIDI Bank LSB | 0 – 127 | 00 00 | 243 |
| 24 | 2 | MIDI Program Number | 1 – 128 | 00 00 |  |

## `1p 00 09 00` — 64 bytes
`.pfm` block: `part.keyctrl`
_p = Part number 0–F                   Part 1 – 16 (Normal, Drum, FM-X, AN-X)_

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 2 | Key Controller Set 1 Switch | Off, On | 00 00 |  |
| 2 | 2 | Key Controller Set 1 Destination | 1 – 58 | 00 01 |  |
| 4 | 2 | Key Controller Set 1 Curve Bank | 0 = Preset, 1 = User, 2 = Library1, – 17= Library16, – 25=Library24 | 00 00 |  |
| 6 | 2 | Key Controller Set 1 Curve Type | 0 – 31 (0 – 17 when Bank is set to Preset) | 00 00 |  |
| 8 | 2 | Key Controller Set 1 Curve Parameter 1 | 0 – 127 | 00 05 | Fixed to “0” except when Bank is set to Preset. |
| 10 | 2 | Key Controller Set 1 Curve Parameter 2 | 0 – 127 | 00 00 | Fixed to “0” except when Bank is set to Preset. |
| 12 | 2 | Key Controller Set 1 Polarity | Unipolar, Bipolar | 00 00 |  |
| 14 | 2 | Key Controller Set 1 Ratio | −128 – +127 | 01 40 |  |
| 16 | 2 | Key Controller Set 2 Switch | Off, On | 00 00 |  |
| 18 | 2 | Key Controller Set 2 Destination | 1 – 58 | 00 01 |  |
| 20 | 2 | Key Controller Set 2 Curve Bank | 0 = Preset, 1 = User, 2 = Library1, – 17= Library16, – 25=Library24 | 00 00 |  |
| 22 | 2 | Key Controller Set 2 Curve Type | 0 – 31 (0 – 17 when Bank is set to Preset) | 00 00 |  |
| 24 | 2 | Key Controller Set 2 Curve Parameter 1 | 0 – 127 | 00 05 | Fixed to “0” except when Bank is set to Preset. |
| 26 | 2 | Key Controller Set 2 Curve Parameter 2 | 0 – 127 | 00 00 | Fixed to “0” except when Bank is set to Preset. |
| 28 | 2 | Key Controller Set 2 Polarity | Unipolar, Bipolar | 00 00 |  |
| 30 | 2 | Key Controller Set 2 Ratio | −128 – +127 | 01 40 |  |
| 32 | 2 | Key Controller Set 3 Switch | Off, On | 00 00 |  |
| 34 | 2 | Key Controller Set 3 Destination | 1 – 58 | 00 01 |  |
| 36 | 2 | Key Controller Set 3 Curve Bank | 0 = Preset, 1 = User, 2 = Library1, – 17= Library16, – 25=Library24 | 00 00 |  |
| 38 | 2 | Key Controller Set 3 Curve Type | 0 – 31 (0 – 17 when Bank is set to Preset) | 00 00 |  |
| 40 | 2 | Key Controller Set 3 Curve Parameter 1 | 0 – 127 | 00 05 | Fixed to “0” except when Bank is set to Preset. |
| 42 | 2 | Key Controller Set 3 Curve Parameter 2 | 0 – 127 | 00 00 | Fixed to “0” except when Bank is set to Preset. |
| 44 | 2 | Key Controller Set 3 Polarity | Unipolar, Bipolar | 00 00 |  |
| 46 | 2 | Key Controller Set 3 Ratio | −128 – +127 | 01 40 |  |
| 48 | 2 | Key Controller Set 4 Switch | Off, On | 00 00 |  |
| 50 | 2 | Key Controller Set 4 Destination | 1 – 58 | 00 01 |  |
| 52 | 2 | Key Controller Set 4 Curve Bank | 0 = Preset, 1 = User, 2 = Library1, – 17= Library16, – 25=Library24 | 00 00 |  |
| 54 | 2 | Key Controller Set 4 Curve Type | 0 – 31 (0 – 17 when Bank is set to Preset) | 00 00 |  |
| 56 | 2 | Key Controller Set 4 Curve Parameter 1 | 0 – 127 | 00 05 | Fixed to “0” except when Bank is set to Preset. |
| 58 | 2 | Key Controller Set 4 Curve Parameter 2 | 0 – 127 | 00 00 | Fixed to “0” except when Bank is set to Preset. |
| 60 | 2 | Key Controller Set 4 Polarity | Unipolar, Bipolar | 00 00 |  |
| 62 | 2 | Key Controller Set 4 Ratio | −128 – +127 | 01 40 |  |

## `1p 03 0c 00` — 80 bytes
`.pfm` block: `part.scenes`
_p = Part number c = Scene number MONTAGE M Data List            245_

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 2 | Part Mute | Off, On | 00 00 |  |
| 2 | 2 | Volume | 0 – 127 | 00 64 |  |
| 4 | 2 | Pan | L63 – C – R63 | 00 40 |  |
| 6 | 2 | Reverb Send | 0 – 127 | 00 00 |  |
| 8 | 2 | Variation Send | 0 – 127 | 00 00 |  |
| 10 | 2 | Dry Level | 0 – 127 | 00 7F |  |
| 12 | 2 | Filter Cutoff Frequency | −64 – +63 | 00 40 | This is not available for FM-X or AN-X when “Scene Mixing / AEG Value Mode” is s |
| 14 | 2 | Filter Resonance/ Width | −64 – +63 | 00 40 | This is not available for FM-X or AN-X when “Scene Mixing / AEG Value Mode” is s |
| 16 | 2 | FEG Depth | −64 – +63 | 00 40 | This is not available for FM-X or AN-X when “Scene Mixing / AEG Value Mode” is s |
| 18 | 2 | AEG Attack Time | −64 – +63 | 00 40 | This is not available for AN-X when “Scene Mixing / AEG Value Mode” is set to “O |
| 20 | 2 | AEG Decay Time | −64 – +63 | 00 40 | This is not available for AN-X when “Scene Mixing / AEG Value Mode” is set to “O |
| 22 | 2 | AEG Sustain Level | −64 – +63 | 00 40 | This is not available for AN-X when “Scene Mixing / AEG Value Mode” is set to “O |
| 24 | 2 | AEG Release Time | −64 – +63 | 00 40 | This is not available for AN-X when “Scene Mixing / AEG Value Mode” is set to “O |
| 26 | 2 | FM-X Filter Cutoff Frequency | 0 – 1023 | 07 7F | This is available only for FM-X when “Scene Mixing / AEG Value Mode” is set to “ |
| 28 | 2 | FM-X Filter Resonance/Width | 0 – 127 | 00 0A | This is available only for FM-X when “Scene Mixing / AEG Value Mode” is set to “ |
| 30 | 2 | FM-X FEG Depth | −64 – +63 | 00 68 | This is available only for FM-X when “Scene Mixing / AEG Value Mode” is set to “ |
| 32 | 2 | AN-X Filter Cutoff Frequency | 14.3 – 21172.5 [Hz] | 07 7F | This is available only for AN-X when “Scene Mixing / AEG Value Mode” is set to “ |
| 34 | 2 | AN-X Filter Resonance | −6 – +42 [dB], 0.1875 [dB] step | 00 00 | This is available only for AN-X when “Scene Mixing / AEG Value Mode” is set to “ |
| 36 | 2 | AN-X FEG Depth | −9600 – +9600 [cent], 50 [cent] step | 02 00 | This is available only for AN-X when “Scene Mixing / AEG Value Mode” is set to “ |
| 38 | 2 | AN-X AEG Attack Time | 1 [ms] – 62 [s] | 00 00 | This is available only for AN-X when “Scene Mixing / AEG Value Mode” is set to “ |
| 40 | 2 | AN-X AEG Decay Time | 1 [ms] – 62 [s] | 01 20 | This is available only for AN-X when “Scene Mixing / AEG Value Mode” is set to “ |
| 42 | 2 | AN-X AEG Sustain Level | 0 – 511 | 03 7F | This is available only for AN-X when “Scene Mixing / AEG Value Mode” is set to “ |
| 44 | 2 | AN-X AEG Release Time | 1 [ms] – 62 [s] | 01 20 | This is available only for AN-X when “Scene Mixing / AEG Value Mode” is set to “ |
| 46 | 2 | Keyboard Control Switch | Off, On | 00 00 | Fixed to “Off” for Part 9 or later. |
| 48 | 2 | Swing | −120 – 0 – +120 | 01 00 |  |
| 50 | 2 | Arp Unit Multiply | 50%, 66%, 75%, 100%, 133%, 150%, 200%, 266%, 300%, 400%, common | 00 03 |  |
| 52 | 2 | Arp Gate Time Rate | 0 – 200% | 00 64 |  |
| 54 | 2 | Arp Velocity Rate | 0 – 200% | 00 64 |  |
| 56 | 2 | Motion Seq Amplitude Part Offset | −127 – +127 | 01 00 |  |
| 58 | 2 | Motion Seq Pulse Shape Part Offset | −100, −98, – 0, – +98, +100 | 00 40 |  |
| 60 | 2 | Motion Seq Smoothness Part Offset | −127 – +127 | 01 00 |  |
| 62 | 2 | Motion Seq Random | 0–127 | 00 00 |  |
| 64 | 2 | MIDI Volume | 0–127 | 00 64 | Available for External |
| 66 | 2 | MIDI Pan | L64–C–R63 | 00 40 | Available for External |
| 68 | 2 | Note Limit Low | C-2–G8 | 00 00 | Available for Internal |
| 70 | 2 | Note Limit High | C-2–G8 | 00 7F | Available for Internal |
| 72 | 2 | Note Shift | −48–+48 [semitones] | 00 40 | Available for Internal |
| 74 | 2 | Zone Note Limit Low | C-2–G8 | 00 00 | Available for External |
| 76 | 2 | Zone Note Limit High | C-2–G8 | 00 7F | Available for External |
| 78 | 2 | Zone Note Shift | −47–+47 [semitones] | 00 40 | Available for External |

## `1p 04 0k 00` — 16 bytes
`.pfm` block: `part.knobnames`
_p = Part number 00 – 0F               Part 1 – 16 (Normal, Drum, FM-X, AN-X) k = knob number 00 – 07               Knob 1 – 8_

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 1 | Assignable Knob 1 Name 1 | 0, 32 – 126 (ASCII) Assign 1-8 |  |  |
| 1 | 1 | Assignable Knob 1 Name 2 | 0, 32 – 126 (ASCII) (same as the knob |  |  |
| 2 | 1 | Assignable Knob 1 Name 3 | 0, 32 – 126 (ASCII) number) |  |  |
| 3 | 1 | Assignable Knob 1 Name 4 | 0, 32 – 126 (ASCII) |  |  |
| 4 | 1 | Assignable Knob 1 Name 5 | 0, 32 – 126 (ASCII) |  |  |
| 5 | 1 | Assignable Knob 1 Name 6 | 0, 32 – 126 (ASCII) |  |  |
| 6 | 1 | Assignable Knob 1 Name 7 | 0, 32 – 126 (ASCII) |  |  |
| 7 | 1 | Assignable Knob 1 Name 8 | 0, 32 – 126 (ASCII) |  |  |
| 8 | 1 | Assignable Knob 1 Name 9 | 0, 32 – 126 (ASCII) |  |  |
| 9 | 1 | Assignable Knob 1 Name 10 | 0, 32 – 126 (ASCII) |  |  |
| 10 | 1 | Assignable Knob 1 Name 11 | 0, 32 – 126 (ASCII) |  |  |
| 11 | 1 | Assignable Knob 1 Name 12 | 0, 32 – 126 (ASCII) |  |  |
| 12 | 1 | Assignable Knob 1 Name 13 | 0, 32 – 126 (ASCII) |  |  |
| 13 | 1 | Assignable Knob 1 Name 14 | 0, 32 – 126 (ASCII) |  |  |
| 14 | 1 | Assignable Knob 1 Name 15 | 0, 32 – 126 (ASCII) |  |  |
| 15 | 1 | Assignable Knob 1 Name 16 | 0, 32 – 126 (ASCII) |  |  |

## `1p 05 bb 00` — 18 bytes
`.pfm` block: `part.ctrlbox`
_p = Part number 00 – 0F               Part 1 – 16 (Normal, Drum, FM-X, AN-X) bb = box number 00 – 7F               Controller Box 1 – 32_

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 2 | Controller Set Switch | Off, On | 00 00 |  |
| 2 | 2 | Controller Set Source | 0 – 39 (Refer to Controller Box Source of Control List) | 00 01 |  |
| 4 | 2 | Controller Set Destination | 1 – 413 (Refer to Controller Box Destination of Control List) | 00 01 |  |
| 6 | 2 | Controller Set Curve Bank | 0 = Preset, 1 = User, 2 = Library1, – 17= Library16, – 25=Library24 | 00 00 |  |
| 8 | 2 | Controller Set Curve Type | 0 – 31 (0 – 17 when Bank is set to Preset) | 00 00 |  |
| 10 | 2 | Controller Set Curve Parameter 1 | 0 – 127 | 00 05 | Fixed to “0” except when Bank is set to Preset. |
| 12 | 2 | Controller Set Curve Parameter 2 | 0 – 127 | 00 00 | Fixed to “0” except when Bank is set to Preset. |
| 14 | 2 | Controller Set Polarity | Unipolar, Bipolar | 00 00 |  |
| 16 | 2 | Controller Set Ratio | −128 – +127 | 01 40 |  |

## `1p 06 L0 00` — 4 bytes
`.pfm` block: `part.lanes.l1`
_p = Part number 00 – 0F               Part 1 – 16 (Normal, Drum, FM-X, AN-X) L = Lane number 00 – 03               Lane 1 – 4_

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 1 | Lane Switch | Off, On | 00 |  |
| 1 | 1 | Lane FX Receive | Off, On | 01 |  |
| 2 | 1 | Lane Trigger Receive | Off, On | 00 |  |
| 3 | 1 | Lane Loop | Off, On | 01 |  |

## `1p 07 L0 00` — 20 bytes
`.pfm` block: `part.lanes.l2`
_p = Part number 00 – 0F               Part 1 – 16 (Normal, Drum, FM-X, AN-X) L = Lane number 00 – 03               Lane 1 – 4_

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 2 | Lane Sync | Off, Tempo, Beat, Arp, Lane1 | 00 00 | Lane 1 is not available for Lane 1. |
| 2 | 2 | Lane Speed | 0 – 127 | 00 3F | This is available only when Sync is set to Off. |
| 4 | 2 | Lane Unit Multiply | 50%, 66%, 75%, 100%, 133%, 150%, 200%, 266%, 300%, 400%, 600%, 800%, 1200%, 1600%, 2400%, 3200%, 6400%, Common, Arp | 00 03 | This is not available when Sync is set to Off. |
| 6 | 2 | Lane Key On Reset | Off, Each-On, 1st-On | 00 00 | This is not available when Sync is set to Arp. |
| 8 | 2 | Lane Velocity Limit Low | 1 – 127 | 00 01 |  |
| 10 | 2 | Lane Velocity Limit High | 1 – 127 | 00 7F |  |
| 12 | 2 | Lane Key On Delay Time Length | 0 – 127 | 00 00 |  |
| 14 | 2 | Lane Key On Delay Step Length | 0 – 32 | 00 00 |  |
| 16 | 2 | Lane Fade In Time Length | 0 – 127 | 00 00 |  |
| 18 | 2 | Lane Fade In Step Length | 0 – 32 | 00 00 |  |

## `1p 08 Lm 00` — 102 bytes
`.pfm` block: `part.lanes.seq`
_p = Part number L = Lane number m = sequence number MONTAGE M Data List     247_

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 2 | Lane Motion Seq Amplitude | 0 – 127 | 00 7F |  |
| 2 | 2 | Lane Motion Seq Smoothness | 0 – 127 | 00 00 |  |
| 4 | 2 | Lane Motion Seq Length | 1 – 16 | 00 0F |  |
| 6 | 2 | Lane Motion Seq Polarity | Unipolar, Bipolar | 00 00 |  |
| 8 | 2 | Motion Seq Grid | 60, 80, 120, 160, 240, 320, 480 | 00 03 |  |
| 10 | 2 | Lane Motion Seq Loop Start | 1 – 16 | 00 00 | This is not available when Loop is set to Off. Loop Start is less than or equal  |
| 12 | 2 | reserved | 00 00 | 00 00 |  |
| 14 | 2 | Lane Motion Seq Step 1 Value | 0 – 127 | 00 40 |  |
| 16 | 2 | Lane Motion Seq Step 2 Value | 0 – 127 | 00 40 |  |
| 18 | 2 | Lane Motion Seq Step 3 Value | 0 – 127 | 00 40 |  |
| 20 | 2 | Lane Motion Seq Step 4 Value | 0 – 127 | 00 40 |  |
| 22 | 2 | Lane Motion Seq Step 5 Value | 0 – 127 | 00 40 | 246 |
| 24 | 2 | Lane Motion Seq Step 6 Value | 0 – 127 | 00 40 |  |
| 26 | 2 | Lane Motion Seq Step 7 Value | 0 – 127 | 00 40 |  |
| 28 | 2 | Lane Motion Seq Step 8 Value | 0 – 127 | 00 40 |  |
| 30 | 2 | Lane Motion Seq Step 9 Value | 0 – 127 | 00 40 |  |
| 32 | 2 | Lane Motion Seq Step Value | 0 – 127 | 00 40 |  |
| 34 | 2 | Lane Motion Seq Step Value @34 | 0 – 127 | 00 40 |  |
| 36 | 2 | Lane Motion Seq Step Value @36 | 0 – 127 | 00 40 |  |
| 38 | 2 | Lane Motion Seq Step Value @38 | 0 – 127 | 00 40 |  |
| 40 | 2 | Lane Motion Seq Step Value @40 | 0 – 127 | 00 40 |  |
| 42 | 2 | Lane Motion Seq Step Value @42 | 0 – 127 | 00 40 |  |
| 44 | 2 | Lane Motion Seq Step Value @44 | 0 – 127 | 00 40 |  |
| 46 | 2 | Lane Motion Seq Step 1 A, B, Reverse A, Type | Reverse B | 00 00 |  |
| 48 | 2 | Lane Motion Seq Step 2 A, B, Reverse A, Type | Reverse B | 00 00 |  |
| 50 | 2 | Lane Motion Seq Step 3 A, B, Reverse A, Type | Reverse B | 00 00 |  |
| 52 | 2 | Lane Motion Seq Step 4 A, B, Reverse A, Type | Reverse B | 00 00 |  |
| 54 | 2 | Lane Motion Seq Step 5 A, B, Reverse A, Type | Reverse B | 00 00 |  |
| 56 | 2 | Lane Motion Seq Step 6 A, B, Reverse A, Type | Reverse B | 00 00 |  |
| 58 | 2 | Lane Motion Seq Step 7 A, B, Reverse A, Type | Reverse B | 00 00 |  |
| 60 | 2 | Lane Motion Seq Step 8 A, B, Reverse A, Type | Reverse B | 00 00 |  |
| 62 | 2 | Lane Motion Seq Step 9 A, B, Reverse A, Type | Reverse B | 00 00 |  |
| 64 | 2 | Lane Motion Seq Step Type | A, B, Reverse A, Reverse B | 00 00 |  |
| 66 | 2 | Lane Motion Seq Step Type @66 | A, B, Reverse A, Reverse B | 00 00 |  |
| 68 | 2 | Lane Motion Seq Step Type @68 | A, B, Reverse A, Reverse B | 00 00 |  |
| 70 | 2 | Lane Motion Seq Step Type @70 | A, B, Reverse A, Reverse B | 00 00 |  |
| 72 | 2 | Lane Motion Seq Step Type @72 | A, B, Reverse A, Reverse B | 00 00 |  |
| 74 | 2 | Lane Motion Seq Step Type @74 | A, B, Reverse A, Reverse B | 00 00 |  |
| 76 | 2 | Lane Motion Seq Step Type @76 | A, B, Reverse A, Reverse B | 00 00 |  |
| 78 | 2 | Lane Motion Seq Step Curve A Bank | 0 = Preset, 1 = User, 2 = Library1, – 17= Library16, – 25=Library24 | 00 00 |  |
| 80 | 2 | Lane Motion Seq Step Curve A Type | 0 – 31 (0 – 17 when Bank is set to Preset) | 00 00 |  |
| 82 | 2 | Lane Motion Seq Step Curve A Parameter 1 | 0 – 127 | 00 05 |  |
| 84 | 2 | Lane Motion Seq Step Curve A Parameter 2 | 0 – 127 | 00 00 |  |
| 86 | 2 | Lane Motion Seq Step Curve A Shape Control SW1 | Off, On | 00 01 |  |
| 88 | 2 | Lane Motion Seq Step Curve A Shape Control SW2 | Off, On | 00 00 |  |
| 90 | 2 | Lane Motion Seq Step Curve B Bank | 0 = Preset, 1 = User, 2 = Library1, – 17= Library16, – 25=Library24 | 00 00 |  |
| 92 | 2 | Lane Motion Seq Step Curve B Type | 0 – 31 (0 – 17 when Bank is set to Preset) | 00 00 |  |
| 94 | 2 | Lane Motion Seq Step Curve B Parameter 1 | 0 – 127 | 00 05 |  |
| 96 | 2 | Lane Motion Seq Step Curve B Parameter 2 | 0 – 127 | 00 00 |  |
| 98 | 2 | Lane Motion Seq Step Curve B Shape Control SW1 | Off, On | 00 01 |  |
| 100 | 2 | Lane Motion Seq Step Curve B Shape Control SW2 | Off, On | 00 00 |  |
