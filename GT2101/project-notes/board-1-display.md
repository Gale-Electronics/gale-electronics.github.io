---
layout: bare
title: "GT2101 — Board 1 — Display (3155ST)"
permalink: /GT2101/project-notes/board-1-display/
description: "Full working study of the GT2101's display board: parts, connector pin map, counting cycle, and the bench sessions that drove it from a Pico."
---

*A working note — part of the GT2101 project's live record, written as the work happens and including the wrong turns. The polished write-ups live in [Technical Notes](/GT2101/technical-notes/).*

---

# GT2101 Board 1 — Display board (Gale 3155ST)

**Studied 21 August 2026** from three drawings — `GaleTT1Layout.pdf`, `GaleTT1ASchem.pdf`
(sheet 1A), `GaleTT1BSchem.pdf` (sheet 1B) — and from sharp photographs of both sides of a
spare board, taken the same day.

**Updated 24 August 2026** after bench session 6 — **the Pico now lights the board's green
LED** (§6b), and the long-standing "no driver transistor needed" claim in §3 is corrected:
it is true on the 5 V bench and **false at the deck's 10 V**.

**Provenance:** the circuit description is 📄, read off hand-traced reverse-engineering
drawings in the same hand and colour conventions as the backplane sheet (FANATSON, 2015).
They are not Gale factory drawings. Anything marked ✅ comes from the photographs of the
board itself and outranks the drawings.

✅ The board is legended **`GT201/3155ST`** on the copper side. That takes the board number
from ❓ (defunct website) to ✅ (read off the part).

---

## 1. What is actually on the board

Five ICs, three transistors for digit select, one for the decimal point, a handful of
resistors and one capacitor. It is a **three-digit frequency counter**: it counts an
incoming frequency for a fixed window and shows the total.

✅ All five part numbers read directly off the parts, 21 August 2026:

| Part on the board | Date code | Job |
|---|---|---|
| **MC14553CP** | 7536 | 3-digit BCD counter with latches + digit multiplexer |
| **MC14511CP** | 7540 | BCD → 7-segment decoder/driver (drives all three digits in turn) |
| **MC14011CP** | 7533 | Quad NAND — gates the incoming frequency; makes latch-enable |
| **MC14013CP** | 7545 | Dual D flip-flop — divides `F REF` to make the latch/reset timing |
| **MC14001CP** | 75-41 | Quad NOR — makes the reset pulse, delayed after the latch pulse |
| **3 × TIS61 PNP** | — | Digit-select drivers (the three digit commons) |
| **1 × BC214 PNP** | — | Decimal point driver |

All five ICs are Motorola. **The date codes run 7533 to 7545 — weeks 33 to 45 of 1975** — so
this board was built at the end of 1975 or very early 1976. ✅ That is a firmer date than
"late 1970s" and worth putting in the archive.

There is also a paper sticker on the component side reading **"OK NOV 81"** with what looks
like *"Workshop"* and a name — possibly *Reg* — written sideways beside it. 📄 A service
note: someone tested this board and passed it in November 1981.

**Condition.** ❓ The copper side shows green corrosion in two or three patches and a
brown, scorched-looking area near one edge. Probably old flux rather than damage, but worth
a clean with isopropyl and a look under a light before this board is powered.

The LED display itself sits on the board at the opposite edge from the connector — the
zig-zag double row of pads at the top of the layout photo.

**The decimal point is hardwired.** The BC214 is driven from one of the digit-select
lines, so the point always lands in the same place. The board can only ever show `NN.N`.
That is why 1332 Hz reads "33.3" and not "333".

**No resistor values are given anywhere on either sheet.** The tracer drew the boxes but
never wrote the values. If we need them they have to be measured on the spare board.

---

## 2. The connector — 8 signals

The numbers below are the **yellow numbers the tracer wrote on both the layout and sheet
1A**. They are consistent between the two drawings, and they match the six Board 1
signals already in [`flexicon-backplane-map.md`](/GT2101/project-notes/flexicon-backplane-map/) — plus two the backplane sheet did not
name (`RESET` out, and the pin numbers themselves).

