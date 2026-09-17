# MONTAGE M / MODX M sound engines: what a performance is made of

This is the working model used by `tools/build_performance.py`. Parameter names are the keys in
`data/midi_param_tables.json` / `docs/params/*.md` (derived from the official Data List); usage
observations come from decoding the 3631 factory performances (`tools/corpus_stats.py`).

## Hierarchy

```
Performance (name, category, tempo, scenes 1–8, Super Knob, 8 common Assignable Knobs,
             32 common controller boxes, system effects: Reverb, Variation, Master EQ, Master FX)
 └─ Part 1..16 (engine, name, volume/pan, note & velocity range, mono/poly, portamento,
                sends to Reverb/Variation, Insertion A + B, 8 arpeggios, Part LFO,
                32 controller boxes, 4 motion-seq lanes, 8 part Assignable Knobs)
     ├─ AWM2 : 1..128 Elements (sample wave, pitch, filter, amp, EGs, element LFO)
     ├─ Drum : 73 keys C0..C6 (wave, pitch, filter, amp per key)
     ├─ FM-X : 8 Operators + algorithm (1..88) + feedback + one filter + PEG + 2nd LFO
     └─ AN-X : 3 Oscillators + noise + 2 Filters + wave folder + EGs/LFOs per section
```

Parts 1–8 can be played from the keyboard (`Keyboard Control Switch`); parts 9–16 are for
MIDI/sequencer use. The audio path per part: engine → Insertion A/B (series A→B, B→A or parallel,
`Insertion Connection Type`) → dry level + Reverb Send / Variation Send → Master EQ → Master FX.

## Part-level parameters that matter most

| Block | Keys | Notes |
|---|---|---|
| p1 (1-byte) | `Part Switch`, `Keyboard Control Switch`, `Mono/Poly Mode` (0 mono, 1 poly), `Key Assign Mode` (0 Single = legato-capable, 1 Multi), `Portamento Switch`, `Part Arp Switch`, `Receive …`/`Transmit …` flags | |
| p2 (2-byte) | `Part Main Category`, `Part Sub Category`, `Velocity Limit Low/High`, `Note Limit Low/High`, `Velocity Sensitivity Depth/Offset`, `Volume`, `Pan`, `Reverb Send`, `Variation Send`, `Dry Level`, `Note Shift`, `Detune`, `Cutoff`/`Resonance` offsets, `AEG/FEG` offsets, `Arpeggio Group` … | offsets are ±64 around 64 |
| p3 (2-byte) | `Portamento Time`, `Portamento Mode` (Fingered/Full-time), `Portamento Time Mode`, `Insertion Connection Type` (0 Parallel, 1 Ins A→B, 2 Ins B→A), 3-band part EQ, side-chain part | factory: 80% use A→B |
| ins A / ins B | `Insertion-A Type` (effect type), `Insertion-A Preset Number`, `Insertion-A Parameter 1..24` | parameter meaning per type: `data/effect_params.json` |
| arp | `Arp Hold` (0 Sync-Off, 1 Off, 2 On), `Arp 1..8 Number`, `Arp Unit Multiply`, `Arp Note/Velocity Limit`, `Arp Key Mode`, `Arp Gate Time`, `Arp Swing`… | 8 arp slots selected by the Scene/arp select |
| lfo | Part LFO: `LFO Wave`, `LFO Speed`, `LFO Destination 1..3`, depths, tempo sync | destinations use the *LFO Box* list |
| ctrlbox ×32 | `Controller Set Switch/Source/Destination/Curve Type/Curve Parameter 1-2/Polarity/Ratio` | the mod matrix, see `controllers-reference.md` |

## AWM2 (sample playback)

Element = one sample "waveform" with its own pitch/filter/amp and envelopes. Factory sounds use
8 elements in 97% of parts (extended element switch allows up to 128).

