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

**Audited 5 September 2026** — all four sheets and the layout re-read at 400 dpi. ⭐ **The two
things this page is load-bearing for both survive intact:** the drive-voltage table in §4 and
the connector map in §3 match the layout footer exactly, figure for figure. **Sheets 3B and 3D
re-read 6 September 2026** for the `F VAR` path.

**Re-audited 8 September 2026** — all four sheets plus `motor-overview/backplane.pdf` read
again, at Matt's request, to double-check the `F VAR` injection before it is made permanent.
⭐ **The injection survives the check and comes out stronger** (§7). ⚠ **But two things in this
page were wrong:** pad 5 does not go to board 2 (§3), and the `ORANGE` post has a **second job**
nobody had recorded (§2a). **Current as of 8 September 2026.**

*Corrections this page used to carry inline are in
[`corrections-log.md`](/GT2101/project-notes/corrections-log/) §1, §2, §10, §11 and §13.*

**Provenance:** ✅ = read off the boards in the photographs. 📄 = from the FANATSON tracings
(dated 08–09/2015 and **marked "PRELIMINARY"** — ✅ verified on sheet 3A, which is headed
`FANATSON 8/2015 PRELIMINARY`; the layout is dated 09/2015). ❓ = inherited, unverified.

> ## Status — **stays in the deck**
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

## 1. The board number

✅ **Board 3 is `GT201/3275ST`.** Legended on the copper side of every board photographed —
read off the part itself, not inherited.

⭐ It slots exactly into the known sequence — 3155ST, 3272ST, **3275ST**, 3276ST, 3285NH —
which corroborates the whole numbering scheme.

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

## 2. What Board 3 does

**Board 3 is the variable-speed frequency generator and the drive-voltage gate.** It makes
`F VAR`, and it decides whether the drive voltage from Board 4 is allowed out to the motor.

📄 What is on it, and what the drawings show each part doing:

| Part | What it does |
|---|---|
| **XR2207** | Voltage-controlled oscillator. Its square output (pin 13) leaves the board as **`F VAR`** — see §3 |
| **LM3900** (quad Norton) | Wired as a *Fensterkomparator* — a **window comparator**, annotated `STILL` / `TURNING` |
| **LM308** ×1–2 | Precision op-amp, signal conditioning either side of the comparator |
| **E113 JFET + BC214 PNP** | An analogue **switch** — the drive gate itself, driven from half a 4013 |
| **MC14013 / MC14011** | Flip-flop and gating around the switch |

⚠ **There is no photodiode, no encoder input, and nothing on the nine-pin connector that could
be one.** The XR2207 is a VCO: it turns a voltage *into* a frequency, which is the opposite of
what a tachometer processor does.
*(The inherited page `Disk-3-Optical-Sensor.pdf` describes this board as an optical sensor. It
is marked ❓ disputed — see [`corrections-log.md`](/GT2101/project-notes/corrections-log/) §13.)*

---

## 2a. ⚠⚠ The `ORANGE` post does TWO jobs — found 8 September 2026

The archive has recorded this post as one thing: *the XR2207's control voltage, by flying lead
from the Helipot.* **That is only half of it.** Three sheets, read together, show the same node
going two ways.

| Path | Sheet | What it does |
|---|---|---|
| through a **resistor**, DC | 📄 3B | to the XR2207's **pin 6**, its timing-resistor terminal — this is the frequency control |
| through a **capacitor**, AC | 📄 3A *and* 3B | to the **LM308's pin 3** (its `+` input). 3A labels the wire `ORANGE POST` in the tracer's own hand |

⚠⚠ **The split is in the board's copper, not in the cable.** There is **one** orange wire and it
lands on **one** point. You cannot see this from the wire — only by following the track, or by
reading the sheets. ⭐ **And it does not matter whether that wire sits on the post or directly on
the XR2207's leg:** either way, when the orange cable left board 3, the LM308 branch lost its
source too. Same conclusion from both.