| # | Signal | Direction | Goes to / comes from | Lands on Board 1 at |
|---|---|---|---|---|
| 1 | **+10 V** | in | PCB 5 | 4553 pin 16, 4511 pin 16 |
| 2 | **START/STOP LOW PULSE** | in ← PCB 2 | blanks the display | 4511 pin 4 (`BL`, active low) |
| 3 | **F DISPLAY** | in ← PCB 2 | the frequency being counted | 4011 pin 13 |
| 4 | **~1 Hz gate** *(tracer wrote "1Hz?")* | in ← PCB 2 | opens/closes the count window | 4011 pins 1+2 |
| 5 | **GREEN LED** | out → PCB 5 | front-panel green LED, cathode side | LED cathode |
| 6 | **RESET** | out → PCB 2 | Board 1 sends its reset pulse *out* to PCB 2 | 4001 pin 10 |
| 7 | **F REF** | in ← PCB 4 | clocks the latch/reset timing | 4013 pin 3 (`CL1`) |
| 8 | **GND** | in | PCB 5 | 4553 pin 8, 4511 pin 8 |

⚠ **1–8 are the tracer's signal index, not a pin count.** The connector is a row of **19
hole positions with only 12 pins fitted**, and the eight labelled signals sit on eight of
those twelve. Section 2a maps them to physical pins.

---

## 2a. The connector, physically — solved from photographs

✅✅ **CONFIRMED ON HARDWARE, 21 August 2026.** Derived by measuring photographs of both
sides of a spare board against the layout drawing — the pin pattern is a fingerprint and it
matched exactly — then **verified on the board with a meter**: all three checks in section 6
beeped as predicted. This table now outranks the drawings.

**Orientation.** The legend `GT201/3155ST` is printed on the **copper** side and reads
normally there. In `GaleTT1Layout.pdf` it is printed backwards — so **the drawing is drawn
in the component-side orientation** (copper seen through the board). Read the drawing as if
you were looking at the parts.

**The row.** 19 positions on a regular pitch; 12 have pins fitted. Looking at the
**component side, parts towards you, displays at the top**, left to right:

```
position  0 1 2 3 4 5 6 7 8 9 . 11 . . . . 16 17 18
pin?      ● ● ● ● ● ● ● · · ●  ·  ● ·  ·  ·  ·  ●  ●  ●
tracer's  1   2     3 4     5                  6  7  8

          |___ group of SEVEN ___|   ·   ·        |_THREE_|
                                  lone  lone
```

So, counting only the **pins you can actually see**, left to right on the component side:

| Pin (of the 12 fitted) | Tracer's # | Signal |
|---|---|---|
| 1 — first of the group of seven | 1 | **+10 V** |
| 2 | — | *unidentified* |
| 3 | 2 | **BLANK** (start/stop low pulse) |
| 4 | — | *unidentified* |
| 5 | — | *unidentified* |
| 6 | 3 | **F DISPLAY** |
| 7 — last of the group of seven | 4 | **gate (~1 Hz?)** |
| 8 — the first lone pin | 5 | **GREEN LED** |
| 9 — the second lone pin | — | *unidentified* |
| 10 — first of the group of three | 6 | **RESET out** |
| 11 | 7 | **F REF** |
| 12 — last pin on the board | 8 | **GND** |

From the **copper** side the whole row mirrors: the group of three is then on the **left**,
reading GND, F REF, RESET; and +10 V is the very last pin on the right.

**Three independent checks that this is right:**

- ✅ The green LED sits **directly above pin 8**, the first lone pin — which is exactly the
  signal the drawing calls `LED GRÜN`.
- ✅ In the layout drawing the pad the tracer numbered 1 is circled in **red**, his colour
  for +10 V throughout all these sheets.
- ✅ The pad he numbered 8 is highlighted **yellow** and runs into the board's widest copper
  area — the ground pour.

❓ **Four fitted pins are unaccounted for** (pins 2, 4, 5 and 9 in the table). They have
pins soldered in, so they carry something. The tracer never labelled them. Worth a beep
test one day, but nothing on the Pico plan depends on them.

---

**Two things the earlier project note got slightly wrong**, now corrected:

- `F DISPLAY` does **not** go to the MC14553 directly. It goes to the 4011 first and
  reaches the 4553 clock only through gate D.
