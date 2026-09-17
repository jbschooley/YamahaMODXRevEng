# FM-X PART COMMON

## `3p 00 00 00` — 82 bytes
`.pfm` block: `fmx.common`
_p = Part number 0–F                   Part 1 – 16 (FM-X)_

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 2 | Random Pan Depth | 0 – 127 | 00 00 |  |
| 2 | 2 | Alternate Pan Depth | L64 – C – R63 | 00 40 |  |
| 4 | 2 | Scaling Pan Depth | −64 – +63 | 00 40 |  |
| 6 | 2 | Key On Delay Time Length | 0 – 127 | 00 00 | This is available only when Tempo Sync is set to Off. |
| 8 | 2 | Key On Delay Tempo Sync Switch | Off, On | 00 00 |  |
| 10 | 2 | Key On Delay Note Length | 5 – 21 (16th, 8th/3, 16th., 8th, 4th/3, 8th., 4th, 2th/3, 4th., 2nd, Whole/3, 2nd., 4thX4, 4thX5, 4thX6, 4thX7, 4thX8) | 00 0E | This is available only when Tempo Sync is set to On. |
| 12 | 2 | Pitch Velocity Sensitivity | −64 – +63 | 00 40 |  |
| 14 | 2 | Random Pitch Depth | 0 – 127 | 00 00 |  |
| 16 | 2 | Pitch Key Follow Sensitivity | −200% – +200% | 00 60 |  |
| 18 | 2 | Pitch Key Follow Sensitivity Center Note | C-2 – G8 | 00 3C |  |
| 20 | 2 | PEG Initial Level | −50 – +50 | 00 32 |  |
| 22 | 2 | PEG Attack Level | −50 – +50 | 00 32 |  |
| 24 | 2 | PEG Decay 1 Level | −50 – +50 | 00 32 |  |
| 26 | 2 | PEG Decay 2 Level | −50 – +50 | 00 32 |  |
| 28 | 2 | PEG Release Level | −50 – +50 | 00 32 |  |
| 30 | 2 | PEG Attack Time | 0 – 99 | 00 00 |  |
| 32 | 2 | PEG Decay 1 Time | 0 – 99 | 00 00 |  |
| 34 | 2 | PEG Decay 2 Time | 0 – 99 | 00 00 |  |
| 36 | 2 | PEG Release Time | 0 – 99 | 00 00 |  |
| 38 | 2 | PEG Depth Velocity Sensitivity | 0–7 | 00 00 |  |
| 40 | 2 | PEG Depth | 8 oct, 2 oct, 1 oct, 0.5 oct | 00 00 |  |
| 42 | 2 | PEG Time Key Follow Sensitivity | 0–7 | 00 00 |  |
| 44 | 2 | 2nd LFO Wave | Triangle, Saw Down, Saw Up, Square, Sine, S/H | 00 00 |  |
| 46 | 2 | 2nd LFO Speed | 0 – 99 | 00 1E | This is available only when LFO Speed Range is set to Normal. |
| 48 | 2 | 2nd LFO Phase | 0°, 90°, 180°, 270° | 00 00 |  |
| 50 | 2 | 2nd LFO Delay Time | 0 – 99 | 00 00 |  |
| 52 | 2 | 2nd LFO Key On Reset | Off, On | 00 00 |  |
| 54 | 2 | 2nd LFO Pitch Modulation Depth | 0 – 99 | 00 00 |  |
| 56 | 2 | 2nd LFO Amplitude Modulation Depth | 0 – 99 | 00 00 |  |
| 58 | 2 | 2nd LFO Filter Modulation Depth | 0 – 99 | 00 00 |  |
| 60 | 2 | Algorithm Number | 1 – 88 | 00 44 |  |
| 62 | 2 | Feedback Level | 0–7 | 00 00 |  |
| 64 | 2 | LFO Speed Range | Normal, Extended | 00 01 |  |
| 66 | 2 | LFO Extended Speed | 0 – 415 | 00 3C | This is available only when LFO Speed Range is set to Extended. |
| 68 | 2 | FM Depth | −99 – +99 | 01 00 |  |
| 70 | 2 | FM Harmonics | −99 – +99 | 01 00 |  |
| 72 | 2 | FM Attack | −99 – +99 | 01 00 |  |
| 74 | 2 | FM Decay | −99 – +99 | 01 00 |  |
| 76 | 2 | FM Sustain | −99 – +99 | 01 00 |  |
| 78 | 2 | FM Release | −99 – +99 | 01 00 |  |
| 80 | 2 | FM Texture | −99 – +99 | 01 00 |  |

