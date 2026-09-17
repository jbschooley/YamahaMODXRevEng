# AN-X PART

## `4p 00 00 00` — 110 bytes
`.pfm` block: `anx.common`
_p = Part number 0–F                   Part 1 – 16 (AN-X)_

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 2 | Random Pan Depth | 0 – 127 | 00 00 |  |
| 2 | 2 | Alternate Pan Depth | L64 – C – R63 | 00 40 |  |
| 4 | 2 | Scaling Pan Depth | −64 – +63 | 00 40 |  |
| 6 | 2 | Key On Delay Time Length | 0 – 127 | 00 00 |  |
| 8 | 2 | Key On Delay Tempo Sync Switch | Off, On | 00 00 |  |
| 10 | 2 | Key On Delay Note Length | 5 – 21 (16th, 8th, 3, 16th., 8th, 4th, 3, 8th., 4th, 2th, 3, 4th., 2nd, Whole, 3, 2nd., 4thX4, 4thX5, 4thX6, 4thX7, 4thX8) | 00 0E |  |
| 12 | 2 | Unison | Off, 2, 4 | 00 00 |  |
| 14 | 2 | Unison Detune | 0 – 15 | 00 00 |  |
| 16 | 2 | Unison Spread | 0 – 15 | 00 00 |  |
| 18 | 2 | reserved | 00 01 | 00 01 |  |
| 20 | 2 | OSC Reset | Off, Phase, Tune, Full | 00 00 |  |
| 22 | 2 | Voltage Drift | 0 – 127 | 00 40 |  |
| 24 | 2 | Ageing | −100 – 0 – +100 | 00 64 |  |
| 26 | 2 | Pitch EG Attack Time | 0 – 255 | 00 00 |  |
| 28 | 2 | Pitch EG Decay Time | 0 – 255 | 01 20 |  |
| 30 | 2 | Pitch EG Sustain Level | 0 – 511 | 00 00 |  |
| 32 | 2 | Pitch EG Release Time | 0 – 255 | 00 73 |  |
| 34 | 2 | Pitch EG Time Velocity Sensitivity | −255 – 0 – +255 | 02 00 |  |
| 36 | 2 | Pitch LFO Wave | Saw, Square, Triangle, Sine, Random | 00 02 |  |
| 38 | 2 | Pitch LFO Speed | 0 – 415 | 01 50 |  |
| 40 | 2 | Pitch LFO Key On Reset | Off, On | 00 00 |  |
| 42 | 2 | Pitch LFO Phase | 0, 30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330 [°] | 00 00 |  |
| 44 | 2 | Pitch LFO Delay Time | 0 – 127 | 00 00 |  |
| 46 | 2 | Pitch LFO Fade In Time | 0 – 214 | 00 00 |  |
| 48 | 2 | Noise Generator Tone | 0 – 64 – 127 | 00 40 |  |
| 50 | 2 | Noise Generator Out Select | Filter, Amp | 00 00 |  |
| 52 | 2 | Noise Generator Out Level | 0 – 511 | 00 00 |  |
| 54 | 2 | Noise Generator Out Level Velocity Sensitivity | −255 – 0 – +255 | 02 00 |  |
| 56 | 2 | Filter Cutoff EG Attack Time | 0 – 255 | 00 00 |  |
| 58 | 2 | Filter Cutoff EG Decay Time | 0 – 255 | 01 20 |  |
| 60 | 2 | Filter Cutoff EG Sustain Level | 0 – 511 | 00 00 |  |
| 62 | 2 | Filter Cutoff EG Release Time | 0 – 255 | 01 20 |  |
| 64 | 2 | Filter Cutoff EG Time Velocity Sensitivity | −255 – 0 – +255 | 02 00 |  |
| 66 | 2 | Filter Cutoff LFO Wave | Saw, Square, Triangle, Sine, Random | 00 02 |  |
| 68 | 2 | Filter Cutoff LFO Speed | 0 – 415 | 01 50 |  |
| 70 | 2 | Filter Cutoff LFO Key On Reset | Off, On | 00 00 |  |
| 72 | 2 | Filter Cutoff LFO Phase | 0, 30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330 [°] | 00 00 |  |
| 74 | 2 | Filter Cutoff LFO Delay Time | 0 – 127 | 00 00 |  |
| 76 | 2 | Filter Cutoff LFO Fade In Time | 0 – 214 | 00 00 253 |  |
| 78 | 2 | Amplitude Level | 0 – 511 | 03 2F |  |
| 80 | 2 | Amplitude Level Velocity Sensitivity | −255 – 0 – +255 | 02 00 |  |
| 82 | 2 | Amplitude Level LFO Depth | −127 – +127 | 01 00 |  |
| 84 | 2 | Amplitude Level Key Follow | 0 – 127 | 00 00 |  |
| 86 | 2 | Amplitude Saturator Drive | 0.0 – 60.0 [dB], 0.75 [dB] step | 00 00 |  |
| 88 | 2 | Amplitude EG Attack Time | 0 – 255 | 00 00 |  |
| 90 | 2 | Amplitude EG Decay Time | 0 – 255 | 00 73 |  |
| 92 | 2 | Amplitude EG Sustain Level | 0 – 511 | 03 7F |  |
| 94 | 2 | Amplitude EG Release Time | 0 – 255 | 01 20 |  |
| 96 | 2 | Amplitude EG Time Velocity Sensitivity | −255 – 0 – +255 | 02 00 |  |
| 98 | 2 | Amplitude LFO Wave | Saw, Square, Triangle, Sine, Random | 00 02 |  |
| 100 | 2 | Amplitude LFO Speed | 0 – 415 | 01 50 |  |
| 102 | 2 | Amplitude LFO Key On Reset | Off, On | 00 00 |  |
| 104 | 2 | Amplitude LFO Phase | 0, 30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330 [°] | 00 00 |  |
| 106 | 2 | Amplitude LFO Delay Time | 0 – 127 | 00 00 |  |
| 108 | 2 | Amplitude LFO Fade In Time | 0 – 214 | 00 00 |  |

