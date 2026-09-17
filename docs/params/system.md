# SYSTEM

## `00 00 00 00` — 70 bytes

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 2 | Tone Generator Volume | 0 – 127 | 00 7F | MIDI Master Volume |
| 2 | 2 | Tone Generator Note Shift | −24 – +24 semi | 00 40 |  |
| 4 | 2 | Tone Generator Tune | −102.4 – +102.3 MSB bit6-0  bit13-7 LSB bit6-0  bit6-0 | 08 00 | MIDI Master Tuning |
| 6 | 2 | Controller Reset | Hold, Reset | 00 01 |  |
| 8 | 2 | Local Control | Off, On | 00 01 |  |
| 10 | 2 | Touch Panel Sound Switch | Off, On | 00 01 |  |
| 12 | 2 | Analog Output L&R Output Gain | 00: −6dB, 01:+0dB, 02: +6dB, 03: +12dB | 00 01 |  |
| 14 | 2 | Assignable Output L&R Output Gain | 00: −6dB, 01:+0dB, 02: +6dB, 03: +12dB | 00 01 |  |
| 16 | 2 | USB Main L&R Output Gain | 00: −6dB, 01:+0dB, 02: +6dB, 03: +12dB | 00 01 |  |
| 18 | 2 | USB Individual Output Gain | 00: −6dB, 01:+0dB, 02: +6dB, 03: +12dB | 00 01 |  |
| 20 | 2 | Keyboard Velocity Curve | Normal, Soft 1, Soft 2, Hard 1, Hard 2, Wide, Fixed | 00 00 |  |
| 22 | 2 | Keyboard Fixed Velocity | 1 – 127 | 00 40 |  |
| 24 | 2 | Receive/Transmit Bank Select | Off, On | 00 01 |  |
| 26 | 2 | Receive/Transmit Program Change | Off, On | 00 01 |  |
| 28 | 2 | FS Assign Control Number | Off, 1 – 95, Arp SW, MS SW, Play/Stop, Live Set +, Live Set −, Oct reset, Tap Tempo | 00 60 |  |
| 30 | 2 | Super Knob Control Number | Off, 1 – 95 | 00 5F |  |
| 32 | 2 | Scene Select Control Number | Off, 1 – 95 | 00 5C |  |
| 34 | 2 | MIDI IN/OUT | MIDI, USB | 00 01 |  |
| 36 | 2 | Audition Lock | Off, On | 00 00 |  |
| 38 | 2 | Power on Mode | Perform, Live Set | 00 01 |  |
| 40 | 2 | Bulk Interval | 0 – 900ms | 00 01 |  |
| 42 | 2 | Power on Live Set Bank | Preset, User1, – User 8, Library 1, –Library 16, Library 17, – Library24 | 00 01 |  |
| 44 | 2 | Power on Live Set Page | Page 1 – Page 16 | 00 00 |  |
| 46 | 2 | Power on Live Set Slot | Slot 1 – Slot 16 | 00 00 |  |
| 48 | 2 | A/D Input Gain | Mic, Line | 00 01 |  |
| 50 | 2 | USB Input Volume | 0 – 127 | 00 7F |  |
| 52 | 2 | LED Half Glow Brightness | Off, 1/4, 1/2 | 00 01 |  |
| 54 | 2 | Direct Monitor Switch | Off, On | 00 01 |  |
| 56 | 2 | MIDI I/O Channel | Ch1, – Ch16 | 00 00 |  |
| 58 | 2 | Global Micro Tuning Equal Temperament, Scale | Pure Major, Pure Minor, Werckmeister, Kirnberger, Valloti&Young, 1/4 Shift, 1/4 tone, 1/8 tone, Indian, Arabic 1, Arabic 2, Arabic 3, User1 – 8, Library1-1 – 16-8, Library17-1 – Library24-8 | 00 00 |  |
| 60 | 2 | Global Micro Tuning C – B Root | 00 00 – 00 0B | 00 00 |  |
| 62 | 2 | Sustain Pedal Select | FC3A (Half On), FC3A (Half Off), FC4A/FC5, Reverse Polarity | 00 00 |  |
| 64 | 2 | After Touch MIDI Out | Off / Ch. / Poly | 00 00 |  |
| 66 | 2 | After Touch Curve | Normal, Soft 1, Soft 2, Hard 1, Hard 2 | 00 00 |  |
| 68 | 2 | Global SSS Time | 0s–30s, Hold | 00 1F |  |

