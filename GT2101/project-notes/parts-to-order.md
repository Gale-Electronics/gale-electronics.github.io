---
layout: bare
title: "GT2101 — Remora — Parts List"
permalink: /GT2101/project-notes/parts-to-order/
description: "What the GT2101 Pico controller build needs, and what each item unblocks."
---

*A working note — part of the GT2101 project's live record, written as the work happens and including the wrong turns. The polished write-ups live in [Technical Notes](/GT2101/technical-notes/).*

---

# GT2101 — parts to order

**Written 22 August 2026.** Nothing had been ordered as of this date, despite earlier
notes describing work as "waiting on the parts order". The original
`GT2101_parts_to_order.md` referenced in `gt2101_pico_controller.md` does not exist in
the project — this replaces it.

**Amended 22 August 2026, after the Board 4 study** — the tacho level-shifter changed
from a PNP to a JFET. See ⚠ below.

**Amended 24 August 2026, after bench session 5** — the auto-lock resistor is far less
fussy than recorded, and a **Pico W** is added. Still nothing ordered.

## ✅✅ ORDERED — 4 September 2026, awaiting delivery

**This supersedes every "nothing has been ordered yet" line in the repo**, which had stood
since 22 August. The parts are for a **perfboard interface card**: the dividers, level
shifters and JFET front-end that let the Pico read what each original board is doing on the
backplane, and intervene later if that turns out to be worth doing.

❓ **What is actually in the box has not been logged.** When it arrives, check the contents
against the list below **before anything goes on the perfboard** — the list has been amended
three times and at least one item on it (the 22 k/10 k divider) has since been superseded by
the corrected row in the resistor table below.

---

## ⚠ Nothing here blocks the current bench work

Board 1 runs at 5 V off the Pico's USB supply, and the Helipot is passive. The display,
the pot, and joining the two together need **no parts at all** — all three are now proven
working. This list is for standalone running, the 10 V installation, and the drive/tacho
work that comes after.

---

## The list

### Resistors — the single most useful item

**E12 assortment, ¼ W metal film, 1%.** Everything below needs them, and three separate
jobs are currently held up for want of one resistor:

| Value | What it's for |
|---|---|
| 100 kΩ | Board 1 pin 10 (RESET) into a Pico input — **unblocks display auto-lock** |
| 10 kΩ ×2 | the tacho JFET inverter — one drain pull-up to 3V3, one gate series |
| 10 kΩ | RC filter for the speed voltage out (×2) |
| 1 MΩ | capacitive touch sensing on the Pico, if the original tab is reused |
| **27 kΩ + 10 kΩ + 1 kΩ** | divider for Board 2 pin 5, the 0 → +10 V touch pulse, into a GPIO. ⚠ **Corrected 4 Sept 2026 — this row said 22 kΩ + 10 kΩ.** 27k/10k gives 2.70 V from a 10 V rail; 22k/10k gives 3.13 V, which works but leaves almost no margin. The 1 kΩ goes in series at the Pico end |
| 1 kΩ–4.7 kΩ | transistor bases throughout |

⚠ **The auto-lock resistor is not critical — 24 August 2026.** The 100 kΩ figure has been
quoted as if it were a requirement. It is not: the resistor exists only to limit current
into the Pico input's clamp diode when the board's 5 V `RESET` output goes high, and
**anything from about 47 kΩ to 470 kΩ does the job**. If one is already in the drawer, the
auto-lock job is not blocked at all. Worth checking before ordering anything.

### Transistors

- **NPN ×20** — BC547 or 2N3904. Five level-shift circuits up to 10 V (`F DISPLAY`,
  `F REF`, gate, `BLANK`) plus the green LED low-side driver.