## `4p 01 0o 00` — 39 bytes
`.pfm` block: `anx.oscsw`
_o = Oscillator number 0–2                   Oscillator 1 – 3 p = Part number 0–F                   Part 1 – 16 (AN-X)_

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 1 | Oscillator Controller Set 1 Switch | Off, On | 01 |  |
| 1 | 1 | Oscillator Controller Set 2 Switch | Off, On | 01 |  |
| 2 | 1 | Oscillator Controller Set 3 Switch | Off, On | 01 |  |
| 3 | 1 | Oscillator Controller Set 4 Switch | Off, On | 01 |  |
| 4 | 1 | Oscillator Controller Set 5 Switch | Off, On | 01 |  |
| 5 | 1 | Oscillator Controller Set 6 Switch | Off, On | 01 |  |
| 6 | 1 | Oscillator Controller Set 7 Switch | Off, On | 01 |  |
| 7 | 1 | Oscillator Controller Set 8 Switch | Off, On | 01 |  |
| 8 | 1 | Oscillator Controller Set 9 Switch | Off, On | 01 |  |
| 9 | 1 | Oscillator Controller Set Switch | 10 Off, On | 01 |  |
| 10 | 1 | Oscillator Controller Set Switch @10 | 11 Off, On | 01 |  |
| 11 | 1 | Oscillator Controller Set Switch @11 | 12 Off, On | 01 |  |
| 12 | 1 | Oscillator Controller Set Switch @12 | 13 Off, On | 01 |  |
| 13 | 1 | Oscillator Controller Set Switch @13 | 14 Off, On | 01 |  |
| 14 | 1 | Oscillator Controller Set Switch @14 | 15 Off, On | 01 |  |
| 15 | 1 | Oscillator Controller Set Switch @15 | 16 Off, On | 01 |  |
| 16 | 1 | Oscillator Controller Set Switch @16 | 17 Off, On | 01 |  |
| 17 | 1 | Oscillator Controller Set Switch @17 | 18 Off, On | 01 |  |
| 18 | 1 | Oscillator Controller Set Switch @18 | 19 Off, On | 01 |  |
| 19 | 1 | Oscillator Controller Set Switch @19 | 20 Off, On | 01 |  |
| 20 | 1 | Oscillator Controller Set Switch @20 | 21 Off, On | 01 |  |
| 21 | 1 | Oscillator Controller Set Switch @21 | 22 Off, On | 01 |  |
| 22 | 1 | Oscillator Controller Set Switch @22 | 23 Off, On | 01 |  |
| 23 | 1 | Oscillator Controller Set Switch @23 | 24 Off, On | 01 |  |
| 24 | 1 | Oscillator Controller Set Switch @24 | 25 Off, On | 01 |  |
| 25 | 1 | Oscillator Controller Set Switch @25 | 26 Off, On | 01 |  |
| 26 | 1 | Oscillator Controller Set Switch @26 | 27 Off, On | 01 |  |
| 27 | 1 | Oscillator Controller Set Switch @27 | 28 Off, On | 01 |  |
| 28 | 1 | Oscillator Controller Set Switch @28 | 29 Off, On | 01 |  |
| 29 | 1 | Oscillator Controller Set Switch @29 | 30 Off, On | 01 |  |
| 30 | 1 | Oscillator Controller Set Switch @30 | 31 Off, On | 01 |  |
| 31 | 1 | Oscillator Controller Set Switch @31 | 32 Off, On | 01 |  |
| 32 | 1 | Oscillator Key Controller Set 1 Switch | Off, On | 01 |  |
| 33 | 1 | Oscillator Key Controller Set 2 Switch | Off, On | 01 |  |
| 34 | 1 | Oscillator Key Controller Set 3 Switch | Off, On | 01 |  |
| 35 | 1 | Oscillator Key Controller Set 4 Switch | Off, On | 01 |  |
| 36 | 1 | LFO Box 1 Switch | Off, On | 01 |  |
| 37 | 1 | LFO Box 2 Switch | Off, On | 01 |  |
| 38 | 1 | LFO Box 3 Switch | Off, On | 01 |  |

