---
layout: bare
title: "GT2101 — Backplane Signal Map"
permalink: /GT2101/project-notes/backplane-signal-map/
description: "What travels between the five boards of the GT2101 control tower, board by board and pin by pin."
---

*A working note — part of the GT2101 project's live record, written as the work happens and including the wrong turns. The polished write-ups live in [Technical Notes](/GT2101/technical-notes/).*

---

# GT2101 Backplane Signal Map

What travels between the five boards in the control tower.

**Source:** `GaleTTbackplane.pdf` — a hand-traced drawing titled *"GALE GT2101 BACKPLANE
SOLDER SIDE (TOWER)"*, signed **FANATSON, 12.9.2015**.

**Status: 📄 traced document, third party.** This is someone's reverse-engineering work
from 2015, not a Gale factory drawing.

**Rewritten 22 August 2026.** The individual board studies (`gt2101_board1_display.md`,
`_board2`, `_board3`, `_board4`) have now read each board's own schematic and layout
sheets, which carry **numbered connector pins and circled destination-board numbers** that
the backplane sheet does not. Where they disagree with this drawing, they win — they are
more specific and there are now four of them agreeing with each other.

The drawing is laid out as **five numbered rows, PCB 1 to PCB 5** — independent
confirmation that the tower holds five boards.

---

## The signal chain, as now understood

```
                    1.048 MHz crystal  ──────────────┐
                         (Board 4)                   │
                                                     ▼
   Helipot ──► Board 2 ──► Board 3 XR2207 ──► F VAR ──► Board 2 ──► ×40 ──► Board 5
   (on Bd 2)                                                                  │
                                                        black switch VAR/FIX ─┤
                                                                              ▼
                                          Board 4 pin 3  ◄──── 4×F (40–3996 Hz)
                                                │
                                          ÷4 ───┼───► pin 9 ──► Board 1 pin 7 (F REF)
                                                │
                                                ▼
   motor TACH (0/−10 V) ──► Board 4 E113 ──► 4046 PLL ──► 1747 ──► pin 6
                                    │                                 │
                                    └──► pin 4 INV TACH ──► Board 2    ▼
                                                              Board 3 pin 6
                                                                      │
                                                     STILL/TURNING gate│
                                                                      ▼
                                                              Board 3 pin 7 ──► motor

   touch disc ──► Board 2 555 ──► pin 5 (0→+10 V pulse) ──► Board 3 pin 4 ──► the gate
```

---

## Signals by board

### Board 1 — Display