### ✅✅ The three posts ARE the Helipot's three leads — confirmed 8 September 2026

📄 Sheet 3B names three flying-lead posts on this board: **`RED`**, **`ORANGE`** and
**`YELLOW`**. ✅ `board-2-touch-timing/Helipot.jpeg` shows the pot carrying exactly three leads —
**red, orange and yellow**. **Same three, same colours.** The archive had *"an `ORANGE` post, by
flying lead from the Helipot"* as an inference; it is now a match on two independent records.

✅ **And the photograph names the wiper.** The pot's legend reads `CCW` / `CW` / **`S`**, and the
**`S`** — the slider — sits at the **orange** terminal. `R 1K`, `L .25`, date code **7603**.

⭐ **So the whole original speed control reads off in one line, which the archive did not have:**

```
   Helipot  CCW end ── RED post    ── board 3 GND
            slider   ── ORANGE post ── XR2207 pin 6  (and the LM308, above)
            CW  end  ── YELLOW post ── board 3 −V
```

**The wiper swung the XR2207's control between GND and −V.** 📄 The two end posts' destinations
are from sheet 3B; the colours and the slider are ✅ from the part.

📄 **And sheet 3C says where the LM308 goes, in block capitals at the top left:
`FROM LM308 PIN 6`** → a resistor → the LM3900's **`1+ IN`**, and along the same wire to
**`2− IN`**. Those are amplifiers 1 and 2 — and **`2 OUT` → pad 2, `1 OUT` → pad 3.**

> **So the two STILL/TURNING lines to board 2 trace back to the `ORANGE` post, and that post is
> now open.**

### ⭐ What this does NOT break — read this before worrying

**The drive gate is untouched, and so is the motor.** The LM3900's *other* pair, amplifiers 3
and 4, sense the **pad 7 net** — `IN 3−`, its pin 8, verified on sheet 3C — and their outputs
feed the 4011 → 4013 → BC214 → J113 chain in §4. **The hardware mute, the touch-pulse latch and
the 0 V-at-rest behaviour are all on that pair.** Nothing about §4 changes.

### ⚠ What it may break — board 2's mode bit, and therefore the display

Pads 2 and 3 → board 2 pads 3 and 4 → the 4001 chain → the **MC14016** that picks the
`F DISPLAY` source (demand vs `INV TACH`) **and** the gate rate (2 Hz vs 0.5 Hz) **together**.
The pairing is deliberate: 1332 Hz × 0.25 s and 333 Hz × 1 s both give **333**, so the display
reads `33.3` either way. **Stick that bit and the source and the window mismatch — the reading
comes out about 4× wrong.**

⭐ **The test costs nothing and was already on the list:** `fvar.rpm(33.3333)`, platter stopped,
expect **`33.3`**. **A reading near `133` is this, not the Pico.**

⚠⚠ **Do not treat the above as settled.** A DC pot wiper, through a *series capacitor*, into an
amplifier, makes no sense as a still-or-turning detector — you cannot see motion in a pot
voltage. ⭐ **The colour match above rules out one of the three escapes** — `ORANGE` really is the
wiper — so what is left is that the component is not a capacitor, or that the tracer drew that
branch wrong. **This is a reading to take, not a conclusion to build on** — see §6.

---

### 📄 A repair recorded on the sheet

Sheet 3A annotates the **E113 JFET** *"defective, replaced by J113 (RS Components)"*, and a
nearby diode *"replaced by 1N4148"*. So at least one of these boards has been worked on.

⭐ **That repair note is load-bearing elsewhere.** The same E113, in the same common-source
configuration, is Board 4's tacho front-end — and it is the circuit the Pico needs to copy for
its own tacho input. **J113 is therefore the part to buy**, with the substitution already proven
in this deck. See [the board 4 study](/GT2101/technical-notes/board-4-servo/) §6.

---

## 3. The connector — nine pins, labelled on the layout

📄 Read directly off the layout sheet, which lists them along the bottom edge. Arrows are
the tracer's: ↓ leaving the board, ↑ entering it. A circled ② means the other end is Board 2.

