---
layout: bare
title: "GT2101 — Board 3 — F VAR and the Drive Gate (3275ST)"
permalink: /GT2101/project-notes/board-3-fvar-gate/
description: "Working study of the GT2101 board that generates the variable speed frequency and mutes the motor drive at rest."
---

*A working note — part of the GT2101 project's live record, written as the work happens and including the wrong turns. The polished write-ups live in [Technical Notes](/GT2101/technical-notes/).*

---

# GT2101 Board 3 — `GT201/3275ST`

**Studied 21 August 2026** from photographs of three spare boards plus four hand-traced
schematic sheets (`3ASchem.pdf`–`3DSchem.pdf`), `3Layout.pdf`, and one page of inherited
archive prose.

⚠ **Nothing in the board-3 folder has been renamed.** Boards 1 and 2 had their drawings
tidied to `Board-N-…`; this folder is still on the tracer's original names.

**Audited 5 September 2026** — all four sheets and the layout re-read at 400 dpi. **The two
things this page is load-bearing for both survive intact**: the drive-voltage table in §4 and
the connector map in §3 match the layout footer exactly, figure for figure. Two corrections
and one new finding, all in §3 and §4.

**Provenance:** ✅ = read off the boards in the photographs. 📄 = from the FANATSON tracings
(dated 08–09/2015 and **marked "PRELIMINARY"** — ✅ verified on sheet 3A, which is headed
`FANATSON 8/2015 PRELIMINARY`; the layout is dated 09/2015). ❓ = inherited, unverified.

> ## Status, updated 29 August 2026 — **stays in the deck**
>
> Board 3 and Board 4 are **one servo split across two boards**: Board 4 decides the drive
> voltage, Board 3 decides whether it is allowed out. See [the board 4 study](/GT2101/technical-notes/board-4-servo/).
>
> ⚠ **This board stays fitted.** Its hardware still-gate is what mutes the motor at rest, and
> the Pico is added alongside it rather than in place of it.
>
> ⚠ **Two measurements to take while the deck runs** (§5): **pin 7 at each speed**, and
> whether the plain board has **empty holes** where the other has its MC1747CL (see
> [`archive-provenance.md`](/GT2101/project-notes/archive-provenance/)).

---

## 1. The board number — archive gap closed

✅ **Board 3 is `GT201/3275ST`.** Legended on the copper side of every board photographed.

The board register recorded **"none recorded"** for Board 3, and the memory doc called the
missing Board 3 record *"the largest gap in the GT2101 record"*. It is now closed, and from
the part itself rather than from the defunct website. It also slots exactly into the known
sequence — 3155ST, 3272ST, **3275ST**, 3276ST, 3285NH — which corroborates the whole
numbering scheme.

### There are two issues of this board