| Signal | Direction | From/to | Notes |
|---|---|---|---|
| `+10V`, `GND` | in | Board 5 | pins 1 and 8 (tracer's numbering) |
| `BLANK` (start/stop low pulse) | in | Board 2 pin 6 | 0 → −10 V pulse |
| `F DISPLAY` | in | **Board 2 pin 8** | the frequency being counted |
| `~1 Hz` gate | in | **Board 2 pin 10** | ✅ sourced — off the 4040's Q21 (≈0.5 Hz) / Q19 (≈2 Hz) |
| `F REF` | in | **Board 4 pin 9** | ✅ 1×F, 10–999 Hz = 10 × rpm. Clocks the latch/reset chain |
| `RESET` | out | **Board 2 pin 13** | resets Board 2's 4040 |
| `LED GRÜN` | out | Board 5 | the green front-panel LED |

The backplane sheet marked the gate with a question mark; Board 2's sheets answer it.

### Board 2 — Touch start/stop + display timing (14 pins)

| Pin | Signal | Direction |
|---|---|---|
| 1 | `+10 V` | in |
| 2 | 1.048 MHz | in ← Board 4 pin 2 |
| 3, 4 | STILL/TURNING status | in ← Board 3 |
| **5** | **`START/STOP PULSE` HI, 0 → +10 V** | out → Board 3 pin 4 |
| 6 | `START/STOP PULSE` LO, 0 → −10 V | out → Board 1 |
| 7 | `F REF ×40` | in ← Board 4 |
| 8 | `F DISPLAY` | out → Board 1 |
| 9 | `INV TACH` | in ← Board 4 pin 4 |
| 10 | the ~1 Hz gate | out → Board 1 |
| 11 | `1332 Hz FIX` (333 × 40) | out → Board 5 |
| 12, 14 | `−10 V`, `GND` | in |
| 13 | `RESET` | in ← Board 1 |

Also carries the Helipot, physically mounted on this board.

✅ **The touch start/stop signal terminates here**, and leaves as a *pulse* on pin 5 —
confirmed against sheet 2A, which is drawn around an electrode labelled `TOUCH SENSOR`.

### Board 3 — `F VAR` generator + drive-voltage gate (9 pins)

| Pin | Signal | Direction |
|---|---|---|
| 1 | `+10 V` | in |
| 2, 3 | STILL/TURNING status | out → Board 2 |
| 4 | start/stop pulse | in ← Board 2 pin 5 |
| 5 | `F VAR` | out → Board 2 |
| **6** | **drive voltage IN** | in ← **Board 4 pin 6** |
| **7** | **drive voltage OUT** | out → the motor |
| 8, 9 | `−10 V`, `GND` | in |

**Drive voltage, both sides of the gate:**

| Condition | Pin 6 (in) | Pin 7 (out) |
|---|---|---|
| **STILL** | **10 V** | **0 V** |
| 33⅓ | 1.2 V | 1.2 V |
| 45 | 1.6 V | 1.6 V |
| 78 | 2.4 V | 2.4 V |

⚠ **The backplane sheet only ever recorded the input column**, which is where the project's
long-standing "STILL = 10 V" came from. That 10 V never leaves Board 3. Read as
**proportional drive with a hard mute at rest**.

### Board 4 — Crystal reference + tacho front-end + servo (9 pins)

| Pin | Signal | Direction |
|---|---|---|
| 1 | `+10 V` | in |
| 2 | 1.048 MHz | out → Board 2 |
| 3 | `4×F` (40–3996 Hz = 40 × rpm) | in ← Board 2 / Board 5 |
| 4 | `INV TACH` (0/+10 V, open drain) | out → Board 2 |
| 5 | `TACH` | in ← the motor. ⚠ **0 V to −10 V** |
| **6** | **drive voltage** | out → **Board 3 pin 6** |
| 7, 8 | `−10 V`, `GND` | in |
| 9 | `1×F` (10–999 Hz = 10 × rpm) | out → Board 1 pin 7 |

⚠ **Board 4 and Board 3 do not share a pinout** — Board 4 has −10 V on 7 and GND on 8;
Board 3 has −10 V on 8 and GND on 9. Never swap a board between slots.

**The 4046 locks the tacho to `1×F`**, with no divider in the loop — so in lock the tacho
runs at **10 Hz per rpm**, i.e. 333 Hz at 33⅓, i.e. **~600 pulses per platter revolution**.

### Board 5 — Power supply + external interface

| Signal | Direction | Notes |
|---|---|---|
| `+10V`, `−10V`, `GND` | out | Rails to the rest of the tower |
| `TACH` | **in** | Arrives from the motor |
| `SPEED OUT ≈1.5V` | **out** | To the motor. Fed from Board 3 pin 7 |
| `F VAR (pot)` | | 3996 Hz, marked ×40 |
| `333Hz ×4 = 1332Hz FIX` | | The fixed 33⅓ path |
| `LED GREEN` | | |

**Black speed switch**, drawn at the bottom of the sheet:

- **VAR — released** → selects `F VAR (pot)`, the Helipot-set speed
- **FIX 33,3 — pressed** → selects the fixed 1332 Hz

The selected frequency then returns to Board 4 pin 3 as `4×F`.

---

## What this settles

**There is no motor power stage in the tower.** The tower's output to the motor is a
low-voltage control signal of about 1.2–2.4 V. The power electronics (BD675A/676A) are on
the separate motor controller PCB. The old archive's `Disk2BPowerDriver.pdf` describes that
PCB and has been misfiled as a tower board.

**The servo lives on Boards 4 and 3, in that order.** Board 4 compares and amplifies;
Board 3 gates. The old description of Board 2 as "Servo Motor Drive" is wrong on both
counts.

**The display maths.** `4×F` = 40 × rpm (1332 Hz at 33⅓) and `1×F` = 10 × rpm (333 Hz).
`F VAR` at 3996 Hz is 99.9 rpm × 40 — the top of the variable range, since the display has
three digits with a fixed point.

---

## Where the Pico connects — SUPERSEDED

This section previously said the Pico's speed voltage injects at Board 5's `SPEED OUT`.
**That was written before Boards 3 and 4 were read.** With both boards out of the
architecture, the Pico takes over **Board 3's slot** and drives the drive-voltage net
directly. See `gt2101_pico_controller.md` for the current wiring plan.

---

## Still open

- What is `R` on the Board 2 row of the backplane sheet?
- Which physical backplane pad each signal corresponds to. The drawing gives positions
  along the backplane, not numbered pins, so each one must be confirmed by continuity
  before anything is connected to it. **The per-board sheets now give pin numbers on the
  boards, which is the easier end to work from.**
- What Board 2 pin 9 did with `INV TACH` — possibly the source of `F DISPLAY`, which would
  mean the display shows measured rather than commanded speed.