## `00 00 01 00` — 22 bytes

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 2 | Click Mode | Off, Rec, Rec/Play, Always | 00 01 | for SEQ |
| 2 | 2 | Click Output Select | 0: MainL&R, 8: AsgnL&R, 9 – 23: USB1&2 – USB29&30 64 – 95: AsgnL, AsgnR, USB1 – USB30 | 00 00 | 〃 |
| 4 | 2 | Click Volume | 0 – 127 | 00 64 | 〃 |
| 6 | 2 | Click Type | 1 – 10 | 00 00 | 〃 |
| 8 | 2 | Click Beat | 16th, 8th, 4th, 2nd, Whole | 00 02 | 〃 |
| 10 | 2 | Recording Count | Off, 1 – 8meas | 00 01 | 〃 |
| 12 | 2 | Transmit Sequencer Control | Off, On | 00 00 | 〃 |
| 14 | 2 | Receive Sequencer Control | Off, On | 00 00 | 〃 |
| 16 | 2 | Song Event Chase | Off, PC, PC+PB+Ctrl | 00 00 | 〃 |
| 18 | 2 | MIDI Sync | Internal, MIDI, A/D In | 00 01 | 〃 |
| 20 | 2 | MIDI Clock Out | Off, On | 00 00 | 〃 |

## `00 00 02 00` — 6 bytes

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 2 | Keyboard Transpose | −11 – +11 semi | 00 40 |  |
| 2 | 2 | Keyboard Octave Shift | −3 – +3 | 00 40 |  |
| 4 | 2 | Global Micro Tuning Switch | Off, On | 00 00 |  |