* **osc**: `Wave Select` (0 preset), `Wave Number` (`data/waveforms.json`: 7647 presets;
  stereo waves end in "St", key-off samples "KeyOff", velocity layers "p/mf/f" or "v01..v09"),
  `Element Pan`, `Note Limit Low/High`, `Velocity Limit Low/High`, `Velocity Cross Fade`,
  `XA Control` (0 Normal, 1 Legato, 2 Key Off, 3 Cycle, 4 Random, 5 A.SW Off, 6 A.SW1 On,
  7 A.SW2 On) and `Element Group Number` for XA groups, `Key On Delay`, `Element Connection Switch`
  (element → insertion or thru).
* **pitch**: `Coarse Tune`, `Fine Tune`, `Pitch Key Follow`, `Pitch Velocity Sensitivity`, PEG
  (Hold/Attack/Decay1/Decay2/Release times + levels, depth, velocity/key follow), `Random Pitch`.
* **filter**: `Filter Type` (0 LPF24D, 1 LPF24A, 2 LPF18, 3 LPF18s, 4 LPF12+HPF12, 5 LPF6+HPF12,
  6 HPF24D, 7 HPF12, 8 BPF12D, 9 BPFw, 10 BPF6, 11 BEF12, 12 BEF6, 13 DualLPF, 14 DualHPF,
  15 DualBPF, 16 DualBEF, 17 LPF12+BPF6, 18 Thru), `Filter Cutoff Frequency` (0–1023),
  `Filter Resonance/ Width`, `HPF Cutoff Frequency`, `Distance`, `Filter Gain`, FEG
  (Hold/Attack/Decay1/Decay2/Release + levels, `FEG Depth` 64 = 0), cutoff key follow and
  scaling break points, element EQ (`EQ Type`, `EQ 1/2 Frequency/Gain`, `EQ Q`), element LFO
  (`LFO Wave`, `LFO Speed`, pitch/filter/amplitude modulation depth, `LFO Extended Speed`).
  Factory usage: type 4 (LPF12+HPF12) is the default and half of all elements; 1 LPF24A and
  0 LPF24D for synth-style resonant sweeps; 5 LPF6+HPF12 on acoustic layers.
* **amp**: `Element Level`, `Level Velocity Sensitivity`, `Level Velocity Offset`, AEG
  (`AEG Attack Time`, `AEG Decay 1 Time`, `AEG Decay 2 Time`, `AEG Release Time`, `AEG Initial/
  Attack/Decay 1/Decay 2 Level`, `Half Damper Time`), level scaling break points, `Amplitude
  Key Follow`, `AEG Time Velocity Sensitivity`.

Typical factory constructions (decoded from the bank):
* **Acoustic piano (CFX Concert)**: 9 velocity layers `CFX v01 St`..`CFX v09 St`, velocity
  windows 2–25, 26–35 … 126–127, each with its own cutoff (brighter for harder layers), plus a
  duplicate set of layers for the top notes (note limit 92–127) with longer release, plus a
  `CFX KeyOff St` element with `XA Control` = Key Off. Insertion A = DAMPER RESONANCE, B = VCM
  EQ 501, reverb HD HALL.
* **Orchestral strings (Seattle Sections)**: one part per section (Violins 1st/2nd, Violas,
  Cellos, Basses) panned across the stage (pan 19/29/64/99/104), each with p/mf/f layers,
  `XA Control` 5/6/7 (assignable-switch articulation) for legato/spiccato alternates, Insertion
  A VCM EQ 501, B EARLY REFLECTION, mod wheel → AEG Attack/Release and fine tune.
* **Analog-style pads**: `Fat Saw St`, `StrongDetuned Pad St`, `PWM Strings St`, `Long Saw` …
  with slow AEG attack, LPF24A/LPF24D, FEG depth and mod wheel → cutoff.

## Drum (AWM2 drum kit)

`[73] key` blocks, key 0 = C0 … 72 = C6, each: `Wave Select`/`Wave Number`, level, pan,
coarse/fine tune, filter (`Filter Type`, cutoff, resonance), AEG, `Drum Key Connection Switch`
(insertion routing), `Alternate Group`, `Receive Note Off`. `data/drum_kits.json` lists Yamaha's
153 kit layouts (wave per key), which is the easiest way to build a kit: copy the key table of the
closest factory kit and change individual keys.

## FM-X (8-operator FM)

