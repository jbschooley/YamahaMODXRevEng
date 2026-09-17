# PERFORMANCE COMMON

## `06 00 00 00` — 20 bytes
`.pfm` block: `common.name`

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 1 | Performance Name 1 | 0, 32 – 126 (ASCII) Initialized Perform |  |  |
| 1 | 1 | Performance Name 2 | 0, 32 – 126 (ASCII) |  |  |
| 2 | 1 | Performance Name 3 | 0, 32 – 126 (ASCII) |  |  |
| 3 | 1 | Performance Name 4 | 0, 32 – 126 (ASCII) |  |  |
| 4 | 1 | Performance Name 5 | 0, 32 – 126 (ASCII) |  |  |
| 5 | 1 | Performance Name 6 | 0, 32 – 126 (ASCII) |  |  |
| 6 | 1 | Performance Name 7 | 0, 32 – 126 (ASCII) |  |  |
| 7 | 1 | Performance Name 8 | 0, 32 – 126 (ASCII) |  |  |
| 8 | 1 | Performance Name 9 | 0, 32 – 126 (ASCII) |  |  |
| 9 | 1 | Performance Name | 0, 32 – 126 (ASCII) |  |  |
| 10 | 1 | Performance Name @10 | 0, 32 – 126 (ASCII) |  |  |
| 11 | 1 | Performance Name @11 | 0, 32 – 126 (ASCII) |  |  |
| 12 | 1 | Performance Name @12 | 0, 32 – 126 (ASCII) |  |  |
| 13 | 1 | Performance Name @13 | 0, 32 – 126 (ASCII) |  |  |
| 14 | 1 | Performance Name @14 | 0, 32 – 126 (ASCII) |  |  |
| 15 | 1 | Performance Name @15 | 0, 32 – 126 (ASCII) |  |  |
| 16 | 1 | Performance Name @16 | 0, 32 – 126 (ASCII) |  |  |
| 17 | 1 | Performance Name @17 | 0, 32 – 126 (ASCII) |  |  |
| 18 | 1 | Performance Name @18 | 0, 32 – 126 (ASCII) |  |  |
| 19 | 1 | Performance Name @19 | 0, 32 – 126 (ASCII) |  |  |

## `06 00 01 00` — 29 bytes
`.pfm` block: `common.c1`

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 1 | Portamento Switch | Off, On | 00 |  |
| 1 | 1 | Assignable Switch 1 Mode | Momentary, Latch | 01 |  |
| 2 | 1 | Assignable Switch 2 Mode | Momentary, Latch | 01 |  |
| 3 | 1 | Scene Mixing / AEG Value Mode | Absolute, Offset | 00 |  |
| 4 | 1 | Ribbon Controller Mode | Hold, Reset | 01 |  |
| 5 | 1 | Reverb Switch | Off, On | 01 |  |
| 6 | 1 | Variation Switch | Off, On | 01 |  |
| 7 | 1 | Master EQ Switch | Off, On | 01 |  |
| 8 | 1 | Master Effect Switch | Off, On | 00 |  |
| 9 | 1 | Arpeggio Master Switch | Off, On | 00 |  |
| 10 | 1 | Motion Seq Master Switch | Off, On | 00 |  |
| 11 | 1 | Assignable Knob1 Link Switch | Off, On | 01 |  |
| 12 | 1 | Assignable Knob2 Link Switch | Off, On | 01 |  |
| 13 | 1 | Assignable Knob3 Link Switch | Off, On | 01 |  |
| 14 | 1 | Assignable Knob4 Link Switch | Off, On | 01 |  |
| 15 | 1 | Assignable Knob5 Link Switch | Off, On | 01 |  |
| 16 | 1 | Assignable Knob6 Link Switch | Off, On | 01 |  |
| 17 | 1 | Assignable Knob7 Link Switch | Off, On | 01 |  |
| 18 | 1 | Assignable Knob8 Link Switch | Off, On | 01 |  |
| 19 | 1 | A/D Part Insertion FX A Switch | Off, On | 01 |  |
| 20 | 1 | A/D Part Insertion FX B Switch | Off, On | 01 |  |
| 21 | 1 | A/D Part Motion Seq Part Switch | Off, On | 01 |  |
| 22 | 1 | Super Knob Motion Seq Switch | Off, On | 00 |  |
| 23 | 1 | Super Knob Motion Seq FX Receive | Off, On | 01 |  |
| 24 | 1 | Super Knob Motion Seq Trigger Receive | Off, On | 00 |  |
| 25 | 1 | Super Knob Motion Seq Loop | Off, On | 01 |  |
| 26 | 1 | Keyboard After Touch Mode | Poly, Channel | 00 | This parameter is set to Channel on MONTAGE M6 and MONTAGE M7, regardless of the |
| 27 | 1 | Smart Morph Super Knob Link | Off, On | 00 |  |
| 28 | 1 | Slider Direction Part 1 –8 | Normal, Reverse | 00 |  |

## `06 00 02 00` — 86 bytes
`.pfm` block: `common.c2`

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 2 | Performance Main Category | 0 – 16 Refer to Performance (NoAsg) Category List | 00 10 |  |
| 2 | 2 | Performance Sub Category | 0–7 Refer to Performance (--) Category List | 00 00 |  |
| 4 | 2 | Selected Part | 1 – 16, Common | 00 10 |  |
| 6 | 2 | Performance Volume | 0 – 127 | 00 7F |  |
| 8 | 2 | Performance Pan | L63 – C – R63 | 00 40 |  |
| 10 | 2 | AEG Attack Time | −64 – +63 | 00 40 |  |
| 12 | 2 | AEG Decay Time | −64 – +63 | 00 40 |  |
| 14 | 2 | AEG Sustain Level | −64 – +63 | 00 40 |  |
| 16 | 2 | AEG Release Time | −64 – +63 | 00 40 |  |
| 18 | 2 | FEG Attack Time | −64 – +63 | 00 40 |  |
| 20 | 2 | FEG Decay Time | −64 – +63 | 00 40 |  |
| 22 | 2 | FEG Release Time | −64 – +63 | 00 40 |  |
| 24 | 2 | FEG Depth | −64 – +63 | 00 40 |  |
| 26 | 2 | Cutoff Frequency | −64 – +63 | 00 40 |  |
| 28 | 2 | Resonance | −64 – +63 | 00 40 |  |
| 30 | 2 | Tempo | 5 – 300 | 00 78 |  |
| 32 | 2 | Portamento Time | −64 – +63 | 00 40 |  |
| 34 | 2 | USB Main Monitor Volume | 0 – 127 | 00 7F |  |
| 36 | 2 | USB Assign Monitor Volume | 0 – 127 | 00 7F |  |
| 38 | 2 | Swing Offset | −120 – 0 – +120 | 01 00 |  |
| 40 | 2 | Unit Multiply | 50%, 66%, 75%, 100%, 133%, 150%, 200%, 266%, 300%, 400% | 00 03 |  |
| 42 | 2 | Scene Select | 1–8 | 00 00 |  |
| 44 | 2 | Audition Phrase Number | Preset (1 – 2320), User, Library (see the Audition Number Table) | 00 01 |  |
| 46 | 2 | Audition Note Shift | −24 – 24 | 00 40 |  |
| 48 | 2 | Audition Velocity Shift | −64 – 63 | 00 40 |  |
| 50 | 2 | Reverb Return | 0 – 127 | 00 40 |  |
| 52 | 2 | Reverb Pan | L63 – C – R63 | 00 40 |  |
| 54 | 2 | Variation Side Chain Part | 0: Part 1, 1: Part 2 – 15: Part 16, 16: A/D, 17: Master, 127: Off | 00 7F |  |
| 56 | 2 | Variation Return | 0 – 127 | 00 60 230 |  |
| 58 | 2 | Variation Pan | L63 – C – R63 | 00 40 |  |
| 60 | 2 | Send Variation To Reverb | 0 – 127 | 00 00 |  |
| 62 | 2 | Insertion-A Side Chain Part | 0: Part 1, 1: Part 2 – 15: Part 16, 16: A/D, 17: Master, 127: Off | 00 7F |  |
| 64 | 2 | Insertion-B Side Chain Part | 0: Part 1, 1: Part 2 – 15: Part 16, 16: A/D, 17: Master, 127: Off | 00 7F |  |
| 66 | 2 | Master Effect Side Chain Part | 0: Part 1, 1: Part 2 – 15: Part 16, 16: A/D, 17: Master, 127: Off | 00 7F |  |
| 68 | 2 | Master Effect Envelope Follower Gain | −24dB – 0dB – +24dB | 00 40 |  |
| 70 | 2 | Master Effect Envelope Follower Attack | 1ms – 40ms | 00 10 |  |
| 72 | 2 | Master Effect Envelope Follower Release | 10ms – 680ms | 00 07 |  |
| 74 | 2 | VCM Rotary Speaker Switch | Off, On | 00 00 |  |
| 76 | 2 | Split Points | Off, 1, 2, 3 | 00 00 |  |
| 78 | 2 | Split Point 1 | C#-2 – F8 | 00 3C |  |
| 80 | 2 | Split Point 2 | D-2 – F#8 | 00 48 |  |
| 82 | 2 | Split Point 3 | D#-2 – G8 | 00 54 |  |
| 84 | 2 | Performance Note Shift | -48–+48[semitones] | 00 40 |  |

