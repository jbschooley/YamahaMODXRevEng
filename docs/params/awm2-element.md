# NORMAL PART ELEMENT

## `2p 00 ee 00` — 43 bytes (Data List prints TOTAL SIZE 36; rows and files give 43)
`.pfm` block: `el.e1`
_p = Part number 0–F                    Part 1 – 16 (Normal) ee = Element number 0 – 127                Element 1 – 128 (Normal)_

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 1 | Element Switch | Off, On | 01 (EL1 only) |  |
| 1 | 1 | Key On Delay Tempo Sync Switch | Off, On | 00 |  |
| 2 | 1 | Half Damper Switch | Off, On | 00 |  |
| 3 | 1 | LFO Box1 Switch | Off, On | 01 |  |
| 4 | 1 | LFO Box2 Switch | Off, On | 01 |  |
| 5 | 1 | LFO Box3 Switch | Off, On | 01 |  |
| 6 | 1 | LFO Speed Range | Normal, Extended | 01 |  |
| 7 | 1 | Controller Set 1 Switch | Off, On | 01 |  |
| 8 | 1 | Controller Set 2 Switch | Off, On | 01 |  |
| 9 | 1 | Controller Set 3 Switch | Off, On | 01 |  |
| 10 | 1 | Controller Set 4 Switch | Off, On | 01 |  |
| 11 | 1 | Controller Set 5 Switch | Off, On | 01 |  |
| 12 | 1 | Controller Set 6 Switch | Off, On | 01 |  |
| 13 | 1 | Controller Set 7 Switch | Off, On | 01 |  |
| 14 | 1 | Controller Set 8 Switch | Off, On | 01 |  |
| 15 | 1 | Controller Set 9 Switch | Off, On | 01 |  |
| 16 | 1 | Controller Set 10 Switch | Off, On | 01 |  |
| 17 | 1 | Controller Set 11 Switch | Off, On | 01 |  |
| 18 | 1 | Controller Set 12 Switch | Off, On | 01 |  |
| 19 | 1 | Controller Set 13 Switch | Off, On | 01 |  |
| 20 | 1 | Controller Set 14 Switch | Off, On | 01 |  |
| 21 | 1 | Controller Set 15 Switch | Off, On | 01 |  |
| 22 | 1 | Controller Set 16 Switch | Off, On | 01 |  |
| 23 | 1 | Controller Set 17 Switch | Off, On | 01 |  |
| 24 | 1 | Controller Set 18 Switch | Off, On | 01 |  |
| 25 | 1 | Controller Set 19 Switch | Off, On | 01 |  |
| 26 | 1 | Controller Set 20 Switch | Off, On | 01 |  |
| 27 | 1 | Controller Set 21 Switch | Off, On | 01 |  |
| 28 | 1 | Controller Set 22 Switch | Off, On | 01 |  |
| 29 | 1 | Controller Set 23 Switch | Off, On | 01 |  |
| 30 | 1 | Controller Set 24 Switch | Off, On | 01 |  |
| 31 | 1 | Controller Set 25 Switch | Off, On | 01 |  |
| 32 | 1 | Controller Set 26 Switch | Off, On | 01 |  |
| 33 | 1 | Controller Set 27 Switch | Off, On | 01 |  |
| 34 | 1 | Controller Set 28 Switch | Off, On | 01 |  |
| 35 | 1 | Controller Set 29 Switch | Off, On | 01 |  |
| 36 | 1 | Controller Set 30 Switch | Off, On | 01 |  |
| 37 | 1 | Controller Set 31 Switch | Off, On | 01 |  |
| 38 | 1 | Controller Set 32 Switch | Off, On | 01 |  |
| 39 | 1 | Key Controller Set 1 Switch | Off, On | 01 |  |
| 40 | 1 | Key Controller Set 2 Switch | Off, On | 01 |  |
| 41 | 1 | Key Controller Set 3 Switch | Off, On | 01 |  |
| 42 | 1 | Key Controller Set 4 Switch | Off, On | 01 |  |

