# MONTAGE M controller / modulation system (as documented in the Data List)

Source: Yamaha *MONTAGE M Data List* (`montage_m_dl_H0.pdf`), Control List pp.198-207,
MIDI Data Format pp.212-215, and the Controller Box parameter blocks of the MIDI Data
Table (pp.221, 225-226, 230-231, 235-238, 244, 246). Machine-readable versions:
`data/control_sources.json`, `data/control_destinations.json`, `data/control_curves.json`.
Everything below is what the Data List says; behaviour not stated there is marked as such.

## 1. The three kinds of controller box

A "controller box" (called **Controller Set** in the SysEx tables) is one row of the
modulation matrix: *Source -> curve -> Destination*. There are three families:

| Box family | SysEx address | Count | Size | Source field | Destination range |
|---|---|---|---|---|---|
| Common/AD Controller Box | `06 05 bb 00` | 32 (bb = 0-31) | 18 bytes | 8-15, 18-39 | 1-393 |
| Part Controller Box | `1p 05 bb 00` (p = part 0-15) | 32 per part | 18 bytes | 0-39 | 1-413 |
| Key Controller Box | `1p 00 09 00`, 4 sets of 16 bytes | 4 sets per part | 64 bytes | none (keyed by note) | 1-58 |

Each Controller Set has the same fields (offsets in hex, all 2-byte 7-bit values):
`00` Switch (Off/On), `02` Source, `04` Destination, `06` Curve Bank
(0 Preset, 1 User, 2-25 Library 1-24), `08` Curve Type (0-31; 0-17 when Bank = Preset),
`0A` Curve Parameter 1 (0-127, default 5), `0C` Curve Parameter 2 (0-127),
`0E` Polarity (Unipolar/Bipolar), `10` Ratio (-128..+127, printed default `01 40`).
Curve Parameters 1/2 are "fixed to 0 except when Bank is set to Preset".
The Key Controller Box has no Source field; its sets go straight from Destination to the
curve fields and its own destination list (p.207) is separate and much shorter.

**Common/AD vs Part boxes.** The Part boxes live inside each Part and address that
Part's tone-generator parameters (element/operator/oscillator parameters, part LFO,
insertion effects A/B of that part, part sends, arpeggio and motion-sequencer settings).
The Common/AD boxes live at Performance level and can only reach Performance-wide things:
Insertion Effect A/B parameters 1-24 (for a Common/AD box these can only be the A/D
part's insertion effects, which is an inference), System effects (Reverb/Variation/Master FX
parameters 151-222), the A/D part's volume/sends (223-225), the **Part 1-16 Assignable
Knob 1-8 values (226-353)**, Performance volume/pan, effect returns, tempo, and the
arp/motion-seq common settings. The Destination table's `common_audio` column is the
authority for what a Common/AD box may target; the four `awm_normal / awm_drum / fmx /
anx` columns are the authority for Part boxes, depending on the Part's engine.

## 2. Sources (p.198)

Numbers 0-39, plus 40-41 reserved. 0 Pitch Bend, 1 Mod Wheel, 2 After Touch,
3-4 Foot Controller 1-2, 5 Foot Switch, 6 Ribbon, 7 Breath, 8-15 Assignable Knob 1-8,
16-17 Assignable Switch 1-2, 18-21 Motion Seq (lane) 1-4, 22-37 Envelope Follower 1-16
(the Data List does not say so, but 1-16 presumably follow Parts 1-16), 38 Envelope
Follower A/D, 39 Envelope Follower Master.
The printed table marks every source 0-39 as usable in both the Common and Part boxes,
but the SysEx definition of the Common/AD box source (p.238) allows only 8-15 and 18-39,
i.e. knobs, motion-seq lanes and envelope followers. Treat the SysEx range as the
encoding limit; the Control List column is looser than the parameter it describes.
The Super Knob is *not* a source number; see section 4.

## 3. Destinations (pp.199-207)

Three separate lists exist and they are **not** interchangeable:

* **Controller Box Destination** (0-413, pp.199-204): used by both Common/AD and Part
  boxes. 0 = Off. Grouped by section heading: Common Parameter 1-59 (InsA/InsB params
  1-24 each, 49 reserved, then part sends/portamento/mono-poly/pitch/volume/part LFO),
  AWM Parameter 60-87 (element level/pan/delay/LFO/tune/PEG/AEG/FEG/filter),
  FM Parameter 88-117 (FM-X common LFO/EGs/filter/feedback, then "OP1-8" operator
  params 105-117), AN-X Parameter 118-150, System Parameter 151-222 (Reverb, Variation,
  Master FX params 1-24 each), AD Parameter 223-225, Part Assignable Knob 226-353
  (Part n Assignable Knob k), Non-TG Parameter 354-374 (performance vol/pan, portamento,
  returns, tempo, arp gate/vel/quantize/octave/swing/unit multiply, motion seq
  amp/shape/smooth/random/grid/length), AN-X Parameter 2 375-376 (unison),
  VCM Rotary Parameter 377-400 (available only for Part 1, footnote *1),
  AN-X Parameter 3 401-413 (per-block LFO speeds, wave folder, modifier EG).
  "OP1-8" / "Oscillator1-3" / "Filter1-2" destinations are single numbers, not one
  per operator. The address map (pp.219/221) lists per-operator "Controller Box Switch"
  blocks (`3p 01 0o 00` FM-X operator o, `4p 01 0o 00` AN-X oscillator, `4p 03 0f 00`
  AN-X filter, 39 bytes each) which by their name select which operator/oscillator/
  filter listens to the boxes; the Data List does not spell out their semantics, and
  no equivalent block is listed for AWM elements. The Data List gives no
  per-destination depth range; depth comes from Ratio, Polarity and the curve.
  Footnotes: *1 Part 1 only; *2 in Ribbon Grid Mode only Lane 1 Sequence 1 (Common:
  Super Knob Lane Sequence 1) is affected; *3 in Grid Mode only Decay 1 is affected.
* **LFO Box Destination** (0-88, pp.205-206): used only by the Part LFO's
  "LFO Destination 1-3" (`1p 00 07 12/16/1A`, documented range 0-69). Different numbering
  from the controller boxes (0 = InsA Param 1, 24-31 and 56-63 reserved, 64-69 AWM
  element params, 70-78 FM-X, 79-88 AN-X). Drum parts have no LFO destinations.
* **Key Controller Box Destination** (0-58, p.207): a third numbering, only for the
  4 Key Controller sets. Categories: Common (1 Part Pitch), AWM TG 2-11, FM-X TG 12-26,
  AN-X TG 27-47, AN-X TG 2 48-58. Not available for Drum or Audio parts.

The `ribbon_grid_mode` column of the main table is a separate context: which
destinations the Ribbon Controller may drive when it is in Grid mode.

## 4. Super Knob and the Assignable Knobs

The Data List does not describe the Super Knob as a matrix source. What it documents:

* **Super Knob Settings** block (`06 00 0D 00`, 90 bytes, p.235): Super Knob Value
  (0-1023), Super Knob Mid Position (Off, 1-1022), and for each Assignable Knob 1-8 a
  *Destination Left / Mid / Right Value* (0-1023 each). So the Super Knob is a 10-bit
  position that is mapped, per knob, through a 2-segment (left-mid-right) curve onto the
  eight Common Assignable Knobs; those knobs are sources 8-15 for Common/AD boxes and
  destinations 226-353 for pushing values into the Parts' own assignable knobs.
  The block also holds the Super Knob LED pattern and Super Knob Motion Seq fields.
* **Assignable Knob 1-8 Link Switch** (Performance Common 1-byte block, offsets
  `0B`-`12`, p.230, default On): whether each Common knob follows the Super Knob.
  A separate **Smart Morph Super Knob Link** (offset `1B`) ties Smart Morph to it.
* **Scene** data (p.237) stores *Scene Super Knob Value* (0-1023), *Scene Super Knob
  Memorize*, *Scene Super Knob Link* and *Scene Super Knob Link Switch 1-8*, so scenes
  can recall a Super Knob position and the per-knob link state.
* **Super Knob Motion Sequencer**: Super Knob Lane Settings (`06 00 12 00`) and
  Super Knob Sequence 1-8 (`06 01 0m 00`, m = 0-7) are a dedicated motion-seq lane driving the
  Super Knob; Performance Common has Super Knob Motion Seq Switch / FX Receive flags.