## `3p 00 01 00` — 70 bytes
`.pfm` block: `fmx.filter`
_p = Part number 0–F                   Part 1 – 16 (FM-X)_

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 2 | Filter Type | LPF24D, LPF24A, LPF18, LPF18s, LPF12+HPF12, LPF6+HPF12, HPF24D, HPF12, BPF12D, BPFw, BPF6, BEF12, BEF6, DualLPF, DualHPF, DualBPF, DualBEF, LPF12+BPF6, Thru | 00 15 |  |
| 2 | 2 | Filter Cutoff Frequency | 0 – 1023 | 07 7F |  |
| 4 | 2 | Filter Cutoff Velocity Sensitivity | −64 – +63 | 00 40 |  |
| 6 | 2 | Filter Resonance/ Width | 0 – 127 | 00 0A | Not available for LPF6+HPF 12. |
| 8 | 2 | Filter Resonance Velocity Sensitivity | −64 – +63 | 00 40 |  |
| 10 | 2 | HPF Cutoff Frequency | 0 – 1023 | 00 00 |  |
| 12 | 2 | Distance | −128 – +127 | 01 00 | This is available when Filter Type is set to Dual. |
| 14 | 2 | Filter Gain | 0 – 255 | 01 7F |  |
| 16 | 2 | FEG Hold Time | 0 – 127 | 00 00 |  |
| 18 | 2 | FEG Attack Time | 0 – 127 | 00 00 |  |
| 20 | 2 | FEG Decay 1 Time | 0 – 127 | 00 00 |  |
| 22 | 2 | FEG Decay 2 Time | 0 – 127 | 00 00 |  |
| 24 | 2 | FEG Release Time | 0 – 127 | 00 00 |  |
| 26 | 2 | FEG Hold Level | −128 – +127 (−9600 – +9600 [cent]) | 01 00 |  |
| 28 | 2 | FEG Attack Level | 〃 | 01 00 |  |
| 30 | 2 | FEG Decay 1 Level | 〃 | 01 00 |  |
| 32 | 2 | FEG Decay 2 Level | 〃 | 01 00 |  |
| 34 | 2 | FEG Release Level | 〃 | 01 00 |  |
| 36 | 2 | FEG Depth | −64 – +63 | 00 68 |  |
| 38 | 2 | FEG Time Velocity Sensitivity Segment | Attack, Atk+Dcy, Decay, Atk+Rls, All | 00 04 |  |
| 40 | 2 | FEG Time Velocity Sensitivity | −64 – +63 | 00 40 |  |
| 42 | 2 | FEG Depth Velocity Sensitivity | −64 – +63 | 00 40 |  |
| 44 | 2 | FEG Depth Velocity Sensitivity Curve | 00 – 04 | 00 02 |  |
| 46 | 2 | FEG Time Key Follow Sensitivity | −64 – +63 | 00 40 |  |
| 48 | 2 | FEG Time Key Follow Sensitivity Center Note | C-2 – G8 | 00 18 | 251 |
| 50 | 2 | Filter Cutoff Key Follow Sensitivity | −200% – +200% | 00 4A |  |
| 52 | 2 | Filter Cutoff Scaling Break Point 1 | C-2 – E8 | 00 24 | BP1<BP2 <BP3<BP 4 |
| 54 | 2 | Filter Cutoff Scaling Break Point 2 | C#-2 – F8 | 00 30 | BP1<BP2 <BP3<BP 4 |
| 56 | 2 | Filter Cutoff Scaling Break Point 3 | D-2 – F#8 | 00 3C | BP1<BP2 <BP3<BP 4 |
| 58 | 2 | Filter Cutoff Scaling Break Point 4 | D#-2 – G8 | 00 48 | BP1<BP2 <BP3<BP 4 |
| 60 | 2 | Filter Cutoff Scaling Offset 1 | −128 – +127 | 01 00 |  |
| 62 | 2 | Filter Cutoff Scaling Offset 2 | 〃 | 01 00 |  |
| 64 | 2 | Filter Cutoff Scaling Offset 3 | 〃 | 01 00 |  |
| 66 | 2 | Filter Cutoff Scaling Offset 4 | 〃 | 01 00 |  |
| 68 | 2 | HPF Cutoff Key Follow Sensitivity | −200% – +200% | 00 40 |  |

