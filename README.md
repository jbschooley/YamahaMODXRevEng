# Yamaha MONTAGE M — User Arpeggio (`.arp`) File Format

This file is an absolute mess because I had Claude generate it as it reverse engineered the firmware and arp files and we tested how different manually written arps behaved. The goal here was to build an arp for Space Song by Beach House. That arp oscillates up exactly 8 notes whether I was holding down 2 or 3. The built in Oct1-4 arps don't limit to 8 notes, they'll oscillate through their defined number of octaves, and I couldn't find anything in the presets that worked nor could I record one that worked. 

Reverse-engineered from files in
`/Library/Yamaha/Expanded Softsynth Plugin for MONTAGE M/contents/current/arpeggio/`.

Filename convention: `XX0000-Arpeggio.arp` where `XX` is the user slot
in hex (`01`–`0A` = User 1–10 by default; higher = additional banks).

All multi-byte integers are **big-endian**.

---

## Top-level layout

```
[PHhd chunk]   ─ header, 22 bytes
[ATrk | ATr2]  ─ track chunk (events + arp config)
[ARPa]         ─ arp metadata (display name, length, time sig)
[TRKa]         ─ per-track playback params
[PHRa]         ─ phrase metadata
```

Every chunk is `4-byte ASCII type` + `4-byte big-endian length` +
`length bytes of data`.