## `4p 02 0o 00` — 78 bytes
`.pfm` block: `anx.osc`
_o = Oscillator number 0–2                    Oscillator 1 – 3 p = Part number 0–F                    Part 1 – 16 (AN-X)_

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 2 | Oscillator Wave | Saw1, Saw2, Square, Triangle, Sine | 00 00 (OSC 1, 2) 00 04 (OSC 3) |  |
| 2 | 2 | Oscillator Octave | 64‘, 32’, 16’, 8’, 4‘, 2’, 1’ | 00 03 |  |
| 4 | 2 | Oscillator Pitch | −1200 – 0 – +1200 [cent] | 03 78 |  |
| 6 | 2 | Oscillator Pitch EG Depth | −4800 – 0 – +4800 [cent] | 01 77 |  |
| 8 | 2 | Oscillator Pitch EG Depth Velocity Sensitivity | −255 – 0 – +255 | 02 00 |  |
| 10 | 2 | Oscillator Pitch LFO Depth | −4800 – 0 – +4800 [cent] | 01 77 |  |
| 12 | 2 | Oscillator Self Sync Pitch | 0 – 4800 [cent] 25 [cent] step | 00 00 |  |
| 14 | 2 | Oscillator Self Sync Pitch Velocity Sensitivity | −255 – 0 – +255 | 02 00 |  |
| 16 | 2 | Oscillator Self Sync EG Depth | −4800 – 0 – 4800 [cent], 25 [cent] step | 02 00 |  |
| 18 | 2 | Oscillator Self Sync LFO Depth | −4800 – 0 – 4800 [cent], 25 [cent] step | 02 00 |  |
| 20 | 2 | Oscillator Pulse Width | 1.0% – 50.0% – 99.0% | 01 00 |  |
| 22 | 2 | Oscillator Pulse Width Velocity Sensitivity | −255 – 0 – +255 | 02 00 |  |
| 24 | 2 | Oscillator Pulse Width EG Depth | −127 – 0 – +127 | 01 00 |  |
| 26 | 2 | Oscillator Pulse Width LFO Depth | −127 – 0 – +127 | 01 00 |  |
| 28 | 2 | Oscillator Wave Shaper | 0 – 255 | 00 00 | This is not available when Wave is set to Square. |
| 30 | 2 | Oscillator Wave Shaper Velocity Sensitivity | −255 – 0 – +255 | 02 00 | This is not available when Wave is set to Square. 254 |
| 32 | 2 | Oscillator Wave Shaper EG Depth | −127 – 0 – +127 | 01 00 | This is not available when Wave is set to Square. |
| 34 | 2 | Oscillator Wave Shaper LFO Depth | −127 – 0 – +127 | 01 00 | This is not available when Wave is set to Square. |
| 36 | 2 | Oscillator FM Level | 0 – 255 | 00 00 | Not available for OSC3 |
| 38 | 2 | Oscillator FM Level Velocity Sensitivity | −255 – 0 – +255 | 02 00 | Not available for OSC3 |
| 40 | 2 | Oscillator Ring Level | 0 – 255 | 00 00 | Not available for OSC3 |
| 42 | 2 | Oscillator Ring Level Velocity Sensitivity | −255 – 0 – +255 | 02 00 | Not available for OSC3 |
| 44 | 2 | Oscillator Out Select | Filter, Amp | 00 00 |  |
| 46 | 2 | Oscillator Out Invert Enable | Off, On | 00 00 |  |
| 48 | 2 | Oscillator Out Level | 0 – 511 | 03 7F (OSC1) 00 00 (OSC 2, 3) |  |
| 50 | 2 | Oscillator Out Level Velocity Sensitivity | −255 – 0 – +255 | 02 00 |  |
| 52 | 2 | Oscillator EG Attack Time | 0 – 255 | 00 00 |  |
| 54 | 2 | Oscillator EG Decay Time | 0 – 255 | 01 20 |  |
| 56 | 2 | Oscillator EG Sustain Level | 0 – 511 | 00 00 |  |
| 58 | 2 | Oscillator EG Release Time | 0 – 255 | 01 20 |  |
| 60 | 2 | Oscillator LFO Wave | Saw, Square, Triangle, Sine, Random | 00 02 |  |
| 62 | 2 | Oscillator LFO Speed | 0 – 415 | 01 50 |  |
| 64 | 2 | Oscillator LFO Key On Reset | Off, On | 00 00 |  |
| 66 | 2 | Oscillator LFO Phase | 0, 30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330[°] | 00 00 |  |
| 68 | 2 | Oscillator LFO Delay Time | 0 – 127 | 00 00 |  |
| 70 | 2 | Oscillator LFO Fade In Time | 0 – 214 | 00 00 |  |
| 72 | 2 | Part LFO Destination 1 Depth Ratio | 0–127 | 00 7F |  |
| 74 | 2 | Part LFO Destination 2 Depth Ratio | 0–127 | 00 7F |  |
| 76 | 2 | Part LFO Destination 3 Depth Ratio | 0–127 | 00 7F |  |

