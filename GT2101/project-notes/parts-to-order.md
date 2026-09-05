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

### ✅ What was actually ordered — logged 4 September 2026

Ten line items, all placed 2 September, all AliExpress, all awaiting delivery. ~£29.

| Item | Variant | On the list? |
|---|---|---|
| **BC547B** TO-92 transistors | 100 pcs | ✅ wanted ×20 |
| **LM358P** op-amp, DIP-8 | 20 pcs | ✅ wanted ×5 |
| **DIP-8 IC sockets** | 10 pcs | ✅ |
| **TTP223** capacitive touch modules | 20 pcs | ✅ wanted ×5 |
| **Prototype board**, double-sided | 5 pcs, 5×7 cm | ✅ **the interface card** |
| **Monolithic ceramic capacitors**, 50 V | **1 µF**, 100 pcs | ✅ wanted ×10 |
| Round-hole pin header strips, 1×40 | **male**, gold | ➕ not on the list |
| **Kapton polyimide tape**, 33 m × 50 mm × 0.06 mm | brown | ⭐ not on the list — see below |
| Solder, 60/40 leaded, 0.8 mm, 50 g | — | ➕ |
| Desoldering braid, 2 mm × 1.5 m | 2 pcs | ➕ |

### ⚠⚠ What is missing — and the perfboard cannot be populated without it

**Every active device arrived. Almost none of the passives did.**

| Missing | What it blocks |
|---|---|
| ⚠⚠ **J113 JFET** | **The tacho, entirely.** Not a divider, not a MOSFET — see below. Nothing substitutes |
| ⚠⚠ **E12 resistor assortment** | **Nearly everything.** The BC547s need base resistors; the LM358 needs its 10 k RC pair and its 10 kΩ output pull-down; the touch input needs 27 k + 10 k + 1 k; the tacho JFET needs 10 k ×2; auto-lock needs one 47 k–470 k |
| ⚠ **100 nF** | Decoupling. The 1 µF variant was ordered from a listing that also offered 47 nF and 100 pF, so this slipped through |
| Female round-hole headers | Only **male** strips were ordered. To plug the Pico into the card rather than solder it down — which is what reversibility wants — the female counterpart is needed |
| Breadboard · jumper wires · DMM grabber clips | Bench convenience, not blocking |

⭐ **So the order is back-to-front against the work.** The chips can wait; the resistors cannot.
**One E12 assortment and five J113s unblock the entire build**, and both are pennies.

### ⭐ The Kapton tape was not on the list and is the most useful thing in the order

33 m of 50 mm polyimide at 0.06 mm. It is **the same material as the flexicon's own coverlay**,
it insulates, it takes soldering heat, and it is thin enough to add no bulk.

**Its immediate job:** a shim between the Pico's solder side and the backplane film. At present
the Pico's castellations sit directly against copper on the film's outer face — the green LED
trace runs up the centre of it — with only a fifty-year-old coverlay between them. See
[`flexicon-backplane-map.md`](/GT2101/project-notes/flexicon-backplane-map/) §7.

⚠ **One caution on the BC547 pack.** The listing title spans several types including
**2N7000**. If the pack turns out to be mixed rather than all BC547B, note that the 2N7000 is
specifically the part that **cannot** work as the tacho input — a MOSFET needs a positive gate,
and the tacho only ever sits at 0 V or −10 V, so it would be off in both states.

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
  nothing to show that the bench does not already show. ⚠ *This pointed at
  `pico-controller-notes.md` § LIVE MONITOR until 5 September 2026. **There is no such
  section** — the monitor has never been specified anywhere in the repo. If it is wanted, it
  needs writing.*

A **Pico 2 W** (RP2350) is the faster alternative and would give the servo loop more
headroom, at slightly higher cost. Either is fine; the plain Pico W is proven with
MicroPython and is the safe choice.

### Op-amp

- **LM358, DIP-8, ×5** plus DIP sockets. Buffers the Pico's filtered PWM into the
  speed-voltage line. ⚠ **Run it from the backplane's +10 V — corrected 5 September 2026.**
  This said "+15 V", which disagrees with
  [`pico-controller-notes.md`](/GT2101/project-notes/pico-controller-notes/), and +15 V means
  a wire across the deck to the reservoir — the exact thing the 3 September supply change got
  rid of. It also needs a **10 kΩ pull-down on its output**, so idle is 0 V by hardware even
  if the PWM stops.

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

⚠⚠ **Corrected 5 September 2026 — the three paragraphs that stood here were written under
the withdrawn remove-the-boards plan.** They said board 3 was *"out of the architecture"*,
that board 4 *"leaves with Board 3"*, and that the J113 was needed because board 4's E113
*"goes out with the board"*. **All five boards stay** — settled 29 August 2026. See
[`project-memory.md`](/GT2101/project-notes/project-memory/) § settled.

⭐ **The J113 is still required, and the quantity is unchanged — only the reason was wrong.**
Board 4 stays, so its E113 tacho front-end stays with it. But that front-end feeds *board 4's
own PLL*, not the Pico. The Pico taps `TACH` in parallel at the backplane (row 4 pad 5) and
needs a front-end of its own. Same part, same circuit, same count.

⚠ **And "no level shifters for boards 3 and 4" is no longer true either.** Both boards are
live, and their pins carry signals the Pico wants to **read**: board 3 pin 7 (the drive
voltage — the calibration prize), board 3 pin 5 (`F VAR`), board 4's `TACH`. A 0–10 V pin
needs a divider into an ADC; `TACH` needs the JFET. Nothing here is decided, but the parts
count for reading the original servo has never been worked out and should be before the
perfboard is laid out.

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