## `06 00 03 00` — 86 bytes
`.pfm` block: `common.ctrl`

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 2 | Ribbon Controller Control Number | Off,1 – 95 | 00 10 |  |
| 2 | 2 | Breath Controller Control Number | Off,1 – 95 | 00 02 |  |
| 4 | 2 | Foot Controller 1 Control Number | Off,1 – 95, Super Knob | 00 0B |  |
| 6 | 2 | Foot Controller 2 Control Number | Off,1 – 95, Super Knob | 00 60 |  |
| 8 | 2 | Assignable Switch 1 Control Number | Off,1 – 95 | 00 56 |  |
| 10 | 2 | Assignable Switch 2 Control Number | Off,1 – 95 | 00 57 |  |
| 12 | 2 | reserved | 00 00 – 00 07 | 00 00 |  |
| 14 | 2 | Motion Seq Trigger Switch Control Number | Off,1 – 95 | 00 59 |  |
| 16 | 2 | Assignable Knob 1 Control Number | Off,1 – 95 | 00 11 |  |
| 18 | 2 | Assignable Knob 2 Control Number | Off,1 – 95 | 00 12 |  |
| 20 | 2 | Assignable Knob 3 Control Number | Off,1 – 95 | 00 13 |  |
| 22 | 2 | Assignable Knob 4 Control Number | Off,1 – 95 | 00 14 |  |
| 24 | 2 | Assignable Knob 5 Control Number | Off,1 – 95 | 00 15 |  |
| 26 | 2 | Assignable Knob 6 Control Number | Off,1 – 95 | 00 16 |  |
| 28 | 2 | Assignable Knob 7 Control Number | Off,1 – 95 | 00 17 |  |
| 30 | 2 | Assignable Knob 8 Control Number | Off,1 – 95 | 00 18 |  |
| 32 | 2 | Assignable Knob 1 Value | 0 – 1023 | 04 00 |  |
| 34 | 2 | Assignable Knob 2 Value | 0 – 1023 | 04 00 |  |
| 36 | 2 | Assignable Knob 3 Value | 0 – 1023 | 04 00 |  |
| 38 | 2 | Assignable Knob 4 Value | 0 – 1023 | 04 00 |  |
| 40 | 2 | Assignable Knob 5 Value | 0 – 1023 | 04 00 |  |
| 42 | 2 | Assignable Knob 6 Value | 0 – 1023 | 04 00 |  |
| 44 | 2 | Assignable Knob 7 Value | 0 – 1023 | 04 00 |  |
| 46 | 2 | Assignable Knob 8 Value | 0 – 1023 | 04 00 |  |
| 48 | 2 | Knob Mode | Selected Part, Multi, Groove, Assign | 00 03 |  |
| 50 | 2 | Common Knob Function Select | 0 – 14 | 00 01 |  |
| 52 | 2 | Multi Knob Function Select | Reverb, Variation, Dry Level, Pan, Volume | 00 00 |  |
| 54 | 2 | Groove Knob Function Quantize, Quantize Select | Strength, Swing, Note Shift, Clock Shift, Gate Time, Velocity Rate, Velocity Offset | 00 00 |  |
| 56 | 2 | AWM2 Knob Function Select | 0 – 17 | 00 00 |  |
| 58 | 2 | Drum Knob Function Select | 0 – 14 | 00 00 |  |
| 60 | 2 | FM-X Knob Function Select | 0 – 21 | 00 00 |  |
| 62 | 2 | AN-X Knob Function Select | 0 – 31 | 00 00 |  |
| 64 | 2 | Ribbon Grid Mode | Continuous, 5 steps, 3 steps | 00 00 |  |
| 66 | 2 | Ribbon Grid Control Part | 1 – 16, Common | 00 10 |  |
| 68 | 2 | Ribbon Grid Control Destination | Complies with Controller Box Destination | 00 00 |  |
| 70 | 2 | Ribbon Grid Step Value 1 | Depends on the Destination | 00 00 |  |
| 72 | 2 | Ribbon Grid Step Value 2 | Depends on the Destination | 00 00 |  |
| 74 | 2 | Ribbon Grid Step Value 3 | Depends on the Destination | 00 00 |  |
| 76 | 2 | Ribbon Grid Step Value 4 | Depends on the Destination | 00 00 |  |
| 78 | 2 | Ribbon Grid Step Value 5 | Depends on the Destination | 00 00 |  |
| 80 | 2 | Slider Mode | Part Control, Elem./ Op./Osc. Control | 00 00 |  |
| 82 | 2 | View Mode | Default, Part Info, Smart Morph, Motion Seq, Part-Note, Velocity-Note, Ribbon | 00 00 |  |
| 84 | 2 | reserved @84 | 00 00 – 7F 7F | 00 00 |  |

## `06 00 04 00` — 52 bytes
`.pfm` block: `common.ins.0`

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 2 | Insertion-A Type | Refer to Effect Parameter List | 00 00 | for A/D Part |
| 2 | 2 | Insertion-A Template Number | 00 00 – 7F 7F | 00 00 | 〃 |
| 4 | 2 | Insertion-A Parameter 1 | Refer to Effect Parameter List for the selected type | 00 00 | 〃 |
| 6 | 2 | Insertion-A Parameter 2 | Refer to Effect Parameter List for the selected type | 00 00 | 〃 |
| 8 | 2 | Insertion-A Parameter 3 | Refer to Effect Parameter List for the selected type | 00 00 | 〃 |
| 10 | 2 | Insertion-A Parameter 4 | Refer to Effect Parameter List for the selected type | 00 00 | 〃 |
| 12 | 2 | Insertion-A Parameter 5 | Refer to Effect Parameter List for the selected type | 00 00 | 〃 |
| 14 | 2 | Insertion-A Parameter 6 | Refer to Effect Parameter List for the selected type | 00 00 | 〃 |
| 16 | 2 | Insertion-A Parameter 7 | Refer to Effect Parameter List for the selected type | 00 00 | 〃 |
| 18 | 2 | Insertion-A Parameter 8 | Refer to Effect Parameter List for the selected type | 00 00 | 〃 |
| 20 | 2 | Insertion-A Parameter 9 | Refer to Effect Parameter List for the selected type | 00 00 | 〃 |
| 22 | 2 | Insertion-A Parameter 10 | Refer to Effect Parameter List for the selected type | 00 00 | 〃 |
| 24 | 2 | Insertion-A Parameter 11 | Refer to Effect Parameter List for the selected type | 00 00 | 〃 |
| 26 | 2 | Insertion-A Parameter 12 | Refer to Effect Parameter List for the selected type | 00 00 | 〃 |
| 28 | 2 | Insertion-A Parameter 13 | Refer to Effect Parameter List for the selected type | 00 00 | 〃 |
| 30 | 2 | Insertion-A Parameter 14 | Refer to Effect Parameter List for the selected type | 00 00 | 〃 |
| 32 | 2 | Insertion-A Parameter 15 | Refer to Effect Parameter List for the selected type | 00 00 | 〃 |
| 34 | 2 | Insertion-A Parameter 16 | Refer to Effect Parameter List for the selected type | 00 00 | 〃 |
| 36 | 2 | Insertion-A Parameter 17 | Refer to Effect Parameter List for the selected type | 00 00 | 〃 |
| 38 | 2 | Insertion-A Parameter 18 | Refer to Effect Parameter List for the selected type | 00 00 | 〃 |
| 40 | 2 | Insertion-A Parameter 19 | Refer to Effect Parameter List for the selected type | 00 00 | 〃 |
| 42 | 2 | Insertion-A Parameter 20 | Refer to Effect Parameter List for the selected type | 00 00 | 〃 |
| 44 | 2 | Insertion-A Parameter 21 | Refer to Effect Parameter List for the selected type | 00 00 | 〃 |
| 46 | 2 | Insertion-A Parameter 22 | Refer to Effect Parameter List for the selected type | 00 00 | 〃 |
| 48 | 2 | Insertion-A Parameter 23 | Refer to Effect Parameter List for the selected type | 00 00 | 〃 |
| 50 | 2 | Insertion-A Parameter 24 | Refer to Effect Parameter List for the selected type | 00 00 | 〃 |