- Board 1 has an *output* on the connector besides the LED: `RESET` to PCB 2. The tower's
  display board is a timing source for PCB 2, not purely a slave.

---

## 3. How it works — signal chain

```
                                          +10V
                                            |
                                          [R]                (pull-up)
   pin 2  START/STOP LOW PULSE  ------------+--------------> 4511 pin 4  BL
            (low = display blanked; open-circuit = display ON)

   pin 3  F DISPLAY  --+--[R]--GND
                       |
                       +-------------------> 4011 D pin 13 ---.
                                                              |  NAND
   pin 4  ~1 Hz gate  -----> 4011 A (pins 1+2 tied) --pin 3--> 4011 D pin 12
                             (used as an inverter)            |
                                                              '--pin 11--> 4553 pin 12  CLOCK

   pin 7  F REF  -----------> 4013 CL1 (pin 3)
                                 |
                                 +--> 4011 C (pins 8,9) --pin 10--[R]--> 4553 pin 10  LATCH ENABLE
                                 |
                                 +--> 4001 C (pins 8,9) --pin 10--+----> pin 6  RESET out to PCB 2
                                                                  |
                                            [R] + 470n(?) to GND --+
                                                     |
                                              4001 B (inverter)
                                                     |  [R]
                                              4001 A (inverter)
                                                     |  [R]
                                                     '-----------> 4553 pin 13  RESET

   4553 Q0..Q3 (pins 9,7,6,5) --> 4511 A,B,C,D (pins 7,1,2,6)
   4511 a..g   (pins 13,12,11,10,9,15,14) --> display segments
   4553 DS1,DS2,DS3 (pins 2,1,15) --> 3 × TIS61 --> the three digit commons
                                  \--> BC214 --[R]--> decimal point
```

**Gate polarity.** 4011 D output = NAND(`F DISPLAY`, NOT `gate`). So:

- gate **LOW** → the clock passes → **the counter counts**
- gate **HIGH** → output stuck high → counting stopped

✅ Settled on the bench 21 August 2026 — counting happens while the gate is LOW.

**Latch/reset sequence.** The 4013 divides `F REF`; one output makes the latch-enable
pulse (via 4011 C) and the other makes the reset (via 4001 C). The reset then goes through
an RC delay and two NOR inverters before reaching the 4553 — that delay is deliberate, so
the value is safely latched into the display *before* the counter is cleared. Classic
frequency-counter housekeeping.

❓ The exact 4013 wiring is the least legible part of sheet 1A — the pen scribbles over
`D1`/`CL2`. The *shape* of the circuit is clear; which flip-flop feeds which gate is not.

**Blanking.** 4511 pin 5 (`LE`) is tied to GND, so the decoder is always transparent — the
only blanking control is pin 4 (`BL`), fed from connector pin 2, with a pull-up to +10 V.
✅ useful consequence: **leave pin 2 unconnected and the display stays lit.**

**Common cathode.** The 4511 sources segment current and the three TIS61s pull the digit
commons down to GND, and the decimal point is sourced from +10 V through the BC214. That
all points to a **common-cathode** display. ❓ inferred from the drawing; confirm with a
meter in diode mode.

### Green LED — and a correction, 24 August 2026

Anode to +10 V, cathode straight out to connector pin 5 (physical pin 8). Sheet 1A draws no
series resistor — but ✅ the photograph shows a **resistor standing vertically directly
above the LED**, its lower lead going into the pad beside it, and the LED itself sitting
immediately above its own connector pin. So the series resistor is on Board 1 and sheet 1A
simply omitted it.

✅ **Measured 21 Aug 2026: 966 Ω in circuit — so a 1 kΩ resistor.** With a green LED of that
era dropping about 2 V, that gives **≈ 8 mA at the deck's +10 V**, and about 3 mA on the 5 V
bench.

⚠ **Earlier versions of this page said "a Pico pin can sink pin 8 directly — no driver
transistor needed." That is true on the bench and FALSE in the deck**, and the difference
is the *off* state, not the on state:

| Supply | Sinking (LED lit) | **Not** sinking (LED out) |
|---|---|---|
| 5 V bench | ~3 mA. Fine | the pin floats to 5 − 2 = **3 V**. Below 3.3 V, nothing conducts. Fine |
| 10 V deck | ~8 mA. Fine | the pin is pulled toward **8 V** through 1 kΩ. The Pico's internal clamp diode conducts and dumps ~4 mA into its own 3V3 rail — continuously, and from the instant the deck is switched on, before the firmware has booted |

**So the 10 V installation needs the low-side NPN** that [`parts-to-order.md`](/GT2101/project-notes/parts-to-order/) has
always listed for it. The two documents disagreed; the parts list was right.

```
   GP5 ──[4k7]── B
                   NPN (BC547 / 2N3904)
   Board 1 pin 8 ── C
             GND ── E
```

With the transistor the sense inverts: **GPIO high = LED lit**, unlike the three display
lines, which the level shifters invert the other way.

---

## 4. What number appears

The counter counts `F DISPLAY` for as long as the gate is open, then shows the total with a
fixed decimal point:

```
displayed = (count) / 10        e.g. count 333  ->  "33.3"
```

With `F DISPLAY` = 1332 Hz at 33⅓ rpm (📄 backplane sheet), a count of 333 needs a window
of **333 / 1332 = 0.25 s**, not 1 s.

❓ So either the tracer's "1Hz?" is a 1 Hz *repetition rate* with a 250 ms open window, or
the frequency relationship is different from what the backplane sheet says. This is the
single biggest unknown left on Board 1 — and the good news is that **it stops mattering
the moment the Pico owns the gate**, because then we set the window.

---

## 5. What this means for the Pico

This is the useful part. Board 1 needs **four wires from the Pico plus power** — five with
the green LED — and the Pico then owns the display completely: no board modification,
nothing unplugged, all original parts.

| Pico → | Board 1 pad | Physical pin | Why |
|---|---|---|---|
| output | 3 — `F DISPLAY` | 6 | the pulses being counted |
| output | 4 — gate | 7 | opens/closes the count window |
| output | 7 — `F REF` | 11 | clocks the 4013, i.e. **commands latch + reset** |
| **open-drain / NPN** | **5 — GREEN LED** | **8** | ✅ **working, bench session 6.** See §3 and §6b |
| output (optional) | 2 — `BLANK` | 3 | blank the display; leave open = always on |
| input (planned) | 6 — `RESET` out | 10 | auto-lock. **Never drive this pin** |
| — | 1 — +10 V (5 V on the bench) | 1 | supply |
| — | 8 — GND | 12 | supply |

Because the Pico drives pin 7 as well as pins 3 and 4, it does not need to *synchronise*
with the deck's timebase — it *is* the timebase. The whole counting cycle becomes a
deliberate four-step sequence rather than a free-running measurement:

```
show(333):
  1. gate HIGH                 stop counting
  2. pulse F REF               latch what's there, then the RC delay clears the counter
  3. gate LOW                  open the window
  4. send 333 pulses on F DISPLAY   (a few kHz — 333 pulses at 20 kHz is 17 ms)
  5. gate HIGH                 close the window
  6. pulse F REF               latch the new 333 into the display
  ... repeat a few times a second
```

That is a completely different shape of code from anything written so far. The old
`display.py` assumed we had to *emit a frequency* and let the deck's own gate measure it —
which meant the Pico had to know the window length and get it exactly right. **Sending a
counted number of pulses and then commanding the latch removes that whole class of error.**
It also means the displayed value is exact by construction: no rounding, no window drift,
no dependence on the "1 Hz?" mystery.

Fallback if the 4013 chain turns out to be awkward: hold the gate open permanently and
send `F DISPLAY` as a true frequency, letting the deck's own `F REF` do the timing — i.e.
the Pico pretends to be PCB 2. That works too, but it depends on knowing the window, so it
is second choice.

⚠ **When this moves from the 5 V bench to the 10 V deck, the three display drives go
through NPN level shifters, and a common-emitter NPN INVERTS.** `GATE_COUNTS_WHEN_LOW`, the
`F REF` pulse polarity and the `F DISPLAY` pulse shape all flip. Decide that deliberately —
either invert in `config.py` or use two transistors per line — rather than meeting it as a
surprise when the digits come up wrong.

