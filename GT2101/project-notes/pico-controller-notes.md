---
layout: bare
title: "GT2101 — Pico Controller — Working Notes"
permalink: /GT2101/project-notes/pico-controller-notes/
description: "The live working record of the GT2101 Pico controller build: architecture, wiring, interfacing, firmware and bench log."
---

*A working note — part of the GT2101 project's live record, written as the work happens and including the wrong turns. The polished write-ups live in [Technical Notes](/GT2101/technical-notes/).*

---

# GT2101 — the Pico controller

**Rewritten 22 August 2026.** The previous version dated from the morning of 20 August,
before the board register and before Boards 1, 2, 3 and 4 were each studied from their own
drawings. Most of its open questions are now answered and several of its statements were
wrong.

**Updated 24 August 2026** after bench session 5 — the Helipot turn count is settled and the
pot now drives the display end to end.

**Updated again 24 August 2026** after bench session 6 — **the Pico drives Board 1's green
LED** (§ BENCH LOG), the "no driver transistor needed" claim in § INTERFACING is corrected,
the Helipot's electrical relationship to Board 2 is settled (§ THE CONTROLS), and the
minimum-intrusion wiring plan is written down for the first time (§ HOW THE PICO MEETS
THE TOWER).

**Updated 4 September 2026** — the supply regulator is corrected (it is the **LM7805**, not a
DC-DC converter), the tower inventory is corrected (§ THE DECK), and **this file is now the
single source for the build detail.**

### ⭐ This file is the build record — 4 September 2026

Until today most of this document also existed, largely word for word, inside
[`project-memory.md`](/GT2101/project-notes/project-memory/): the boards table, the controls,
the drive voltages, the tacho, the whole of interfacing including both schematics, power,
firmware, toolchain and the bench log. **That duplication produced three live contradictions**
— the withdrawn "board 3 is out" alarm, the superseded 22k/10k divider, and a parts-ordered
status that disagreed with itself.

The memory doc has been cut back to a bootstrap and now points here. **Circuit detail,
interfacing, power, firmware and the bench log belong in this file and nowhere else.** The
drive-voltage table's home is
[`board-3-fvar-gate.md`](/GT2101/project-notes/board-3-fvar-gate/); the pad map's home is
[`flexicon-backplane-map.md`](/GT2101/project-notes/flexicon-backplane-map/).

**Scope:** Matt is adding new control logic to the GT2101's control tower using a Pico and
a handful of small parts. Everything else on the deck stays original.

**The replacement controller is out of scope entirely** — it is coming out of the tower and
the original boards are going back in. It is not being reverse-engineered, recloned or dated,
and neither its firmware nor the manufacturing enquiry that went with it is being pursued.

---

## THE DECK

Gale **GT2101**, late-1970s acrylic-plinth turntable. The project folder holds the original
Gale schematic and layout PDFs (TT1–TT5, backplane, motor PCB) plus a parts list.

⚠ **Those PDFs are image-only scans** — a text read returns empty text. That is how Boards
1–4 were worked out: the PDF attached directly to the chat and read visually. ✅ **Since
5 September 2026 that is no longer the only way** — with the
`engineering-drawings-schematics` folder connected, a session can render a sheet to PNG at
~400 dpi and read the pencil annotations directly. That is how the drive-voltage columns and
Board 1's 4013 wiring were settled.

⚠ **They are also not Gale factory drawings.** Every schematic and layout in the archive is
hand-drawn reverse-engineering by one person (FANATSON) in 2015. The typed prose pages are
worse — **all six have now been checked and five were substantially wrong**; the sixth
describes board 5, the one board whose function can be guessed from its parts list. See
[`archive-provenance.md`](/GT2101/project-notes/archive-provenance/).

### ⚠⚠ Which tower — corrected 4 September 2026

**There are two towers, and this section used to assume there was one.** It said "the control
tower currently runs a modern replacement board", as though the deck in use and the tower on
the bench were the same object. They are not.

| | |
|---|---|
| **Howie's tower** | Built by **Howie** with his own PCBs and parts throughout. ⭐ **It is fitted to the working deck and driving it well.** The deck is playable because of it, which is why none of this work is under time pressure. ✅ Its original boards were all kept. It gets restored eventually — modern parts out, its own boards back in, Pico inside |
| **Alex's tower — "the test tower"** | A working original tower from **Alex**. ⭐ **Every bench session and every photograph in this repo is this tower** — the LM7805, the restored flexicon, the display and the green LED. Ready to start testing |

**So nothing is currently being taken out of anything.** The bench work happens on the test
tower precisely so that the restoration target is not the test subject.

⚠ **The boards being tested are Howie's tower's originals**, kept when his build replaced
them. ⚠ **The restored flexicon is Howie's tower's original cable too**, and it is currently
in the test tower — see [`project-memory.md`](/GT2101/project-notes/project-memory/) § the
hardware for why that is worth changing.

Nothing further about the replacement controller is recorded; it is not part of the project.

---

## THE FIVE BOARDS — and which ones stay

Numbered 1 at the top to 5 at the bottom. Full detail in
[the board register](/GT2101/engineering-drawings-schematics/); signals and pads in [`flexicon-backplane-map.md`](/GT2101/project-notes/flexicon-backplane-map/).