## `06 00 05 00` — 52 bytes
`.pfm` block: `common.ins.1`

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 2 | Insertion-B Type | Refer to Effect Parameter List | 00 00 | for A/D Part |
| 2 | 2 | Insertion-B Preset Number | 00 00 – 7F 7F | 00 00 | 〃 |
| 4 | 2 | Insertion-B Parameter 1 | Refer to Effect Parameter List for the selected type | 00 00 | 〃 |
| 6 | 2 | Insertion-B Parameter 2 | Refer to Effect Parameter List for the selected type | 00 00 | 〃 |
| 8 | 2 | Insertion-B Parameter 3 | Refer to Effect Parameter List for the selected type | 00 00 | 〃 |
| 10 | 2 | Insertion-B Parameter 4 | Refer to Effect Parameter List for the selected type | 00 00 | 〃 |
| 12 | 2 | Insertion-B Parameter 5 | Refer to Effect Parameter List for the selected type | 00 00 | 〃 |
| 14 | 2 | Insertion-B Parameter 6 | Refer to Effect Parameter List for the selected type | 00 00 | 〃 |
| 16 | 2 | Insertion-B Parameter 7 | Refer to Effect Parameter List for the selected type | 00 00 | 〃 |
| 18 | 2 | Insertion-B Parameter 8 | Refer to Effect Parameter List for the selected type | 00 00 | 〃 |
| 20 | 2 | Insertion-B Parameter 9 | Refer to Effect Parameter List for the selected type | 00 00 | 〃 |
| 22 | 2 | Insertion-B Parameter 10 | Refer to Effect Parameter List for the selected type | 00 00 | 〃 |
| 24 | 2 | Insertion-B Parameter 11 | Refer to Effect Parameter List for the selected type | 00 00 | 〃 |
| 26 | 2 | Insertion-B Parameter 12 | Refer to Effect Parameter List for the selected type | 00 00 | 〃 |
| 28 | 2 | Insertion-B Parameter 13 | Refer to Effect Parameter List for the selected type | 00 00 | 〃 |
| 30 | 2 | Insertion-B Parameter 14 | Refer to Effect Parameter List for the selected type | 00 00 | 〃 |
| 32 | 2 | Insertion-B Parameter 15 | Refer to Effect Parameter List for the selected type | 00 00 | 〃 |
| 34 | 2 | Insertion-B Parameter 16 | Refer to Effect Parameter List for the selected type | 00 00 | 〃 |
| 36 | 2 | Insertion-B Parameter 17 | Refer to Effect Parameter List for the selected type | 00 00 | 〃 |
| 38 | 2 | Insertion-B Parameter 18 | Refer to Effect Parameter List for the selected type | 00 00 | 〃 |
| 40 | 2 | Insertion-B Parameter 19 | Refer to Effect Parameter List for the selected type | 00 00 | 〃 |
| 42 | 2 | Insertion-B Parameter 20 | Refer to Effect Parameter List for the selected type | 00 00 | 〃 |
| 44 | 2 | Insertion-B Parameter 21 | Refer to Effect Parameter List for the selected type | 00 00 | 〃 |
| 46 | 2 | Insertion-B Parameter 22 | Refer to Effect Parameter List for the selected type | 00 00 | 〃 |
| 48 | 2 | Insertion-B Parameter 23 | Refer to Effect Parameter List for the selected type | 00 00 | 〃 |
| 50 | 2 | Insertion-B Parameter 24 | Refer to Effect Parameter List for the selected type | 00 00 | 〃 |

## `06 00 06 00` — 14 bytes
`.pfm` block: `common.arp`

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 2 | Arpeggio Select | 1–8 | 00 00 |  |
| 2 | 2 | Arpeggio Synchro Quantize Value | Off, 60, 80, 120, 160, 240, 320, 480 | 00 00 |  |
| 4 | 2 | Arpeggio Quantize Strength Offset | −100 – +100 | 01 00 |  |
| 6 | 2 | Arpeggio Gate Time Rate Offset | −100 – 0 – +100 | 01 00 |  |
| 8 | 2 | Arpeggio Velocity Rate Offset | 〃 | 01 00 |  |
| 10 | 2 | Arpeggio Octave Range Offset | −6 – +6 | 00 40 |  |
| 12 | 2 | Arpeggio Output Octave Shift Offset | −20 – +20 | 00 40 |  |

## `06 00 07 00` — 52 bytes
`.pfm` block: `common.reverb`

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 2 | Reverb Type | Refer to Effect Parameter List | 01 00 |  |
| 2 | 2 | Reverb Preset Number | 00 00 – 7F 7F | 00 00 |  |
| 4 | 2 | Reverb Parameter 1 | Refer to Effect Parameter List for the selected type | Hall / Basic |  |
| 6 | 2 | Reverb Parameter 2 | Refer to Effect Parameter List for the selected type | Hall / Basic |  |
| 8 | 2 | Reverb Parameter 3 | Refer to Effect Parameter List for the selected type | Hall / Basic |  |
| 10 | 2 | Reverb Parameter 4 | Refer to Effect Parameter List for the selected type | Hall / Basic |  |
| 12 | 2 | Reverb Parameter 5 | Refer to Effect Parameter List for the selected type | Hall / Basic |  |
| 14 | 2 | Reverb Parameter 6 | Refer to Effect Parameter List for the selected type | Hall / Basic |  |
| 16 | 2 | Reverb Parameter 7 | Refer to Effect Parameter List for the selected type | Hall / Basic |  |
| 18 | 2 | Reverb Parameter 8 | Refer to Effect Parameter List for the selected type | Hall / Basic |  |
| 20 | 2 | Reverb Parameter 9 | Refer to Effect Parameter List for the selected type | Hall / Basic |  |
| 22 | 2 | Reverb Parameter 10 | Refer to Effect Parameter List for the selected type | Hall / Basic |  |
| 24 | 2 | Reverb Parameter 11 | Refer to Effect Parameter List for the selected type | Hall / Basic |  |
| 26 | 2 | Reverb Parameter 12 | Refer to Effect Parameter List for the selected type | Hall / Basic |  |
| 28 | 2 | Reverb Parameter 13 | Refer to Effect Parameter List for the selected type | Hall / Basic |  |
| 30 | 2 | Reverb Parameter 14 | Refer to Effect Parameter List for the selected type | Hall / Basic |  |
| 32 | 2 | Reverb Parameter 15 | Refer to Effect Parameter List for the selected type | Hall / Basic Default MSB/LSB |  |
| 34 | 2 | Reverb Parameter 16 | Refer to Effect Parameter List for the selected type | Hall / Basic |  |
| 36 | 2 | Reverb Parameter 17 | Refer to Effect Parameter List for the selected type | Hall / Basic |  |
| 38 | 2 | Reverb Parameter 18 | Refer to Effect Parameter List for the selected type | Hall / Basic |  |
| 40 | 2 | Reverb Parameter 19 | Refer to Effect Parameter List for the selected type | Hall / Basic |  |
| 42 | 2 | Reverb Parameter 20 | Refer to Effect Parameter List for the selected type | Hall / Basic |  |
| 44 | 2 | Reverb Parameter 21 | Refer to Effect Parameter List for the selected type | Hall / Basic |  |
| 46 | 2 | Reverb Parameter 22 | Refer to Effect Parameter List for the selected type | Hall / Basic |  |
| 48 | 2 | Reverb Parameter 23 | Refer to Effect Parameter List for the selected type | Hall / Basic |  |
| 50 | 2 | Reverb Parameter 24 | Refer to Effect Parameter List for the selected type | Hall / Basic |  |

## `06 00 08 00` — 52 bytes
`.pfm` block: `common.variation`

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 2 | Variation Type | Refer to Effect Parameter List | 03 00 |  |
| 2 | 2 | Variation Preset Number | 00 00 – 7F 7F | 00 00 |  |
| 4 | 2 | Variation Parameter 1 | Refer to Effect Parameter List for the selected type | Chorus / Baisc |  |
| 6 | 2 | Variation Parameter 2 | Refer to Effect Parameter List for the selected type | Chorus / Baisc |  |
| 8 | 2 | Variation Parameter 3 | Refer to Effect Parameter List for the selected type | Chorus / Baisc |  |
| 10 | 2 | Variation Parameter 4 | Refer to Effect Parameter List for the selected type | Chorus / Baisc |  |
| 12 | 2 | Variation Parameter 5 | Refer to Effect Parameter List for the selected type | Chorus / Baisc |  |
| 14 | 2 | Variation Parameter 6 | Refer to Effect Parameter List for the selected type | Chorus / Baisc |  |
| 16 | 2 | Variation Parameter 7 | Refer to Effect Parameter List for the selected type | Chorus / Baisc |  |
| 18 | 2 | Variation Parameter 8 | Refer to Effect Parameter List for the selected type | Chorus / Baisc |  |
| 20 | 2 | Variation Parameter 9 | Refer to Effect Parameter List for the selected type | Chorus / Baisc |  |
| 22 | 2 | Variation Parameter 10 | Refer to Effect Parameter List for the selected type | Chorus / Baisc |  |
| 24 | 2 | Variation Parameter 11 | Refer to Effect Parameter List for the selected type | Chorus / Baisc |  |
| 26 | 2 | Variation Parameter 12 | Refer to Effect Parameter List for the selected type | Chorus / Baisc |  |
| 28 | 2 | Variation Parameter 13 | Refer to Effect Parameter List for the selected type | Chorus / Baisc |  |
| 30 | 2 | Variation Parameter 14 | Refer to Effect Parameter List for the selected type | Chorus / Baisc |  |
| 32 | 2 | Variation Parameter 15 | Refer to Effect Parameter List for the selected type | Chorus / Baisc |  |
| 34 | 2 | Variation Parameter 16 | Refer to Effect Parameter List for the selected type | Chorus / Baisc |  |
| 36 | 2 | Variation Parameter 17 | Refer to Effect Parameter List for the selected type | Chorus / Baisc |  |
| 38 | 2 | Variation Parameter 18 | Refer to Effect Parameter List for the selected type | Chorus / Baisc |  |
| 40 | 2 | Variation Parameter 19 | Refer to Effect Parameter List for the selected type | Chorus / Baisc |  |
| 42 | 2 | Variation Parameter 20 | Refer to Effect Parameter List for the selected type | Chorus / Baisc |  |
| 44 | 2 | Variation Parameter 21 | Refer to Effect Parameter List for the selected type | Chorus / Baisc |  |
| 46 | 2 | Variation Parameter 22 | Refer to Effect Parameter List for the selected type | Chorus / Baisc |  |
| 48 | 2 | Variation Parameter 23 | Refer to Effect Parameter List for the selected type | Chorus / Baisc |  |
| 50 | 2 | Variation Parameter 24 | Refer to Effect Parameter List for the selected type | Chorus / Baisc |  |