* **common**: `Algorithm Number` (1–88, connections in `data/fmx_algorithms.json`), `Feedback
  Level` (0–7), PEG (5 levels + 4 times, applied to every operator), `2nd LFO …` (pitch / amp /
  filter modulation), `FM Depth/Harmonics/Attack/Decay/Sustain/Release/Texture` (the Smart
  Morph-era macro controls), key-on delay, pan depth.
* **filter** (one per part): same filter set as AWM2 (`Filter Type` default 21 = thru? see
  table; factory: 1 LPF24A, 21, 0), FEG, cutoff scaling, part EQ, LFO.
* **op ×8**: `Oscillator Frequency Mode` (0 Ratio, 1 Fixed), `Tune Coarse` (0–31; ratio 0.5 when
  0, then 1..31), `Tune Fine`, `Detune`, `Spectral Form` (0 Sine, 1 All 1, 2 All 2, 3 Odd 1,
  4 Odd 2, 5 Res 1, 6 Res 2), `Spectral Skirt`, `Spectral Resonance`, per-op PEG, AEG (4 levels +
  hold/attack/decay1/decay2/release times), `Operator Level` (0–99), level scaling (break point,
  low/high depth/curve), `Level Velocity Sensitivity`, key follow. `op_sw` blocks (39 one-byte
  switches) choose which controller boxes / LFO reach that operator.
* Factory usage: the most used algorithms are 12, 66, 10, 25, 9, 24, 11, 80; 81% of operators
  are pure sine; 7% use fixed frequency (noise/click/bell partials).
* Example (**FM Wr 2**, Wurlitzer): algorithm 10, feedback 7, operators 3–8 at levels
  69/77/99/70/77/99 with coarse 1/2/1/1/1/1, mod wheel → tremolo insertion depth.

## AN-X (virtual analog)

* **common** (110 bytes): pan depths, key-on delay, `Unison` (0 off, 1 = 2 voices, 2 = 4),
  `Unison Detune`, `Unison Spread`, `OSC Reset` (0 Off, 1 Phase, 2 Tune, 3 Full), `Voltage Drift`,
  `Ageing`, Pitch EG (attack/decay/sustain/release, times 0–255, sustain 0–511) and Pitch LFO,
  `Noise Generator Tone/Out Select/Out Level`, Filter Cutoff EG (A/D/S/R) and Cutoff LFO,
  `Amplitude Level`, `Amplitude Saturator Drive`, Amplitude EG (A/D/S/R) and LFO.
