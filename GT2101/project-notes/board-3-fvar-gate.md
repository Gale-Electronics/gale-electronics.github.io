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
schematic sheets (3A–3D), a layout sheet, and one page of inherited archive prose.

**Provenance:** ✅ = read off the boards in the photographs. 📄 = from the FANATSON tracings
(dated 08–09/2015 and **marked "PRELIMINARY"**). ❓ = inherited, unverified.

> ## Status, 22 August 2026 — ❌ OUT of the Pico architecture
>
> Board 3 and Board 4 are **one servo split across two boards**: Board 4 decides the drive
> voltage, Board 3 decides whether it is allowed out. Both leave, unmodified. See
> `gt2101_board4.md`.
>
> ⚠ **Two things to do before it comes out**, because they cannot be done afterwards:
> **measure pin 7 at each speed on the running deck** (§5), and check whether the plain
> board has **empty holes** where the other has its MC1747CL (see
> `gt2101_archive_provenance.md`).
>
> The corroded **ISSUE B** spare is the leading candidate to carry the Pico in slot 3.

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

❓ The inherited page `Disk3OpticalSensor.pdf` calls Board 3 the *"Optical Sensor /
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

📄 A repair is recorded on sheet 3A: the **E113 JFET is annotated "defective, replaced by
J113 (RS Components)"**, and a nearby diode "replaced by 1N4148". So at least one of these
boards has been worked on.

✅ **That repair note is now load-bearing elsewhere.** The same E113, in the same
common-source configuration, is Board 4's tacho front-end — and it is the circuit the Pico
needs to copy for its own tacho input. **J113 is therefore the part to buy**, with the
substitution already proven in this deck. See `gt2101_board4.md` §6.

---

## 3. The connector — nine pins, labelled on the layout

📄 Read directly off the layout sheet, which lists them along the bottom edge. Arrows are
the tracer's: ↓ leaving the board, ↑ entering it. A circled ② means the other end is Board 2.

| Pin | Signal | Direction | Notes |
|---|---|---|---|
| 1 | **+10 V** | in | |
| 2 | — | out → Board 2 | unnamed on the drawing. Board 2 pin 3 calls it STILL/TURNING status |
| 3 | — | out → Board 2 | unnamed. Board 2 pin 4, likewise |
| 4 | **start/stop pulse** | in ← Board 2 pin 5 | ✅ named from the Board 2 study: a 0 → +10 V pulse |
| 5 | **`F VAR`** | out → Board 2 | from XR2207 pin 13 via a resistor, through the 4011 |
| 6 | **drive voltage IN** | in ← **Board 4 pin 6** | ✅ source now named |
| 7 | **drive voltage OUT** | out | see the table below |
| 8 | **−10 V** | in | |
| 9 | **GND** | in | |

⚠ The layout sheet is headed **"NORMAL COPPER SIDE (mounted upside down)"** — so unlike the
Board 1 and Board 4 drawings, this one is *not* mirrored. Do not carry an orientation habit
across.

⚠ **Board 3 and Board 4 do not share a pinout** — Board 3 has −10 V on 8 and GND on 9;
Board 4 has −10 V on 7 and GND on 8. Both have +10 V on pin 1. Never swap a board between
slots.

---

## 4. The drive voltage — and a correction that matters

📄 The layout sheet tabulates **both sides** of the drive path:

| Condition | Pin 6 (in) | Pin 7 (out) |
|---|---|---|
| **STILL** | **10 V** | **0 V** |
| 33⅓ rpm | 1.2 V | 1.2 V |
| 45 rpm | 1.6 V | 1.6 V |
| 78 rpm | 2.4 V | 2.4 V |

**The backplane sheet only ever recorded one column, and it was the input one.** That is
where "STILL = 10 V" came from, and it has been sitting in the project notes as though it
were what reaches the motor.

It isn't. **When the platter is stopped, the demand rails to 10 V and Board 3 holds its
output at 0 V.** Running, it passes the voltage straight through. That is exactly what the
LM3900 window comparator and the JFET switch are for: the comparator decides STILL versus
TURNING, and the switch mutes the drive when the platter is not moving.

✅ **What opens the gate is now known:** Board 2's touch pulse arrives on pin 4 and clocks
the 4013 that drives the switch. Sheets 2A and 3A agree end to end — **the touch disc is
what lets the drive out.**

### What this changes

- **The motor is already protected — while Board 3 is fitted.** The memory doc worried that
  reading the drive table the wrong way round would "command full drive into a stationary
  platter — the case that cooks the BD675A/676A". That 10 V never leaves Board 3.
- ⚠ **With Board 3 out of the architecture, that protection leaves with it.** `V_IDLE = 0 V`
  and the ceiling in `drive.set_drive()` become the only thing standing between the firmware
  and a stationary motor. This is the single biggest risk the Pico build takes on.
- **`V_IDLE` in the firmware should be 0 V, not 10 V.** The motor wants nothing when
  stopped, 1.2 V at 33⅓, 1.6 V at 45, 2.4 V at 78. Those four numbers are the real
  specification for `drive.nominal_drive()`.

📄 still, not ✅ — these are the tracer's figures on a sheet marked PRELIMINARY. Measuring
pin 7 on a running deck would settle it, and is the single most valuable measurement left
in the project.

---

## 5. What to read here **before the board comes out**

The board is leaving, but while it is still fitted it is the best instrument in the project
— it is the original servo, running, with the right answers on its pins.

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
| What pins 2 and 3 carry exactly | Board 2 calls them STILL/TURNING status; not confirmed at either end |
| ~~What drives the XR2207's control voltage~~ | ✅ **Moot, 24 August 2026.** The Helipot is now wired directly to the Pico and to nothing else — whatever path it had through Board 2 is already broken |
| Whether ISSUE B behaves the same | Different chip set; the schematics do not describe it. **Matters now, since ISSUE B is the candidate Pico carrier** — check what its edge fingers connect to before cutting anything |
| Whether the STILL gate is really 0 V | 📄 only. Measure pin 7 with the platter stopped, before removal |
| Why one plain board has an MC1747CL and the other doesn't | Possibly a running change within the same issue; possibly the empty-holes test in `gt2101_archive_provenance.md` |
| ~~Is the archive's "optical sensor" page salvageable~~ | ✅ **Answered: no.** Board 4 is a crystal reference, tacho front-end and PLL servo — there is no photodiode or optical encoder anywhere in the tower. The page describes no board that exists |