## `00 00 03 00` — 112 bytes

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 2 | DAW Type | 0=Cubase, 1=Logic, 2=ProTools, 3=AbletonLive | 00 00 |  |
| 2 | 2 | Remote Control Mode | 0=Track, 1=Plugin, 2=Transport, 3=ESP Control | 00 00 |  |
| 4 | 2 | Super Knob Control Number | 1 – 95 | 00 5F |  |
| 6 | 2 | Assignable Knob 1 Control Number | 1 – 95 | 00 11 |  |
| 8 | 2 | Assignable Knob 2 Control Number | 1 – 95 | 00 12 |  |
| 10 | 2 | Assignable Knob 3 Control Number | 1 – 95 | 00 13 |  |
| 12 | 2 | Assignable Knob 4 Control Number | 1 – 95 | 00 14 |  |
| 14 | 2 | Assignable Knob 5 Control Number | 1 – 95 | 00 15 |  |
| 16 | 2 | Assignable Knob 6 Control Number | 1 – 95 | 00 16 |  |
| 18 | 2 | Assignable Knob 7 Control Number | 1 – 95 | 00 17 |  |
| 20 | 2 | Assignable Knob 8 Control Number | 1 – 95 | 00 18 |  |
| 22 | 2 | Slider 1 Control Number | 1 – 95 | 00 46 |  |
| 24 | 2 | Slider 2 Control Number | 1 – 95 | 00 47 |  |
| 26 | 2 | Slider 3 Control Number | 1 – 95 | 00 48 |  |
| 28 | 2 | Slider 4 Control Number | 1 – 95 | 00 49 |  |
| 30 | 2 | Slider 5 Control Number | 1 – 95 | 00 4A |  |
| 32 | 2 | Slider 6 Control Number | 1 – 95 | 00 4B |  |
| 34 | 2 | Slider 7 Control Number | 1 – 95 | 00 4C |  |
| 36 | 2 | Slider 8 Control Number | 1 – 95 | 00 4D |  |
| 38 | 2 | Scene 1 Control Number | 1 – 95 | 00 19 |  |
| 40 | 2 | Scene 2 Control Number | 1 – 95 | 00 1A |  |
| 42 | 2 | Scene 3 Control Number | 1 – 95 | 00 1B |  |
| 44 | 2 | Scene 4 Control Number | 1 – 95 | 00 1C |  |
| 46 | 2 | Scene 5 Control Number | 1 – 95 | 00 1D |  |
| 48 | 2 | Scene 6 Control Number | 1 – 95 | 00 1E |  |
| 50 | 2 | Scene 7 Control Number | 1 – 95 | 00 1F |  |
| 52 | 2 | Scene 8 Control Number | 1 – 95 | 00 55 |  |
| 54 | 2 | Ribbon Controller Control Number | 1 – 95 | 00 10 |  |
| 56 | 2 | Foot Switch Control Number | 1 – 95 | 00 58 |  |
| 58 | 2 | Foot Controller 1 Control Number | 1 – 95 | 00 0B |  |
| 60 | 2 | Foot Controller 2 Control Number | 1 – 95 | 00 5F |  |
| 62 | 2 | Assignable Switch 1 Control Number | 1 – 95 | 00 56 |  |
| 64 | 2 | Assignable Switch 2 Control Number | 1 – 95 | 00 57 |  |
| 66 | 2 | Motion Seq Trigger Switch Control Number | 1 – 95 | 00 59 |  |
| 68 | 2 | Time Control Number | 1 – 95 | 00 05 |  |
| 70 | 2 | Portamento Switch Control Number | 1 – 95 | 00 41 |  |
| 72 | 2 | Display Knob 1 Control Number | 1 – 95 | 00 4E |  |
| 74 | 2 | Display Knob 2 Control Number | 1 – 95 | 00 4F |  |
| 76 | 2 | Display Knob 3 Control Number | 1 – 95 | 00 50 |  |
| 78 | 2 | Display Knob 4 Control Number | 1 – 95 | 00 51 |  |
| 80 | 2 | Display Knob 5 Control Number | 1 – 95 | 00 52 |  |
| 82 | 2 | Display Knob 6 Control Number | 1 – 95 | 00 53 |  |
| 84 | 2 | Ribbon Controller Mode | Hold, Reset | 00 01 |  |
| 86 | 2 | Foot Switch Mode | Momentary, Latch | 00 01 |  |
| 88 | 2 | Assignable Switch 1 Mode | Momentary, Latch | 00 01 |  |
| 90 | 2 | Assignable Switch 2 Mode | Momentary, Latch | 00 01 |  |
| 92 | 2 | Motion Seq Trigger Switch Mode | Momentary, Latch | 00 01 |  |
| 94 | 2 | Scene 1 Switch Mode | Momentary, Latch | 00 00 |  |
| 96 | 2 | Scene 2 Switch Mode | Momentary, Latch | 00 00 |  |
| 98 | 2 | Scene 3 Switch Mode | Momentary, Latch | 00 00 |  |
| 100 | 2 | Scene 4 Switch Mode | Momentary, Latch | 00 00 |  |
| 102 | 2 | Scene 5 Switch Mode | Momentary, Latch | 00 00 |  |
| 104 | 2 | Scene 6 Switch Mode | Momentary, Latch | 00 00 |  |
| 106 | 2 | Scene 7 Switch Mode | Momentary, Latch | 00 00 |  |
| 108 | 2 | Scene 8 Switch Mode | Momentary, Latch | 00 00 |  |
| 110 | 2 | Portamento Switch Mode | Momentary, Latch | 00 01 |  |

