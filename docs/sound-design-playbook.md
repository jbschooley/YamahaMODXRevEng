# Playbook: from "make me a sound like X" to an installed performance

This is the procedure to follow (by a person or by an assistant working in this repo) when asked
for a sound by description, by reference to a song, or by name of a classic patch.

## 0. Tools

| Step | Command |
|---|---|
| Look at how a factory sound is built | `python3 tools/pfm.py dump <factory .pfm> \| less` or the summary loop in `tools/corpus_stats.py` |
| Find a factory performance by name | `grep -i "<name>" data/performances.json` → number → `3F` + hex(number−1) file in the plugin bundle (`docs/pfm-format.md`) |
| Find waveforms | `python3 -c "import json;[print(w['number'],w['name'],w['main_category'],w['sub_category']) for w in json.load(open('data/waveforms.json'))['waveforms'] if 'saw' in w['name'].lower()]"` |
| Find arpeggios | same on `data/arpeggio_types.json` (`main_category`, `sub_category`, `original_tempo`, `time_signature`) |
| Effect types / parameters | `data/effect_types.json`, `data/effect_params.json` (`parameter_sets[].parameters`) |
| Controller sources / destinations | `data/control_sources.json`, `data/control_destinations.json` (short names work in specs) |
| Build | `python3 tools/build_performance.py spec.json out.pfm` (or `out.syx`) |
| Install into the plugin | `python3 tools/install.py add out.pfm` (close the DAW/plugin first) |
| Send to a MODX M / MONTAGE M | build `.syx`, send with any sysex tool (SysEx Librarian, `sendmidi`); it lands in the edit buffer, then STORE on the panel |

## 1. Decide the architecture

1. **Engine per part**
   * Real instruments (piano, EP samples, strings, brass, guitar, drums) → **AWM2** with the
     matching factory waveforms (search `data/waveforms.json` by category: Piano, Keys, Organ,
     Guitr, Bass, Strng, Brass, SaxWW, SynLd, Pads, SyCmp, CPerc, Dr/Pc, S.EFX, M.EFX, Ethnc).
   * Analog synth bass/lead/pad/brass, PWM, sync, wave-folder, "Minimoog / Juno / Prophet / OB"
     descriptions → **AN-X**.
   * DX-style EP, bells, glassy pads, FM basses, metallic percussion → **FM-X** (algorithm from
     `data/fmx_algorithms.json`; alg 12/66/10/25 are the most used factory choices).
   * Kits → **Drum** part; start from a factory kit's key table (`data/drum_kits.json`).
2. **Layering**: one part per timbral layer (e.g. sub + mid + noise, or piano + pad). Parts 1–8
   are keyboard parts. Pan/level them in `p2`, keep detune in `pitch`/`Oscillator Pitch`.
3. **Splits**: `note_range` per part; `velocity_range` for velocity switching between parts;
   inside AWM2 use element note/velocity limits (this is how every factory piano works).

## 2. Shape the tone (per engine)

* **AWM2**: choose waves (velocity layers p/mf/f or v01..v09 if available), set element
  `Note/Velocity Limit`, `Filter Type` + `Filter Cutoff Frequency` (0–1023, ~640 = open for most
  samples; brighter layers get higher cutoff), `Filter Resonance/ Width`, `FEG Depth` (64 = none,
  >64 opens on attack), AEG A/D1/D2/R (0–127; pads A 60–90, R 70–100; plucks D1 40–60 with
  `AEG Decay 1 Level` low), `Element Level` (100–127), `Element Pan`, `XA Control` 2 for key-off
  samples, 1 for legato alternates.
* **AN-X**: waves per oscillator (Saw1 default; Square + `Oscillator Pulse Width` 128 = 50%;
  sine sub at octave −1), `Oscillator Octave` (3 = 8'), `Oscillator Pitch` 504 = 0 (±504 = ±1200
  cents; detune ±5–40 for fatness), `Oscillator Out Level` (0–511), `Unison` 1 + `Unison
  Detune` 3–8 for supersaw, filter 1 `Filter Type` 1 (LPF24) with `Filter Cutoff` (basses
  300–500, pads 500–800), `Filter Resonance`, `Filter Cutoff EG Depth` (256 = 0, 330–400 = plucky
  sweep), common `Filter Cutoff EG …` and `Amplitude EG …` (times 0–255, sustain 0–511; the init
  template values are a good starting point), `Amplitude Saturator Drive` for grit, wave folder
  for folded/west-coast tones, `Oscillator Self Sync Pitch` for sync leads, `Oscillator FM Level`
  / `Oscillator Ring Level` for cross-mod.
* **FM-X**: pick the algorithm, set carriers to level 90–99 and modulators to 60–85 (brightness),
  ratios via `Tune Coarse` (1,2,3,14 …), `Feedback Level` for saw-like brightness, per-op AEG for
  decays (EP: modulator decays faster than carrier), `Spectral Form` ≠ 0 for AN-like operators.
  Use the FM-X filter (`fmx.filter`) for a subtractive layer on top.
