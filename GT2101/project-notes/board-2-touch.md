---
layout: bare
title: "GT2101 — Board 2 — Touch & Display Timing (3272ST)"
permalink: /GT2101/project-notes/board-2-touch/
description: "Working study of the GT2101's touch start/stop board, its 14-pin connector map, and the Helipot it carries."
---

*A working note — part of the GT2101 project's live record, written as the work happens and including the wrong turns. The polished write-ups live in [Technical Notes](/GT2101/technical-notes/).*

---

# GT2101 Board 2 — `GT201/3272ST`

**Studied 22 August 2026** from sheets `Board-2A-Schem.pdf`, `Board-2BSchem.pdf` and
`2Layout.pdf` (FANATSON, 17.09.2015), plus photographs of the spare board.

⚠ **The three filenames in that folder are inconsistent** — one hyphenated, one not, one
never renamed at all. They were `2ASchem` / `2BSchem` / `2Layout` when this page was
written. Board 1's folder was tidied and this one was half-tidied.

**Audited 5 September 2026** — every claim re-read against all three sheets at 400 dpi.
**Current as of 6 September 2026.**

**Provenance:** ✅ read off the board · 📄 from the FANATSON tracings · ❓ unverified.

*Corrections this page used to carry inline are in
[`corrections-log.md`](/GT2101/project-notes/corrections-log/) §1, §9 and §13.*

---

## 1. ✅ THE TOUCH SENSOR IS CONFIRMED

Sheet 2A is drawn around an electrode explicitly labelled **`TOUCH SENSOR`**. The
touch-sense hypothesis in [the board register](/GT2101/engineering-drawings-schematics/) — the bent copper tab beside
the Helipot bush, a 555 centimetres away — is no longer a hypothesis.

**The chain, 📄 from sheet 2A:**

```
TOUCH SENSOR ─ 10n ─ 10k ─→ MC1455P1 (=NE555) TRIGGER (pin 2)
                              │  220k / 270k / diode across DISCHARGE + THRESHOLD
                              ↓
                       T1 ─ 220k / 0.47µ ─ 1µ ─ T2  (1M bias to −10 V)
                              ↓
                       MC1748CP1 op-amp   (inverting, 1M feedback, 15k on +)
                              ↓
                            [10K]
                              ↓
                    ┌─── node ───┬──── diode to GND ────┐
                    │            │   (clamps one polarity)
                    │            └──→ connector pin 6 (LO)
                    ↓
             ¼ MC14011 NAND, inputs 5+6 tied = inverter, output pin 4
                    ↓
             connector pin 5 (HI)
```

⚠⚠ **The 10K and the diode are the important part of that chain.** Pin **5** is taken from the
CMOS gate *output*; pin **6** is taken from the gate's *input* node — the same node the clamp
diode sits on. **The two pads are not the same kind of thing.**

⚠ The tracer's own warning on the sheet: **"T1, T2: types, values, pinouts only educated
guess. NO REFERENCES ON MY UNIT, NOT MEASURED!"** The 555 and the 4011 output stage are
drawn confidently; the two transistors are not.

### The output is a PULSE, not a level and not a latch

📄 Both waveforms are drawn on sheet 2A:

| Pin | Name | Waveform | Goes to |
|---|---|---|---|
| **5** | `START/STOP PULSE` **HI** | 0 V → **+10 V** pulse | PCB **3** |
| **6** | `START/STOP PULSE` **LO** | 0 V → **−10 V** pulse *(disputed — see below)* | PCB **1** |

### ⚠⚠ Sheet 2A contradicts itself about pin 6 — opened 5 September 2026

The waveform above is the tracer's own annotation. **But the circuit he drew on the same
sheet does not seem able to produce it**, and the far end of the wire argues against it too:

1. **On this board.** Pin 6 taps the node *after* the 10K and *on* the clamp diode, which
   is the 4011's input node. A diode to ground there is the standard way of keeping a
   ±10 V op-amp output inside a CMOS gate's input range. If it is doing that, the node
   cannot reach −10 V — it stops at roughly −0.6 V.
2. **At the far end.** ✅ Board 1 physical pin 3 is the 4511's `BL` pin, and Board 1 puts a
   **pull-up to +10 V** on it (see [`board-1-display.md`](/GT2101/project-notes/board-1-display/)
   §3). A pull-up means the line is meant to *rest high and be pulled low* — and a −10 V
   pulse into a CMOS input with a pull-up to +10 V would be abusive.
3. **"HI" and "LO" may simply mean which way the pulse goes** — pin 5 rests low and pulses
   high, pin 6 rests high and pulses low. That reading fits both boards and needs no −10 V
   anywhere.

⚠ **Nothing in the Pico plan changes yet, and the ☠ warning below stands.** Do not treat
pin 6 as safe on the strength of a hand-traced diode. But this is worth one meter reading
before any wiring near that pad is designed, and it is a safe one: **meter on DC volts,
black on GND, red on Board 2 pad 6, tower running, touch the disc.** Two numbers — the
resting voltage and the lowest it reaches. If it never goes below 0 V, the −10 V waveform
is wrong and the pad is ordinary logic.