---

## 6. Bench session 1 — DONE ✅ 21 August 2026

All three checks beeped as predicted, and the resistor above the green LED measured 966 Ω.
The pin map is confirmed. The rest of this section is kept as the record of how it was done.

---

The photographs did the discovery job, so this is now a **confirmation**, not a hunt. Three
beeps and it's done. Nothing is powered, nothing is soldered, the Pico is not involved.

**Goal: prove the pin map in section 2a on your own board.** One meter, continuity setting
(the one that beeps).

Hold the board **component side towards you, displays at the top**. The connector row runs
along the bottom: a group of seven pins, two lone pins, then a group of three at the
right-hand end.

### First: how to find leg 1 on a chip, without counting

Legs are numbered **anticlockwise seen from the component side**, starting at pin 1. Laid
out flat with the marked end to the left, a 16-pin chip goes:

```
        16 15 14 13 12 11 10  9      <- top row, numbers run RIGHT to LEFT
       ┌───────────────────────┐
       (  mark      MC14511CP  │
       └───────────────────────┘
         1  2  3  4  5  6  7  8      <- bottom row, numbers run LEFT to RIGHT
```

Two facts fall out of that, and they are all you need:

- **Pin 1 and the highest pin face each other across the narrow end.** (16 on the 4511 and
  4553; **14** on the 4011, 4001 and 4013, which are 14-pin chips.)
- **The two lowest-numbered legs at the other end are the middle pair** — 8 and 9, or 7 and
  8 on a 14-pin chip.

⚠ **Do not trust the round dots.** These Motorola packages have several circular moulding
dimples that look exactly like a pin-1 dot — the 4011 on your board has at least three. Use
the meter instead:

**On every one of these five chips, the highest-numbered pin is +10 V and the pin
diagonally opposite it is GND.** So:

1. Meter on continuity. One probe stays on the **last connector pin at the right-hand end**
   (the one section 2a says is +10 V).
2. Touch the other probe to each of the chip's **four corner legs** in turn.
3. Exactly one beeps. That leg is the highest-numbered pin — 16 on the 4511, 14 on the 4011.
4. **Pin 1 is the leg straight across the body from it.** GND is the one diagonally opposite.

Now count along the row from pin 1 whenever you need a numbered leg.

### Then: the three checks

| Check | One probe on | Other probe on | Expect |
|---|---|---|---|
| 1 | the **last connector pin on the right** | the four corner legs of the 4511 | exactly **one** beeps → that connector pin is +10 V and that leg is 16 |
| 2 | the **first lone pin** (just right of the group of seven) | either leg of the green LED | beep — this is the LED pin |
| 3 | the **last pin of the group of seven** | 4011 leg 1 (found by the method above) | beep — this is the gate |

---

## 6a. Bench session 2 — DONE ✅ 21 August 2026

**A Raspberry Pi Pico put `12.3`, `45.0`, `78.0` and `33.3` on this 1975 display, on
demand, with the board otherwise entirely original.** What the session established:

- ✅ **Gate polarity: counting happens while the gate line is LOW**, exactly as sheet 1A
  implied. `GATE_COUNTS_WHEN_LOW = True`.
- ✅ **The 4013 runs a four-state cycle**, one state per `F REF` pulse, measured by stepping
  pulses one at a time and reading the display:

  | state | what happens |
  |---|---|
  | 1 | **LATCH** — the counter value is captured and appears |
  | 2 | hold |
  | 3 | **RESET** — counter cleared, **and the digits go dark** |
  | 4 | hold |

- ✅ **The reset is a state, not a pulse.** While the 4013 sits in state 3 the 4553's reset
  is held down and the counter cannot count at all. Anything loaded during that state is
  thrown away and the display comes up `0.0`. The driver must step out of reset *first*,
  then load. This cost an hour and is the single most important thing on this page.
- ✅ **The dark state is the landmark.** Since the Pico is the only thing driving `F REF`,
  once it has seen the digits go dark it knows exactly where it is in the lap and stays in
  step indefinitely.