## `3p 01 0o 00` — 39 bytes
`.pfm` block: `fmx.opsw`
_p = Part number 0–F                   Part 1 – 16 (FM-X) o = Operator number 0–7                   Operator 1 – 8_

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 1 | Controller Set 1 Switch | Off, On | 01 |  |
| 1 | 1 | Controller Set 2 Switch | Off, On | 01 |  |
| 2 | 1 | Controller Set 3 Switch | Off, On | 01 |  |
| 3 | 1 | Controller Set 4 Switch | Off, On | 01 |  |
| 4 | 1 | Controller Set 5 Switch | Off, On | 01 |  |
| 5 | 1 | Controller Set 6 Switch | Off, On | 01 |  |
| 6 | 1 | Controller Set 7 Switch | Off, On | 01 |  |
| 7 | 1 | Controller Set 8 Switch | Off, On | 01 |  |
| 8 | 1 | Controller Set 9 Switch | Off, On | 01 |  |
| 9 | 1 | Controller Set 10 Switch | Off, On | 01 |  |
| 10 | 1 | Controller Set 11 Switch | Off, On | 01 |  |
| 11 | 1 | Controller Set 12 Switch | Off, On | 01 |  |
| 12 | 1 | Controller Set 13 Switch | Off, On | 01 |  |
| 13 | 1 | Controller Set 14 Switch | Off, On | 01 |  |
| 14 | 1 | Controller Set 15 Switch | Off, On | 01 |  |
| 15 | 1 | Controller Set 16 Switch | Off, On | 01 |  |
| 16 | 1 | Controller Set 17 Switch | Off, On | 01 |  |
| 17 | 1 | Controller Set 18 Switch | Off, On | 01 |  |
| 18 | 1 | Controller Set 19 Switch | Off, On | 01 |  |
| 19 | 1 | Controller Set 20 Switch | Off, On | 01 |  |
| 20 | 1 | Controller Set 21 Switch | Off, On | 01 |  |
| 21 | 1 | Controller Set 22 Switch | Off, On | 01 |  |
| 22 | 1 | Controller Set 23 Switch | Off, On | 01 |  |
| 23 | 1 | Controller Set 24 Switch | Off, On | 01 |  |
| 24 | 1 | Controller Set 25 Switch | Off, On | 01 |  |
| 25 | 1 | Controller Set 26 Switch | Off, On | 01 |  |
| 26 | 1 | Controller Set 27 Switch | Off, On | 01 |  |
| 27 | 1 | Controller Set 28 Switch | Off, On | 01 |  |
| 28 | 1 | Controller Set 29 Switch | Off, On | 01 |  |
| 29 | 1 | Controller Set 30 Switch | Off, On | 01 |  |
| 30 | 1 | Controller Set 31 Switch | Off, On | 01 |  |
| 31 | 1 | Controller Set 32 Switch | Off, On | 01 |  |
| 32 | 1 | Operator Key Controller Set 1 Switch | Off, On | 01 |  |
| 33 | 1 | Operator Key Controller Set 2 Switch | Off, On | 01 |  |
| 34 | 1 | Operator Key Controller Set 3 Switch | Off, On | 01 |  |
| 35 | 1 | Operator Key Controller Set 4 Switch | Off, On | 01 |  |
| 36 | 1 | LFO Box 1 Switch | Off, On | 01 |  |
| 37 | 1 | LFO Box 2 Switch | Off, On | 01 |  |
| 38 | 1 | LFO Box 3 Switch | Off, On | 01 |  |