Pin 5 arrives at Board 3's connector pin 4, which feeds the 4011 that clocks the 4013
that drives the BC214 / J113 drive gate. So **the touch pulse is what opens and closes
the motor drive** — sheets 2A and 3A agree end to end.

### Consequence for the Pico — this is the easy case

- **Tap pin 5.** It swings 0 → +10 V, so a **27 kΩ / 10 kΩ divider plus 1 kΩ in series**
  and a rising-edge interrupt on a GPIO. Pin 6 swings **negative**, and ☠ a divider does
  **not** make it safe — dividing −10 V just gives a smaller negative voltage, still below
  ground and straight into the Pico's lower clamp diode. There is no reason to use it.
  See [`flexicon-backplane-map.md`](/GT2101/project-notes/flexicon-backplane-map/) §4:
  pads 5 and 6 are next door to each other, and **getting the right pad is what protects
  the Pico, not the resistors.**
- ⚠⚠ **Pin 5 is a LIVE net.** Board 2 drives it and board 3 pin 4 receives it. The Pico
  **listens in parallel** through the divider and **must never drive it.** That is the
  ⚠ *listen before driving* rule in
  [`pico-controller-notes.md`](/GT2101/project-notes/pico-controller-notes/) § how the Pico
  meets the tower — driving a live net gives continuous, dynamic contention that would
  partly "work", which is the worst kind of fault to chase.
- **The Pico holds the start/stop state in software**, since the hardware only emits an
  edge. Each pulse toggles. That is what `controls.py` would have done anyway.
- **The touch chain is self-contained** — it needs only +10 V, −10 V and GND, and does not
  depend on Boards 3 or 4 for anything.

---

## 2. The connector — 14 pins, mapped

📄 From the layout sheet's footer, cross-checked against sheet 2B. Arrows are the
tracer's; a circled number is the board at the other end.

| Pin | Signal | Direction |
|---|---|---|
| 1 | **+10 V** | in |
| 2 | 1.048 MHz crystal ← ④ | in |
| 3 | ← ③ (STILL/TURNING status) | in |
| 4 | ← ③ (STILL/TURNING status) | in |
| 5 | **`START/STOP PULSE` HI** → ③ | out |
| 6 | **`START/STOP PULSE` LO** → ① | out |
| 7 | `F REF ×40` ← ④ | in |
| 8 | **`F DISPLAY`** → ① | out |
| 9 | `INV TACH` ← ④ | in |
| 10 | → ① — ✅ **confirmed the ~1 Hz gate**, 5 Sept 2026 (see below) | out |
| 11 | `1332 Hz FIX` (= 33.3 × 40) → ⑤ | out |
| 12 | **−10 V** | in |
| 13 | **`RESET` ← ①** | in |
| 14 | **GND** | in |

⚠ Sheets 2B and 2Layout disagree slightly on pins 7 and 11 — 2B calls pin 7 "F VAR or FIX
from the speed switch via PCB 4" and pin 11 "1332 Hz FIX 'D'". Same signals, different
descriptions. Both sheets agree on the *directions*, and the numbers agree too
(`F REF ×40` at 33⅓ rpm **is** 1332 Hz), so this is a naming difference rather than a
conflict. **Pin 11's direction is now settled** — sheet 2B shows it driven by the 4040's
`Q10`, so it is an output, as the layout says.

📄 The layout footer reads **`= 33,3 × 40`** — i.e. 33.3 × 40 = 1332 Hz.

⚠ The layout sheet is headed **"② MIRRORED"** — the opposite of Board 3's sheet, which is
not. Do not carry an orientation habit between them.

### ⭐⭐ What this settles about Board 1 — the display timebase closes on both boards at once

- `F DISPLAY` reaches Board 1 from **Board 2 pin 8** — and pin 8 is the common terminal of
  a **4016 two-way switch** choosing between **pin 7** (`F VAR/FIX`, the *demand*
  frequency, ~1332 Hz at 33⅓) and **pin 9** (`INV TACH`, the *actual* speed). That is the
  "switches between motor tach and demand" line in
  [`folder-findings.md`](/GT2101/project-notes/folder-findings/) §2.3, drawn out.
- ⚠ **The gate on pin 10 comes from the MC14521, not the 4040** — the 4040 is a 12-stage
  counter and has no `Q21`. `Q21` and `Q19` are on the **MC14521 24-stage divider**, clocked
  by the **1.048711 MHz crystal signal arriving on pin 2** from PCB 4. The arithmetic is exact
  and settles it beyond doubt:

  | | |
  |---|---|
  | 1 048 711 Hz ÷ 2²¹ | **0.4999 Hz** — the sheet's `Q21 = 0.5 Hz` |
  | 1 048 711 Hz ÷ 2¹⁹ | **2.000 Hz** — the sheet's `Q19 = 2 Hz` |