| Board | Gale no. | What it does | In the Pico build? |
|---|---|---|---|
| 1 (top) | `3155ST` | Display | **stays** — the Pico drives it ✅ working |
| 2 | `3272ST` | Touch start/stop, display timing, carries the Helipot | **stays** — as touch sensor and pot bracket only |
| 3 | `3275ST` | `F VAR` generator + drive-voltage gate | **stays** |
| 4 | `3276ST` C | Crystal, reference divider, tacho front-end, **the servo** | **stays** |
| 5 (bottom) | `3285NH` | Power supply + external interface | **stays** |
| backplane | `3281NH` | Flexible ribbon by *flexicon* | stays |

**Boards 3 and 4 are one servo split over two boards** — 4 decides the drive voltage, 3
decides whether it is allowed out. Understanding that corrected a wrong description of
Boards 2 and 3 inherited from the defunct website.

⚠ **All five boards stay in the deck.** The original servo is left intact and running; the
Pico is added alongside it.

---

## ARCHITECTURE — Pico is brains only

Matt's stated goal: **"all the logic from the Pico, everything else original."** Original
power supply, original LED display, original front-panel controls, original motor PCB,
original wiring loom.

**The Pico mounts inside the tower on its own bracket**, located on the boards either side
of the flexicon and straddling the film with guaranteed clearance. ⚠ Nothing mounts on,
hangs from, touches or is strain-relieved to the flexicon, and no socket is vacated to make
room — every original board stays where it is.

### Where the Pico connects

| Job | Where | How |
|---|---|---|
| **Speed setting** | Helipot, mounted on Board 2 but wired only to the Pico | passive, straight to GP26. ✅ working |
| **Start/stop** | Board 2 pin 5 — a 0 → +10 V pulse | **27k/10k divider + 1k series** into a GPIO, rising-edge interrupt |
| **Display** | Board 1 pins 6, 7, 11 (+3, 10 optional) | ✅ working at 5 V; needs level shifting at 10 V |
| **Green LED** | Board 1 pin 8 | ✅ working at 5 V, open-drain on GP5. **NPN driver required at 10 V** |
| **Tacho in** | the `TACH` net, 0/−10 V | **J113 JFET inverter** — see below |
| **Drive out** | Board 3's pin-7 net | LM358 buffering filtered PWM |

**The Pico holds start/stop state in software.** Board 2 only ever emits an edge, so each
pulse toggles — which is what `controls.py` was going to do anyway.

---

## HOW THE PICO MEETS THE TOWER — minimum intrusion

**Rewritten 29 August 2026.** ⚠ **No board is removed and no socket is vacated. All five
boards stay in the tower.** An earlier version of this section described a different scheme;
it is withdrawn in full.

### The principle: the backplane is the loom

Every signal the Pico needs already terminates on the flexicon backplane, so it is reached
there rather than by soldering to an original board. See
[`flexicon-backplane-map.md`](/GT2101/project-notes/flexicon-backplane-map/) for the pad map,
which is confirmed in service.

| What the Pico needs | Where it appears |
|---|---|
| +10 V, −10 V, GND | pad 1 and the last two pads of every row |
| **`TACH` from the motor**, 0 to −10 V | **row 4 pad 5** (also row 5 pad 5) — J113 JFET, never a divider |
| **touch pulse**, 0 → +10 V | **row 2 pad 5** ☠ — pad 6 next to it swings 0 → −10 V |
| **demand** (drive voltage out of board 4) | **row 4 pad 6** = row 3 pad 6 |
| **drive out to the motor** | **row 3 pad 7** — the calibration prize |
| `F REF` to the display | row 4 pad 9 → row 1 pad 7 |
| black switch VAR/FIX selection | row 4 pad 3 |

### The rules

- ⭐ **Wires go to board connector pins**, where spares exist for boards 1–5. Any break, when
  one is finally justified, goes to a **brass staple** on the solder side — never to a pad.
  The film never sees the iron. **No spare flexicon exists.**
- ⚠ **Listen before driving.** Boards 2 and 4 are alive and pulsing. Driving a net before its
  break is made gives continuous, dynamic contention that would partially "work" — the worst
  kind of fault.
- ⚠ **Rows 3 and 4 do not share a pinout.** Row 3 has −10 V on 8 and GND on 9; row 4 has
  −10 V on 7 and GND on 8. Never carry an assumption between them.
- The Pico sits on its own bracket, located on the boards either side of the flexicon and
  straddling the film with clearance. Nothing mounts on, hangs from or is strain-relieved to
  the flexicon.

The order the joints are made in is
[`project-memory.md`](/GT2101/project-notes/project-memory/) § NEXT. **No break is
made anywhere until the touch wire is on and the log is complete.**

### One circuit point to decide now

`V_IDLE` = 0 V. Board 3's hardware gate enforces it and stays in place, but an LM358 on a single
supply will not sit at a true 0 V unaided. Run it from the backplane's +10 V (no wire) with
a **10 kΩ pull-down on its output**, so idle is 0 V by hardware even if the PWM stops or the
Pico hangs. Using −10 V as its negative rail gives a cleaner zero but puts a
negative-voltage fault mode in front of the motor drive — not worth it.

### The two checks that settle it — ✅ both answered, 3 September 2026

1. ~~**+10 V rail under load**~~ ✅ **Answered.** The rail carries the Pico — through the
   **LM7805**, drawing whatever the Pico draws (~25 mA), and **no wire to the reservoir is
   needed.** See § POWER. ⚠ *This entry previously said "with a DC-DC converter the draw is
   ~15 mA". There is no DC-DC converter — corrected 4 September 2026.*