| Pin | Signal | Direction | Notes |
|---|---|---|---|
| 1 | **+10 V** | in | |
| 2 | **LM3900 `OUT 2`** (its pin 4) | out → Board 2 | 📄 Named on sheet 3C, annotated `STILL +10 V` / `TURNING ≠10 V`. Arrives at Board 2 pin 3 |
| 3 | **LM3900 `OUT 1`** (its pin 5) | out → Board 2 | 📄 Likewise named on 3C, with its own level annotation. Arrives at Board 2 pin 4 |
| 4 | **start/stop pulse** | in ← Board 2 pin 5 | ✅ named from the Board 2 study: a 0 → +10 V pulse |
| 5 | **`F VAR`** | out → **board 5 pad 4** ⚠ *not* board 2 | ✅✅ **MEASURED END TO END 7 Sept 2026 on spare board B:** pull-up **10.66 kΩ**, series `R` **10.16 kΩ**, 4011 pin 4 beeps to this pad. ⚠⚠ **The XR2207 is a 14-pin chip** — pin 13 is the **2nd leg from the left along the top row**, printing upright, notch left. ⚠ **This pad is the 4011 OUTPUT — never inject here.** ⭐ **Detailed 6 Sept 2026:** XR2207 pin 13 is an **open-collector** `SQUARE OUT` with a pull-up resistor to the XR2207's own **regulated `+V` (its pin 1)** — ⚠ *not* to +10 V, which this row used to say; a series `R` carries it to the **4011's pins 5+6, strapped as an inverter**, whose pin 4 is this pad. This makes it the cheapest place in the project for the Pico to inject a speed command — see [`pico-controller-notes.md`](/GT2101/project-notes/pico-controller-notes/) § `F VAR` |
| 6 | **drive voltage IN** | in ← **Board 4 pin 6** | ✅ source now named |
| 7 | **drive voltage OUT** | out | see the table below |
| 8 | **−10 V** | in | |
| 9 | **GND** | in | |

### ⚠⚠ Pad 5 goes to **board 5**, not board 2 — corrected 8 September 2026

This row read *"out → Board 2"* from the day the table was built, and
[`flexicon-backplane-map.md`](/GT2101/project-notes/flexicon-backplane-map/) §5 said the same.
**Both were wrong, and board 2's own 14-pin map is the tell — it has no `F VAR` input.**

📄 `motor-overview/backplane.pdf`, read at 350 dpi, draws row 3 pad 5 (labelled **`VAR`**)
running **straight down to row 5 pad 4**, passing row 4 with no pad on the way. From there the
**black switch** chooses it or the fixed 1332 Hz, and the choice returns on **row 5 pad 3**.

⭐ **And that return is one net with three pads** — board 5 pad 3 = **board 4 pad 3** = **board 2
pad 7**. The same selected frequency feeds the servo *and* the display. That is how board 2 gets
a demand frequency without ever seeing `F VAR` itself.

⚠ **`F VAR` is already ×40 when it leaves this board.** The old signal chain in the flexicon map
showed a `×40` stage on board 2; there is none, anywhere. The backplane sheet writes
**`3996 Hz (×40)`** beside row 5 pad 4 and **`1332 Hz`** beside pad 7, both in the tracer's hand.
⭐ **So the Pico's 1333 Hz for 33⅓ rpm is confirmed twice more**, and the error never reached the
firmware.

⚠ **Pins 2 and 3 are named on sheet 3C, not on the layout** — which is where this table was
built from, and why they were long recorded as "unnamed". They are the window comparator's two
outputs, reporting STILL versus TURNING to Board 2. ⚠ The **level** annotations beside them are
faint pencil and the `+` / `≠` marks do not read cleanly even at 400 dpi, so **which state is
high is still 📄 with a question mark.** The *identity* of the pins is not.

⚠ The layout sheet is headed **"NORMAL COPPER SIDE (mounted upside down)"** — so unlike the
Board 1 and Board 4 drawings, this one is *not* mirrored. Do not carry an orientation habit
across.