## `06 00 09 00` — 68 bytes
`.pfm` block: `common.rotary`

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 2 | VCM Rotary Speaker Type | Refer to Effect Parameter List | 06 42 |  |
| 2 | 2 | VCM Rotary Speaker Preset Number | 00 00 – 7F 7F | 00 00 |  |
| 4 | 2 | VCM Rotary Speaker Parameter 1 | Refer to Effect Parameter List for the selected type | Rotary Speaker Studio/Basic |  |
| 6 | 2 | VCM Rotary Speaker Parameter 2 | Refer to Effect Parameter List for the selected type | Rotary Speaker Studio/Basic |  |
| 8 | 2 | VCM Rotary Speaker Parameter 3 | Refer to Effect Parameter List for the selected type | Rotary Speaker Studio/Basic |  |
| 10 | 2 | VCM Rotary Speaker Parameter 4 | Refer to Effect Parameter List for the selected type | Rotary Speaker Studio/Basic |  |
| 12 | 2 | VCM Rotary Speaker Parameter 5 | Refer to Effect Parameter List for the selected type | Rotary Speaker Studio/Basic |  |
| 14 | 2 | VCM Rotary Speaker Parameter 6 | Refer to Effect Parameter List for the selected type | Rotary Speaker Studio/Basic |  |
| 16 | 2 | VCM Rotary Speaker Parameter 7 | Refer to Effect Parameter List for the selected type | Rotary Speaker Studio/Basic |  |
| 18 | 2 | VCM Rotary Speaker Parameter 8 | Refer to Effect Parameter List for the selected type | Rotary Speaker Studio/Basic |  |
| 20 | 2 | VCM Rotary Speaker Parameter 9 | Refer to Effect Parameter List for the selected type | Rotary Speaker Studio/Basic |  |
| 22 | 2 | VCM Rotary Speaker Parameter 10 | Refer to Effect Parameter List for the selected type | Rotary Speaker Studio/Basic |  |
| 24 | 2 | VCM Rotary Speaker Parameter 11 | Refer to Effect Parameter List for the selected type | Rotary Speaker Studio/Basic |  |
| 26 | 2 | VCM Rotary Speaker Parameter 12 | Refer to Effect Parameter List for the selected type | Rotary Speaker Studio/Basic |  |
| 28 | 2 | VCM Rotary Speaker Parameter 13 | Refer to Effect Parameter List for the selected type | Rotary Speaker Studio/Basic |  |
| 30 | 2 | VCM Rotary Speaker Parameter 14 | Refer to Effect Parameter List for the selected type | Rotary Speaker Studio/Basic |  |
| 32 | 2 | VCM Rotary Speaker Parameter 15 | Refer to Effect Parameter List for the selected type | Rotary Speaker Studio/Basic |  |
| 34 | 2 | VCM Rotary Speaker Parameter 16 | Refer to Effect Parameter List for the selected type | Rotary Speaker Studio/Basic |  |
| 36 | 2 | VCM Rotary Speaker Parameter 17 | Refer to Effect Parameter List for the selected type | Rotary Speaker Studio/Basic |  |
| 38 | 2 | VCM Rotary Speaker Parameter 18 | Refer to Effect Parameter List for the selected type | Rotary Speaker Studio/Basic |  |
| 40 | 2 | VCM Rotary Speaker Parameter 19 | Refer to Effect Parameter List for the selected type | Rotary Speaker Studio/Basic |  |
| 42 | 2 | VCM Rotary Speaker Parameter 20 | Refer to Effect Parameter List for the selected type | Rotary Speaker Studio/Basic |  |
| 44 | 2 | VCM Rotary Speaker Parameter 21 | Refer to Effect Parameter List for the selected type | Rotary Speaker Studio/Basic |  |
| 46 | 2 | VCM Rotary Speaker Parameter 22 | Refer to Effect Parameter List for the selected type | Rotary Speaker Studio/Basic |  |
| 48 | 2 | VCM Rotary Speaker Parameter 23 | Refer to Effect Parameter List for the selected type | Rotary Speaker Studio/Basic |  |
| 50 | 2 | VCM Rotary Speaker Parameter 24 | Refer to Effect Parameter List for the selected type | Rotary Speaker Studio/Basic |  |
| 52 | 2 | VCM Rotary Speaker Parameter 25 | Refer to Effect Parameter List for the selected type | Rotary Speaker Studio/Basic |  |
| 54 | 2 | VCM Rotary Speaker Parameter 26 | Refer to Effect Parameter List for the selected type | Rotary Speaker Studio/Basic |  |
| 56 | 2 | VCM Rotary Speaker Parameter 27 | Refer to Effect Parameter List for the selected type | Rotary Speaker Studio/Basic |  |
| 58 | 2 | VCM Rotary Speaker Parameter 28 | Refer to Effect Parameter List for the selected type | Rotary Speaker Studio/Basic |  |
| 60 | 2 | VCM Rotary Speaker Parameter 29 | Refer to Effect Parameter List for the selected type | Rotary Speaker Studio/Basic Default MSB/LSB |  |
| 62 | 2 | VCM Rotary Speaker Parameter 30 | Refer to Effect Parameter List for the selected type | Rotary Speaker Studio/Basic |  |
| 64 | 2 | VCM Rotary Speaker Parameter 31 | Refer to Effect Parameter List for the selected type | Rotary Speaker Studio/Basic |  |
| 66 | 2 | VCM Rotary Speaker Parameter 32 | Refer to Effect Parameter List for the selected type | Rotary Speaker Studio/Basic |  |

## `06 00 0A 00` — 34 bytes
`.pfm` block: `common.meq`

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 2 | Master EQ Low Gain | −12 – +12 [dB] | 00 40 |  |
| 2 | 2 | Master EQ Low Frequency | 32 – 2000 [Hz] | 00 0C |  |
| 4 | 2 | Master EQ Low Q | 0. 1 – 12.0 | 00 07 | This is not available when “shelving” is selected. |
| 6 | 2 | Master EQ Low Shape | Shelf, Peak | 00 00 |  |
| 8 | 2 | Master EQ Low Mid Gain | −12 – +12 [dB] | 00 40 |  |
| 10 | 2 | Master EQ Low Mid Frequency | 100 – 10.0 [kHz] | 00 14 |  |
| 12 | 2 | Master EQ Low Mid Q | 0.1 – 12.0 | 00 07 |  |
| 14 | 2 | Master EQ Mid Gain | −12 – +12 [dB] | 00 40 |  |
| 16 | 2 | Master EQ Mid Frequency | 100 – 10.0 [kHz] | 00 1C |  |
| 18 | 2 | Master EQ Mid Q | 0.1 – 12.0 | 00 07 |  |
| 20 | 2 | Master EQ High Mid Gain | −12 – +12 [dB] | 00 40 |  |
| 22 | 2 | Master EQ High Mid Frequency | 100 – 10.0 [kHz] | 00 2C |  |
| 24 | 2 | Master EQ High Mid Q | 0.1 – 12.0 | 00 07 |  |
| 26 | 2 | Master EQ High Gain | −12 – +12 [dB] | 00 40 |  |
| 28 | 2 | Master EQ High Frequency | 0.5 – 16.0 [kHz] | 00 34 |  |
| 30 | 2 | Master EQ High Q | 0.1 – 12.0 | 00 07 | This is not available when “shelving” is selected. |
| 32 | 2 | Master EQ High Shape | Shelf, Peak | 00 00 |  |