2. ~~**Board 1 pin 8 to deck GND, unpowered**~~ ✅✅ **Answered, and the net is fully
   understood.** See § THE GREEN LED below. Short version: **the black switch grounds it,
   board 5 has no circuitry on it, and there is nothing for the Pico to fight.**

---

## THE CONTROLS — confirmed by Matt on the deck

| Control | Where | What it does |
|---|---|---|
| **Red switch** | bottom of tower | mains power on/off. Out of scope entirely |
| **Black switch** | bottom of tower | VAR released = speed set by the disc; FIX pressed = locked 33⅓. Plain passive switch |
| **Tinted disc, turned** | top of tower | sets the speed. **Beckman Helipot 7286, 0.25%**, bolted to Board 2, shaft up through the top plate |
| **Tinted disc, touched** | top of tower | **starts/stops the platter, and is CAPACITIVE, not a switch.** Responds to a finger, not a plastic pen |

The same disc both starts the platter and sets the speed, so the firmware distinguishes
them: a tap under `TAP_MAX_MS` (600 ms) toggles start/stop; a sustained touch is treated as
adjusting speed and ignored.

### ✅ The disc is smoke-tinted — not clear, and not red

**Matt, 24 August 2026.** Earlier notes called it the "clear disc" twice. **The red you see
through it comes from the LEDs behind it**, on the original boards and on Howie's tower alike —
the disc itself contributes density, not colour.

⚠ **This matters for any display-overlay idea.** A neutral smoke tint supplies **density but no
colour**, so a white module behind it reads *white*, not red. Anyone assuming the disc would
tint a modern display back to the original look would be wrong.

⚠ *Recovered 4 September 2026 from the now-retired fresh-eyes brief, which turned out to be the
only place this finding still lived after a de-duplication pass dropped it from
`project-memory.md`.*

**Touch sensing — three options still open.** ✅ The original sensor is now confirmed on the
drawings: a bent copper tab beside the Helipot bush, into a 555, out as a pulse on Board 2
pin 5. Reading that pulse is the cheapest option and needs two resistors. The alternatives
are sensing the tab directly on a Pico pin through 1 MΩ, or a TTP223 module. Buy the TTP223s
anyway, they cost almost nothing.

### ✅ The Helipot is electrically OFF Board 2 — Matt, 24 August 2026

**All three pot leads run directly to the Pico. Nothing else connects to it.** The pot is
held to Board 2 only by a **brass nut and washer** — Board 2 is now its bracket, not its
circuit.

Consequences:

- **This closes an open question in [`board-3-fvar-gate.md`](/GT2101/project-notes/board-3-fvar-gate/)**, which still asks what drove the
  XR2207's control voltage, "presumably the Helipot via Board 2." Whatever that path was, it
  is already broken.
- **Board 2's remaining jobs are exactly two:** the touch sensor, and holding the pot.
- ⚠ **Do not disturb the brass nut and washer.** The touch electrode is a bent copper tab
  beside that bush and the sensitivity depends on what the bush and shaft are tied to. No
  ground strap, no steel replacement, no cleaning under the washer. If touch behaviour
  changes after the tower is reassembled, that hardware is the first suspect.
- The pot body stays on Board 2's ground reference while its track runs off the Pico's
  3V3. In a 7286 the element is isolated from the case, so that is fine — and once the Pico
  is in a slot, its AGND and deck ground are the same node anyway. Nothing changes between
  bench and installation.
- Board 2 sits close to where the Pico is bracketed, so the pot's tail stays short.
- **For the final build:** 100 nF from the wiper to AGND at the Pico end. The wiper will run
  through the tower alongside the motor drive line, and with ten turns nothing is lost in
  response.

❓ **Helipot resistance unresolved.** The label reads *R 1K*; one bench reading gave 10 kΩ
end to end. Does not affect any wiring.

✅ **Helipot wire colours, identified on the bench 20 Aug:** **orange = wiper** → GP26_A0
(physical pin 31); **red** = track end → 3V3(OUT), pin 36; **yellow** = track end → AGND,
pin 33.

✅ **TEN TURNS — Matt, 24 August 2026.** The 7286 is a ten-turn pot, like the 7246. Measured
end to end on GP26: **160 at one stop, 65535 at the other** — the full ADC range, so no
scaling headroom is lost. ⚠ **Consequence for the bench:** a partial twist covers only a few
per cent of the range, and a reading stuck low is far more likely to be an unfinished turn
than a broken wire. This closed the 24 August fault report, where the pot appeared dead
because only 14 % of its travel had been used.

⚠ **Consequence for the firmware:** ten turns across the speed range is very fine control —
about 3 rpm per turn if mapped 30–80 rpm. Decide deliberately whether the whole range is
wanted, or a narrow trim band around the three standard speeds.

---

## DRIVE VOLTAGE — proportional, with a hard mute at rest

⭐ **The table's single home is
[`board-3-fvar-gate.md`](/GT2101/project-notes/board-3-fvar-gate/) §4.** It is deliberately not
repeated here.

⚠ **Why not:** those four figures were living in **three files at once** until 4 September 2026,
and that is precisely the arrangement that produced the `V_IDLE` contradiction — one copy
corrected on 29 August, another still carrying the withdrawn alarm six days later. **One fact,
one home.**