## `2p 01 ee 00` — 40 bytes
`.pfm` block: `el.osc`
_p = Part number 0–F                   Part 1 – 16 (Normal) ee = Element number 0 – 127               Element 1 – 128 (Normal)_

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 2 | Wave Select | 0=Preset, 1=User, 2–17=Library1–16, 18-25=Library17–24 | 00 00 |  |
| 2 | 2 | Element Group Number | 1–8 | 00 00 |  |
| 4 | 2 | Wave Number | 1 – 7620 (USR, Library: 1 – 1024) | 00 06 |  |
| 6 | 2 | (reserved) Receive Note Off | on | 00 01 | Fixed to “on” |
| 8 | 2 | (reserved) Key Assign | 1=multi | 00 01 | Fixed to “multi” |
| 10 | 2 | (reserved) Alternate Group | 0=off | 00 00 | Fixed to “off” |
| 12 | 2 | Element Pan | L63 – C – R63 | 00 40 |  |
| 14 | 2 | Random Pan Depth | 0 – 127 | 00 00 |  |
| 16 | 2 | Alternate Pan Depth | L64 – C – R63 | 00 40 |  |
| 18 | 2 | Scaling Pan Depth | −64 – +63 | 00 40 |  |
| 20 | 2 | XA Control | Normal, Legato, Key Off, Cycle, Random, A.SW Off, A.SW1 On, A.SW2 On | 00 00 |  |
| 22 | 2 | Note Limit Low | C-2 – G8 | 00 00 |  |
| 24 | 2 | Note Limit High | C-2 – G8 | 00 7F |  |
| 26 | 2 | Velocity Limit Low | 1 – 127 | 00 01 |  |
| 28 | 2 | Velocity Limit High | 1 – 127 | 00 7F |  |
| 30 | 2 | Velocity Cross Fade | 0 – 127 | 00 00 |  |
| 32 | 2 | Key On Delay Time Length | 0 – 127 | 00 00 | This is available only when Tempo Sync is set to Off. |
| 34 | 2 | Element Connection Switch | Thru, InsA, InsB | 00 01 |  |
| 36 | 2 | (reserved) Output Select | 0=stereo out | 00 00 | Fixed to “stereo out” |
| 38 | 2 | Key On Delay Note Length | 5 – 21 (16th, 8th/3, 16th., 8th, 4th/3, 8th., 4th, 2th/3, 4th., 2nd, Whole/3, 2nd., 4thX4, 4thX5, 4thX6, 4thX7, 4thX8) | 00 0B | This is available only when Tempo Sync is set to On. |

## `2p 02 ee 00` — 54 bytes
`.pfm` block: `el.amp`
_p = Part number 0–F                   Part 1 – 16 (Normal) ee = Element number 0 – 127               Element 1 – 128 (Normal)_

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 2 | Element Level | 0 – 127 | 00 7F |  |
| 2 | 2 | Level Velocity Sensitivity | −64 – +63 | 00 40 |  |
| 4 | 2 | Level Velocity Offset | 0 – 127 | 00 00 |  |
| 6 | 2 | Level Sensitivity Key Curve | 00 – 04 | 00 03 |  |
| 8 | 2 | AEG Attack Time | 0 – 127 | 00 00 |  |
| 10 | 2 | AEG Decay 1 Time | 0 – 127 | 00 40 |  |
| 12 | 2 | AEG Decay 2 Time | 0 – 127 | 00 40 |  |
| 14 | 2 | Half Damper Time | 0 – 127 | 00 7F |  |
| 16 | 2 | AEG Release Time | 0 – 127 | 00 32 |  |
| 18 | 2 | AEG Initial Level | 0 – 127 | 00 00 |  |
| 20 | 2 | AEG Attack Level | 0 – 127 | 00 7F |  |
| 22 | 2 | AEG Decay 1 Level | 0 – 127 | 00 7F |  |
| 24 | 2 | AEG Decay 2 Level | 0 – 127 | 00 7F |  |
| 26 | 2 | AEG Time Velocity Segment | Attack, Atk+Dcy, Decay, Atk+Rls, All | 00 04 |  |
| 28 | 2 | AEG Time Velocity Sensitivity | −64 – +63 | 00 40 |  |
| 30 | 2 | AEG Time Key Follow Sensitivity | −64 – +63 | 00 40 |  |
| 32 | 2 | AEG Time Key Follow Center Note | C-2 – G8 | 00 18 |  |
| 34 | 2 | Level Scaling Break Point 1 | C-2 – E8 | 00 24 | BP1<BP 2<BP3< BP4 |
| 36 | 2 | Level Scaling Break Point 2 | C#-2 – F8 | 00 30 | BP1<BP 2<BP3< BP4 |
| 38 | 2 | Level Scaling Break Point 3 | D-2 – F#8 | 00 3C | BP1<BP 2<BP3< BP4 |
| 40 | 2 | Level Scaling Break Point 4 | D#-2 – G8 | 00 48 | BP1<BP 2<BP3< BP4 |
| 42 | 2 | Level Scaling Offset 1 | −128 – +127 | 01 00 | 248 |
| 44 | 2 | Level Scaling Offset 2 | 〃 | 01 00 |  |
| 46 | 2 | Level Scaling Offset 3 | 〃 | 01 00 |  |
| 48 | 2 | Level Scaling Offset 4 | 〃 | 01 00 |  |
| 50 | 2 | Level Key Follow Sensitivity | −64 – +63 | 00 40 |  |
| 52 | 2 | AEG Time Key Follow Sensitivity Release Adjustment | 0 – 127 | 00 40 |  |

