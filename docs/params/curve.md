# CURVE

## `01 00 nn 00` — 20 bytes
_nn = user curve number 00 – 1F           User Curve 1 – 32_

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 1 | Curve Name 1 | 0, 32 – 126 (ASCII) Init Curve |  |  |
| 1 | 1 | Curve Name 2 | 0, 32 – 126 (ASCII) 1-32 (same as |  |  |
| 2 | 1 | Curve Name 3 | 0, 32 – 126 (ASCII) the table |  |  |
| 3 | 1 | Curve Name 4 | 0, 32 – 126 (ASCII) number) |  |  |
| 4 | 1 | Curve Name 5 | 0, 32 – 126 (ASCII) |  |  |
| 5 | 1 | Curve Name 6 | 0, 32 – 126 (ASCII) |  |  |
| 6 | 1 | Curve Name 7 | 0, 32 – 126 (ASCII) |  |  |
| 7 | 1 | Curve Name 8 | 0, 32 – 126 (ASCII) |  |  |
| 8 | 1 | Curve Name 9 | 0, 32 – 126 (ASCII) |  |  |
| 9 | 1 | Curve Name | 00, 20 – 7E | 10 | 0, 32 – 126 (ASCII) |
| 10 | 1 | Curve Name @10 | 00, 20 – 7E | 11 | 0, 32 – 126 (ASCII) |
| 11 | 1 | Curve Name @11 | 00, 20 – 7E | 12 | 0, 32 – 126 (ASCII) |
| 12 | 1 | Curve Name @12 | 00, 20 – 7E | 13 | 0, 32 – 126 (ASCII) |
| 13 | 1 | Curve Name @13 | 00, 20 – 7E | 14 | 0, 32 – 126 (ASCII) |
| 14 | 1 | Curve Name @14 | 00, 20 – 7E | 15 | 0, 32 – 126 (ASCII) |
| 15 | 1 | Curve Name @15 | 00, 20 – 7E | 16 | 0, 32 – 126 (ASCII) |
| 16 | 1 | Curve Name @16 | 00, 20 – 7E | 17 | 0, 32 – 126 (ASCII) |
| 17 | 1 | Curve Name @17 | 00, 20 – 7E | 18 | 0, 32 – 126 (ASCII) |
| 18 | 1 | Curve Name @18 | 00, 20 – 7E | 19 | 0, 32 – 126 (ASCII) |
| 19 | 1 | Curve Name @19 | 00, 20 – 7E | 20 | 0, 32 – 126 (ASCII) |

## `01 01 nn 00` — 34 bytes

| off | sz | key | range / values | default | notes |
|---|---|---|---|---|---|
| 0 | 2 | Curve Input 1 | 0 | 00 00 | Fixed to “0” |
| 2 | 2 | Curve Input 2 | 1 – 1017 | 01 12 |  |
| 4 | 2 | Curve Input 3 | 2 – 1018 | 02 24 |  |
| 6 | 2 | Curve Input 4 | 3 – 1019 | 03 36 |  |
| 8 | 2 | Curve Input 5 | 4 – 1020 | 04 48 |  |
| 10 | 2 | Curve Input 6 | 5 – 1021 | 05 5A |  |
| 12 | 2 | Curve Input 7 | 6 – 1022 | 06 6C |  |
| 14 | 2 | Curve Input 8 | 7 – 1023 | 07 7F | Fixed to 07 7F in the Linear Mode |
| 16 | 2 | Curve Output 1 | 0 – 1023 | 00 00 |  |
| 18 | 2 | Curve Output 2 | 0 – 1023 | 01 12 |  |
| 20 | 2 | Curve Output 3 | 0 – 1023 | 02 24 |  |
| 22 | 2 | Curve Output 4 | 0 – 1023 | 03 36 |  |
| 24 | 2 | Curve Output 5 | 0 – 1023 | 04 48 |  |
| 26 | 2 | Curve Output 6 | 0 – 1023 | 05 5A |  |
| 28 | 2 | Curve Output 7 | 0 – 1023 | 06 6C |  |
| 30 | 2 | Curve Output 8 | 0 – 1023 | 07 7F |  |
| 32 | 2 | Curve Type | 00 = Linear, 01 = Step | 00 00 |  |