**What the build needs from it:** drive is **proportional, with a hard mute at rest.** Lowest
speed is lowest voltage, rising roughly through the origin — what a brushless motor needs, since
back-EMF rises with speed. **"STILL = 10 V" is Board 4's loop railing to maximum demand with the
platter stopped, and Board 3 mutes it to 0 V.**

⚠⚠ **Corrected 5 September 2026.** This read *"the backplane sheet only ever recorded the
input column."* **It doesn't — the sheet carries both columns**, side by side on the row 3
pads, with an up-arrow into pad 6 and a down-arrow out of pad 7:

        "O.C."
        STILL: 10V        STILL: 0V
        33: 1,2V          33: 1,2V
        45: 1,6V          45: 1,6V
        78: 2,4V          78: 2,4V ✓

📄 Read off `motor-overview/backplane.pdf` at 400 dpi. **So the long-standing "STILL = 10 V"
came from reading one of two columns that were both there** — not from the sheet omitting
one. ⭐ Worth keeping, because the archive had written itself a false account of its own
mistake, and that is the same failure as the DC-DC entry in
[`archive-provenance.md`](/GT2101/project-notes/archive-provenance/).

### `V_IDLE` is 0 V — and Board 3 enforces it in hardware

**`V_IDLE` is 0 V, not 10 V.** The 1975 design never let 10 V reach a stationary platter:
Board 4's loop rails to maximum demand at rest and Board 3's gate mutes it to 0 V.

⚠ **Corrected 29 August 2026.** This section previously read "with Board 3 out, firmware is
the only thing holding it there," and called it the single most important consequence of the
architecture. **Board 3 is not out — all five boards stay** — so the hardware gate stays in
circuit and `V_IDLE` plus the ceiling in `drive.set_drive()` are belt-and-braces agreeing
with it, not the only braces. Give the LM358 its 10 kΩ output pull-down anyway, so idle is
0 V even if the PWM stops or the Pico hangs.

📄 not ✅ — these are the tracer's figures on a sheet marked PRELIMINARY. **Measuring Board 3
pin 7 on the running deck is the most valuable measurement left in the project.**

---

## TACHO — ~600 pulses per platter revolution

Board 4's 4046 locks the tacho to `1×F` with **no divider in the loop**, so in lock the
tacho runs at **10 Hz per rpm** — 333 Hz at 33⅓ rpm, i.e. **600 pulses per platter
revolution.**

⚠ **This replaces the old figure of 60/rev**, which was inferred from the assumption that
the PLL reference was the ×40 frequency. It is the ×10 frequency. Ten times out.

**What needs changing:** `TACHO_PPR`; the ring buffer ("one revolution") becomes 600
entries; `bench.tacho()` hand-turning 10 revolutions should show **~6000** edges; and the
KP/KI tuning was simulated at the old figure and should be re-checked.

📄 not yet measured. `bench.tacho()` settles it in five minutes.

---

## INTERFACING

Pico is 3.3 V; the original boards run 10 V CMOS.

- **Helipot and black switch need NO level shifting** — both passive. ✅ proven on the bench.
- **Shift up (3.3 → 10 V):** `F DISPLAY`, `F REF`, gate, `BLANK`. ~4 NPN circuits.
  ⚠ **A common-emitter NPN inverts.** `GATE_COUNTS_WHEN_LOW`, the `F REF` pulse polarity and
  the `F DISPLAY` pulse shape all flip when the bench 5 V wiring becomes the 10 V wiring.
  Either invert them in `config.py` or use two transistors per line — but decide it
  deliberately rather than meeting it as a surprise.
- **Shift down (+10 V → 3.3 V):** Board 2's start/stop pulse. **27k/10k + 1k in series**
  (2.70 V from a 10 V rail). ⚠ Supersedes 22k/10k, which gives 3.13 V — works, but little margin.
- **Speed voltage out:** LM358 on +10 or +15 V, PWM 30 kHz + two-stage RC (10k/1µF ×2),
  10 kΩ pull-down on the output.

### ⚠ Green LED — correction, 24 August 2026

Earlier versions of this file said the 1 kΩ series resistor is on Board 1, so a Pico pin can
sink connector pin 8 directly, **"no driver transistor needed."** That is true on the bench
and **false in the deck** — and the difference is the *off* state, not the on state:

| Supply | Sinking (LED lit) | **Not** sinking (LED out) |
|---|---|---|
| 5 V bench | ~3 mA. Fine | the pin floats to 5 − 2 = **3 V**. Nothing conducts. Fine |
| 10 V deck | ~8 mA. Fine | the pin is pulled toward **8 V** through 1 kΩ; the Pico's clamp diode conducts and dumps ~4 mA into its own 3V3 rail, continuously, from the instant the deck is switched on |

**So the 10 V installation needs the low-side NPN** that [`parts-to-order.md`](/GT2101/project-notes/parts-to-order/) has
always listed for it. The two documents disagreed; the parts list was right.

On the bench, open-drain and no parts at all — ✅ proven, bench session 6.

### ⭐⭐ THE GREEN LED — what it is for, settled 3 September 2026

**It is the 33⅓ / FIX indicator. The black switch grounds it. Board 5 has no circuitry on
it whatsoever.**

```
board 1: +10 V ── green LED ── 1 kΩ ── board 1 pin 8
                                          │
                       row 1 pad 5 ── the centre run ── row 5 pad 1
                                          │
                        board 5 pin 1 ── black switch ── 0 V
```