## `00 01 0n 00` — 24 bytes
_n = user table number 00 – 07               Table 1 – 8_

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 2 | Micro Tuning C | −99 – 0 – +99 [cent] | 01 00 |  |
| 2 | 2 | Micro Tuning C# | 〃 | 01 00 |  |
| 4 | 2 | Micro Tuning D | 〃 | 01 00 |  |
| 6 | 2 | Micro Tuning D# | 〃 | 01 00 |  |
| 8 | 2 | Micro Tuning E | 〃 | 01 00 |  |
| 10 | 2 | Micro Tuning F | 〃 | 01 00 |  |
| 12 | 2 | Micro Tuning F# | 〃 | 01 00 |  |
| 14 | 2 | Micro Tuning G | 〃 | 01 00 |  |
| 16 | 2 | Micro Tuning G# | 〃 | 01 00 |  |
| 18 | 2 | Micro Tuning A | 〃 | 01 00 |  |
| 20 | 2 | Micro Tuning A# | 〃 | 01 00 |  |
| 22 | 2 | Micro Tuning B | 〃 | 01 00 |  |

## `00 02 0n 00` — 20 bytes
_n = user table number 00 – 07               Table 1 – 8_

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 1 | Micro Tuning Table – 7E Name 1 | 0, 32 – 126 (ASCII) Init Tuning 1 |  |  |
| 1 | 1 | Micro Tuning Table – 7E Name 2 | 0, 32 – 126 (ASCII) – 8 (same as the |  |  |
| 2 | 1 | Micro Tuning Table – 7E Name 3 | 0, 32 – 126 (ASCII) table number) |  |  |
| 3 | 1 | Micro Tuning Table – 7E Name 4 | 0, 32 – 126 (ASCII) |  |  |
| 4 | 1 | Micro Tuning Table – 7E Name 5 | 0, 32 – 126 (ASCII) |  |  |
| 5 | 1 | Micro Tuning Table – 7E Name 6 | 0, 32 – 126 (ASCII) |  |  |
| 6 | 1 | Micro Tuning Table – 7E Name 7 | 0, 32 – 126 (ASCII) |  |  |
| 7 | 1 | Micro Tuning Table – 7E Name 8 | 0, 32 – 126 (ASCII) |  |  |
| 8 | 1 | Micro Tuning Table – 7E Name 9 | 0, 32 – 126 (ASCII) |  |  |
| 9 | 1 | Micro Tuning Table – 7E Name 10 | 0, 32 – 126 (ASCII) |  |  |
| 10 | 1 | Micro Tuning Table – 7E Name 11 | 0, 32 – 126 (ASCII) |  |  |
| 11 | 1 | Micro Tuning Table – 7E Name 12 | 0, 32 – 126 (ASCII) |  |  |
| 12 | 1 | Micro Tuning Table – 7E Name 13 | 0, 32 – 126 (ASCII) |  |  |
| 13 | 1 | Micro Tuning Table – 7E Name 14 | 0, 32 – 126 (ASCII) |  |  |
| 14 | 1 | Micro Tuning Table – 7E Name 15 | 0, 32 – 126 (ASCII) |  |  |
| 15 | 1 | Micro Tuning Table – 7E Name 16 | 0, 32 – 126 (ASCII) |  |  |
| 16 | 1 | Micro Tuning Table – 7E Name 17 | 0, 32 – 126 (ASCII) |  |  |
| 17 | 1 | Micro Tuning Table – 7E Name 18 | 0, 32 – 126 (ASCII) |  |  |
| 18 | 1 | Micro Tuning Table – 7E Name 19 | 0, 32 – 126 (ASCII) |  |  |
| 19 | 1 | Micro Tuning Table – 7E Name 20 | 0, 32 – 126 (ASCII) |  |  |

## `00 00 7F 00` — 6 bytes

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 2 | Soundmondo Format Version Major | 00 – 7F | 01 |  |
| 2 | 2 | Soundmondo Format Version Minor | 00 – 7F | 02 |  |
| 4 | 2 | Soundmondo Format Version Bugfix | 00 – 7F | 00 |  |