## `06 00 0B 00` — 52 bytes
`.pfm` block: `common.mfx`

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 2 | Master Effect Type | Refer to Effect Parameter List | 08 20 |  |
| 2 | 2 | Master Effect Preset Number | 00 00 – 7F 7F | 00 00 |  |
| 4 | 2 | Master Effect Parameter 1 | Refer to Effect Parameter List for the selected type | Multi Band Comp / Basic |  |
| 6 | 2 | Master Effect Parameter 2 | Refer to Effect Parameter List for the selected type | Multi Band Comp / Basic |  |
| 8 | 2 | Master Effect Parameter 3 | Refer to Effect Parameter List for the selected type | Multi Band Comp / Basic |  |
| 10 | 2 | Master Effect Parameter 4 | Refer to Effect Parameter List for the selected type | Multi Band Comp / Basic |  |
| 12 | 2 | Master Effect Parameter 5 | Refer to Effect Parameter List for the selected type | Multi Band Comp / Basic |  |
| 14 | 2 | Master Effect Parameter 6 | Refer to Effect Parameter List for the selected type | Multi Band Comp / Basic |  |
| 16 | 2 | Master Effect Parameter 7 | Refer to Effect Parameter List for the selected type | Multi Band Comp / Basic |  |
| 18 | 2 | Master Effect Parameter 8 | Refer to Effect Parameter List for the selected type | Multi Band Comp / Basic |  |
| 20 | 2 | Master Effect Parameter 9 | Refer to Effect Parameter List for the selected type | Multi Band Comp / Basic |  |
| 22 | 2 | Master Effect Parameter 10 | Refer to Effect Parameter List for the selected type | Multi Band Comp / Basic |  |
| 24 | 2 | Master Effect Parameter 11 | Refer to Effect Parameter List for the selected type | Multi Band Comp / Basic |  |
| 26 | 2 | Master Effect Parameter 12 | Refer to Effect Parameter List for the selected type | Multi Band Comp / Basic |  |
| 28 | 2 | Master Effect Parameter 13 | Refer to Effect Parameter List for the selected type | Multi Band Comp / Basic |  |
| 30 | 2 | Master Effect Parameter 14 | Refer to Effect Parameter List for the selected type | Multi Band Comp / Basic |  |
| 32 | 2 | Master Effect Parameter 15 | Refer to Effect Parameter List for the selected type | Multi Band Comp / Basic |  |
| 34 | 2 | Master Effect Parameter 16 | Refer to Effect Parameter List for the selected type | Multi Band Comp / Basic |  |
| 36 | 2 | Master Effect Parameter 17 | Refer to Effect Parameter List for the selected type | Multi Band Comp / Basic |  |
| 38 | 2 | Master Effect Parameter 18 | Refer to Effect Parameter List for the selected type | Multi Band Comp / Basic |  |
| 40 | 2 | Master Effect Parameter 19 | Refer to Effect Parameter List for the selected type | Multi Band Comp / Basic |  |
| 42 | 2 | Master Effect Parameter 20 | Refer to Effect Parameter List for the selected type | Multi Band Comp / Basic |  |
| 44 | 2 | Master Effect Parameter 21 | Refer to Effect Parameter List for the selected type | Multi Band Comp / Basic |  |
| 46 | 2 | Master Effect Parameter 22 | Refer to Effect Parameter List for the selected type | Multi Band Comp / Basic |  |
| 48 | 2 | Master Effect Parameter 23 | Refer to Effect Parameter List for the selected type | Multi Band Comp / Basic |  |
| 50 | 2 | Master Effect Parameter 24 | Refer to Effect Parameter List for the selected type | Multi Band Comp / Basic |  |

## `06 00 0C 00` — 12 bytes
`.pfm` block: `common.msq`

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 2 | Motion Seq Select | 1–8 | 00 00 |  |
| 2 | 2 | Motion Seq Amplitude Performance Offset | −127 – +127 | 01 00 |  |
| 4 | 2 | Motion Seq Pulse Shape Performance Offset | −100, −98, – 0, – +98, +100 | 00 40 |  |
| 6 | 2 | Motion Seq Smoothness Performance Offset | −127 – +127 | 01 00 |  |
| 8 | 2 | Motion Seq Random Performance Offset | −127 – +127 | 01 00 |  |
| 10 | 2 | Motion Seq View Lane Common | Super Knob, 1, 2, 3, 4 | 00 00 |  |

## `06 00 0D 00` — 90 bytes
`.pfm` block: `common.superknob`

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 2 | Super Knob Value | 0 – 1023 | 04 00 |  |
| 2 | 2 | Super Knob Mid Position | Off, 1 – 1022 | 00 00 |  |
| 4 | 2 | Assignable Knob 1 Destination Left Value | 0 – 1023 | 00 00 |  |
| 6 | 2 | Assignable Knob 1 Destination Mid Value | 0 – 1023 | 04 00 |  |
| 8 | 2 | Assignable Knob 1 Destination Right Value | 0 – 1023 | 07 7F |  |
| 10 | 2 | Assignable Knob 2 Destination Left Value | 0 – 1023 | 00 00 |  |
| 12 | 2 | Assignable Knob 2 Destination Mid Value | 0 – 1023 | 04 00 |  |
| 14 | 2 | Assignable Knob 2 Destination Right Value | 0 – 1023 | 07 7F |  |
| 16 | 2 | Assignable Knob 3 Destination Left Value | 0 – 1023 | 00 00 |  |
| 18 | 2 | Assignable Knob 3 Destination Mid Value | 0 – 1023 | 04 00 |  |
| 20 | 2 | Assignable Knob 3 Destination Right Value | 0 – 1023 | 07 7F |  |
| 22 | 2 | Assignable Knob 4 Destination Left Value | 0 – 1023 | 00 00 |  |
| 24 | 2 | Assignable Knob 4 Destination Mid Value | 0 – 1023 | 04 00 |  |
| 26 | 2 | Assignable Knob 4 Destination Right Value | 0 – 1023 | 07 7F |  |
| 28 | 2 | Assignable Knob 5 Destination Left Value | 0 – 1023 | 00 00 |  |
| 30 | 2 | Assignable Knob 5 Destination Mid Value | 0 – 1023 | 04 00 |  |
| 32 | 2 | Assignable Knob 5 Destination Right Value | 0 – 1023 | 07 7F |  |
| 34 | 2 | Assignable Knob 6 Destination Left Value | 0 – 1023 | 00 00 |  |
| 36 | 2 | Assignable Knob 6 Destination Mid Value | 0 – 1023 | 04 00 |  |
| 38 | 2 | Assignable Knob 6 Destination Right Value | 0 – 1023 | 07 7F |  |
| 40 | 2 | Assignable Knob 7 Destination Left Value | 0 – 1023 | 00 00 |  |
| 42 | 2 | Assignable Knob 7 Destination Mid Value | 0 – 1023 | 04 00 |  |
| 44 | 2 | Assignable Knob 7 Destination Right Value | 0 – 1023 | 07 7F |  |
| 46 | 2 | Assignable Knob 8 Destination Left Value | 0 – 1023 | 00 00 |  |
| 48 | 2 | Assignable Knob 8 Destination Mid Value | 0 – 1023 | 04 00 |  |
| 50 | 2 | Assignable Knob 8 Destination Right Value | 0 – 1023 | 07 7F |  |
| 52 | 2 | Super Knob LED Pattern | Off, Type 1, Type 2-1, Type 2-2, Type 3-1, Type 3-2, Type 4-1, Type 4-2, Type 5-1, Type 5-2, Type 6, Type 7-1, Type 7-2, Type 8-1, Type 8-2, Type 9, Type 10, Type 11, Type 1B, Type 2-1B, Type 2- 2B, Type 3-1B, Type 3-2B, Type 4-1B, Type 4-2B, Type 5- 1B, Type 5-2B, Type 6B, Type 7-1B, Type 7-2B, Type 8-1B, Type 8-2B, Type 9B, Type 10B, Type 11B, Rotary 1, Rotary 2, Rotary 3, Rotary 4, Rotary 5, Rotary 6, Rotary 7, Rotary 8, Rotary 9, Rotary 10 | 00 01 |  |
| 54 | 2 | Super Knob Motion Seq Random | 0 – 127 | 00 00 |  |
| 56 | 2 | Number of Waypoints | 0–6 | 00 00 |  |
| 58 | 2 | Start X | 1 – 32 | 00 00 |  |
| 60 | 2 | Start Y | 1 – 32 | 00 00 |  |
| 62 | 2 | End X | 1 – 32 | 00 1F |  |
| 64 | 2 | End Y | 1 – 32 | 00 1F |  |
| 66 | 2 | Waypoint 1 X | 1 – 32 | 00 0F |  |
| 68 | 2 | Waypoint 1 Y | 1 – 32 | 00 07 |  |
| 70 | 2 | Waypoint 2 X | 1 – 32 | 00 17 |  |
| 72 | 2 | Waypoint 2 Y | 1 – 32 | 00 07 |  |
| 74 | 2 | Waypoint 3 X | 1 – 32 | 00 17 |  |
| 76 | 2 | Waypoint 3 Y | 1 – 32 | 00 0F |  |
| 78 | 2 | Waypoint 4 X | 1 – 32 | 00 0F |  |
| 80 | 2 | Waypoint 4 Y | 1 – 32 | 00 17 |  |
| 82 | 2 | Waypoint 5 X | 1 – 32 | 00 07 |  |
| 84 | 2 | Waypoint 5 Y | 1 – 32 | 00 17 |  |
| 86 | 2 | Waypoint 6 X | 1 – 32 | 00 07 |  |
| 88 | 2 | Waypoint 6 Y | 1 – 32 | 00 0F |  |