## `4p 03 0f 00` — 39 bytes
`.pfm` block: `anx.filtsw`
_f = Filter number 0–1                   Filter 1 – 2 p = Part number 0–F                    Part 1 – 15 (AN-X)_

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 1 | Filter Controller Box1 Switch | Off, On | 01 |  |
| 1 | 1 | Filter Controller Box2 Switch | Off, On | 01 |  |
| 2 | 1 | Filter Controller Box3 Switch | Off, On | 01 |  |
| 3 | 1 | Filter Controller Box4 Switch | Off, On | 01 |  |
| 4 | 1 | Filter Controller Box5 Switch | Off, On | 01 |  |
| 5 | 1 | Filter Controller Box6 Switch | Off, On | 01 |  |
| 6 | 1 | Filter Controller Box7 Switch | Off, On | 01 |  |
| 7 | 1 | Filter Controller Box8 Switch | Off, On | 01 |  |
| 8 | 1 | Filter Controller Box9 Switch | Off, On | 01 |  |
| 9 | 1 | Filter Controller Box10 Switch | Off, On | 01 |  |
| 10 | 1 | Filter Controller Box11 Switch | Off, On | 01 |  |
| 11 | 1 | Filter Controller Box12 Switch | Off, On | 01 |  |
| 12 | 1 | Filter Controller Box13 Switch | Off, On | 01 |  |
| 13 | 1 | Filter Controller Box14 Switch | Off, On | 01 |  |
| 14 | 1 | Filter Controller Box15 Switch | Off, On | 01 |  |
| 15 | 1 | Filter Controller Box16 Switch | Off, On | 01 |  |
| 16 | 1 | Filter Controller Box17 Switch | Off, On | 01 |  |
| 17 | 1 | Filter Controller Box18 Switch | Off, On | 01 |  |
| 18 | 1 | Filter Controller Box19 Switch | Off, On | 01 |  |
| 19 | 1 | Filter Controller Box20 Switch | Off, On | 01 |  |
| 20 | 1 | Filter Controller Box21 Switch | Off, On | 01 |  |
| 21 | 1 | Filter Controller Box22 Switch | Off, On | 01 |  |
| 22 | 1 | Filter Controller Box23 Switch | Off, On | 01 |  |
| 23 | 1 | Filter Controller Box24 Switch | Off, On | 01 |  |
| 24 | 1 | Filter Controller Box25 Switch | Off, On | 01 |  |
| 25 | 1 | Filter Controller Box26 Switch | Off, On | 01 |  |
| 26 | 1 | Filter Controller Box27 Switch | Off, On | 01 |  |
| 27 | 1 | Filter Controller Box28 Switch | Off, On | 01 |  |
| 28 | 1 | Filter Controller Box29 Switch | Off, On | 01 |  |
| 29 | 1 | Filter Controller Box30 Switch | Off, On | 01 |  |
| 30 | 1 | Filter Controller Box31 Switch | Off, On | 01 |  |
| 31 | 1 | Filter Controller Box32 Switch | Off, On | 01 |  |
| 32 | 1 | Filter Key Controller Box1 Switch | Off, On | 01 |  |
| 33 | 1 | Filter Key Controller Box2 Switch | Off, On | 01 |  |
| 34 | 1 | Filter Key Controller Box3 Switch | Off, On | 01 |  |
| 35 | 1 | Filter Key Controller Box4 Switch | Off, On | 01 |  |
| 36 | 1 | LFO Box 1 Switch | Off, On | 01 |  |
| 37 | 1 | LFO Box 2 Switch | Off, On | 01 |  |
| 38 | 1 | LFO Box 3 Switch | Off, On | 01 |  |