❗ **The phase is lost at every power-down** — the 4013 comes up in a random state and
nothing on the board resets it. So `bench.lock()` has to be run once after each power-up,
with a human watching for the dark state. **The permanent fix is to read the board's own
`RESET` output on connector pin 10** into a Pico input; then the Pico can find the dark
state by itself with nobody watching. That needs one wire and one resistor (anything from
about 47 kΩ to 470 kΩ at 5 V; a divider in the deck at 10 V). **Not yet done.**

---

## 6b. Bench session 6 — GREEN LED ✅ 24 August 2026

**The Pico lights and extinguishes Board 1's green LED on command.** One wire, no
components, board otherwise untouched.

| | |
|---|---|
| Wire | **Board 1 physical pin 8** (the first lone pin, component side, displays at the top) → **Pico physical pin 7 = GP5** |
| Supply | 5 V bench, Pico on USB, display wiring from session 2 left in place |
| Parts added | **none** |

```python
import time
from machine import Pin
led = Pin(5, Pin.OPEN_DRAIN, value=1)   # 1 = out, 0 = lit
for _ in range(20):
    led.value(0); time.sleep(0.5)
    led.value(1); time.sleep(0.5)
```

### Three things this session established

1. ✅ **`OPEN_DRAIN`, not `OUT`.** The pin must either pull to ground or let go completely;
   it must never drive high. Driving high would put the LED's supply into the Pico once
   this moves to the 10 V deck. Writing it open-drain from the start means the same line of
   code survives the move.
2. ✅ **The net is free at the Pico end** — grounding pin 8 by hand lights the LED, so
   nothing else is holding it. ⚠ This does **not** clear Board 5, which is not in the bench
   chain. See §7.
3. ⚠ **Running the four REPL lines back-to-back shows nothing** — the LED lights for
   microseconds. This looked like a dead circuit and was not. Any future bench step that
   toggles an output needs a delay or a loop, and this page should say so before someone
   loses an evening to it.

⚠ **Type it in Thonny's Shell pane, not the editor.** The green play button reboots the
Pico and throws away the display's phase lock. Ctrl-C to break the loop.

### To make it permanent

```python
# config.py
GREEN_LED_PIN    = 5
GREEN_LED_DIRECT = True   # True  = Pico sinks it, open-drain  (5 V bench)
                          # False = via NPN low-side driver, active high (10 V tower)
```

**What it should indicate** is still open. The obvious use is a lock indicator: out when stopped, flashing through the
4 s soft-start ramp, steady once the tacho says the platter is within tolerance. That also
makes the servo visible during the tacho bring-up, which is the next subsystem.

---

## 7. Open questions

| ❓ | Why it matters | How to settle it |
|---|---|---|
| ~~Gate active-low vs active-high~~ | ✅ **Settled: counts while the gate is LOW.** | — |
| ~~How many `F REF` edges per latch/reset~~ | ✅ **Settled: a four-state cycle — latch, hold, reset, hold.** | — |
| ~~Whether `LE` on the 4553 latches on high or low~~ | Moot — we drive the board's own 4011 C, not the 4553 directly | — |
| **Phase is lost at power-down** | `bench.lock()` needs a human every power-up | Wire connector pin 10 (`RESET` out) into a Pico input |
| ~~Value of the LED series resistor~~ | ✅ **Settled: 1 kΩ, ≈8 mA at 10 V.** | — |
| ~~Can the Pico drive the green LED~~ | ✅ **Settled 24 Aug: yes, open-drain on GP5.** | — |
| **Does Board 5 ground the green LED net?** | If it does, the LED is permanently lit in the assembled tower and the Pico cannot switch it. The bench cannot answer this — Board 5 is never in the bench chain | Beep test in the tower, unpowered: Board 1 pin 8 to deck GND. **Silence = free** |
| What it should indicate | Free feature, no decision yet | Lock indicator is the obvious use |
| What the four unlabelled fitted pins carry | Nothing depends on it yet | Beep test, some other day |
| The green corrosion / brown patch on the copper | Could be leakage between tracks | Clean and inspect before powering |
| Resistor values throughout | Only matters if a part is faulty | Measure if needed |
| Exact 4013 wiring | Cosmetic — we drive the chain, not analyse it | Leave open |
| The 250 ms window discrepancy | Only matters for the fallback plan | Leave open |