* **osc ×3** (78 bytes): `Oscillator Wave` (0 Saw1, 1 Saw2, 2 Square, 3 Triangle, 4 Sine),
  `Oscillator Octave` (0 64' … 3 8' … 6 1'), `Oscillator Pitch` (cents, 504 = 0), pitch EG/LFO
  depth, `Oscillator Self Sync Pitch` + EG/LFO depth (sync sweeps), `Oscillator Pulse Width`
  (128 = 50%) + velocity/EG/LFO depth, `Oscillator Wave Shaper` (+ depths), `Oscillator FM Level`,
  `Oscillator Ring Level`, `Oscillator Out Select`, `Oscillator Out Level` (0–511), its own EG
  (A/D/S/R) and LFO. `osc_sw` blocks select which controller boxes reach the oscillator.
* **filter ×2** (30 bytes): `Filter Type` (0 Thru, 1 LPF24, 2 LPF18, 3 LPF12, 4 LPF6, 5 HPF24,
  6 HPF18, 7 HPF12, 8 HPF6, 9 BPF12, 10 BPF6), `Filter Cutoff` (0–1023), `Filter Resonance`,
  `Filter Cutoff EG Depth` (256 = 0), `Filter Cutoff LFO Depth`, `Filter Cutoff Key Follow`,
  `Filter Saturator Drive`, `Filter Out Level`. Factory default routing: filter 1 = LPF24
  (type 1), filter 2 = HPF24 (type 5) or Thru.
* **fold** (34 bytes): `Modifier Wave Folder` amount + velocity/EG/LFO depth, `Modifier Wave
  Folder Texture`, `Modifier Wave Folder Type` (0 Soft, 1 Hard), Modifier EG (A/D/S/R) and LFO.
* Factory usage: oscillators mostly Saw1 (wave 0) at 8' (octave 3); 3rd oscillator is often a
  sine sub (wave 4); unison on 33% of parts; filter 1 LPF24 in 76% of parts.
* Examples: **Classic Mini Bass** = osc1 Saw 16' +37 ct, osc2 Saw 8' −37 ct, osc3 Square 2'
  PW 251, filter 1 LPF24 cutoff 445 res 44, FEG depth 326 (+70), AEG 45/90/511/37, insertion
  VCM FLANGER → RING MODULATOR, knobs 1–8 mapped to FEG depth/decay, sync, flanger, ring mod,
  delay mix. **AN-X Super SAW PAT** = three Saw1 8' at out level 511, unison 2-voice detune 3,
  LPF24 cutoff 1023, insertion VCM EQ 501 → CROSS DELAY, mod wheel → OSC pitch LFO + LFO speed.

## System effects and Master

* Reverb block (`common.reverb`): `Reverb Type` + `Reverb Parameter 1..24`. Factory: REV-X HALL
  43%, then SPX HALL, HD HALL, R3 HALL, REV-X ROOM.
* Variation block: `Variation Type` + 24 params; TEMPO CROSS DELAY 23%, then 2 MODULATOR,
  G CHORUS, TEMPO DELAY STEREO, ENSEMBLE DETUNE.
* Master FX (`Master Effect Switch` in c1, `common.mfx`): MULTI BAND COMP (default) or VCM
  COMPRESSOR 376 in nearly every factory performance; on in 24% of them.
* Insertion effects per part: A is most often VCM EQ 501 (32%), then none, VCM COMPRESSOR 376,
  CLASSIC COMPRESSOR, AMP SIMULATOR 1; B is most often none, TEMPO CROSS DELAY, VCM EQ 501,
  VCM COMPRESSOR 376, G CHORUS, CROSS DELAY, AUTO PAN, EARLY REFLECTION.
* Effect parameter meanings: `data/effect_params.json` (per type, parameter number → name,
  raw range, lookup table in `data/effect_data_assign.json`).

## Controllers (the "add a wheel/knob/Super Knob effect" layer)

Everything a performer touches goes through **controller boxes** (see
`docs/controllers-reference.md` for the full source/destination lists):

* Part box: `source` (0 Pitch Bend, 1 Mod Wheel, 2 After Touch, 3/4 Foot Ctrl 1/2, 5 Foot Switch,
  6 Ribbon, 7 Breath, 8–15 Assignable Knob 1–8, 16/17 Assignable Switch 1/2, 18–21 Motion Seq
  lane 1–4, 22–39 envelope followers) → `destination` (engine parameter, insertion effect
  parameter 1–24 of A/B, sends, volume, pan …) with `Ratio` (−128..+127, raw = display + 128),
  `Polarity` (0 unipolar, 1 bipolar), `Curve Type` (0–17 preset curves) and two curve params.
* Factory habits: Mod Wheel → element LFO pitch depth (vibrato) or cutoff; Ribbon → cutoff/pitch;
  Assignable Knob n → cutoff / element level / sends / insertion parameters; Assignable Switch 2 →
  AEG release; After Touch → LFO depth.
* **Super Knob**: the 8 *common* Assignable Knobs each have a `Link Switch` (c1 block); the Super
  Knob sweeps every linked knob between its Left/Mid/Right value (`common.superknob` block). A
  common controller box then maps `AsgnKnob n` → `Part p Assign k` (destination "Part 1 Assign 1"
  = part 1's Assignable Knob 1), and the part's own boxes map `AsgnKnob k` → the parameter. That
  chain is what every "…PAT"/Super Knob factory sound does, e.g. AN-X Sticky Bass: common box
  AsgnKnob 1 → Part 1..8 Assign 1, part boxes AsgnKnob 1 → Cutoff (+53). Knob names live in
  `common.knobnames` / `part.knobnames` (16 chars).
* Scenes (`common.scenes`, `part.scenes`) store per-scene mixing/arp/motion-seq snapshots and a
  Super Knob value; `Scene Select` in c2 picks the initial one.