## `4p 04 0f 00` — 30 bytes
`.pfm` block: `anx.filt`
_f = Filter number 0–1                  Filter 1 – 2 p = Part number 0–F                   Part 1 – 16 (AN-X)_

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 2 | Filter Type | Thru, LPF24, LPF18, LPF12, LPF6, HPF24, HPF18, HPF12, HPF6, BPF12, BPF6 | 00 01 (Filter 1) 00 05 (Filter 2) |  |
| 2 | 2 | Filter Cutoff | 0 – 1023 | 07 7F (Filter 1) 00 00 (Filter 2) |  |
| 4 | 2 | Filter Cutoff Velocity Sensitivity | −255 – 0 – +255 | 02 00 |  |
| 6 | 2 | Filter Cutoff EG Depth | −9600 – +9600 [cent], 50 [cent] step | 02 00 |  |
| 8 | 2 | Filter Cutoff EG Depth Velocity Sensitivity | −255 – 0 – +255 | 02 00 |  |
| 10 | 2 | Filter Cutoff LFO Depth | −9600 – +9600 [cent], 50 [cent] step | 02 00 |  |
| 12 | 2 | Filter Cutoff Key Follow | Off, 1/3, 1/2, 2/3, 1, 2 [oct] | 00 00 |  |
| 14 | 2 | Filter Resonance | 0 – 255 | 00 00 | Not available for LPF6 and HPF6. |
| 16 | 2 | Filter Resonance Velocity Sensitivity | −255 – 0 – +255 | 02 00 | Not available for LPF6 and HPF6. |
| 18 | 2 | Filter Saturator Drive | 0.0 – 60.0 [dB], 0.75 [dB] step | 00 00 |  |
| 20 | 2 | Filter Saturator Drive Velocity Sensitivity | −255 – 0 – +255 | 02 00 |  |
| 22 | 2 | Filter Out Level | −12.0 – +12.0 [dB], 0.375 [dB] step | 00 40 | 255 |
| 24 | 2 | Part LFO Destination 1 Depth Ratio | 0–127 | 00 7F |  |
| 26 | 2 | Part LFO Destination 2 Depth Ratio | 0–127 | 00 7F |  |
| 28 | 2 | Part LFO Destination 3 Depth Ratio | 0–127 | 00 7F |  |