## `3p 02 0o 00` — 76 bytes
`.pfm` block: `fmx.op`
_p = Part number 0–F                   Part 1 – 16 (FM-X) o = Operator number 0–7                   Operator 1 – 8_

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 2 | Oscillator Key On Reset | Off, On | 00 01 |  |
| 2 | 2 | Oscillator Frequency Mode | Ratio, Fixed | 00 00 |  |
| 4 | 2 | Tune Coarse | 0 – 31 | 00 01 |  |
| 6 | 2 | Tune Fine | 0 – 127 | 00 00 |  |
| 8 | 2 | Detune | −15 – 0 – 15 | 00 0F |  |
| 10 | 2 | Pitch Key Follow Sensitivity | 0 – 99 | 00 00 | This is available when Oscillator Mode is set to Fixed. |
| 12 | 2 | Pitch Velocity Sensitivity | −7 – 0 – +7 | 00 07 |  |
| 14 | 2 | Spectral Form | Sine, All 1, All 2, Odd 1, Odd 2, Res 1, Res 2 | 00 00 |  |
| 16 | 2 | Spectral Skirt | 0–7 | 00 00 |  |
| 18 | 2 | Spectral Resonance | 0 – 99 | 00 00 |  |
| 20 | 2 | PEG Initial Level | −50 – 0 – +50 | 00 32 |  |
| 22 | 2 | PEG Attack Level | −50 – 0 – +50 | 00 32 |  |
| 24 | 2 | PEG Attack Time | 0 – 99 | 00 00 |  |
| 26 | 2 | PEG Decay Time | 0 – 99 | 00 00 |  |
| 28 | 2 | AEG Attack Level | 0 – 99 | 00 63 |  |
| 30 | 2 | AEG Decay 1 Level | 0 – 99 | 00 63 |  |
| 32 | 2 | AEG Decay 2 Level | 0 – 99 | 00 63 |  |
| 34 | 2 | AEG Release (Hold) Level | 0 – 99 | 00 00 |  |
| 36 | 2 | AEG Attack Time | 0 – 99 | 00 00 |  |
| 38 | 2 | AEG Decay 1 Time | 0 – 99 | 00 00 |  |
| 40 | 2 | AEG Decay 2 Time | 0 – 99 | 00 00 |  |
| 42 | 2 | AEG Release Time | 0 – 99 | 00 28 |  |
| 44 | 2 | AEG Hold Time | 0 – 99 | 00 00 |  |
| 46 | 2 | AEG Time Key Follow Sensitivity | 0–7 | 00 00 |  |
| 48 | 2 | Operator Level | 0 – 99 | 00 00 | When Operator number is “7,” the initial value is 00 55. |
| 50 | 2 | Level Scaling Break Point | A-1 – C8 | 00 27 |  |
| 52 | 2 | Level Scaling Low Depth | 0 – 99 | 00 00 |  |
| 54 | 2 | Level Scaling High Depth | 0 – 99 | 00 00 |  |
| 56 | 2 | Level Scaling Low Curve −Linear, −Exp, | +Exp, +Linear | 00 00 |  |
| 58 | 2 | Level Scaling High Curve | −Linear, −Exp, +Exp, +Linear | 00 00 |  |
| 60 | 2 | Level Velocity Sensitivity | −7 – 0 – +7 | 00 07 |  |
| 62 | 2 | 2nd LFO Pitch Modulation Depth Offset | 0–7 | 00 03 |  |
| 64 | 2 | 2nd LFO Amplitude Modulation Depth Offset | 0–7 | 00 03 |  |
| 66 | 2 | Pitch Controller Sensitivity | −7 – 0 – 7 | 00 07 |  |
| 68 | 2 | Level Controller Sensitivity | −7 – 0 – 7 | 00 07 | 252 |
| 70 | 2 | Part LFO Destination 1 Depth Ratio | 0–127 | 00 7F |  |
| 72 | 2 | Part LFO Destination 2 Depth Ratio | 0–127 | 00 7F |  |
| 74 | 2 | Part LFO Destination 3 Depth Ratio | 0–127 | 00 7F |  |

## `7p 01 0o 00` — 4 bytes
_p = Part number 0–F                   Part 1 – 16 (FM-X) o = Operator number 0–7                   Operator 1 – 8_

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 2 | Operator Ratio | 00 00 – 18 7F | 00 00 |  |
| 2 | 2 | Operator Frequency | 00 00 – 15 7F | 00 00 |  |