- **Pin 10 is a 4016 two-way switch between those two**, so the gate Board 1 receives is
  either **0.5 Hz or 2 Hz**. The same control line (from the 4001 chain, ultimately from
  the STILL/TURNING inputs on pins 3 and 4) switches the `F DISPLAY` source as well — one
  mode bit moves both.

- ⭐ **This confirms Board 1's window from the other end.** A **2 Hz square wave gives a
  250 ms count window**, and 1332 Hz × 0.25 s = **333** → the display reads `33.3`. That is
  exactly the window [`board-1-display.md`](/GT2101/project-notes/board-1-display/) §4
  derived from the count, and exactly what its 5 Sept audit concluded: **the display
  timebase is fixed and crystal-derived, and the tracer's "1Hz?" on Board 1 was a good
  guess at a 2 Hz line.** Two boards, two sheets, one answer.

- ⚠ **Board 1's pin 10 `RESET` output lands on Board 2 pin 13, and it resets the
  MC14521 — not the 4040.** Its `R` pin sits on that pad with a 1M pull-down, so the line
  rests low and Board 1 pulses it high.

- ⭐ **So the two boards are a loop, not a master and a slave.** Board 2's crystal divider
  generates the window; Board 1 counts in it, latches, resets, and sends that reset back to
  re-zero Board 2's divider. That is why `config.py` says **never drive Board 1's pin 10** —
  driving it would re-zero the tower's display timebase on every write.

---

## 3. It is ONE board, not two

**The archive's "2A" and "2B" are the tracer's two schematic sheets of a single board.**

That matters because two inherited prose pages made it look like two. `Disk-2A-Servo-Control.pdf`
describes a servo board; `Disk-2B-Power-Driver.pdf` describes LM324/LM358 op-amps, BD675A/BD676A
power transistors and three-phase drive currents *"mounted directly above the motor housing"* —
⚠ **which is the motor controller PCB, filed as a tower disk by mistake.**

Both pages are marked ❓ disputed, along with the rest of the inherited prose set. See
[`corrections-log.md`](/GT2101/project-notes/corrections-log/) §13. **Prefer the tracings and
the hardware.**

---

## 4. Chips on the board ✅

Read off the spare, 20 August 2026: **MC1455P1** (7336), **MC14040CP** (M75-39),
**MC14521CP** (7521), **MC14016CP** (M75-04), **MC14011CP** (AA7533), **MC14001CP** (7532),
**MC1748CP1** (M 535 A). Paper sticker reading **"OK NOV 81"** still attached.

---

## 5. Open questions

| ❓ | Why it matters | How to settle it |
|---|---|---|
| ⚠⚠ **Does pin 6 really swing to −10 V?** | It decides whether that pad is dangerous or ordinary logic, and §1 carries a ☠ warning on it. Sheet 2A's circuit and Board 1's pull-up both say no; sheet 2A's own waveform says yes | One meter reading: DC volts, black on GND, red on pad 6, tower running, touch the disc (§1) |
| What the touch tab actually is — contact, or a gap to the shaft | Determines whether the sense is conductive or capacitive | — |
| Whether the 555's threshold is reliable in practice | If not, take the tab straight to a Pico pin instead | — |
| T1 and T2's real identities | ⚠ The tracer's own note: *"types, values, pinouts only educated guess. NO REFERENCES ON MY UNIT, NOT MEASURED!"* Nobody has read them off the board | — |
| ❓ Where the 4040's clock comes from, and what its `Q10` ÷1024 output really is | Pin 11 is labelled 1332 Hz, but 1.048711 MHz does not divide down to 1332 Hz through a `NAND(Q10, Q9)` reset. Either the crystal figure, the decode or the label is out by about a factor of two | Nothing depends on it. Note it and move on unless pin 11 ever matters |

### ✅ Settled

Which Board 1 pin the LO pulse lands on (**row 2 pad 6 → row 1 pad 2 = Board 1 physical pin 3,
`BLANK`** — left connected, touching the disc blanks the display; whether to break that is an
open item in [`flexicon-backplane-map.md`](/GT2101/project-notes/flexicon-backplane-map/) §10) · pins 7 and 11, where the two
sheets disagreed (**a naming difference, not a conflict**; directions agree and `F REF ×40` at
33⅓ **is** 1332 Hz; pin 11 is an output driven by the 4040's `Q10`) · the timing chain belongs
to the **MC14521**, not the 4040.

---

## 6. ✅ The Helipot is electrically OFF this board — 24 August 2026

**Matt, on the bench:** all three Helipot leads run directly to the Pico, and **nothing else
is connected to the pot**. It is held to Board 2 by a **brass nut and washer** only.

So Board 2's role in the Pico build is exactly two things: **the touch sensor, and a bracket
for the pot.**

⚠ **Do not disturb the brass nut and washer.** The touch electrode is a bent copper tab
beside that bush, and the sensitivity depends on what the bush and shaft are electrically
tied to. No ground strap, no steel replacement, no cleaning under the washer. If touch
behaviour changes after the tower is reassembled, that hardware is the first suspect.