* **Monophonic leads/basses**: `mono: true` (+ `legato: true` for single-trigger) and
  `portamento` with `Portamento Time` 5–30; `Portamento Mode` 0 Fingered for legato-only glide.

## 3. Effects

* Insertion A/B per part: EQ (VCM EQ 501) and compression for "pro" polish; chorus/flanger/phaser
  (G CHORUS, VCM FLANGER, VCM PHASER STEREO) for width; AMP SIMULATOR 1/2 and distortions for
  grit; TEMPO CROSS DELAY / TEMPO DELAY STEREO for rhythmic delays; ROTARY SPEAKER 1/2 or VCM
  ROTARY SPEAKER CLASSIC for organs; DAMPER RESONANCE on pianos; LO-FI / BIT CRUSHER / VINYL BREAK
  for texture. `ins_connect` 1 = A→B (default).
* System: reverb REV-X HALL (default) or HD HALL / R3 PLATE; variation for a shared delay or
  chorus, fed by each part's `variation_send`.
* Master FX MULTI BAND COMP or VCM COMPRESSOR 376 (`master_fx.on = true`) for glue.
* Effect parameters are numbered 1–24 per type; read `data/effect_params.json` for the mapping and
  `data/effect_data_assign.json` for value tables (e.g. delay times, LFO rates in Hz).

## 4. Performance controls (always add these)

Every factory performance wires the physical controllers; a preset without them feels dead.
Suggested default set, expressed as spec `controllers` entries:

| Purpose | Part box | Notes |
|---|---|---|
| Vibrato on mod wheel | `{"source": "Modulation Wheel", "dest": "E.LFO PMD", "ratio": 32}` (AWM2) / `"OSC Pitch LFO"` (AN-X) / `"LFO2 PMD"` (FM-X) | |
| Filter on mod wheel or ribbon | `{"source": "Ribbon", "dest": "Cutoff", "ratio": 40}` | AWM2/AN-X/FM-X all expose `Cutoff`/`Resonance` |
| Knob 1 cutoff, knob 2 resonance | `{"source": "AsgnKnob 1", "dest": "Cutoff", "ratio": 48}`, `{"source": "AsgnKnob 2", "dest": "Resonance", "ratio": 32}` | pair with a common box `AsgnKnob 1 → Part 1 Assign 1` so the Super Knob drives it |
| Knob → effect depth | `{"source": "AsgnKnob 3", "dest": "InsB Param 10", "ratio": 64}` | which parameter number = the effect's mix/depth (see effect_params) |
| Release on Assignable Switch 2 | `{"source": "AsgnSw 2", "dest": "AEG Release", "ratio": 40}` | |
| Aftertouch vibrato | `{"source": "AfterTouch", "dest": "E.LFO PMD", "ratio": 20}` | |
| Sends on knobs | `{"source": "AsgnKnob 7", "dest": "Rev Send", "ratio": 64}` | |

Super Knob: set `superknob.links` (which common knobs follow it) and `superknob.knob_names`; put
the common boxes in the spec's top-level `controllers` (e.g. `AsgnKnob 1 → Part 1 Assign 1`); the
part's box then reads `AsgnKnob 1`. Set `Controller Set Polarity` 1 (bipolar) when the knob should
cut and boost around the stored value.

## 5. Arpeggios and motion

Per part `arp.numbers` (up to 8 slots, chosen by the arp select / scene) and `arp.hold`; set
`Part Arp Switch` 1 and the builder turns on `Arpeggio Master Switch`. Pick arps by category and
`original_tempo` from `data/arpeggio_types.json`; the performance `tempo` should match the song.
User arps (`.arp` files, README) are numbers 12032+ (`docs/lists-reference.md`).

## 6. Song-based requests

1. Identify the instruments in the recording (bass, pad, lead, keys, drums) and their character
   (analog vs FM vs sampled), the tempo, the key range each instrument occupies.
2. Create one part per instrument, order them by importance (part 1 = main sound), set
   `note_range`/`velocity_range` so they can be played together or split, and give each part a
   name the player will recognise on the screen.
3. Reuse factory building blocks: decode the closest factory performance
   (`tools/pfm.py dump`) and copy its element/oscillator/effect settings into the spec's raw
   `params`/`elements`/`anx`/`fmx` sections, then adjust.
4. Add the controller set from section 4 and an arp if the part is rhythmic.
5. Build, install (or export `.syx`), test by ear, iterate on the spec.

## 7. Known gaps

* `install.py` writes the plugin's index the same way the plugin does for its own saves, but the
  plugin was not run against a generated file in this session: the first install should be
  checked in the plugin UI, with `performance.cfg.bak-*` available to roll back.
* Effect preset numbers (`preset`) are assumed to be the 0-based position in the Effect Preset
  List (not stated by Yamaha).
* Display-unit conversions (e.g. filter cutoff to Hz, EG times to ms) are not tabulated by the
  Data List; use factory values from the bank as references.