✅ Confirmed two ways on the hardware, bench session 8: **press the black button and the LED
lights**, and **pad 1 beeps to deck `GND` only while the button is held.**

✅ Confirmed by omission on the drawing: `Board-5-Schem.pdf` carries three outputs — `2 (+10 V)`,
`9 (0 V)`, `8 (−10 V)` — and **pin 1 is not on it at all.** Board 5 is a power supply plus a
passive interface for the external flying leads. The `PNP hfe=283` on that sheet is the
**−10 V pass transistor**, not an LED driver.

⚠ **Two things this corrects:**

1. ~~*Board 5 may drive the net to 9.18 V and the Pico would be fighting an output.*~~
   **Wrong.** [`folder-findings.md`](/GT2101/project-notes/folder-findings/)'s *"9.18 V selected / 0 not"* has its states
   reversed: **~9 V is LED OFF** (board 1's own pull-up, read back through the LED) and
   **0 V is ON**. A passive switch and GP5 open-drain are both sinks — no contention.
2. ⭐ **GP5 in session 6 was standing in for the black switch.** Same node, same direction.
   That is why one wire and no components worked.

⚠ **A functional collision remains, and it is a design decision, not a fault.** With the
black switch in FIX, that LED is lit whatever the Pico wants. **The Pico can turn it on; it
cannot turn it off.** So a lock-indicator scheme only works while the switch is in VAR.

**This closes the open item "decide what the green LED should indicate."** Gale already
decided. Giving it a new job means overriding a working original function — which is exactly
the kind of decision the project's own principle says to take deliberately.

⚠ **The 10 V NPN is still required.** That hazard comes from board 1's 1 kΩ pull-up acting
on the Pico's *off* state and is unaffected by any of the above.

### ⚠ Tacho input — use a JFET, not a PNP

The tacho swings **0 V to −10 V** (LM339 on GND/−10 V on the motor PCB). It destroys a Pico
input if connected direct.

```
        +3.3 V
          │
         10k
          │
  TACH ──[10k]──┤ G   ┌─── to a Pico GPIO   (inverted: TACH low = pin low)
  0/-10V        │  J113 JFET
                └── S ── GND
```

- TACH at 0 V → JFET conducts → pin LOW
- TACH at −10 V → JFET pinched off → pin HIGH

**This is Gale's own circuit** — an E113 in exactly this configuration is Board 4's tacho
front-end, and sheet 3A records a defective E113 on Board 3 being *"replaced by J113 (RS
Components)"*.

⚠ **Not a MOSFET** — a 2N7000/BS170 needs a positive gate, so with a signal that only sits
at 0 V or −10 V it would be off in both states.

⚠ **The PNP circuit in the old notes cannot work** — "22k base series, 100k to GND, emitter
3V3" leaves the base below the emitter at *both* tacho levels, so the PNP conducts always
and the output sits high permanently. Do not build it.

**Bench shortcut, used successfully 21 Aug:** the display boards work at **5 V**, so on the
bench the Pico drives them **directly, with no level shifters**. The transistors on order
are only needed for the final 10 V installation.

---

## POWER — ✅ LM7805 off the tower's +10 V rail, 3 September 2026

✅✅ **SETTLED, bench session 8. The Pico runs on the tower's own +10 V rail, through an
LM7805.**

```
row 5 (board 5) pad 2  = +10 V ──► LM7805 IN
row 5 (board 5) pad 9  = GND   ──► LM7805 GND ──► Pico GND
                                   LM7805 OUT ──► 5 V ──► Pico
```

The Pico self-starts and its LED blinks with no other supply connected.

✅ **Where the regulator physically is:** in the void at the bottom of the tower stack,
**underneath board 5** — a module small enough to sit in that space. Nothing hangs off a
board, nothing crosses the deck.

### ⚠⚠ There is no DC-DC converter — corrected 4 September 2026

This section, `project-memory.md` and `flexicon-backplane-map.md` all recorded session 8 as
*"+10 V through a DC-DC converter to 5 V, retires the LM7805"*. **Wrong on both counts.**
Matt, off the hardware: *"we are using the LM7805 … ten volts in from board five, into that,
five volts out for the Pico. It works."*

**What changed on 3 September was the regulator's INPUT, not the regulator.** The same
LM7805 built on 19 August is still doing the job; it was simply moved off the +15 V reservoir
and onto the backplane's +10 V.

| | 19 August | 3 September |
|---|---|---|
| Regulator | LM7805 | **the same LM7805** |
| Fed from | **+15 V**, a wire to the 4700 µF reservoir | **+10 V**, row 5 pads 2 and 9 |
| Dropped across it | 10 V | **5 V** |
| Dissipation at ~25 mA | ≈0.25 W | **≈0.13 W** |
| Wiring | a wire run across the deck | **backplane pads only** |

⭐ **Both gains are real; they were credited to the wrong part.** The one that matters for the
project's principle is the last row — the supply is taken where every other signal is taken,
at the backplane, nothing soldered to an original board. The second is heat: the 7805 now
sheds **half** what it did, because it drops 5 V instead of 10. The heatsink question shrinks
accordingly.

✅ **Dropout headroom is comfortable.** A standard 7805 needs roughly 7 V in to hold 5 V out.
The tower's "+10 V" rail measures **+11.9 V** 📄, so there is about 5 V of margin. Only a rail
collapse would drop the Pico out of regulation.

### ⚠⚠ Switching noise — the concern is NOT void. Corrected twice on 4 September 2026