## `06 00 0E 00` — 42 bytes
`.pfm` block: `common.ad`

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 2 | A/D Part Input Mode | L Mono, R Mono, L+R Mono, Stereo | 00 03 |  |
| 2 | 2 | A/D Part Volume | 0 – 127 | 00 64 |  |
| 4 | 2 | A/D Part Pan | L63 – C – R63 | 00 40 |  |
| 6 | 2 | A/D Part Reverb Send | 0 – 127 | 00 00 |  |
| 8 | 2 | A/D Part Variation Send | 0 – 127 | 00 00 |  |
| 10 | 2 | A/D Part Insertion Connect Type | Ins AB, Ins BA | 00 01 |  |
| 12 | 2 | A/D Part Output Select 0: MainL&R, | 8: AsgnL&R, 9 – 23: USB1&2 – USB29&30, 64 – 95: AsgnL, AsgnR, USB1 – USB30, 125: Off | 00 00 |  |
| 14 | 2 | A/D Part Dry Level | 0 – 127 | 00 7F |  |
| 16 | 2 | A/D Part Envelope Follower Gain | −24dB – 0dB – +24dB | 00 40 |  |
| 18 | 2 | A/D Part Envelope Follower Attack | 1ms – 40ms | 00 10 |  |
| 20 | 2 | A/D Part Envelope Follower Release | 10ms – 680ms | 00 07 |  |
| 22 | 2 | A/D Part Type | 2-band EQ 1 Thru, LPF, HPF, Low Shelf Hi Shelf, Peak/ Dip | 00 00 |  |
| 24 | 2 | A/D Part Frequency | 2-band EQ 1 63.0 – 18.0k | 00 30 |  |
| 26 | 2 | A/D Part Gain | 2-band EQ 1 −12.00dB – +12.00dB | 00 40 |  |
| 28 | 2 | A/D Part Q | 2-band EQ 1 0.1 – 12.0 | 00 01 |  |
| 30 | 2 | A/D Part Type @30 | 2-band EQ 2 Thru, LPF, HPF, Low Shelf Hi Shelf, Peak/ Dip | 00 00 |  |
| 32 | 2 | A/D Part Frequency @32 | 2-band EQ 2 63.0 – 18.0k | 00 30 |  |
| 34 | 2 | A/D Part Gain @34 | 2-band EQ 2 −12.00dB – +12.00dB | 00 40 |  |
| 36 | 2 | A/D Part Q @36 | 2-band EQ 2 0.1 – 12.0 | 00 01 |  |
| 38 | 2 | A/D Part Output Level | 2-band EQ −12.00dB – +12.00dB | 00 40 |  |
| 40 | 2 | A/D Part Motion Seq Random | 0 – 127 | 00 00 |  |

## `06 00 0F 00` — 14 bytes
`.pfm` block: `common.usb`

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 2 | Digital Part Input Mode | L Mono, R Mono, L+R Mono, Stereo | 00 03 |  |
| 2 | 2 | Digital Part Volume | 0 – 127 | 00 64 |  |
| 4 | 2 | Digital Part Pan | L63 – C – R63 | 00 40 |  |
| 6 | 2 | Digital Part Reverb Send | 0 – 127 | 00 00 |  |
| 8 | 2 | Digital Part Variation Send | 0 – 127 | 00 00 |  |
| 10 | 2 | Digital Part Dry Level | 0 – 127 | 00 7F |  |
| 12 | 2 | Digital Part Output Select | 0: MainL&R, 8: AsgnL&R, 9 – 23: Usb1&2 – USB29&30 64 – 95: AsgnL, AsgnR, USB1 – USB30, 125: Off | 00 00 |  |

## `06 00 12 00` — 20 bytes
`.pfm` block: `common.sklane`

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 2 | Super Knob Motion Seq Sync | Off, Tempo, Beat | 00 00 |  |
| 2 | 2 | Super Knob Motion Seq Speed | 0 – 127 | 00 3F | This is available only when Sync is set to Off. |
| 4 | 2 | Super Knob Motion Seq Unit Multiply | 50%, 66%, 75%, 100%, 133%, 150%, 200%, 266%, 300%, 400%, 600%, 800%, 1200%, 1600%, 2400%, 3200%, 6400%, Common | 00 03 | This is not available when Sync is set to Off. |
| 6 | 2 | Super Knob Motion Seq Key On Reset | Off, Each-On, 1st-On | 00 00 | This is not available when Sync is set to Arp. |
| 8 | 2 | Super Knob Motion Seq Velocity Limit Low | 1 – 127 | 00 01 |  |
| 10 | 2 | Super Knob Motion Seq Velocity Limit High | 1 – 127 | 00 7F |  |
| 12 | 2 | Super Knob Motion Seq Lane Key On Delay Time Length | 0 – 127 | 00 00 |  |
| 14 | 2 | Super Knob Motion Seq Lane Key On Delay Step Length | 0 – 32 | 00 00 |  |
| 16 | 2 | Super Knob Motion Seq Lane Fade In Time Length | 0 – 127 | 00 00 |  |
| 18 | 2 | Super Knob Motion Seq Lane Fade In Step Length | 0 – 32 | 00 00 |  |

## `06 01 0m 00` — 102 bytes
`.pfm` block: `common.skseq`
_m = motionSeq number 0–7              MotionSeq 1 – 8_

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 2 | Super Knob Motion Seq Amplitude | 0 – 127 | 00 7F |  |
| 2 | 2 | Super Knob Motion Seq Smoothness | 0 – 127 | 00 00 |  |
| 4 | 2 | Super Knob Motion Seq Length | 1 – 16 | 00 0F |  |
| 6 | 2 | Super Knob Motion Seq Unipolar, Bipolar Polarity | 00 00 – 00 01 | 00 00 |  |
| 8 | 2 | Motion Seq Grid | 60, 80, 120, 160, 240, 320, 480 | 00 03 |  |
| 10 | 2 | Super Knob Motion Seq Loop Start | 1 – 16 | 00 00 | This is not available when Loop is set to Off. Loop Start is less than or equal  |
| 12 | 2 | reserved | 00 00 | 00 00 |  |
| 14 | 2 | Super Knob Motion Seq Step 1 Value | 0 – 127 | 00 40 |  |
| 16 | 2 | Super Knob Motion Seq Step 2 Value | 0 – 127 | 00 40 |  |
| 18 | 2 | Super Knob Motion Seq Step 3 Value | 0 – 127 | 00 40 |  |
| 20 | 2 | Super Knob Motion Seq Step 4 Value | 0 – 127 | 00 40 |  |
| 22 | 2 | Super Knob Motion Seq Step 5 Value | 0 – 127 | 00 40 |  |
| 24 | 2 | Super Knob Motion Seq Step 6 Value | 0 – 127 | 00 40 |  |
| 26 | 2 | Super Knob Motion Seq Step 7 Value | 0 – 127 | 00 40 |  |
| 28 | 2 | Super Knob Motion Seq Step 8 Value | 0 – 127 | 00 40 |  |
| 30 | 2 | Super Knob Motion Seq Step 9 Value | 0 – 127 | 00 40 |  |
| 32 | 2 | Super Knob Motion Seq Step 10 Value | 0 – 127 | 00 40 |  |
| 34 | 2 | Super Knob Motion Seq Step 11 Value | 0 – 127 | 00 40 |  |
| 36 | 2 | Super Knob Motion Seq Step 12 Value | 0 – 127 | 00 40 |  |
| 38 | 2 | Super Knob Motion Seq Step 13 Value | 0 – 127 | 00 40 |  |
| 40 | 2 | Super Knob Motion Seq Step 14 Value | 0 – 127 | 00 40 |  |
| 42 | 2 | Super Knob Motion Seq Step 15 Value | 0 – 127 | 00 40 |  |
| 44 | 2 | Super Knob Motion Seq Step 16 Value | 0 – 127 | 00 40 |  |
| 46 | 2 | Super Knob Motion Seq A, B, Reverse A, Step 1 Type | Reverse B | 00 00 |  |
| 48 | 2 | Super Knob Motion Seq A, B, Reverse A, Step 2 Type | Reverse B | 00 00 |  |
| 50 | 2 | Super Knob Motion Seq A, B, Reverse A, Step 3 Type | Reverse B | 00 00 |  |
| 52 | 2 | Super Knob Motion Seq A, B, Reverse A, Step 4 Type | Reverse B | 00 00 |  |
| 54 | 2 | Super Knob Motion Seq A, B, Reverse A, Step 5 Type | Reverse B | 00 00 |  |
| 56 | 2 | Super Knob Motion Seq A, B, Reverse A, Step 6 Type | Reverse B | 00 00 |  |
| 58 | 2 | Super Knob Motion Seq A, B, Reverse A, Step 7 Type | Reverse B | 00 00 |  |
| 60 | 2 | Super Knob Motion Seq A, B, Reverse A, Step 8 Type | Reverse B | 00 00 |  |
| 62 | 2 | Super Knob Motion Seq A, B, Reverse A, Step 9 Type | Reverse B | 00 00 |  |
| 64 | 2 | Super Knob Motion Seq A, B, Reverse A, Step 10 Type | Reverse B | 00 00 |  |
| 66 | 2 | Super Knob Motion Seq A, B, Reverse A, Step 11 Type | Reverse B | 00 00 |  |
| 68 | 2 | Super Knob Motion Seq A, B, Reverse A, Step 12 Type | Reverse B | 00 00 |  |
| 70 | 2 | Super Knob Motion Seq A, B, Reverse A, Step 13 Type | Reverse B | 00 00 |  |
| 72 | 2 | Super Knob Motion Seq A, B, Reverse A, Step 14 Type | Reverse B | 00 00 |  |
| 74 | 2 | Super Knob Motion Seq A, B, Reverse A, Step 15 Type | Reverse B | 00 00 |  |
| 76 | 2 | Super Knob Motion Seq A, B, Reverse A, Step 16 Type | Reverse B | 00 00 | 236 |
| 78 | 2 | Super Knob Motion Seq Step Curve A Bank | 0 = Preset, 1 = User, 2 = Library1, – 17 = Library16, – 25 = Library24 | 00 00 |  |
| 80 | 2 | Super Knob Motion Seq Step Curve A Type | 0 – 31 (0 – 17 when Bank is set to Preset) | 00 00 |  |
| 82 | 2 | Super Knob Motion Seq Step Curve A Parameter 1 | 0 – 127 | 00 05 |  |
| 84 | 2 | Super Knob Motion Seq Step Curve A Parameter 2 | 0 – 127 | 00 00 |  |
| 86 | 2 | Super Knob Motion Seq Step Curve A Shape Control SW1 | Off, On | 00 01 |  |
| 88 | 2 | Super Knob Motion Seq Step Curve A Shape Control SW2 | Off, On | 00 00 |  |
| 90 | 2 | Super Knob Motion Seq Step Curve B Bank | 0 = Preset, 1 = User, 2 = Library1, – 17= Library16, – 25=Library24 | 00 00 |  |
| 92 | 2 | Super Knob Motion Seq Step Curve B Type | 0 – 31 (0 – 17 when Bank is set to Preset) | 00 00 |  |
| 94 | 2 | Super Knob Motion Seq Step Curve B Parameter 1 | 0 – 127 | 00 05 |  |
| 96 | 2 | Super Knob Motion Seq Step Curve B Parameter 2 | 0 – 127 | 00 00 |  |
| 98 | 2 | Super Knob Motion Seq Step Curve B Shape Control SW1 | Off, On | 00 01 |  |
| 100 | 2 | Super Knob Motion Seq Step Curve B Shape Control SW2 | Off, On | 00 00 |  |