## `2p 03 ee 00` — 48 bytes
`.pfm` block: `el.pitch`
_p = Part number 0–F                   Part 1 – 16 (Normal) ee = Element number 0 – 127               Element 1 – 128 (Normal)_

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 2 | Coarse Tune | −48 – +48 | 00 40 |  |
| 2 | 2 | Fine Tune | −64 – +63 | 00 40 |  |
| 4 | 2 | Pitch Velocity Sensitivity | −64 – +63 | 00 40 |  |
| 6 | 2 | Random Pitch Depth | 0 – 127 | 00 00 |  |
| 8 | 2 | Pitch Key Follow Sensitivity | −200% – +200% | 00 60 |  |
| 10 | 2 | Pitch Key Follow Sensitivity Center Note | C-2 – G8 | 00 3C |  |
| 12 | 2 | Fine Tune Key Follow Scaling Sensitivity | −64 – +63 | 00 40 |  |
| 14 | 2 | PEG Hold Time | 0 – 127 | 00 00 |  |
| 16 | 2 | PEG Attack Time | 0 – 127 | 00 28 |  |
| 18 | 2 | PEG Decay 1 Time | 0 – 127 | 00 40 |  |
| 20 | 2 | PEG Decay 2 Time | 0 – 127 | 00 40 |  |
| 22 | 2 | PEG Release Time | 0 – 127 | 00 40 |  |
| 24 | 2 | PEG Hold Level | −128 – +127 (−4800 – +4800 [cent]) | 01 00 |  |
| 26 | 2 | PEG Attack Level | 〃 | 01 00 |  |
| 28 | 2 | PEG Decay 1 Level | 〃 | 01 00 |  |
| 30 | 2 | PEG Decay 2 Level | 〃 | 01 00 |  |
| 32 | 2 | PEG Release Level | 〃 | 01 00 |  |
| 34 | 2 | PEG Depth | −64 – +63 | 00 54 |  |
| 36 | 2 | PEG Time Velocity Sensitivity Segment | Attack, Atk+Dcy, Decay, Atk+Rls, All | 00 04 |  |
| 38 | 2 | PEG Time Velocity Sensitivity | −64 – +63 | 00 40 |  |
| 40 | 2 | PEG Depth Velocity Sensitivity | −64 – +63 | 00 40 |  |
| 42 | 2 | PEG Depth Velocity Sensitivity Curve | 00 – 04 | 00 02 |  |
| 44 | 2 | PEG Time Key Follow Sensitivity | −64 – +63 | 00 40 |  |
| 46 | 2 | PEG Time Key Follow Sensitivity Center Note | C-2 – G8 | 00 3C |  |