The original worry was *"a switching converter is new noise on a rail that feeds 1975 CMOS
and the display."* When the DC-DC turned out not to exist, that was declared **void on the
grounds that a linear regulator does not switch.** ⚠ **That was too strong, and it is
withdrawn.**

**The Pico has its own switching regulator on board.** A buck-boost converter sits on VSYS
making the 3.3 V rail, and it is inside the tower no matter how the Pico is fed. A linear
7805 upstream removes one switcher. It does not remove that one.

⚠ **And there is empirical evidence, from this project's own hardware.** Howie's tower — a
modern microcontroller and its own supply inside a GT2101 tower — **puts a small amount of
audible noise through the speakers.** Nobody has diagnosed it. It is one data point, not a
verdict, and Remora's position is much better (a fraction of the current, no segment LEDs or
encoder driven from it, all original analogue paths untouched) — **but "linear regulator,
therefore no noise" is not a conclusion this project has earned.**

### ⭐ The cheap mitigation — decide it now, not later

On a plain Pico, **GP23 controls that regulator's mode.** Left alone it runs in power-save
(PFM), which is efficient at low load and ripples more. Driven high it is forced into PWM
mode: noticeably lower output ripple for a little more idle current.

```python
# config.py — for a device whose whole job is playing records, this is the right default
from machine import Pin
Pin(23, Pin.OUT, value=1)      # SMPS forced PWM — lower supply ripple
```

⚠⚠ **Not on a Pico W.** GP23 is the wireless enable there, and
[`parts-to-order.md`](/GT2101/project-notes/parts-to-order/) currently has a **Pico W** on the
list. **That is a real conflict to decide, not a footnote** — a Pico W buys the live web
monitor and gives up the quietest available supply setting on an audio device.

100 µF + 100 nF across the 7805's input and output remains ordinary good practice, and keep
the Pico away from the `TACH` wiring when it is mounted.

✅ **Side effect: row 5 pad 9 = `GND` is now confirmed.** It was 📄 from the FANATSON sheet
and had never been checked against the part. Carrying the Pico's supply return proves it.
First of row 5's pads 3–9 to be confirmed — see `flexicon-backplane-map.md` §7.

❓ **Not yet recorded: where the 5 V lands on the Pico.** It must be **VSYS (pin 39)**, not
VBUS (pin 40). VBUS is the USB rail and an external supply on it fights the cable. Confirm
and record.

### The +15 V input, 19 August 2026 — superseded as to its INPUT only

Kept because it is how the +10 V question came to be asked, and because the reasoning about
the deck's rails is still correct.

`GaleTT5Schem.pdf` shows +10 V made from +15 V via a 560R and a shunt zener — that alone
gives only ~9 mA, far less than the display needs, so **+15 V** was first taken straight off
the 4700µF reservoir. ±15 V is unregulated and may sit at 16–18 V unloaded.

Built: **+15 V → LM7805 → Pico VSYS (pin 39) / GND (pin 38)**. Heatsink **cold** at the
Pico's ~25 mA (≈0.25 W). Rule of thumb for Matt: too hot to keep a finger on = needs help.
The LED display runs from the deck's own +10 V rail, not from the 7805.

~~❓ **Worth re-testing:** if the tower's +10 V rail can supply ~50 mA, the 7805 can be fed
from a slot finger instead.~~ ✅ **Answered 3 September 2026: yes.** The 7805 is fed from the
backplane now, and sheds half the heat doing it.

Safety rule used throughout: **one power source at a time** — USB out when the tower is on.

⚠ **Do not put Board 5 in the bench chain** — it takes AC from the mains transformer and
carries mains; a DC bench supply can't drive it.

---

## FIRMWARE — MODULAR

Eight files so each subsystem can be brought up alone. **`config.py` holds every setting —
it should be the only file Matt ever edits.**

`config.py` · `tacho.py` · `display.py` · `controls.py` · `drive.py` · `controller.py` ·
`main.py` · `bench.py`

**`main.py` is the entry point — MicroPython auto-runs that filename and nothing else.**

Bring-up order from the REPL: `bench.blink()` → `bench.lock()` / `bench.digits()` →
**`bench.green()`** → `bench.controls()` → `bench.tacho()` → `bench.drive(confirm=True)` →
`bench.loop()`. `bench.drive()` refuses to run without `confirm=True`.

⚠ **`display.py` and `bench.py` were rewritten from scratch on 21 August 2026** for the
counted-pulse scheme in [`board-1-display.md`](/GT2101/project-notes/board-1-display/). The old frequency-emitting `display.py`
and the old `bench.display()` are superseded.

Design points:

- Tacho edges timestamped into a ring buffer one revolution long. **Window chosen by
  state**: ~6 pulses spinning up, ~10 running, a full revolution for the display. One long
  window makes the loop oscillate — lag is the problem, not noise. ⚠ **Re-scale these for
  600 ppr.**
- **KP=0.08, KI=0.04**, tuned in simulation at the old 60 ppr figure; re-check.
- Integral clamped tighter during start-up (`nominal × 1.5`) so the P term supplies
  acceleration and the integral doesn't wind to the ceiling and overshoot.
- `drive.nominal_drive(rpm)` interpolates steady-state volts from the three measured points.
- Safety: soft-start ramp 4 s; hard drive ceiling clamped inside `drive.set_drive()`; stall
  timeout 8 s below half speed; no-tacho timeout 2 s. **Plus the still-gate, now firmware's
  job.**