- **⚠ N-channel JFET ×5 — J113** (2N5457 or BF245 also work). **This is the tacho input
  inverter, and it must be a JFET.**

  The tacho swings **0 V to −10 V**. A JFET conducts at V_gs = 0 and pinches off at −10 V,
  so it inverts cleanly: gate to `TACH`, source to GND, drain pulled up to 3V3 through
  10 kΩ, drain straight to a Pico pin. Two parts, no divider, nothing else.

  **This is Gale's own circuit** — an E113 in exactly this configuration is the tacho
  front-end on Board 4, and sheet 3A records a defective E113 on Board 3 being *"replaced
  by J113 (RS Components)"*. The substitution is already proven in this deck.

  ⚠ **Not a MOSFET.** A 2N7000/BS170 needs a *positive* gate voltage, so with a signal
  that only ever sits at 0 V or −10 V it would stay off in both states and never switch.

  ⚠ **Not the PNP circuit** described in earlier notes ("22k base series, 100k to GND,
  emitter 3V3"). With the base at 0 V *and* at −10 V both well below a 3.3 V emitter, that
  PNP is forward-biased in both states and its output sits high permanently. It cannot
  work. **PNPs are no longer needed for anything on this list.**

### ⭐ Raspberry Pi Pico W — added 24 August 2026

**Buy one, keep the plain Pico as the spare.** Matt's idea, 24 August: watch the deck live
on a page served on the home network.

- ✅ **Drop-in.** GP numbering is identical, and none of the four wires in use (GP2, GP3,
  GP4, GP26) clash with the wireless chip. No rewiring, no config change.
- ⚠ **GP23, GP24, GP25 and GP29 belong to the wireless chip** on a Pico W, and the on-board
  LED moves to `Pin("LED")` rather than GP25. Nothing in this project uses those pins, but
  do not assign them later without checking.
- ⚠ **Power.** WiFi adds roughly 50 mA average with much larger bursts. The LM7805 copes,
  but it is more heat to shed — decide the heatsink after this is fitted, not before.
  ⭐ **Easier than it was:** since 3 September the 7805 runs from **+10 V**, not +15 V, so it
  drops 5 V instead of 10 and dissipates half as much. Even at a Pico W's ~50 mA that is
  ≈0.25 W — about what the plain Pico cost on the old +15 V input.
- The monitor is only worth writing **once the tacho is read**; until then the page has
  nothing to show that the bench does not already show. See [`pico-controller-notes.md`](/GT2101/project-notes/pico-controller-notes/)
  § LIVE MONITOR.

A **Pico 2 W** (RP2350) is the faster alternative and would give the servo loop more
headroom, at slightly higher cost. Either is fine; the plain Pico W is proven with
MicroPython and is the safe choice.

### Op-amp

- **LM358, DIP-8, ×5** plus DIP sockets. Buffers the Pico's filtered PWM into the
  speed-voltage line. Runs happily on the single +15 V rail.

### Capacitors

- **1 µF ×10** — the two-stage RC on the speed output
- **100 nF ×20** — decoupling, always wanted, always missing

### Touch — buy the cheap insurance

- **TTP223 modules ×5.**

Still undecided whether the original touch sense gets kept. Three options are open: keep
Board 2 powered and read its 555 output; keep the original bent-tab electrode but sense
it on a Pico pin with a 1 MΩ resistor; or use a TTP223. The modules cost almost nothing,
so buy them regardless and decide later — though [`board-2-touch.md`](/GT2101/project-notes/board-2-touch/) has now confirmed the
touch sensor on the drawings, and reading Board 2's pin 5 pulse through a divider is
looking like the cheapest option of the three.

### Build materials

- **Breadboard**, half-size or larger
- **Jumper wire kit**, male-male and male-female
- **Stripboard / Veroboard** for the final build — ⭐ **this is the perfboard interface card
  ordered on 4 September**, the one place all the dividers, level shifters and the JFET
  front-end live, so that no original board and no backplane pad carries a component
- **DMM grabber test clips** — there's a lot of continuity-buzzing ahead and croc clips
  keep slipping off 50-year-old edge fingers
- **Heatsink for the LM7805** — sized after the display and WiFi current are measured, not
  before. ⭐ **Probably not needed at all now:** on the +10 V input the regulator dissipates
  ≈0.13 W at the plain Pico's ~25 mA, and it has been running in the tower without one

---

## What earlier work removed from the list

**Board 3 level shifters — not needed.** Board 3 (`GT201/3275ST`) is out of the
architecture. Its two jobs — generating `F VAR` from the pot, and gating the drive
voltage to 0 V when the platter is still — both become firmware. Nothing on its nine-pin
connector needs interfacing to the Pico.

**Board 4 level shifters — not needed either.** Board 4 (`GT201/3276ST`) is the other
half of the same servo and leaves with Board 3 — see [the board 4 study](/GT2101/technical-notes/board-4-servo/). Its crystal,
reference divider, PLL and error amplifier all become firmware.

**But Board 4's departure adds one part.** Its E113 JFET is the deck's tacho front-end,
and it goes out with the board — which is why the J113 above is now a **required**
purchase rather than an optional one.

**Helipot parts — none, ever.** Passive, proven on the bench, reads on GP26 with no
conditioning of any kind. ✅ Ten turns, full 160–65535 ADC span, confirmed 24 August 2026.

---

## Still to decide before the final build

- Whether the original touch sense is kept, and in which form
- ~~Whether the Pico is powered from the tower (its own 7805 off the +15 V reservoir) or stays
  on USB~~ — ✅✅ **settled 3 September 2026: from the tower.** The **LM7805** is fed from
  **board 5 pad 2 (+10 V) and pad 9 (GND)** — not the reservoir — and lives in the void at the
  bottom of the tower stack. See [`pico-controller-notes.md`](/GT2101/project-notes/pico-controller-notes/) § POWER
- Whether the WiFi monitor becomes part of the finished deck or stays a bench instrument
- The bracket that carries the Pico inside the tower — it locates on the boards either side
  of the flexicon and must straddle the film with guaranteed clearance. ❓ The ~12 mm gap is
  still unmeasured, and nothing is printed until that number exists