## `06 02 0c 00` — 19 bytes
`.pfm` block: `common.scenes.s1`
_c = scene number 0–7                   Scene 1 – 8_

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 1 | Scene Arpeggio Master Switch | Off, On | 00 |  |
| 1 | 1 | Scene Motion Seq Master Switch | Off, On | 00 |  |
| 2 | 1 | Scene Arpeggio Memorize Switch | Off, On | 00 |  |
| 3 | 1 | Scene Motion Seq Memorize Switch | Off, On | 00 |  |
| 4 | 1 | Scene Super Knob Memorize Switch | Off, On | 00 |  |
| 5 | 1 | Scene Mixing Memorize Switch | Off, On | 00 |  |
| 6 | 1 | Scene AEG Memorize Switch | Off, On | 00 |  |
| 7 | 1 | Scene Arp/MS FX Memorize Switch | Off, On | 00 |  |
| 8 | 1 | Scene Super Knob Link Memorize Switch | Off, On | 00 |  |
| 9 | 1 | Scene Super Knob Link Switch1 | Off, On | 01 |  |
| 10 | 1 | Scene Super Knob Link Switch2 | Off, On | 01 |  |
| 11 | 1 | Scene Super Knob Link Switch3 | Off, On | 01 |  |
| 12 | 1 | Scene Super Knob Link Switch4 | Off, On | 01 |  |
| 13 | 1 | Scene Super Knob Link Switch5 | Off, On | 01 |  |
| 14 | 1 | Scene Super Knob Link Switch6 | Off, On | 01 |  |
| 15 | 1 | Scene Super Knob Link Switch7 | Off, On | 01 |  |
| 16 | 1 | Scene Super Knob Link Switch8 | Off, On | 01 |  |
| 17 | 1 | Scene Keyboard Control Switch Memorize Switch | Off, On | 00 |  |
| 18 | 1 | Scene Note Range Memorize Switch | Off, On | 00 |  |

## `06 03 0c 00` — 44 bytes
`.pfm` block: `common.scenes.s2`
_c = scene number 0–7                   Scene 1 – 8_

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 2 | Scene Arpeggio Select | 1–8 | 00 00 |  |
| 2 | 2 | Scene Motion Seq Select | 1–8 | 00 00 |  |
| 4 | 2 | Scene Super Knob Value | 0 – 1023 | 04 00 |  |
| 6 | 2 | reserved | 00 00 | 00 00 |  |
| 8 | 2 | Pan | L63 – C – R63 | 00 40 |  |
| 10 | 2 | Reverb Return | 0 – 127 | 00 40 |  |
| 12 | 2 | Variation Return | 0 – 127 | 00 60 |  |
| 14 | 2 | Filter Cutoff Frequency | −64 – +63 | 00 40 |  |
| 16 | 2 | Filter Resonance/Width | −64 – +63 | 00 40 |  |
| 18 | 2 | FEG Depth | −64 – +63 | 00 40 |  |
| 20 | 2 | AEG Attack Time | −64 – +63 | 00 40 |  |
| 22 | 2 | AEG Decay Time | −64 – +63 | 00 40 |  |
| 24 | 2 | AEG Sustain Level | −64 – +63 | 00 40 |  |
| 26 | 2 | AEG Release Time | −64 – +63 | 00 40 |  |
| 28 | 2 | Swing | −120 – 0 – +120 | 01 00 |  |
| 30 | 2 | Unit Multiply | 50%, 66%, 75%, 100%, 133%, 150%, 200%, 266%, 300%, 400% | 00 03 |  |
| 32 | 2 | Arpeggio Gate Time Rate Offset | −100 – 0 – +100 | 01 00 |  |
| 34 | 2 | Arpeggio Velocity Rate Offset | −100 – 0 – +100 | 01 00 |  |
| 36 | 2 | Motion Seq Amplitude Performance Offset | −127 – +127 | 01 00 |  |
| 38 | 2 | Motion Seq Pulse Shape Performance Offset | −100, −98, – 0, – +98, +100 | 00 40 |  |
| 40 | 2 | Motion Seq Smoothness Performance Offset | −127 – +127 | 01 00 |  |
| 42 | 2 | Motion Seq Random Performance Offset | −127 – +127 | 01 00 |  |

## `06 04 0k 00` — 16 bytes
`.pfm` block: `common.knobnames`
_k = knob number 0–7                   Knob 1 – 8 MONTAGE M Data List              237_

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 1 | Assignable Knob Name 1 | 0, 32 – 126 (ASCII) Assign 1-8 |  |  |
| 1 | 1 | Assignable Knob Name 2 | 0, 32 – 126 (ASCII) (same as the knob |  |  |
| 2 | 1 | Assignable Knob Name 3 | 0, 32 – 126 (ASCII) number) |  |  |
| 3 | 1 | Assignable Knob Name 4 | 0, 32 – 126 (ASCII) |  |  |
| 4 | 1 | Assignable Knob Name 5 | 0 ,32 – 126 (ASCII) |  |  |
| 5 | 1 | Assignable Knob Name 6 | 0, 32 – 126 (ASCII) |  |  |
| 6 | 1 | Assignable Knob Name 7 | 0, 32 – 126 (ASCII) |  |  |
| 7 | 1 | Assignable Knob Name 8 | 0, 32 – 126 (ASCII) |  |  |
| 8 | 1 | Assignable Knob Name 9 | 0, 32 – 126 (ASCII) |  |  |
| 9 | 1 | Assignable Knob Name 10 | 0, 32 – 126 (ASCII) |  |  |
| 10 | 1 | Assignable Knob Name 11 | 0, 32 – 126 (ASCII) |  |  |
| 11 | 1 | Assignable Knob Name 12 | 0, 32 – 126 (ASCII) |  |  |
| 12 | 1 | Assignable Knob Name 13 | 0, 32 – 126 (ASCII) |  |  |
| 13 | 1 | Assignable Knob Name 14 | 0, 32 – 126 (ASCII) |  |  |
| 14 | 1 | Assignable Knob Name 15 | 0, 32 – 126 (ASCII) |  |  |
| 15 | 1 | Assignable Knob Name 16 | 0, 32 – 126 (ASCII) |  |  |

## `06 05 bb 00` — 18 bytes
`.pfm` block: `common.ctrlbox`
_bb = box number 0 – 31               Box 1 – 32_

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 2 | Controller Set Switch | Off, On | 00 00 |  |
| 2 | 2 | Controller Set Source | 8 – 15, 18 – 39 (Refer to Controller Box Source of Control List) | 00 08 |  |
| 4 | 2 | Controller Set Destination | 1 – 393 (Refer to Controller Box Destination of Control List) | 00 01 |  |
| 6 | 2 | Controller Set Curve Bank | 0 = Preset, 1 = User, 2 = Library1, – 17= Library16, – 25=Library24 | 00 00 |  |
| 8 | 2 | Controller Set Curve Type | 0 – 31 (0 – 17 when Bank is set to Preset) | 00 00 |  |
| 10 | 2 | Controller Set Curve Parameter 1 | 0 – 127 | 00 05 | Fixed to “0” except when Bank is set to Preset |
| 12 | 2 | Controller Set Curve Parameter 2 | 0 – 127 | 00 00 | Fixed to “0” except when Bank is set to Preset |
| 14 | 2 | Controller Set Polarity | Unipolar, Bipolar | 00 00 |  |
| 16 | 2 | Controller Set Ratio | −128 – +127 | 01 40 |  |