- **Fault codes distinguished on purpose:** pulses seen then lost → `SEL` (platter
  stopped); none ever → `SEn` (sensor/level shifter). A jam triggers both conditions, so
  this decides whether Matt looks at the platter or at the wiring.

### ⚠ Display update discipline — added 24 August 2026

Two rules that came out of bench session 5, and they belong in `controller.py` and anything
else that calls `display.show()`:

1. **Nothing may call `display.show()` before the phase lock exists.** Unlocked, `show()`
   silently falls back to blind mode and lands somewhere different at every power-up. This
   is the failure that was reported as "the display stopped working" on 24 August, and it
   will keep recurring until the auto-lock wire in § NEXT is fitted.
2. **Average the ADC and only call `show()` when the value actually changes.** A raw
   `read_u16()` mapped straight to the display jitters ±1 count, which flickers the last
   digit continuously. Sixteen reads averaged plus a one-count deadband cleans it up
   completely. ✅ proven on the bench.

### Green LED — added 24 August 2026

```python
# config.py
GREEN_LED_PIN    = 5
GREEN_LED_DIRECT = True   # True  = Pico sinks it, open-drain  (5 V bench)
                          # False = via NPN low-side driver, active high (10 V tower)
```

⚠ **`Pin.OPEN_DRAIN`, never `Pin.OUT`, while `GREEN_LED_DIRECT` is True.** The pin must
either pull to ground or let go completely. Driving it high is what would put the LED's
supply into the Pico at 10 V.

⚠ **Any bench step that toggles an output needs a delay or a loop.** Four REPL lines run
back to back light the LED for microseconds and look exactly like a dead circuit. This cost
part of an evening on 24 August.

⚠ **Corrected 5 September 2026.** This read *"what the LED should indicate is undecided …
it has no job of its own."* ✅ **It has one: it is the 33⅓ / FIX indicator**, grounded by the
black switch — settled 3 September and written up in **§ THE GREEN LED above, in this same
file.** A lock indicator (out when stopped, flashing through the 4 s soft-start ramp, steady
once the tacho says the platter is in tolerance) is still the obvious second job, but ⚠ it
only works while the black switch is in **VAR**, and it overrides an original function.

Superseded: `tacho_count.py` — `bench.tacho()` does the same job and reads `config.py`.

---

## TOOLCHAIN

**Thonny 5.0.0** on Windows. MicroPython installed from inside Thonny (bottom-right corner
→ *Install MicroPython…*) — no separate UF2 download. **No drivers needed**; Windows 10/11
handle both the BOOTSEL drive and the serial port. Working pattern: File → Open (This
computer) → green play to test → red Stop → File → Save as (Raspberry Pi Pico).

⚠ **After saving a changed file to the Pico, press the red Stop button before re-running.**
MicroPython keeps the previously imported module in memory, so without the reboot you get
the old code with the new file on disk. This caused an hour of confusing results on 21 Aug.
Do **not** "run config.py" to reboot — the red Stop button is the way.

⚠ **But the red Stop button also throws away the display's phase lock**, because it drops
the imported `display` module and its `_locked` flag with it. Once `bench.lock()` has been
run, break loops with **Ctrl-C**, which leaves the module state intact. Stop only when a
file on the Pico has actually changed — and expect to run `bench.lock()` again afterwards.

⚠ **For the same reason, type one-off bench experiments into the Shell pane, not the
editor.** The green play button reboots the Pico and costs the display lock.

**Meter note:** Matt's DMM shows **`0.L`** for open circuit. It does not go blank.

---

## BENCH LOG

| # | Date | Outcome |
|---|---|---|
| 1 | 19 Aug | Pico programmed and self-starting from `main.py` ✅ |
| 2 | 19 Aug | +15 V → LM7805 → Pico. Runs on deck power, USB out, heatsink cold ✅ |
| 3 | 20 Aug | **Helipot read into the Pico on GP26**, full 0–100% sweep ✅ |
| 4 | 21 Aug | **Board 1 display driven by the Pico** — `12.3`, `45.0`, `78.0`, `33.3`, every segment and decimal point good, board otherwise untouched ✅ |
| 5 | 24 Aug | **Helipot drives the display end to end** — turn the disc, the digits follow ✅. Also: the pot is **ten turns**, full ADC span 160–65535 ✅. Fault reported as "display won't change" was the phase lock lost at power-up, not a hardware failure |
| 6 | 24 Aug | **Board 1's green LED driven by the Pico** — one wire, Board 1 pin 8 → GP5, open-drain, no components ✅. Confirmed the LED net is free at the Pico end. Corrected the "no driver transistor needed" claim for the 10 V install |
| 7 | 26 Aug | **Board 1 driven by the Pico *through the repaired flexicon*** at 5 V, no other board connected. The display works — row 1's pad map proven by function, not inspection ✅ |
| 8 | **3 Sept** | ⭐ **The Pico runs on the tower's own power.** +10 V off **board 5 pad 2**, GND off **pad 9**, into the **LM7805**, 5 V out to the Pico; the regulator sits in the void under board 5. Self-starting, LED blinking, no bench supply to the Pico ✅. ⚠ *Logged at the time as "through a DC-DC converter … retires the LM7805" — corrected 4 Sept: same 7805, new input.* **Confirms row 5 pad 9 = GND** — the first of that row's pads 3–9 off the sheet ✅. **Green LED net metered end to end** (board 5 pad 1 → board 1 pad 5) and confirmed to have nothing else on it — not GND, not the +10 V rail ✅. **Both rebuilt supply rails on the flexicon mapped pad by pad** ✅. All three display digits good |