## `2p 04 ee 00` — 108 bytes (Data List prints TOTAL SIZE 106; rows and files give 108)
`.pfm` block: `el.filter`
_p = Part number ee = Element number_

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 2 | Filter Type | LPF24D, LPF24A, LPF18, LPF18s, LPF12+HPF12, LPF6+HPF12, HPF24D, HPF12, BPF12D, BPFw, BPF6, BEF12, BEF6, DualLPF, DualHPF, DualBPF, DualBEF, LPF12+BPF6, Thru | 00 04 |  |
| 2 | 2 | Filter Cutoff Frequency | 0 – 1023 | 05 00 |  |
| 4 | 2 | Filter Cutoff Velocity Sensitivity | −64 – +63 | 00 40 |  |
| 6 | 2 | Filter Resonance/ Width | 0 – 127 | 00 00 | Not available for LPF6+HP F12. |
| 8 | 2 | Filter Resonance Velocity Sensitivity | −64 – +63 | 00 40 |  |
| 10 | 2 | HPF Cutoff Frequency | 0 – 1023 | 00 00 |  |
| 12 | 2 | Distance | −128 – +127 | 01 00 | This is available when Filter Type is set to Dual. |
| 14 | 2 | Filter Gain | 0 – 255 | 01 66 |  |
| 16 | 2 | FEG Hold Time | 0 – 127 | 00 00 |  |
| 18 | 2 | FEG Attack Time | 0 – 127 | 00 00 |  |
| 20 | 2 | FEG Decay 1 Time | 0 – 127 | 00 40 |  |
| 22 | 2 | FEG Decay 2 Time | 0 – 127 | 00 40 |  |
| 24 | 2 | FEG Release Time | 0 – 127 | 00 50 |  |
| 26 | 2 | FEG Hold Level | −128 – +127 (−9600 – +9600 [cent]) | 01 00 |  |
| 28 | 2 | FEG Attack Level | 〃 | 01 7F |  |
| 30 | 2 | FEG Decay 1 Level | 〃 | 01 7F |  |
| 32 | 2 | FEG Decay 2 Level | 〃 | 01 7F |  |
| 34 | 2 | FEG Release Level | 〃 | 01 00 |  |
| 36 | 2 | FEG Depth | −64 – +63 | 00 68 |  |
| 38 | 2 | FEG Time Velocity Sensitivity Segment | Attack, Atk+Dcy, Decay, Atk+Rls, All | 00 04 |  |
| 40 | 2 | FEG Time Velocity Sensitivity | −64 – +63 | 00 40 |  |
| 42 | 2 | FEG Depth Velocity Sensitivity | −64 – +63 | 00 40 |  |
| 44 | 2 | FEG Depth Velocity Sensitivity Curve | 00 – 04 | 00 02 |  |
| 46 | 2 | FEG Time Key Follow Sensitivity | −64 – +63 | 00 40 |  |
| 48 | 2 | FEG Time Key Follow Sensitivity Center Note | C-2 – G8 | 00 18 |  |
| 50 | 2 | Filter Cutoff Scaling Break Point 1 | C-2 – E8 | 00 24 | BP1<BP 2<BP3< BP4 |
| 52 | 2 | Filter Cutoff Scaling Break Point 2 | C#-2 – F8 | 00 30 | BP1<BP 2<BP3< BP4 |
| 54 | 2 | Filter Cutoff Scaling Break Point 3 | D-2 – F#8 | 00 3C | BP1<BP 2<BP3< BP4 |
| 56 | 2 | Filter Cutoff Scaling Break Point 4 | D#-2 – G8 | 00 48 | BP1<BP 2<BP3< BP4 |
| 58 | 2 | Filter Cutoff Scaling Offset 1 | −128 – +127 | 01 00 |  |
| 60 | 2 | Filter Cutoff Scaling Offset 2 | 〃 | 01 00 |  |
| 62 | 2 | Filter Cutoff Scaling Offset 3 | 〃 | 01 00 |  |
| 64 | 2 | Filter Cutoff Scaling Offset 4 | 〃 | 01 00 |  |
| 66 | 2 | Filter Cutoff Key Follow Sensitivity | −200% – +200% | 00 4A | 249 |
| 68 | 2 | HPF Cutoff Key Follow Sensitivity | −200% – +200% | 00 40 |  |
| 70 | 2 | EQ Type | 2-band, P.EQ, Boost6, Boost12, Boost18, Thru | 00 00 |  |
| 72 | 2 | EQ Q | 0.7 – 10.3 | 00 00 available only when P.EQ is selected for EQ Type. | This is |
| 74 | 2 | EQ 1 Frequency | 50.1 – 2.00k (2-band) 139.7 – 12.9k (P.EQ) | 00 36 (2- available band) only 01 1D when (P.EQ) 2-band or P.EQ is selected for EQ Type. | This is |
| 76 | 2 | EQ 1 Gain | −12.00dB – +12.00dB | 00 40 |  |
| 78 | 2 | EQ 2 Frequency | 503.8 – 10.1k | 01 67 available only when 2-band is selected for EQ Type. | This is |
| 80 | 2 | EQ 2 Gain | −12.00dB – +12.00dB | 00 40 |  |
| 82 | 2 | LFO Wave | Saw, Triangle, Square | 00 01 |  |
| 84 | 2 | LFO Key On Reset | Off, On | 00 01 |  |
| 86 | 2 | LFO Delay Time | 0 – 127 | 00 00 |  |
| 88 | 2 | LFO Speed | 0 – 63 | 00 26 available only when LFO Speed Range is set to Normal. | This is |
| 90 | 2 | LFO Amplitude Modulation Depth | 0 – 127 | 00 00 |  |
| 92 | 2 | LFO Pitch Modulation Depth | 0 – 127 | 00 00 |  |
| 94 | 2 | LFO Filter Modulation Depth | 0 – 127 | 00 00 |  |
| 96 | 2 | LFO Fade In Time | 0 – 127 | 00 00 |  |
| 98 | 2 | Part LFO Phase Offset +0, +90, +120, | +180, +240, +270 | 00 00 |  |
| 100 | 2 | Part LFO Destination 1 Depth Ratio | 0 – 127 | 00 7F |  |
| 102 | 2 | Part LFO Destination 2 Depth Ratio | 0 – 127 | 00 7F |  |
| 104 | 2 | Part LFO Destination 3 Depth Ratio | 0 – 127 | 00 7F |  |
| 106 | 2 | LFO Extended Speed | 0 – 415 | 00 3C available only when LFO Speed Range is set to Extended | This is |