## `4p 05 00 00` — 34 bytes
`.pfm` block: `anx.fold`
_p = Part number 0–F                   Part 1 – 16 (AN-X)_

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 2 | Modifier Wave Folder | 0 – 255 | 00 00 |  |
| 2 | 2 | Modifier Wave Folder Velocity Sensitivity | −255 – 0 – +255 | 02 00 |  |
| 4 | 2 | Modifier Wave Folder EG Depth | −127 – 0 – +127 | 01 00 |  |
| 6 | 2 | Modifier Wave Folder LFO Depth | −127 – 0 – +127 | 01 00 |  |
| 8 | 2 | Modifier Wave Folder Texture | 0 – 255 | 01 00 |  |
| 10 | 2 | Modifier Wave Folder Type | Soft, Hard | 00 01 |  |
| 12 | 2 | Modifier EG Attack Time | 0 – 255 | 00 00 |  |
| 14 | 2 | Modifier EG Decay Time | 0 – 255 | 01 20 |  |
| 16 | 2 | Modifier EG Sustain Level | 0 – 511 | 00 00 |  |
| 18 | 2 | Modifier EG Release Time | 0 – 255 | 01 20 |  |
| 20 | 2 | Modifier EG Time Velocity Sensitivity | −255 – 0 – +255 | 02 00 |  |
| 22 | 2 | Modifier LFO Wave | Saw, Square, Triangle, Sine, Random | 00 02 |  |
| 24 | 2 | Modifier LFO Speed | 0 – 415 | 01 50 |  |
| 26 | 2 | Modifier LFO Key On Reset | OFF, ON | 00 00 |  |
| 28 | 2 | Modifier LFO Phase | 0, 30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330[°] | 00 00 |  |
| 30 | 2 | Modifier LFO Delay Time | 0 – 127 | 00 00 |  |
| 32 | 2 | Modifier LFO Fade In Time | 0 – 214 | 00 00 |  |

## `7p 00 00 00` — 4 bytes
_p = Part number 0–F                   Part 1 – 16 (AN-X)_

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 2 | Oscillator 1 Ring / FM | Ring 255 – 0 – FM 255 | 02 00 |  |
| 2 | 2 | Oscillator 2 Ring / FM | Ring 255 – 0 – FM 255 | 02 00 |  |