`ATrk` is used in **factory/preset** arp data — events reference
held-chord indices. `ATr2` is used in **user-recorded** arps — events
embed literal pitches. This distinction is the key technical finding
of this investigation. See [[#Event encodings]].

---

## PHhd chunk

Variant of Standard MIDI File's `MThd`:

```
50 48 68 64        "PHhd"
00 00 00 0e        length = 14
00 01              SMF format 1
00 01              1 track
01 e0              480 PPQN
<8 bytes>          internal name (ASCII, space-padded, no null)
```

The 8-char internal name is what the synth shows in some lists.
The user-facing display name lives in the ARPa chunk (longer string).

---

## ATrk / ATr2 chunk

```
41 54 72 [6b|32]   "ATrk" or "ATr2"
LL LL LL LL        length in bytes (everything below)

# Config block:
00 00 00 NN        config-block length (NN excludes this 4-byte prefix)
00 02 01 80        constants (purpose unknown; same in every file)
EF                 empty/has-data flag: 00 = has data, 01 = empty template
ff 00 ff 0f ff 07 ff ff ff ff   note/vel/channel mask bits (10 bytes)
MM MM MM MM        mode bytes — 00 00 00 00 (user) or 00 00 03 00 (preset)
00 06 00 7f 00     (5 bytes — note/vel range defaults?)
KK NN              original key (e.g. 0x3c=C4) + chord-template note count NN
<NN × 2 bytes>     chord template: each note is `pitch flag`
                   flag = 01 in user-recorded, 00 in preset
00                 padding (1 byte)

# Meta event — track name:
00                 delta = 0
ff 03 LL           meta text status + length
"A00:<displayname>"

# Arp events:
<event 1>
<event 2>
...

# End of track:
<delta> ff 2f 00
```

### Config block sizing

The `00 00 00 NN` length-prefix is `41 + 2 × (chord_count − 7)` in
preset arps and `47 + 2 × (chord_count − 8)` in user arps (the user
config is 6 bytes longer due to wider range/limit fields).

---

## Walker mode is set in the config header, not the events

**Initial finding from the MONTAGE 3.51 firmware (unencrypted ext2 image):**
the synth has playback modes selected by a single **direction byte**
at config offset `0x08`. Verified by hand-test on the ESP-M plugin:

| `dir` byte | Mode | Walker source | Example arps |
|---|---|---|---|
| `0x00` | Event-driven | Event indices drive playback (with octave-wrap on overflow when loaded internally; *template-fixed when loaded from disk* — see [[#Disk-load vs firmware-load divergence]]) | `MA_Up`, `Floyd Bs`, `EA_Jazz`, user `0x99`/`0x90` arps |
| `0x06` | Built-in Up Oct1 | Synth ignores event indices, walks held chord ascending across 1 octave | `MA_Up Oct1` |
| `0x07` | Built-in Up Oct2 | …across 2 octaves | `MA_Up Oct2` |
| `0x08` | Built-in Up Oct3 | …across 3 octaves | `MA_Up Oct3` |
| `0x09` | Built-in Up Oct4 | …across 4 octaves | **`MA_Up Oct4` (= "1/16 Up Oct4")** |
| `0x0a–0x0d` | Built-in Down Oct1–4 | descending walker | `MA_Down OctN` |
| `0x01`, `0x02`, `0x1a`, others | Other walker/effect modes | not yet investigated; `0x1a` is the largest non-zero bucket (~1200 arps) | — |

In built-in-walker mode, every event has `idx=0`; the events only
supply timing/velocity/gate. The synth ignores `idx` entirely and
generates notes from its own walker logic.

In event-driven mode (`dir=0x00`), each event's `idx` byte specifies
which held-chord position to play. Internal firmware load applies
`held[II mod N] + 12 × (II div N)` automatically when `II ≥ N`
(N = number of held notes). Disk load, see below.

The synth UI prepends a "1/16 " (or other rate) prefix when displaying
factory `MA_` arps whose name ends in `OctN`; bare `MA_Up` and similar
stay raw because the UI doesn't auto-rename them.

## Disk-load vs firmware-load divergence

The plugin has **two distinct arp loaders**, and they don't honor the
same fields. Verified by writing identically-structured files and
testing them on hardware:

| Behavior | Firmware (RPF) load | Disk (`.arp` file) load |
|---|---|---|
| `dir` walker enum (0x06–0x0d) | activates walker | activates walker ✓ |
| Walker length | bar/walker-internal | **bar-locked — track length, ARPa tick field, and timesig are all ignored** |
| `0x91` events with `dir=0x00` | held-key chord index + octave-wrap on overflow | **template-fixed playback** — the chord template in the config is read as literal pitches, held keys do not transpose. Template-first / held-as-fallback for `idx ≥ template_size`. |
| `0x99` events | Org-Note semantics | Org-Note semantics ✓ |
| `0x90` events | literal pitches or Normal walker | literal pitches or Normal walker ✓ |
| Track length (ARPa total ticks) | respected | respected for `dir=0x00`; **ignored for `dir=0x06–0x0d`** (walker dictates duration) |
| `ATr2` vs `ATrk` chunk | both accepted | both accepted; user-slot files normally use `ATr2`, library imports use `ATrk` |

So three combined truths emerge:

1. The factory walker arps' octave-wrap-with-held-keys behavior is
   reachable on disk via `dir=0x06–0x0d`, **but the walker is bar-locked**
   — there is no way to truncate it to 8 sixteenths from the file.
2. `0x91` chord-index events with `dir=0x00` are template-driven on
   disk; the magical "wrap held key with +12 per overflow" we see in
   firmware factory arps doesn't activate from disk-loaded arps.
3. The only on-disk modes that respond to held keys are Normal
   (`0x90`, hold-top fallback), Org Note (`0x99`, literal-template
   fallback), and walker (`dir=0x06–0x0d`, bar-locked).

The behavior of "8-note loop with held-key octave-wrap regardless of
chord size" is **not achievable in a single user-slot `.arp` file**
on this plugin. The combination of held-key response and sub-measure
loop length lives only inside the firmware loader.

### Verification table

| Test arp | What was built | What the synth played |
|---|---|---|
| **SpaceArp v2** (`010000`, ATr2, dir=0x00, 0x91 events idx 0..7, 960 ticks) | Hoped: held-key wrap looping every 8 | **Silent** — disk-loader doesn't activate held-key wrap for `0x91` events |
| **SpaceWlk** (`010001`, ATr2, dir=0x09, all idx=0, 960 ticks, 2/4 timesig) | Hoped: Up Oct4 truncated to 8 slots | Plays Up Oct4 walker correctly using held keys, **but bar-locked** — with 3 held it plays 12 notes (full Oct4 walk), not 8 |
| **SpaceATk** (`010002`, ATrk, dir=0x00, 0x91 events idx 0..7, 960 ticks) | Hoped: held-key wrap looping every 8 | Plays `C3 D3 F3 G3 D4 F4 G4` (the chord template literally) at idx 0..6, then held note at idx=7 — proves disk-loaded `0x91+dir=0x00` is template-first, not held-key-driven |
| **SpacWlk2** (`010003`, ATr2, dir=0x09, 8 events at 1/8 rate filling 1 bar) | Test: does walker compress its N-note output into the arp's slot count? | **Walker still plays 12 notes with 3 held.** Confirms walker count = `chord_size × octaves` regardless of arp slot count or tick rate. Walker has cross-loop state; resets only on bar boundary of its own internal cycle, not on arp loop. **Unit Multiply slow-down approach is dead** — it would just play 12 notes faster, not 8. |
| **SpacWlk3** (`010004`, hybrid dir=0x09 + 2-entry template) | Test: does walker use template as the chord source instead of held keys? | Sounded "Floyd-Bs-like" — chord-responsive but not ascending. Walker enum overridden by `byte[1]=0x02` template flag, became event-driven mode. |
| **SpaceAsc** (`010005`, walker-style layout + 4-entry template + dir=0x00 + idx 0..7) | Test: does the walker-style 3×7-byte track-param block + chord template enable held-key chord-index playback like MA_80'sSynthRock? | **Played template literally for idx 0-3 (C E G B), then held keys for idx 4-7. With < 4 held → silence in held slots.** So the synth's rule for this layout is: `idx < template_size → template[idx]`; `idx ≥ template_size → held[idx − template_size]` (silent if no such held note). **No octave-wrap on overflow.** |
| **SpcAsc2** (`010006`, walker-style layout + NO template + idx 0..7) | Test: with no template, does the synth wrap held-key indices with octave shift? | *(test pending)* |
| **SpcAsc3** (`010007`, walker-style + no template + idx `0x00 01 10 11 20 21 30 31`) | Test: do high-nibble octave-encoded indices give `held[pos] + 12×octave`? Inspired by MA_80'sSynthRock's `idx=0x73` events. | *(test pending)* |

### ★ Verified index encoding for chord-relative arps

When the arp uses the **walker-style config layout** (3×7-byte
track-param blocks at config offset 0x13) with `byte[1]=0x02` and
`dir=0x00`, the index byte of `0x91` events is interpreted as a
packed `(octave, position)` pair:

```
idx = (octave_offset << 4) | chord_position
```

- **Low nibble** = literal position in held chord (0 = lowest held).
  No modulo — position 2 means held[2] literally; if no such held note,
  silence.
- **High nibble = signed 3-bit two's complement octave shift:**
  - `0x0` = 0, `0x1`–`0x3` = +1 to +3 octaves
  - `0x4`–`0x7` = −4 to −1 octaves
  - `0x8`–`0xf` = silent/reserved
  - Total range: **−4 to +3 octaves** (8 octaves spanning the held key).

### `byte[1]=0x01` mode — 1-indexed positions

A second, less-explored mode: when `byte[1]=0x01` (used by 85 firmware
arps including MC_Funk 4), position references **skip the lowest held
note**. `idx low-nibble 0` = `held[1]`, `idx 1` = `held[2]`, etc.

Verified by hand-test:
- 2 held → `idx 0 = held[1]` (top), `idx 1` = silence
- 3 held → `idx 0 = held[1]`, `idx 1 = held[2]`, `idx 2` = silence

Useful for arps where the held root is supplied by another voice (e.g.
bass + chord splits) and the arp plays only the upper voices.

### ★ `byte[2]` — min-held-notes floor

Discovered 2026-05-23. The 3rd config byte (offset 2) is the **minimum
held-notes count** required before the arp will fire at all.

| `byte[2]` | Behavior |
|---|---|
| `0x01` (default) | Plays for ≥1 held note |
| `0x02` | Plays for ≥2 held; silent for 1 |
| `0x03` | Plays for ≥3 held; silent for fewer |
| ... | Linearly extends |

Combined with `byte[3]` (max cap), the two together define a **valid
chord-size range** that the arp will respond to. Outside that range,
the arp is completely silent.

### ★ `byte[3]` — max-held-notes cap

Discovered 2026-05-23. The 4th config byte (offset 3) is a **maximum
held-notes cap** that gates whether the arp plays at all.

| `byte[3]` | Behavior |
|---|---|
| `0x01` | Plays only if exactly 1 note held (or fewer needed by indices) |
| `0x02` | Plays for ≤2 held; silent for 3+ |
| `0x03` | Plays for ≤3 held; silent for 4+ |
| `0x04` | Plays for ≤4 held; silent for 5+ |
| `0x08` | Plays for ≤8 held |
| `0x10` (=16) | Plays for any chord size (all chromatic notes in one octave) |
| `0xff` | Same as `0x10` — effectively caps at 16 |
| `0x80` (default) | Unlimited / no cap |

The cap **counts only held notes within a single octave** — higher octaves
of the same note are not counted toward the limit (filtered by separate
note-range mechanism in the config).

Combines with walker dir bytes to produce **chord-size-locked arps**:
- `dir=0x09 + byte[3]=0x02` → exactly 8 notes for 2-held, silent otherwise (clean safety-net)
- `dir=0x07 + byte[3]=0x04` → exactly 8 notes for 4-held, silent otherwise

When held count is below the cap but the arp's indices reference
higher positions, those events become silent — creating apparent
slower-rate playback (e.g. `byte[3]=0x01` + 8 1/16 events with mixed
positions = 4 audible 1/8 notes).

**This is the first verified hidden parameter that meaningfully alters
arp behavior outside the dir-byte enum.**

### ★ Complete `dir`-byte mode taxonomy (verified)

Comprehensive position-overflow / direction-of-traversal behavior by `dir` byte:

| `dir` | Mode | Position-overflow behavior | Notes |
|---|---|---|---|
| `0x00` | Event-driven, exact | Position > held_count → **silent** | Default; verified by SpcAsc N |
| `0x01`–`0x05` | Event-driven, **clamping** | Position > held_count → **clamps to held[held_count-1]** (top held note, no octave shift) | Verified by SpcD01..05; equivalent across these five values; behaves like Normal mode's "hold top" |
| `0x06`–`0x0d` | Built-in Up/Down OctN walker | Auto-modulo + octave shift internally | Bar-locked, ignores event indices |
| `0x0e` | Built-in **Up-Down B walker** | Walks up to top chord position with auto octave-bump on top, then down. Pattern for 3-held with SpcAsc 2 indices: `C E G' E' C'' E'' G''' E'''` | Built-in walker variant — ignores event indices' position content but respects octave hints. 9 firmware arps incl. `MA_U/D B Oct1` |
| `0x11`, `0x13` | Other built-in walkers | Jumpy octave-mixing patterns. Respond to chord size. Don't loop after 8 notes. | Singletons in firmware. Likely specialty walkers; bar-locked. |
| `0x16`–`0x19` | Built-in Random OctN walker | Random-direction walker | (Not directly tested in isolation) |
| `0x1a` | Style/literal mode | Indices treated as literal MIDI note numbers | Verified silent in our walker-style layout; needs different config |

**The single missing mode**: position % held_count *with* automatic octave shift on overflow. The built-in walker does this, but it's bar-locked. No event-driven mode exposes the formula `held[idx % N] + 12 × (idx ÷ N)` — that's available **only** in the firmware-internal walker code path.

### Practical authoring patterns

- **Per-chord-size arps**: `dir=0x00`, indices reference exact positions 0..N-1 with octave shifts. Silent for held_count < N. Clean, exact pattern.
- **Graceful-degradation arps**: `dir=0x01`, same indices. Fewer-held cases clamp to top instead of going silent — adds musical "filler" notes.
- **Bass-skip arps**: `byte[1]=0x01`, plays held[1..N-1] only. Lets you split the held root onto another voice.

### Multi-track ATr2 limit

Disk-loaded user-slot arps **only play the first ATr2 track** even if
`PHhd` declares multiple. Multi-track factory arps (MA_Up, MC_Funk 4,
EA_Unplugged 4, etc.) only render multi-voice when loaded from the
firmware RPF code path. The disk loader silently ignores tracks 2+.
This is a hard limit; no `byte0` track-index manipulation enables it.

**Tested combinations that all confirm Track 0 only:**
- `byte[0]=0/1` track-index increment per Yamaha convention
- `byte[1]=0x02` (chord-template mode) and `byte[1]=0x01` (1-indexed) — both
- Different meta prefixes (A01, A05) per track per MA_Up convention
- Per-track `byte[2]/byte[3]` chord-size caps
- Time-offset events in Track 1 (delta=480 lead-in)

**Workaround for chord-size-adaptive arps**: use multiple **Parts** in
a single Performance, each with its own chord-size-locked arp from the
SpcExN family. The synth's part-layering combines them automatically —
only the part matching the held chord size fires audibly. This is the
canonical Yamaha architecture for adaptive arps and is **how the Space
Song arp described in the doc header was actually solved**.

This explains MA_80'sSynthRock's `idx=0x73` events — that's octave 7,
chord position 3 (very high notes), interleaved with low-octave
notes to produce its signature melody.

The synth **transposes the entire pattern by the lowest held note**,
so a given index sequence produces the same intervallic pattern at
any root.

### Authoring recipe for "N ascending across M octaves, looping"

To play `held[0]..held[N-1]` ascending through `M` octaves with a
fixed `N×M`-event loop:

1. Use the walker-style config layout (byte[1]=0x02, dir=0x00,
   3×7-byte track-param blocks, no chord template — `key=0x3c count=0`).
2. Each event status `0x91`, gate=120, delta=120 (1/16 spacing).
3. Index sequence: for octave `o` in `0..M-1`, for position `p` in `0..N-1`,
   emit index `(o<<4)|p`.
4. Total ticks = `N × M × 120`, set in ARPa.
5. Timesig 2/4 if total ≤ 960 ticks, else 4/4 with appropriate bar count.

**Limitation:** position is literal, not auto-modulo. A single arp
that "ascends through whatever chord I hold" requires either:
- One arp per chord size (built with positions 0..N-1 for that size), or
- Accept that extra held notes are ignored if your arp only references
  the first 2-3 positions.

The built-in walker (`dir=0x06–0x0d`) handles auto-modulo, but it's
bar-locked and can't be truncated to a custom note count.

### The fundamental constraint

The synth's built-in walker is **arithmetically locked** to `chord_size × octaves` notes per cycle, with cross-loop state. There is no field in the `.arp` file that overrides this. Yamaha designed it this way and never built a sub-cycle truncation mechanism.

### Verified walker-manipulation failures

Every plausible mechanism for getting the walker to reset or truncate has been hand-tested and confirmed to fail:

| Approach | Result |
|---|---|
| Sub-measure tick length (960 ticks, ½ bar) | Walker ignores |
| 2/4 ARPa timesig | Walker ignores |
| 1/4 ARPa timesig | Walker ignores |
| 3/8 ARPa timesig | Walker ignores |
| 1/8 event rate (delta=240) | Walker ignores rate |
| Note-range filter (C4–C5) on track-param | Walker output not filtered |
| Explicit non-zero event indices in walker mode | Walker uses them but with non-obvious octave multiplication; chaotic output |
| `byte[1]=0x01` (clamping) + walker dir byte | **Parser crash** — invalid combination |

### Known parser crashes (do not use)

- **`byte[1]=0x01` combined with walker `dir` (`0x06`–`0x0d`)**: crashes the plugin loader. Arps in this configuration must be deleted or replaced before plugin restart. The two modes share a code path that doesn't validate the combination.

The behavior of "8 notes loop, octave-wrap on overflow, responsive to varying held-chord size" is unreachable as a single user-slot arp. It would require either:
- A walker mode with explicit step-count parameter (doesn't exist)
- Sub-measure walker reset (doesn't exist)
- Held-key reference within `0x99`/`0x91` events that wraps with octaves on disk load (doesn't exist; firmware-internal only)

### Pure-walker arps with non-1-bar lengths

`MD_New R&B 3`, `MA_SynthRiff6-10`, etc. — all with `dir=0x06` (Up Oct1)
and `ticks=3840` (2 bars). These prove walker arps **can** be > 1 bar.
None < 1 bar exist in the firmware. The walker has a minimum effective
length of 1 bar; sub-measure tick lengths in the file are rounded up
or ignored.

### Unexplored `dir` byte buckets

Sampled from the firmware:

| `dir` | Count | Sample names | Likely meaning |
|---|---|---|---|
| `0x00` | 1822 | `MA_Up`, `Floyd Bs` | event-driven (chord-index or literal) |
| `0x01` | 292 | `MA_SimpleNt`, `MD_Hip Hop 2` | possibly "single-track style/genre" arp |
| `0x02` | 51 | `MA_Trance Lead5`, `MA_Cycle2` | event-driven with multi-track style |
| `0x06–0x0d` | 27 | `MA_Up/Down Oct1-4` | Up/Down walker enum |
| `0x0e` | 9 | `MA_U/D B Oct1`, `MA_Walkin` | possibly Up/Down "B" variant walker |
| `0x16–0x19` | ~18 | `MA_Random Oct1-4` | random-direction walker |
| `0x1a` | 1201 | `BA_60sChartSwing`, `EB_Slow Blues` — event indices are MIDI note numbers (55, 59, 64) | **Fixed-style with literal MIDI pitches stored in `idx` byte** — disk-load equivalent of "Fixed" convert mode |

`0x1a` is the largest bucket and explains why so many factory style
arps are fundamentally locked to specific pitches. None of the
non-walker dir bytes appear to expose a "fixed N-step walker"
mechanism that would solve the 8-note-loop problem.

## Event encodings

Each event begins with a **delta-time VLQ** (standard SMF variable-length
quantity — bytes with bit 7 set continue into the next byte).

There are **three distinct status bytes**, each used in a different
authoring context:

### `0x90` — Literal pitch (User "Fixed" convert)

```
<delta-VLQ> 90 PP VV
```
Plays absolute MIDI note PP at velocity VV. Held key is ignored.

### `0x91` — Chord-index reference (used by all factory arps)

```
<delta-VLQ> 91 II VV FL <gate-VLQ>
```
- `II` = index into held chord (only used when `dir=0x00`)
- `VV` = velocity
- `FL` = flag (always observed as `00`)
- `<gate-VLQ>` = note duration in ticks

When `dir≠0x00`, `II` is ignored — the synth walker generates the note.
When `dir=0x00`, the synth plays `held[II mod N] + 12 × (II div N)`,
where N is the held-chord size. This is how `Floyd Bs` works (indices
0–6) and how `MA_Up` works (indices including `0x13`=19, well beyond
any normal held-chord size — the modulo+octave-shift is the whole
point).

**User Arp Record cannot produce `0x91` events.** They appear only in
factory arps and in hand-authored files. See
[[#Limitations of User Arp Record]].

### `0x99` — Chord-index with literal fallback (User "Org Note" convert)

```
<delta-VLQ> 99 II 00 90 PP 00 00 VV GG
```
- `II` = chord-index
- `PP` = literal pitch (fallback when no held note at index `II`)
- `VV` = velocity
- `GG` = gate in ticks (single byte, not VLQ)

When held-note count ≥ `II + 1`, plays held note at index `II`.
When fewer notes held, falls back to literal `PP` — this is why
"Org Note" mode invents a third note when you hold only two.

---

## ARPa chunk

```
41 52 50 61        "ARPa"
00 00 00 LL        length

00 00 00 NL        name length (typically 8)
<NL bytes> 00      display name + null terminator
00 00 01           flag bytes
01 00 00 00 00 01 e0    quarter-note division (0x01e0 = 480)
01 00 00 07 80          total length in ticks (0x780 = 1920 = 1 bar)
01 e0 04 02 18 08       1 beat (480) + MIDI time-sig meta values
                        (numerator=4, denom-exp=2 → 4/4, 24 ck/click, 8 32nds/q)
ff ff ff TT 00          TT = 03 in preset, 00 in user
```

The `0x780 = 1920` value at offset +18 is the **total arp length in ticks**.
Changing this byte cluster could theoretically resize the arp, but
the synth seems to use the integer measure count from elsewhere when
displaying the Length parameter.

---

## TRKa chunk

```
54 52 4b 61        "TRKa"
00 00 00 10        length 16

03 01 01           ???
00 00 00 64        velocity ratio (0x64 = 100%)
00 64              ???
00 00              ???
00 64 00 64 64 00  more per-track params (gate ratio, swing, etc.)
```

Differences between Floyd Bs and a recorded user arp here are
1–2 bytes — likely Convert Type encoding.

---

## PHRa chunk

```
50 48 52 61        "PHRa"
00 00 00 LL        length

00 00 00 00        4 bytes (zero)
00 NL              name-length byte (12 = `"A00:" + 8-char name`)
"A00:<displayname>"
01 00 00 00 00 01 e0    trailing values (PPQN, end)
```

---

## Limitations of User Arp Record

Confirmed via web research and binary diff:

| Convert Type | Status used | Behavior |
|---|---|---|
| Fixed | `0x90` | Same notes regardless of held key |
| Normal | `0x90` + transpose | Sticks on last held note when N held < pattern needs |
| Org Note | `0x99` | Falls back to literal recorded pitch |

**No user-facing path generates `0x91` events.** The synth's
"Convert" pipeline always bakes in either a literal pitch or a
literal-pitch fallback. Octave-wrap on under-held chords is therefore
unreachable through stock UI.

Hand-authoring a `.arp` file with `0x91` events bypasses this and is
the only known way to get factory-style wrap behavior in a User slot.

Also confirmed:
- **No "Copy preset to User slot" command** exists in MONTAGE M's UI.
  Yamaha's recommended workflow is Record → Convert, which loses the
  `0x91` encoding.
- **Length parameter minimum is 1 measure** (integer measures only).
  Unit Multiply (50–400%) only scales timing — it doesn't change
  the loop boundary.

---

## Hand-authoring recipe (for an N-note ascending wrap-loop)

For "play held-chord-indices `0..N-1` ascending, then repeat":

1. Build a 1-measure track with `ceil(1920 / step_ticks)` events.
   For a 1/16 pattern: `step_ticks = 120`, so 16 events per measure.
2. Use `0x91` status. Set index `II = step_number mod N`.
3. Use a generous chord template in the config (matches an extended
   C-major to be safe).
4. Match the rest of the file byte-for-byte against Floyd Bs
   (`120000-Arpeggio.arp`), swapping only the name strings.

See [[SpaceArp - hand-built example]] for a concrete file.

---

## Empirical verification base

The format above was reverse-engineered from:

- **10 user-recorded `.arp` files** in `contents/current/arpeggio/`
  (sp1/2/3 = same recording saved as Normal/Fixed/Org Note;
  see [[User slot inventory]])
- **3 library-imported `.arp` files** (EA_Jazz, Floyd Bs ×2) — legacy
  content, possibly Motif-era
- **MONTAGE 3.51 firmware image** (`montage351/8N70OS_.PGM`,
  377 MB unencrypted ext2 filesystem containing 10,249 factory arps
  with names, full chunks, all event encodings). This is the
  authoritative reference for:
    - the `dir` byte enum at config offset `0x08`
    - confirmation that `MA_Up Oct1–4` are the firmware-internal
      names for "1/16 Up Oct1–4"
    - existence of sub-measure arps (e.g. `Mute 2/4` at 960 ticks)
      that prove the synth respects ARPa's `tick-length` field

The MONTAGE M ESP-M plugin uses an **encrypted RPF** (`8O42_`) instead
of a plain ext2 filesystem — so the same arps can't be extracted from
the current plugin directly, but the on-disk `.arp` format that the
plugin emits is identical to the firmware's.

## Sources

- [MONTAGE Connect Part II: Working with User Arpeggios](https://yamahasynth.com/learn/montage-series-synthesizers/montage-connect-ii-working-user-arpeggios/)
- [Custom Arpeggios Length forum thread](https://yamahasynth.com/community/montage-series-synthesizers/custom-arpeggios-length/)
- [MONTAGE M Operation Manual — Part Edit (AWM2)](https://manual.yamaha.com/mi/synth/montage_m/en/om02screenparameters0080.html)
- [Mastering MONTAGE: Arpeggio Making 101 Part 1](https://hub.yamaha.com/keyboards/synthesizers/mastering-montage-arpeggio-making-101-part-i/)

---

## The Space Song arp — final production recipe

The goal was an arp that loops every 8 notes regardless of whether
2 or 3 notes are held — the bass-line pattern from Beach House's
"Space Song". This required two arps assigned to two Parts in a
single Performance, because **the synth's disk loader doesn't
support multi-track arps**. Each arp is chord-size-locked so only
one fires at a time depending on what's held.

### Per-arp anatomy

Both arps share the same structure; only the chord-size lock and
index sequence differ.

**Common scaffolding** (identical across both):

```
PHhd  (22 bytes)
  "PHhd"  +  length=14
  format=1  tracks=1  PPQN=480
  internal_name (8 chars, e.g. "SpcEx2  ")

ATr2 chunk
  "ATr2"  +  track_length
  
  config block (44 bytes):
    00 00 00 2c           ← config length prefix
    00 02 01              ← byte[0..2] = track_idx(0), template-flag(2), const(1)
    NN                    ← byte[3] = chord-size CAP  ← varies per arp
    00                    ← dir byte = 0x00 (event-driven mode)
    ff 00 ff 0f ff 07 ff ff ff ff   ← 10-byte mask
    00 02 00 7f           ← walker-style header (enables held-key transposition)
    03 00 00 06 00 7f 01  ← track-param block 1
    03 00 00 06 00 7f 01  ← track-param block 2  (3× identical)
    03 00 00 06 00 7f 01  ← track-param block 3
    00 3c 00 00           ← key=C4, chord-template count=0 (no template)
  
  meta event:  00 ff 03 0c "A01:<name>"   (12 chars)
  
  arp events:  8 × `91 IDX 6c 00 78` with leading delta (0 for first, 0x78=120 else)
  
  EOT:  78 ff 2f 00       ← total ticks = 8 × 120 = 960 (½ measure)

ARPa  (47 bytes): display name + 960 ticks + 2/4 timesig
TRKa  (24 bytes): standard track params
PHRa  (35 bytes): standard phrase metadata
```

### SpcEx2 — locked to 2 held notes

- `byte[2] = 0x02` (min 2 held)
- `byte[3] = 0x02` (max 2 held)
- **Event indices**: `0x00 0x01 0x10 0x11 0x20 0x21 0x30 0x31`
  - 8 events: pos 0 and pos 1 alternating, octave shifting +0, +12, +24, +36
- **Behavior when exactly 2 held (e.g. C E)**:
  ```
  C   E   C'   E'   C''   E''   C'''   E'''
  (loops every 8 notes, ½ measure)
  ```
- Silent for any chord size other than 2

### SpcEx3 — locked to 3 held notes

- `byte[2] = 0x03` (min 3 held)
- `byte[3] = 0x03` (max 3 held)
- **Event indices**: `0x00 0x01 0x02 0x10 0x11 0x12 0x20 0x21`
  - 8 events: pos 0/1/2 + pos 0/1/2 +12 + pos 0/1 +24
- **Behavior when exactly 3 held (e.g. C E G)**:
  ```
  C   E   G   C'   E'   G'   C''   E''
  (loops every 8 notes, ½ measure)
  ```
- Silent for any chord size other than 3

### Index encoding refresher

Each event's `idx` byte is split:
- **Low nibble (bits 0–3)**: literal position in held chord (0 = lowest, no auto-modulo)
- **High nibble (bits 4–6)**: octave shift, **signed 3-bit two's complement** (−4 to +3)
- Bit 7 reserved (high-bit-set indices = silent)

So `0x12` = position 2 at octave +1 = `held[2] + 12 semitones`.

### Performance setup

In MONTAGE M:

1. Load both arps into User slots (any free `01000X` slots work).
2. In a Performance, configure two Parts with the same target patch:
   - **Part A**: assign SpcEx2 to its arp slot
   - **Part B**: assign SpcEx3 to its arp slot
3. Trigger both Parts from the same keyboard zone (no key split, no
   velocity zones).
4. Play 2 notes → only Part A audibly fires (SpcEx2 plays, SpcEx3
   silent because its `byte[2]=0x03` floor isn't met).
5. Play 3 notes → only Part B audibly fires (SpcEx3 plays, SpcEx2
   silent because its `byte[3]=0x02` cap is exceeded).
6. The synth combines the parts' arp outputs into a single audible
   stream — you hear one arp at a time, switching seamlessly as you
   change voicing.

### Why this works (architectural summary)

The 8-note half-measure loop is achievable because:
- `dir=0x00` + walker-style 3×7-byte config = held-key transposition
  at disk-load (verified empirically; this is the same mechanism
  factory `MA_80'sSynthRock` uses).
- High-nibble octave encoding gives multi-octave reach without
  needing a longer event sequence.
- ARPa `tick=960` + 2/4 timesig respects sub-measure loop length
  (verified by `Mute 2/4` factory arp at the same length).
- `byte[2]`/`byte[3]` gate the arp on chord size, enabling clean
  Part-Layer multi-arp without overlap.

What's **not** achievable in one file: chord-size adaptation in a
single arp. The walker (`dir=0x06–0x0d`) auto-modulos and octave-wraps
but is bar-locked and produces `chord_size × octaves` notes — never
exactly 8 across varying chord sizes. Event-driven mode doesn't apply
modulo to position bytes. The only practical adaptive solution is
multiple Parts, each with a chord-size-locked single-track arp.

### Extending to other chord sizes

The same recipe scales:

| Chord size | byte[2] | byte[3] | Indices | Notes played |
|---|---|---|---|---|
| 1 | `0x01` | `0x01` | `0x40 0x50 0x60 0x70 0x00 0x10 0x20 0x30` | held −4 oct through +3 oct (8-octave sweep) |
| 2 | `0x02` | `0x02` | `0x00 0x01 0x10 0x11 0x20 0x21 0x30 0x31` | 2 notes × 4 octaves |
| 3 | `0x03` | `0x03` | `0x00 0x01 0x02 0x10 0x11 0x12 0x20 0x21` | 3 notes through ~2.67 octaves |
| 4 | `0x04` | `0x04` | `0x00 0x01 0x02 0x03 0x10 0x11 0x12 0x13` | 4 notes × 2 octaves |

For arbitrary chord sizes N, the index pattern is:
- 8 events; positions cycle `0..N-1` with octave bumps when wrapping.

Any of these can be combined as separate Parts in one Performance
for adaptive behavior — though the synth supports up to 8 Parts per
Performance, so all four chord-size variants can coexist.