## `06 06 L0 00` — 4 bytes
`.pfm` block: `common.lanes.l1`
_L = lane number 0–3                  Lane 1 – 4_

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 1 | Part Motion Seq Lane Switch | Off, On | 00 |  |
| 1 | 1 | Part Motion Seq Lane FX Receive | Off, On | 01 |  |
| 2 | 1 | Part Motion Seq Lane Trigger Receive | Off, On | 00 |  |
| 3 | 1 | Part Motion Seq Lane Loop | Off, On | 01 |  |

## `06 07 L0 00` — 20 bytes
`.pfm` block: `common.lanes.l2`
_L = lane number 0–3                   Lane 1 – 4_

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 2 | Part Motion Seq Lane Sync | Off, Tempo, Beat, Lane1 | 00 00 | Lane 1 is not available for Lane 1. |
| 2 | 2 | Part Motion Seq Lane Speed | 0 – 127 | 00 3F | This is available only when Sync is set to Off. |
| 4 | 2 | Part Motion Seq Lane Unit | 50%, 66%, 75%, 100%, 133%, 150%, 200%, 266%, 300%, 400%, 600%, 800%, 1200%, 1600%, 2400%, 3200%, 6400%, Common | 00 03 | This is not available when Sync is set to Off. |
| 6 | 2 | Part Motion Seq Lane Key On Reset | Off, Each-On, 1st-On | 00 00 |  |
| 8 | 2 | Part Motion Seq Lane Velocity Limit Low | 1 – 127 | 00 01 |  |
| 10 | 2 | Part Motion Seq Lane Velocity Limit High | 1 – 127 | 00 7F |  |
| 12 | 2 | Part Motion Seq Lane Key On Delay Time Length | 0 – 127 | 00 00 |  |
| 14 | 2 | Part Motion Seq Lane Key On Delay Step Length | 0 – 32 | 00 00 |  |
| 16 | 2 | Part Motion Seq Lane Fade In Time Length | 0 – 127 | 00 00 |  |
| 18 | 2 | Part Motion Seq Lane Fade In Step Length | 0 – 32 | 00 00 |  |

## `06 08 L 00` — 102 bytes
`.pfm` block: `common.lanes.seq`
_L = lane number 0–3                  Lane 1 – 4 m = motionSeq number 0–7              MotionSeq 1 – 8_

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 2 | Part Motion Seq m Amplitude | 0 – 127 | 00 40 |  |
| 2 | 2 | Part Motion Seq Smoothness | 0 – 127 | 00 00 |  |
| 4 | 2 | Part Motion Seq Length | 1 – 16 | 00 0F |  |
| 6 | 2 | Part Motion Seq Polarity | Unipolar, Bipolar | 00 00 |  |
| 8 | 2 | Motion Seq Grid | 60, 80, 120, 160, 240, 320, 480 | 00 03 |  |
| 10 | 2 | Lane Motion Seq Loop Start | 1 – 16 | 00 00 | This is not available when Loop is set to Off. Loop Start is less than or equal  |
| 12 | 2 | reserved | 00 00 | 00 00 |  |
| 14 | 2 | Part Motion Seq Step 1 Value | 0 – 127 | 00 40 |  |
| 16 | 2 | Part Motion Seq Step 2 Value | 0 – 127 | 00 40 |  |
| 18 | 2 | Part Motion Seq Step 3 Value | 0 – 127 | 00 40 |  |
| 20 | 2 | Part Motion Seq Step 4 Value | 0 – 127 | 00 40 |  |
| 22 | 2 | Part Motion Seq Step 5 Value | 0 – 127 | 00 40 |  |
| 24 | 2 | Part Motion Seq Step 6 Value | 0 – 127 | 00 40 |  |
| 26 | 2 | Part Motion Seq Step 7 Value | 0 – 127 | 00 40 |  |
| 28 | 2 | Part Motion Seq Step 8 Value | 0 – 127 | 00 40 |  |
| 30 | 2 | Part Motion Seq Step 9 Value | 0 – 127 | 00 40 |  |
| 32 | 2 | Part Motion Seq Step Value | 0 – 127 | 00 40 |  |
| 34 | 2 | Part Motion Seq Step Value @34 | 0 – 127 | 00 40 |  |
| 36 | 2 | Part Motion Seq Step Value @36 | 0 – 127 | 00 40 |  |
| 38 | 2 | Part Motion Seq Step Value @38 | 0 – 127 | 00 40 |  |
| 40 | 2 | Part Motion Seq Step Value @40 | 0 – 127 | 00 40 |  |
| 42 | 2 | Part Motion Seq Step Value @42 | 0 – 127 | 00 40 |  |
| 44 | 2 | Part Motion Seq Step Value @44 | 0 – 127 | 00 40 |  |
| 46 | 2 | Part Motion Seq Step 1 Type | A, B, Reverse A, Reverse B | 00 00 |  |
| 48 | 2 | Part Motion Seq Step 2 Type | A, B, Reverse A, Reverse B | 00 00 |  |
| 50 | 2 | Part Motion Seq Step 3 Type | A, B, Reverse A, Reverse B | 00 00 |  |
| 52 | 2 | Part Motion Seq Step 4 Type | A, B, Reverse A, Reverse B | 00 00 |  |
| 54 | 2 | Part Motion Seq Step 5 Type | A, B, Reverse A, Reverse B | 00 00 |  |
| 56 | 2 | Part Motion Seq Step 6 Type | A, B, Reverse A, Reverse B | 00 00 |  |
| 58 | 2 | Part Motion Seq Step 7 Type | A, B, Reverse A, Reverse B | 00 00 |  |
| 60 | 2 | Part Motion Seq Step 8 Type | A, B, Reverse A, Reverse B | 00 00 |  |
| 62 | 2 | Part Motion Seq Step 9 Type | A, B, Reverse A, Reverse B | 00 00 |  |
| 64 | 2 | Part Motion Seq Step Type | A, B, Reverse A, Reverse B | 00 00 |  |
| 66 | 2 | Part Motion Seq Step Type @66 | A, B, Reverse A, Reverse B | 00 00 | 238 |
| 68 | 2 | Part Motion Seq Step Type @68 | A, B, Reverse A, Reverse B | 00 00 |  |
| 70 | 2 | Part Motion Seq Step Type @70 | A, B, Reverse A, Reverse B | 00 00 |  |
| 72 | 2 | Part Motion Seq Step Type @72 | A, B, Reverse A, Reverse B | 00 00 |  |
| 74 | 2 | Part Motion Seq Step Type @74 | A, B, Reverse A, Reverse B | 00 00 |  |
| 76 | 2 | Part Motion Seq Step Type @76 | A, B, Reverse A, Reverse B | 00 00 |  |
| 78 | 2 | Part Motion Seq Step Curve A Bank | 0 = Preset, 1 = User, 2 = Library1, – 17= Library16, – 25=Library24 | 00 00 |  |
| 80 | 2 | Part Motion Seq Step Curve A Type | 0 – 31 (0 – 17 when Bank is set to Preset) | 00 00 |  |
| 82 | 2 | Part Motion Seq Step Curve A Parameter 1 | 0 – 127 | 00 05 |  |
| 84 | 2 | Part Motion Seq Step Curve A Parameter 2 | 0 – 127 | 00 00 |  |
| 86 | 2 | Part Motion Seq Step Curve A Shape Control SW1 | Off, On | 00 01 |  |
| 88 | 2 | Part Motion Seq Step Curve A Shape Control SW2 | Off, On | 00 00 |  |
| 90 | 2 | Part Motion Seq Step Curve B Bank | 0 = Preset, 1 = User, 2 = Library1, – 17= Library16, – 25=Library24 | 00 00 |  |
| 92 | 2 | Part Motion Seq Step Curve B Type | 0 – 31 (0 – 17 when Bank is set to Preset) | 00 00 |  |
| 94 | 2 | Part Motion Seq Step Curve B Parameter 1 | 0 – 127 | 00 05 |  |
| 96 | 2 | Part Motion Seq Step Curve B Parameter 2 | 0 – 127 | 00 00 |  |
| 98 | 2 | Part Motion Seq Step Curve B Shape Control SW1 | Off, On | 00 01 |  |
| 100 | 2 | Part Motion Seq Step Curve B Shape Control SW2 | Off, On | 00 00 |  |

## `06 09 00 00` — 8 bytes

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 2 | Motion Control Flag | Off, On | 00 |  |
| 2 | 2 | Reserved |  |  |  |
| 4 | 2 | Reserved @4 |  |  |  |
| 6 | 2 | Reserved @6 |  |  |  |
