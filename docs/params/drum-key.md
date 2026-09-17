# DRUM VOICE KEY

## `2p 10 kk 00` — 64 bytes
`.pfm` block: `drum.key`
_p = Part number 00 – 0F                Part 1 – 16 (Drum) kk = Key number 00 – 48                Key C0 – C6 MONTAGE M Data List           250_

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 2 | Drum Key Switch | Off, On | 00 01 |  |
| 2 | 2 | Wave Select | 0=Preset, 1=User, 2–17=Library1–16, 18-25=Library17– 24 | 00 00 |  |
| 4 | 2 | Receive Note Off | Off, On | 00 00 |  |
| 6 | 2 | Key Assign Mode | Single, Multi | 00 01 |  |
| 8 | 2 | Alternate Group | 0:Off, 1 – 127 | 00 00 |  |
| 10 | 2 | Wave Number | 1 – 7620 (USR, Library:1 – 1024) | 28 1C |  |
| 12 | 2 | Pan | L63 – C – R63 | 00 40 |  |
| 14 | 2 | Random Pan Depth | 0 – 127 | 00 00 |  |
| 16 | 2 | Alternate Pan Depth | L64 – C – R63 | 00 40 |  |
| 18 | 2 | Drum Key Reverb Send Level | 0 – 127 | 00 5A |  |
| 20 | 2 | Drum Key Variation Send Level | 0 – 127 | 00 00 |  |
| 22 | 2 | Drum Key Connection Switch | Thru, InsA, InsB | 00 00 |  |
| 24 | 2 | Drum Key Output Select | 0: MainL&R, 8: AsgnL&R, 9-23: USB1&2 – USB29&30, 64 – 95: AsgnL, AsgnR, USB1 – USB30 | 00 00 |  |
| 26 | 2 | Drum Key Level | 0 – 127 | 00 7F |  |
| 28 | 2 | Level Velocity Sensitivity | −64 – +63 | 00 40 |  |
| 30 | 2 | AEG Attack Time | 0 – 127 | 00 00 |  |
| 32 | 2 | AEG Decay 1 Time | 0 – 127 | 00 60 |  |
| 34 | 2 | AEG Decay 2 Time | 0 – 126, Hold | 00 50 |  |
| 36 | 2 | AEG Decay 1 Level | 0 – 127 | 00 7F |  |
| 38 | 2 | Coarse Tune | −48 – +48 | 00 40 |  |
| 40 | 2 | Fine Tune | −64 – +63 | 00 40 |  |
| 42 | 2 | Pitch Velocity Sensitivity | −64 – +63 | 00 40 |  |
| 44 | 2 | LPF Cutoff Frequency | 0 – 1023 | 07 7F |  |
| 46 | 2 | LPF Cutoff Velocity Sensitivity | −64 – +63 | 00 40 |  |
| 48 | 2 | LPF Resonance | 0 – 127 | 00 00 |  |
| 50 | 2 | HPF Cutoff Frequency | 0 – 1023 | 00 00 |  |
| 52 | 2 | EQ Type | 2 Band, P.EQ, Boost6, Boost12, Boost18, Thru | 00 00 |  |
| 54 | 2 | EQ Q | 0.7 – 10.3 | 00 00 |  |
| 56 | 2 | EQ 1 Frequency | 50.1 – 2.00k (2-band) 139.7 – 12.9k (P.EQ) | 00 36 (2- band) 01 1D (P.EQ) | This is available only when 2-band or P.EQ is selected for EQ Type. |
| 58 | 2 | EQ 1 Gain | −12.00dB – +12.00dB | 00 40 |  |
| 60 | 2 | EQ 2 Frequency | 503.8 – 10.1k | 01 67 | This is available only when 2-band is selected for EQ Type. |
| 62 | 2 | EQ 2 Gain | −12.00dB – +12.00dB | 00 40 |  |