---

## STATUS, 4 September 2026

**Bench sessions 1–8 complete.** Board 1 is done apart from auto-lock: the display, the green
LED and the deck's speed pot all answer to the Pico, the pot drives the display in real time,
and the Pico runs on the tower's own power.

**All five boards have been identified from their own etched part numbers and studied from
their own drawings.** The architecture is settled: **all five boards stay**, and the Pico is
added alongside the original logic — listening first, injecting later.

✅ **The parts are ordered — 4 September 2026, awaiting delivery.** Supersedes "nothing has
been ordered yet", which had stood since 22 August. They are for a **perfboard interface
card** carrying the dividers, level shifters and JFET front-end. ⚠ **Log what is actually in
the box against [`parts-to-order.md`](/GT2101/project-notes/parts-to-order/) before anything
is built** — that list has been amended three times and at least one item on it (the 22k/10k
touch divider) is already superseded.

Equipment: spare boards 1–5, a spare motor PCB, a spare motor, a DMM, bench supply and scope.
✅ **And two towers** — inventory settled 4 September 2026, see § THE DECK above: Howie's on
the deck, Alex's on the bench.

---

## NEXT

**Board 1's only remaining job is auto-lock, and it is now the project's most annoying
recurring fault, not a nicety.** The board's 4013 comes up in a random state at every
power-up, so `bench.lock()` needs a human watching for the digits to go dark — and every
time that step is skipped, the display looks broken.

⭐ **Try the free fix first — new 5 September 2026.** The audit of sheet 1A found a gate the
notes had never recorded: **4001 D = NOR(4013 Q2, GATE)** drives the 4013's reset inputs, so
**the gate line — which the Pico already drives — can park the divider.** From any power-up
state, holding `GATE` low and sending up to four `F REF` pulses should land it in a known
state with no extra hardware at all. **One bench session to find out**, and it needs nothing
ordered. See [`board-1-display.md`](/GT2101/project-notes/board-1-display/) §3 and §6a.

If that fails: wiring connector pin 10 (`RESET` out) into a Pico input lets the Pico find the
dark state by itself. One wire and one resistor — anything from about 47 kΩ to 470 kΩ at 5 V.
**Check the drawer before ordering; this may not be blocked at all.**

Otherwise the next subsystem is **controls** (Board 2 pin 5, two resistors) or **tacho**
(needs the J113).

---

## Open items

- ~~**Order the parts.**~~ — ✅ **done 4 September 2026, awaiting delivery.** ⚠ The order is
  back-to-front against the work: the active devices arrived, almost none of the passives did.
  **One E12 resistor assortment and five J113s unblock the entire build**, and both are
  pennies. See [`parts-to-order.md`](/GT2101/project-notes/parts-to-order/).
- **Confirm the tacho pulses per revolution** — expect ~600 per platter turn.
- **Measure Board 3 pin 7 on the running deck** at each speed. Four numbers that are
  currently 📄 become ✅, and they are the whole specification for `drive.nominal_drive()`.
- **Settle the Helipot's resistance** — label says 1 kΩ, one bench reading said 10 kΩ.
- ~~Helipot turn count~~ — ✅ **settled 24 Aug: ten turns.**
- ~~Whether the Helipot is still electrically on Board 2~~ — ✅ **settled 24 Aug: it is not.**
- ~~Can the Pico drive the green LED~~ — ✅ **settled 24 Aug: yes.**
- **Decide the speed range the ten turns map onto** — full 30–80 rpm, or a trim band.
- Decide which of the three touch options to use.
- ~~**Does Board 5 ground the green LED net?**~~ — ✅✅ **closed 3 Sept.** The **black
  switch** grounds it; board 5 has no circuitry on pin 1. See § THE GREEN LED.
- ~~**Decide what the green LED should indicate.**~~ — ✅ **it already indicates something:
  FIX / 33⅓.** The open question is now whether to *override* that, which is a decision
  about the project's principle rather than a wiring question.
- ~~**Can the tower's +10 V rail supply ~50 mA?**~~ — ✅ **settled 3 Sept: yes.** It carries
  the Pico through the LM7805. No wire to the reservoir.
- **Record where the Pico's 5 V lands** — VSYS (pin 39), not VBUS (pin 40).
- ⚠⚠ **Look for switching noise on the +10 V rail — REOPENED 4 Sept.** Briefly closed on the
  grounds that the LM7805 is linear. **Wrong: the Pico carries its own buck-boost converter on
  VSYS**, and Howie's tower is evidence that a microcontroller inside a GT2101 tower can be
  audible. See § POWER.
- **Decide plain Pico vs Pico W**, and decide it before building. GP23 forces the Pico's SMPS
  into low-ripple PWM mode — but GP23 *is* the wireless enable on a Pico W. Quietest supply,
  or the web monitor. Not both.
- **Log what the parts box actually contains when it arrives**, against
  [`parts-to-order.md`](/GT2101/project-notes/parts-to-order/), before anything goes on the
  perfboard.
- Measure display current with all eights lit.
- Read Board 5's etched part number, and check Boards 1, 2 and 5 for issue letters.
- Measure the tower gap height (a socketed Pico needs ~12 mm).