⚠⚠ **And do not carry one between this board's own sheets either.**
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

📄 `motor-overview/backplane.pdf`, read at 400 dpi, records **both columns side by side** on the
two adjacent pads, the second reading **`STILL: 0 V`** in the tracer's own hand.

⚠ **Do not read the input column as what reaches the motor.** **When the platter is stopped,
the demand rails to 10 V and Board 3 holds its
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

- **The motor is protected in hardware.** The 10 V never leaves Board 3, so there is no path
  by which full drive reaches a stationary platter and cooks the BD675A/676A.
- ✅ **Board 3 stays fitted, so the hardware still-gate stays in circuit.** `V_IDLE = 0 V` and
  the ceiling in `drive.set_drive()` are belt-and-braces agreeing with the hardware, not the
  only braces.
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
| **Which of pins 2 and 3 is high in which state** | They are the LM3900 window comparator's `OUT 2` (pin 4 → pad 2) and `OUT 1` (pin 5 → pad 3), named on sheet 3C with STILL/TURNING annotations (§3). The pencil `+`/`≠` marks do not read cleanly. **One meter reading on pads 2 and 3, platter stopped then turning, closes it** |
| **Whether the STILL gate is really 0 V** | 📄 only. Measure pin 7 with the platter stopped. ⭐ **Worth more than it looks:** pin 7 is also what the window comparator senses (§4), so one reading tests the gate *and* the STILL/TURNING logic at once |
| ⭐ **What is the real negative rail?** | Pin 8 to pin 9, DC volts. Two pins side by side, and confusing them offsets every reading on this board by the whole rail — see the bench warning in [`pico-controller-notes.md`](/GT2101/project-notes/pico-controller-notes/) § `F VAR`. The archive only has ±10 V on paper |
| ⚠⚠ **Are pads 2 and 3 still doing anything?** | §2a. Sheets 3A/3B/3C put them at the end of a chain that starts at the now-open `ORANGE` post. If they are dead, board 2's display mux is stuck and the display can read ~4× out. **Two readings close it: pads 2 and 3 to pad 9, platter stopped then turning. If they do not move, the lines are dead** |
| ❓ **Is that really a capacitor between the `ORANGE` post and the LM308?** | §2a. It is what both 3A and 3B draw, and it is what makes the chain above implausible. ⭐ **Now the only escape left**, since the colour match has confirmed `ORANGE` is the wiper. One continuity check on a **spare** board — post to LM308 pin 3, powered down — would say whether it is a capacitor, a link, or nothing. ⚠ Not a job for the live tower |
| Whether ISSUE B behaves the same | Different chip set; the schematics do not describe it. Archive interest only — the spare is not being pressed into service |
| Why one plain board has an MC1747CL and the other doesn't | Possibly a running change within the same issue; possibly the empty-holes test in [`archive-provenance.md`](/GT2101/project-notes/archive-provenance/) |

### ✅ Settled

⭐⭐ **What board 3 pin 5 is doing — MEASURED 6 September 2026: 0.05 V, parked, stable**, in both
black-switch positions and across a power cycle. **The XR2207 is not oscillating**, because its
control voltage arrives on the `ORANGE` post and that wire is now on the Pico. ⭐ **So the Pico
can inject `F VAR` here with no break at all** — one BC547B, one base resistor, one wire. It
also confirms the black switch sits *downstream* of this board, on board 5.

Also settled: what pins 2 and 3 carry (**the window comparator's two outputs**) · what drives the XR2207's
control voltage (**an `ORANGE` post on this board, by flying lead from the Helipot — not via
Board 2**; that lead is now on the Pico, so the input is open — ⚠ **but see §2a: that post is
not single-purpose**) · whether the archive's "optical
sensor" page is salvageable (**no** — Board 4 is the crystal, tacho front-end and PLL servo;
there is no photodiode or optical encoder anywhere in the tower).