| | Boards A and B (Matt's two main spares) | The third board |
|---|---|---|
| Legend | `GT201/3275ST` | `GT201/3275ST` **ISSUE B** |
| Copper | one routing | visibly different routing |
| ICs | XR2207P, LM308N, **LM3900N**, MC14013CP, MC14011CP (+ MC1747CL on one) | XR2207P, LM308N, MC1747CL, **NE555**, two Motorola 14-pin house-coded parts. **No LM3900.** |

⚠ **The four schematic sheets show the LM3900, so they describe the plain issue, not
ISSUE B.** Anything measured on an ISSUE B board must be treated as a separate case until
someone traces it. The ISSUE B board also shows noticeable green corrosion.

**Date codes** on the plain boards: 7428–7545 and 518–534 — so 1974 to 1975, the same
window as Board 1.

---

## 2. What Board 3 actually does — the archive is wrong

❓ The inherited page `Disk-3-Optical-Sensor.pdf` *(was `Disk3OpticalSensor.pdf`)* calls Board 3 the *"Optical Sensor /
Tachometer Processor"*, says it converts an optical encoder output into a speed signal and
is *"mounted close to the motor's internal photodiode assembly"*. It is typed prose with no
stated source, in the same style as the rest of the defunct-website material.

**It does not match the board.** There is no photodiode, no encoder input, and nothing on
the nine-pin connector that could be one. What is actually there:

| Part | What the drawings show it doing |
|---|---|
| **XR2207** | Voltage-controlled oscillator. Its square output (pin 13) leaves the board as **`F VAR`** |
| **LM3900** (quad Norton) | Wired as a *Fensterkomparator* — a **window comparator**, annotated `STILL` / `TURNING` |
| **LM308** ×1–2 | Precision op-amp, signal conditioning either side of the comparator |
| **E113 JFET + BC214 PNP** | An analogue **switch**, driven from half a 4013 |
| **MC14013 / MC14011** | Flip-flop and gating around the switch |

Read together with the connector table in section 3, Board 3 is the **variable-speed
frequency generator and the drive-voltage gate** — not a tachometer processor. The XR2207
is a VCO: it turns a voltage *into* a frequency, which is the opposite of what a tacho
processor does.

**Recommended for the archive: mark that page ❓ disputed, with this note.**

✅ **Re-read in full 5 September 2026 and every charge above holds** — and one detail is worth
adding, because it explains the whole set. **Its chip list is right** (LM308, XR2207, LM3900
really are on this board); only the *function* is invented. The same pattern shows in the
other three inherited pages, which between them get parts wrong that the galeaudio.com list
also gets wrong. **These pages look like function guessed from a parts list by someone who
never had the board.** Four checked across the Board 1, 2 and 3 audits; four wrong.

📄 A repair is recorded on sheet 3A: the **E113 JFET is annotated "defective, replaced by
J113 (RS Components)"**, and a nearby diode "replaced by 1N4148". So at least one of these
boards has been worked on.

✅ **That repair note is now load-bearing elsewhere.** The same E113, in the same
common-source configuration, is Board 4's tacho front-end — and it is the circuit the Pico
needs to copy for its own tacho input. **J113 is therefore the part to buy**, with the
substitution already proven in this deck. See [the board 4 study](/GT2101/technical-notes/board-4-servo/) §6.

---

## 3. The connector — nine pins, labelled on the layout

📄 Read directly off the layout sheet, which lists them along the bottom edge. Arrows are
the tracer's: ↓ leaving the board, ↑ entering it. A circled ② means the other end is Board 2.

| Pin | Signal | Direction | Notes |
|---|---|---|---|
| 1 | **+10 V** | in | |
| 2 | **LM3900 `OUT 2`** (its pin 4) | out → Board 2 | ⚠ **corrected 5 Sept 2026 — it *is* named, on sheet 3C.** Annotated `STILL +10 V` / `TURNING ≠10 V`. Arrives at Board 2 pin 3 |
| 3 | **LM3900 `OUT 1`** (its pin 5) | out → Board 2 | likewise named on 3C, with its own level annotation. Arrives at Board 2 pin 4 |
| 4 | **start/stop pulse** | in ← Board 2 pin 5 | ✅ named from the Board 2 study: a 0 → +10 V pulse |
| 5 | **`F VAR`** | out → Board 2 | from XR2207 pin 13 via a resistor, through the 4011 |
| 6 | **drive voltage IN** | in ← **Board 4 pin 6** | ✅ source now named |
| 7 | **drive voltage OUT** | out | see the table below |
| 8 | **−10 V** | in | |
| 9 | **GND** | in | |

⚠ **Pins 2 and 3 were listed here as "unnamed on the drawing" until the 5 Sept audit.** They
are named — just on sheet 3C rather than on the layout, which is where this table came from.
That substantially answers the first open question in §6: they are the window comparator's
two outputs, reporting STILL versus TURNING to Board 2. ⚠ The **level** annotations beside
them are faint pencil and the `+` / `≠` marks do not read cleanly even at 400 dpi, so which
state is high is still 📄-with-a-question-mark. The *identity* of the pins is not.

⚠ The layout sheet is headed **"NORMAL COPPER SIDE (mounted upside down)"** — so unlike the
Board 1 and Board 4 drawings, this one is *not* mirrored. Do not carry an orientation habit
across.

⚠⚠ **And do not carry one between this board's own sheets either — added 5 Sept 2026.**
Sheet **3C is headed `LM3900 gespiegelt` and footed `LM3900 MIRRORED!`**, and sheet **3D is
footed `4011 MIRRORED!`**. So the layout is un-mirrored while two of the four schematic
sheets are mirrored, on the same board, in the same set. Read the pin numbers the tracer
wrote; do not count legs from a corner.

⚠ **Board 3 and Board 4 do not share a pinout** — Board 3 has −10 V on 8 and GND on 9;
Board 4 has −10 V on 7 and GND on 8. Both have +10 V on pin 1. Never swap a board between
slots.

---

## 4. The drive voltage — and a correction that matters

✅ **Re-read off `3Layout.pdf` at 400 dpi on 5 September 2026 and every figure matches** —
both columns, all four rows, and the pin directions. This is the project's most load-bearing
table and it is a faithful transcription.

⭐⭐ **And it is recorded in four independent places in the archive**, all agreeing, all read at
400 dpi on 5 September 2026: `3Layout.pdf`'s footer (both columns), `Board-4-Schem.pdf` beside
the 1747 B output, `Board-4-Layout.pdf`'s footer at pin 6, and `motor-overview/backplane.pdf`
(both columns again — see the correction below). 📄 still, not ✅ — none of it is a measurement
— but for a figure the whole firmware drive table rests on, four agreeing records is as strong
as a paper archive gets.

📄 The layout sheet tabulates **both sides** of the drive path:

| Condition | Pin 6 (in) | Pin 7 (out) |
|---|---|---|
| **STILL** | **10 V** | **0 V** |
| 33⅓ rpm | 1.2 V | 1.2 V |
| 45 rpm | 1.6 V | 1.6 V |
| 78 rpm | 2.4 V | 2.4 V |

⚠⚠ **This paragraph used to say "the backplane sheet only ever recorded one column, and it
was the input one." It is not true, and it was corrected on 5 September 2026.**

`motor-overview/backplane.pdf`, read at 400 dpi, records **both columns, side by side on the
two adjacent pads** — and the second column reads **`STILL: 0 V`** in the tracer's own hand.
The information was complete in the archive the whole time.

⭐ **So "STILL = 10 V" was never a gap in the source. It was a misreading of a source that had
both numbers on it.** That is a less comfortable account than the one this page used to give,
and it is the accurate one. A missing column is bad luck; a misread column is a habit, and the
defence against it is the one this project keeps relearning: **go back to the drawing.**

The figure had been sitting in the project notes as though the input column were what reaches
the motor.

It isn't. **When the platter is stopped, the demand rails to 10 V and Board 3 holds its
output at 0 V.** Running, it passes the voltage straight through. That is exactly what the
LM3900 window comparator and the JFET switch are for: the comparator decides STILL versus
TURNING, and the switch mutes the drive when the platter is not moving.

✅ **What opens the gate is now known:** Board 2's touch pulse arrives on pin 4 and clocks
the 4013 that drives the switch. Sheets 2A and 3A agree end to end — **the touch disc is
what lets the drive out.**

### The gate, as sheet 3A actually draws it — 5 September 2026

```
   pad 4 (touch pulse from Board 2) --[R]--> 4013 CL2 (pin 11)
   4011 pin 11 -------------------- [R]--> 4013 R2  (pin 10)   ← sheet 3D labels this
                                                                 output "R (4013) (PIN 10)"
   4013 Q̄2 --> BC214 PNP --[R to −10 V]--> diode --> E113 GATE
   E113 channel sits in series between pad 6 (in) and pad 7 (out),
   with a resistor across it
```

So the 4013 is **clocked** by the touch pulse and **reset** by the 4011 — the touch pulse
alone does not tell the whole story, and anything that resets that 4013 shuts the drive off.
📄 The E113's two repair notes sit right here on the sheet, and both read verbatim as this
page quotes them: **"Defective. Replaced by J113 (RS-Components)"** and, on the diode just
before it, **"Replaced by 1N4148"**. ✅ Verified 5 Sept 2026.

### ⭐ The comparator watches pin 7 itself — new, 5 September 2026

Sheet 3C feeds the LM3900's **`IN 3−` (its pin 8) from the pad 7 net**, through a resistor
divider — the tracer marks the shared net with an asterisk on both 3A and 3C. **So the
window comparator senses the drive voltage that this same board gates.**

That is not circular by accident, it is the point: once the gate is shut, pin 7 is 0 V, the
comparator keeps reading STILL, and the state holds. **It is a latch, and the touch pulse on
pin 4 is what breaks it.** It also means pin 7 is the pin that decides what Board 2 and the
display are told about STILL versus TURNING — one more reason it is the measurement worth
taking.

### What this changes

- **The motor is protected in hardware, and stays that way.** The memory doc worried that
  reading the drive table the wrong way round would "command full drive into a stationary
  platter — the case that cooks the BD675A/676A". That 10 V never leaves Board 3.
- ✅ **Board 3 stays fitted, so the hardware still-gate stays in circuit.** ⚠ An earlier
  version of this section warned that "with Board 3 out of the architecture, that protection
  leaves with it," and called it the single biggest risk of the build. **That was written
  under the withdrawn remove-the-boards plan and does not apply.** `V_IDLE = 0 V` and the
  ceiling in `drive.set_drive()` are belt-and-braces agreeing with the hardware, not the only
  braces. Do not inherit that alarm.
- **`V_IDLE` in the firmware should be 0 V, not 10 V.** The motor wants nothing when
  stopped, 1.2 V at 33⅓, 1.6 V at 45, 2.4 V at 78. Those four numbers are the real
  specification for `drive.nominal_drive()`.

📄 still, not ✅ — these are the tracer's figures on a sheet marked PRELIMINARY. Measuring
pin 7 on a running deck would settle it, and is the single most valuable measurement left
in the project.

---

## 5. What to read here **on the running deck**

While it is fitted and running this board is the best instrument in the project — it is the
original servo, live, with the right answers on its pins.

- **Pin 7, the drive voltage out.** 0–10 V, so a two-resistor divider into an ADC input.
  This is the calibration prize: run the deck on its original electronics, let the 1975
  servo settle at each speed, and log what voltage it actually chooses. Four numbers that
  are currently 📄 become ✅.
- **Pin 6, the demand in.** Reading pins 6 and 7 together shows the gate operating — you
  would see 10 V in and 0 V out with the platter stopped, which is a direct confirmation of
  section 4 without needing a scope.
- **Pin 5, `F VAR`.** A frequency, so a divider and an edge count. Tells the Pico what
  speed the original electronics is asking for — useful for checking the Pico's own
  pot-to-rpm mapping against Gale's.

---

## 6. Open questions

| ❓ | Why it matters |
|---|---|
| ~~What pins 2 and 3 carry exactly~~ — ✅ **largely answered 5 Sept 2026** | They are the LM3900 window comparator's `OUT 2` (pin 4 → pad 2) and `OUT 1` (pin 5 → pad 3), named on sheet 3C with STILL/TURNING annotations (§3). ⚠ Which state is the high one is still 📄 — the pencil `+`/`≠` marks do not read cleanly. One meter reading on pads 2 and 3, platter stopped then turning, would close it |
| ~~What drives the XR2207's control voltage~~ | ✅ **Moot, 24 August 2026.** The Helipot is now wired directly to the Pico and to nothing else — whatever path it had through Board 2 is already broken |
| Whether ISSUE B behaves the same | Different chip set; the schematics do not describe it. Archive interest only — the spare is not being pressed into service |
| Whether the STILL gate is really 0 V | 📄 only. Measure pin 7 with the platter stopped. ⭐ **Worth more than it looks**: pin 7 is also what the window comparator senses (§4), so one reading there tests the gate *and* the STILL/TURNING logic at once |
| Why one plain board has an MC1747CL and the other doesn't | Possibly a running change within the same issue; possibly the empty-holes test in [`archive-provenance.md`](/GT2101/project-notes/archive-provenance/) |
| ~~Is the archive's "optical sensor" page salvageable~~ | ✅ **Answered: no.** Board 4 is a crystal reference, tacho front-end and PLL servo — there is no photodiode or optical encoder anywhere in the tower. The page describes no board that exists |