## 5. MIDI channel messages for controllers (MIDI Data Format pp.212-215)

Transmitted and received: Modulation CC1, Portamento Time CC5, Volume CC7, Pan CC10,
Sustain CC64 (footnote *5: unless the pedal is "FC3 (Half On)" only 0/127 are sent),
Portamento Sw CC65, Harmonic Content/Resonance CC71, Release CC72, Attack CC73,
Brightness/Cutoff CC74, Decay CC75, Effects 1 Depth = Reverb Send CC91, Effects 4
Depth = Variation Send CC94, and **Assignable Controller CC 1-95** (footnote *4).
Receive only: Data Entry CC6/38 and Inc/Dec CC96/97 (RPN), Expression CC11,
Sostenuto CC66. CC71-75 are offsets around 64. Footnote *2: CC5, 65, 72 are invalid
on Drum parts.

Default CC numbers of the assignable controllers (footnote *4, p.213; the matching
System parameters on pp.225-226/231 give the ranges):

| Controller | Default CC | System parameter range |
|---|---|---|
| Breath Controller | 2 | Off, 1-95 |
| Foot Controller 1 | 11 | Off, 1-95, Super Knob |
| Foot Controller 2 | "Super Knob" (i.e. it drives the Super Knob, not a CC) | Off, 1-95, Super Knob |
| Assignable Knob 1-8 | 17-24 | 1-95 each |
| Ribbon Controller | 16 | Off, 1-95 |
| Assignable Function (Switch) 1 / 2 | 86 / 87 | Off, 1-95 |
| Motion Seq Trigger | 89 | - |
| Foot Switch | "Arp SW" | Off, 1-95, Arp SW, MS SW, Play/Stop, Live Set +/-, Oct reset, Tap Tempo |
| Super Knob Control Number | 95 (`00 5F`) | Off, 1-95 |
| Scene Select Control Number | 92 (`00 5C`) | Off, 1-95 |

Pitch Bend is transmitted with 10-bit resolution. RPNs: 0 Pitch Bend Sensitivity
(0-24), 1 Master Fine Tune, 2 Master Coarse Tune (-24..+24), 7F7F reset.
**Reset All Controllers (CC121)** resets Pitch Bend, Aftertouch, Mod (0), Expression,
Breath, FC1, FC2 (127), Foot Switch, Ribbon (0/center), AF1/AF2, Sustain, Sostenuto (0)
and Motion Seq Lanes 1-4 to 0 (minimum when Unipolar, centre when Bipolar); it does
**not** reset Assignable Knobs 1-8, Volume, Pan, CC71-75, sends, portamento switch or
the RPN values. Transmit channel follows MIDI I/O Channel when the Part is Internal with
Keyboard Control on, Tx/Rx Channel otherwise; External parts use their Transmit Channel.

## 6. Curves, polarity, ratio

The Control List section has **no** curve tables. The only curve enumerations in the
Data List are the Controller Set fields above (Curve Bank / Type / Param 1-2 / Polarity /
Ratio) and the user-curve format (Curve Edit Buffer `01 01 nn 00`, p.228: eight
Input/Output breakpoints 0-1023 and Curve Type 0 Linear / 1 Step). The names of the 18
preset curve shapes are not printed in the Data List (`control_curves.json` records them
as null). Polarity Unipolar/Bipolar is also used by every motion-seq lane.

## 7. Caveats found while extracting

* Check marks are a private-use glyph (U+F0A1) in the PDF text layer; they were
  verified against a rendered page before being mapped to `true`.
* Common/AD source range mismatch (section 2) and Key Controller destination range
  (table says 0 = Off, SysEx says 1-58) are inconsistencies in the source document.
* Part controller box count: address map says "bb: 0...32", parameter table says
  "Controller Box 1-32"; 32 is used here.
* p.207 row 55 is printed "Oscillator1?3 Frequency" (typo, recorded in the JSON).
* LFO Box list runs to 88 but the LFO Destination parameter is documented as 0-69.
* Depth/range per destination, curve names and the Super Knob curve semantics beyond
  the Left/Mid/Right values are not in the Data List; consult the Reference Manual.
