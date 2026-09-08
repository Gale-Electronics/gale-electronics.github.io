---
layout: bare
title: "GT2101 — Pico Controller — Working Notes"
permalink: /GT2101/project-notes/pico-controller-notes/
description: "The live working record of the GT2101 Pico controller build: architecture, wiring, interfacing, firmware and bench log."
---

*A working note — part of the GT2101 project's live record, written as the work happens and including the wrong turns. The polished write-ups live in [Technical Notes](/GT2101/technical-notes/).*

---

# GT2101 — the Pico controller

**Current as of 6 September 2026.**

### ⭐ This file is the build record

**Circuit detail, interfacing, power, firmware and the bench log belong in this file and
nowhere else.** Two facts have their homes elsewhere, deliberately, and are not repeated here:

- **the drive-voltage table** → [`board-3-fvar-gate.md`](/GT2101/project-notes/board-3-fvar-gate/) §4
- **the backplane pad map** → [`flexicon-backplane-map.md`](/GT2101/project-notes/flexicon-backplane-map/)

⚠ **One fact, one home.** This document and `project-memory.md` once held the same material
word for word, and that duplication produced three live contradictions that took a week to
find. If you are about to add circuit detail to any other file, it belongs here.

*The corrections this page used to carry inline are in
[`corrections-log.md`](/GT2101/project-notes/corrections-log/) — §1 the withdrawn
remove-the-boards plan, §2 `V_IDLE`, §4 the supply, §6 the tacho figure, §7 the touch divider,
§8 the tacho level shifter, §12 the green LED.*

**Scope:** Matt is adding new control logic to the GT2101's control tower using a Pico and
a handful of small parts. Everything else on the deck stays original.

**Howie's tower is out of scope as a subject** — it is not being reverse-engineered, recloned
or dated, and neither its firmware nor the manufacturing enquiry that went with it is being
pursued. ⚠ **That is an editorial rule, not a plan to remove it.** It is on the working deck,
it works very well, and it stays there. See § THE DECK.

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

### ⚠⚠ There are TWO towers

**The deck in use and the tower on the bench are not the same object.**

| | |
|---|---|
| **Howie's tower** | ✅ **New PCBs and a new power supply, fitted inside the ORIGINAL tower housing.** ⭐ **It is on the working deck now and it drives it very well** — Matt's own assessment, 6 September 2026: *"it works very well on my turntable… it's very solid."* The deck is playable because of it, which is why none of this work is under time pressure. ✅ Its original boards were all kept |
| **Alex's tower — "the test tower"** | A working original tower from **Alex**. ✅ **A spare** (Matt, 6 Sept 2026) — not the restoration target. ⭐ **Every bench session and every photograph in this repo is this tower** — the LM7805, the restored flexicon, the display and the green LED |

⚠⚠ **NOTHING IS BEING REMOVED FROM THE WORKING DECK.** ✅ Restated by Matt, 6 September 2026,
correcting a claim that had stood in the archive since August. The bench work happens on the
test tower **precisely so that the working deck is not the test subject.**

⚠ **Do not write Howie's tower up as a problem.** It is well made, it works, and it is the
reason this project can take its time. The archive's rule about non-original hardware means it
is not *documented* as a subject — **it does not mean it is in the way.**

### ✅✅ THE RESTORATION TARGET IS HOWIE'S TOWER — settled by Matt, 6 September 2026

**Howie's tower is the one that gets restored.** Its own original boards go back into its own
original housing, on its own original flexicon — the orange-wire one Matt repaired — with Remora
inside. ⭐ **Housing, boards and backplane reunite as a matched set.**

⭐ **The reasoning holds for a sharper reason than "it would be nice":** *Howie's tower is the
only tower that needs restoring at all.* Alex's is already a working original. So "which tower
do I restore" has exactly one answer.

⭐ **And it resolves a standing warning.** The restored flexicon is Howie's tower's own cable and
is currently fitted to the *test* tower — the one about to receive experimental connections.
Under this plan it goes home, which is where it was always meant to end up.

### ⚠ The order matters more than the plan does

**The reason nothing here is under time pressure is that Howie's tower plays.** If it comes
apart before Remora is proven, that goes away.

1. **Howie's modern tower stays on the deck, playing, untouched.**
2. All Remora bring-up happens on **Alex's tower**, as now.
3. Only once Remora works end to end, build the restored tower complete — Howie's originals, its
   own flexicon, Remora inside — **off the deck.**
4. **Swap towers once, at the end.** If anything is wrong, swap back the same evening.

Towers are swappable; that is why this is reversible at the tower level rather than the board
level.

✅✅ **The gating question is answered, 6 September 2026: Alex's tower HAS its own flexicon.**
So there are two films, both towers can be complete at once, and restoring Howie's tower does
not end bench work. ⭐ **A break is also no longer unrecoverable** — see
[`flexicon-backplane-map.md`](/GT2101/project-notes/flexicon-backplane-map/) §8. ⚠ **Keep
soldering to the brass staples anyway:** a spare is not a licence, and neither film is
manufacturable.

⚠ **The boards being tested are Howie's tower's originals**, kept when his build replaced
them. ⚠ **The restored flexicon is Howie's tower's original cable too**, and it is currently
in the test tower.

### The spares — ✅ Matt, 6 September 2026

**Beyond the two towers' own sets there are loose spares**, so a damaged board during Remora
bring-up is an inconvenience rather than a disaster:

| Spare | Status |
|---|---|
| **Board 1 — display** | ✅ a spare exists |
| **Board 5 — power** | ❓ *"I think I've got an extra"* — **Matt's own hedge; confirm before relying on it** |
| **Board 3** | ✅ three were photographed for the board 3 study — two plain, one ISSUE B |
| **Motor PCB** | ✅ a spare exists |
| **A whole motor** | ✅ exists — see below |

⚠⚠ **The spare motor is suspected FAULTY.** ✅ Matt, 6 September 2026: *"the spare motor I have,
I think, has a fault, but [we'll] get to the meter… later."* **Nothing has been measured.**

⭐ **A hypothesis worth testing first, because it is free:** the archive already holds a
photograph of a **shattered encoder disc**, and a broken disc would produce exactly the symptoms
of a dead motor — no tacho, so no lock, so no drive. ❓ **Is the shattered disc this motor's?**
**Look before metering.** It also connects to the standing job of photographing an *intact* disc
while one exists — no disc geometry is recorded anywhere in this archive.

❓ **Two things from the 6 September note are not yet recorded, because the transcription was
unclear and nothing gets guessed into this archive:** a reference to *"three … panels"* — LED
panels? the three digits? — and something about the display and the Helipot working. **Ask
before writing either down.**

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

## ⭐⭐ ARCHITECTURE — Remora is a TWO-WIRE project

**Settled 6 September 2026.** This replaces a six-connection scheme in which the Pico read the
touch pulse, drove the display, drove the green LED, read the tacho and injected the drive
voltage. **It does none of those.**

> ### Remora is a digital replacement for exactly one chip's worth of function: the XR2207.
>
> Nothing else in the tower changes hands.

| | The wire | What it is |
|---|---|---|
| **IN** | the Helipot's **orange** wiper lead → **GP26** | ✅ working since 20 August |
| **OUT** | **`F VAR`** — one NPN onto the XR2207 pin 13 node | § `F VAR` below |

Plus supply, which is not signal and is already in place: **+10 V and GND from board 5 pads 2
and 9**, through the LM7805; and the Helipot's other two leads to **3V3** and **AGND**.

⭐ **The orange wire is the same wire it always was.** It ran from the pot straight onto board
3's `ORANGE` post and set the XR2207's frequency. Only its far end has moved. The Pico sits in
the middle of a path Gale already built.

⚠⚠ **But that post had a second job, found 8 September 2026.** The same node also feeds board
3's **LM308**, and the LM308 drives the **STILL/TURNING** pads that tell board 2 whether the
platter is moving. **Remora has taken over one of the post's two jobs and left the other
vacant.** The drive gate and the motor mute are *not* affected — they run off a different pair
of LM3900 amplifiers — but board 2's display mux may be. Full statement in
[`board-3-fvar-gate.md`](/GT2101/project-notes/board-3-fvar-gate/) §2a, and the consequence for
the display in § `F VAR` below.

### What two wires buys

- **Crystal-accurate speed at any rpm** — pitch control, arbitrary speeds, no thermal drift.
  The XR2207 is an analogue VCO; the Pico has a crystal.
- **The original display, touch start/stop, drive gate and green LED all keep doing their own
  jobs**, untouched. Restoring `F VAR` restores the whole display chain by itself (§ `F VAR`).
- ⚠ **FIX is not a Remora feature.** The black switch stays original — **decided 7 September
  2026**, see § `F VAR`. In FIX the deck does select its fixed reference and ignore the Pico, but
  that is Gale's behaviour, not a fallback this build is designed around.

### ⚠ What two wires gives up — state this plainly

**The Pico is blind.** It commands; the 1975 servo closes the loop. So:

- **If the deck runs at the wrong speed, the Pico does not know.** No lock indication, no
  logging, nothing real to put on a web page.
- **It does not know whether the platter is running**, so it cannot ramp or soft-start.
- Every drive-side safety feature in the firmware (`V_IDLE`, the ceiling in `drive.set_drive()`)
  becomes irrelevant, because **the Pico never touches the drive voltage.** Board 3's hardware
  gate is the only gate, which is what it was designed to be.

### ⭐ The natural phase 2 — one more wire, still listen-only

**`TACH` in, through the J113** (row 4 pad 5). That turns *command* into *command and know what
happened*: lock indication, real speed on a monitor, fault detection. **It injects nothing** and
changes no original function.

⚠ **Nothing is foreclosed.** The backplane taps for the touch pulse, the demand and the drive
voltage stay exactly where they are, documented in
[`flexicon-backplane-map.md`](/GT2101/project-notes/flexicon-backplane-map/), if a later phase
ever wants them.

---

## HOW THE PICO MEETS THE TOWER — minimum intrusion

⚠⚠ **No board is removed and no socket is vacated. All five boards stay in the tower.**

### The principle: the backplane is the loom

Every signal the Pico could ever want already terminates on the flexicon backplane, so it is
reached there rather than by soldering to an original board. See
[`flexicon-backplane-map.md`](/GT2101/project-notes/flexicon-backplane-map/) for the pad map,
which is confirmed in service.

**The two-wire build uses none of these** — the pot is a flying lead and `F VAR` is taken at
board 3. The table is kept because it is the map for any later phase:

| Signal | Where it appears | Used by the two-wire build? |
|---|---|---|
| +10 V, −10 V, GND | pad 1 and the last two pads of every row | **yes** — supply |
| **`TACH` from the motor**, 0 to −10 V | **row 4 pad 5** (also row 5 pad 5) — J113 JFET, never a divider | phase 2 |
| **touch pulse**, 0 → +10 V | **row 2 pad 5** ☠ — pad 6 next to it swings 0 → −10 V | no |
| **demand** (drive voltage out of board 4) | **row 4 pad 6** = row 3 pad 6 | no |
| **drive out to the motor** | **row 3 pad 7** — the calibration prize | no |
| `F REF` to the display | row 4 pad 9 → row 1 pad 7 | no |
| black switch VAR/FIX selection | row 4 pad 3 | no |

### The rules

- ⭐ **Wires go to board connector pins**, where spares exist for boards 1–5. Any break, when
  one is finally justified, goes to a **brass staple** on the solder side — never to a pad.
  The film never sees the iron. **No spare flexicon exists.**
- ⚠ **Listen before driving.** Boards 2 and 4 are alive and pulsing. Driving a net before its
  break is made gives continuous, dynamic contention that would partially "work" — the worst
  kind of fault. ⭐ **The two-wire architecture is largely a way of obeying this rule by
  construction:** there is only one net the Pico drives, and it is an open-collector node
  designed to be shared.
- ⚠ **Rows 3 and 4 do not share a pinout.** Row 3 has −10 V on 8 and GND on 9; row 4 has
  −10 V on 7 and GND on 8. Never carry an assumption between them.

⚠❓ **How the Pico is physically mounted is contradicted between two published pages** and was
not settled on 6 September 2026. `technical-notes/fitting-the-controller/` says adhesive tape
and two cable ties onto the pillars, *"no glue, no drilling, no bracket"*; this file previously
said a printed bracket straddling the film. **Whichever it is: nothing mounts on, hangs from,
touches or is strain-relieved to the flexicon, and the Pico straddles the film with clearance.**

### ✅ The two checks that settled the power question

1. **The +10 V rail carries the Pico** through the **LM7805**, drawing whatever the Pico draws
   (~25 mA), and **no wire to the reservoir is needed.** See § POWER.
2. **The green LED net is fully understood:** the black switch grounds it, board 5 has no
   circuitry on it, and **there is nothing for the Pico to fight.** See § THE GREEN LED.

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

> ⚠ **Not used by the two-wire build.** The Pico never touches the drive voltage; board 3's
> hardware gate is the only gate. Kept because it is what any later phase would need, and
> because measuring board 3 pin 7 is still the best number in the project.


⭐ **The table's single home is
[`board-3-fvar-gate.md`](/GT2101/project-notes/board-3-fvar-gate/) §4.** It is deliberately not
repeated here.

⚠ **Why not:** those four figures once lived in **three files at once**, and that is precisely
the arrangement that produced the `V_IDLE` contradiction — one copy corrected, another still
carrying the withdrawn alarm six days later. **One fact, one home.**

**What the build needs from it:** drive is **proportional, with a hard mute at rest.** Lowest
speed is lowest voltage, rising roughly through the origin — what a brushless motor needs, since
back-EMF rises with speed. **"STILL = 10 V" is Board 4's loop railing to maximum demand with the
platter stopped, and Board 3 mutes it to 0 V.**

📄 `motor-overview/backplane.pdf` carries **both columns**, side by side on the row 3 pads, with
an up-arrow into pad 6 and a down-arrow out of pad 7:

        "O.C."
        STILL: 10V        STILL: 0V
        33: 1,2V          33: 1,2V
        45: 1,6V          45: 1,6V
        78: 2,4V          78: 2,4V ✓

📄 Read off `motor-overview/backplane.pdf` at 400 dpi, both columns.
*How "STILL = 10 V" survived so long:*
[`corrections-log.md`](/GT2101/project-notes/corrections-log/) §2.

### `V_IDLE` is 0 V — and Board 3 enforces it in hardware

**`V_IDLE` is 0 V, not 10 V.** The 1975 design never let 10 V reach a stationary platter:
Board 4's loop rails to maximum demand at rest and Board 3's gate mutes it to 0 V.

✅ **The hardware gate stays in circuit**, so `V_IDLE` and the ceiling in `drive.set_drive()`
are belt-and-braces agreeing with it, not the only braces. ⚠ **Give the LM358 its 10 kΩ output
pull-down anyway**, so idle is 0 V by hardware even if the PWM stops or the Pico hangs.

📄 not ✅ — these are the tracer's figures on a sheet marked PRELIMINARY. **Measuring Board 3
pin 7 on the running deck is the most valuable measurement left in the project.**

---

## ⭐⭐ `F VAR` — the one-wire way in — proposed 6 September 2026

**A proposal, not a build.** Read off sheets `3BSchem.pdf` and `3DSchem.pdf` at 400 dpi on
6 September 2026. Nothing here has been built or measured, and the one thing it depends on is
not yet known — see the session at the end, which needs no parts.

**The idea:** the original servo is a phase-locked loop, and `F VAR` is the frequency it locks
to. If the Pico generates `F VAR` instead of board 3's XR2207, the Pico sets the speed with
crystal accuracy while **board 4's PLL, board 3's gate and the motor PCB all keep doing exactly
what Gale designed.** The Pico never goes near the drive voltage, so the hardware mute stays
entirely in charge of the motor.

### What the drawings actually show

```
                        +10 V
                          │
                      [R pull-up]
                          │
   XR2207 pin 13 ─────────┼──────[ R ]────── 4011 pins 5 + 6 (strapped)
   "SQUARE OUT",                                      │
   open collector                               4011 gate B
                                                      │
                                              pin 4 ──┴──→ board 3 pin 5, `F VAR`
```

📄 **Sheet 3B.** Pin 13 is labelled `SQUARE OUT`. Its only path upward is through a resistor to
the XR2207's own **regulated `+V`** (its pin 1, behind a zener — ⚠ *not* raw +10 V), so it is an
**open-collector output**: it can pull the node down but cannot drive it up. A second series
resistor, marked only `R` by the tracer with no value, carries it on to the 4011.

⭐⭐ **Re-read 8 September 2026, and it makes the case stronger than the measurement did.** On
sheet 3B the XR2207's **pins 4, 5 and 7 are all drawn `NC`**, so **pin 6 is the only timing
terminal in use** — and pin 6 is the one fed from the `ORANGE` post. With that lead on the Pico,
**the timing network is open, the timing current is zero, and the VCO cannot oscillate as a
matter of topology.** The 0.05 V reading of 6 September is no longer the only argument; it is now
the confirmation of one. ⭐ And the level it sits at says the same thing from the other side: pad
5 low means the pin 13 node is **high**, i.e. the XR2207's output transistor is **off** and the
node is genuinely released for the Pico's.

📄 **Sheet 3D.** The 4011's pins 5 and 6 are strapped together, so gate B is wired as a plain
**inverter**, and its output on pin 4 leaves the board as `F VAR` (up-arrow into the circled ⑤).
⚠ Sheet 3D is footed `4011 MIRRORED!` — read the pin numbers the tracer wrote.

### ⭐ Why this is the cheapest injection point in the project

**The Pico can join that node in exactly the style the XR2207 already uses.** An NPN with its
collector on the pin 13 node and its emitter on GND is simply a second open collector in a
wired-OR. Three consequences:

1. **No pull-up is needed** — the board already has one, supplying the high level.
2. **Two open collectors on one node cannot fight destructively.** The worst case is a wrong
   frequency, not a damaged output. That is a very different risk profile from injecting onto
   a push-pull CMOS output.
3. ⭐ **The polarities cancel.** The NPN inverts, the 4011 inverts again, so board 3 pin 5
   follows the Pico pin the right way up. This is the one level-shift in the project that does
   not need its `config.py` polarity thought about — cf. § INTERFACING, where every other NPN
   shifter flips a signal.

**Parts: one BC547B and one base resistor, 1 kΩ–10 kΩ.** That is the entire interface.

### The frequencies

`F VAR` is **40 Hz per rpm**. That figure is forced by the display, not chosen: board 1 counts
`F DISPLAY` over the 250 ms window and shows the count ÷ 10 as rpm (see
[`board-1-display.md`](/GT2101/project-notes/board-1-display/)).

| Speed | `F VAR` | after board 4's ÷4 | tacho at 600 ppr |
|---|---|---|---|
| 33⅓ rpm | 1333 Hz | 333 Hz | 333 Hz ✓ |
| 45 rpm | 1800 Hz | 450 Hz | 450 Hz ✓ |
| 78 rpm | 3120 Hz | 780 Hz | 780 Hz ✓ |

⭐ **The two columns are arrived at independently and agree.** The display arithmetic (count ×
4 = `F VAR`) and the servo arithmetic (`F VAR` ÷ 4 = the tacho frequency the PLL locks to) give
the same number. That agreement is the evidence that `F VAR` really is the deck's speed command
rather than a display artefact. ⚠ It rests on the ~600 ppr figure, which is still 📄 — see
§ TACHO. **Measuring the tacho settles this table too.**

### ⭐⭐ What it does to the display — the bonus that removes the worst contention

**Restoring `F VAR` restores the original display chain, and the Pico then does not need to
drive board 1 at all.**

Follow the timebase chain through as it was settled on 5 September (see
[`board-1-display.md`](/GT2101/project-notes/board-1-display/) §3 and
[`board-2-touch.md`](/GT2101/project-notes/board-2-touch/)): board 2's MC14521 makes the 2 Hz
gate, board 2's 4016 selects `F VAR/FIX` when stopped and `INV TACH` when running, board 1
counts it over 250 ms and shows the result. **Give board 2 a good `F VAR` and the whole of
that works again by itself** — demand shown when stopped, real tacho speed when running,
exactly as Gale intended, with no Pico involvement.

⭐ **This matters more than it sounds.** § HOW THE PICO MEETS THE TOWER warns that boards 2 and
4 are alive and pulsing and that driving a net before its break is made gives continuous
dynamic contention — "the worst kind of fault". **Board 1's display is the single worst case of
that**, because it is the one subsystem the Pico already drives: bench sessions 4, 5 and 7 all
ran board 1 with **no other board connected**, while in a complete tower board 2 drives the
gate and `F DISPLAY`, board 4 supplies `F REF`, and board 1's reset runs back into board 2's
MC14521. Joining that loop would need several breaks in a flexicon with no spare.

**The `F VAR` route makes all of them unnecessary.** One injection point replaces four, and the
display work already done becomes a proven bench capability rather than something that has to
survive installation.

#### ⚠⚠ One thing has to be true for that, and it is not yet checked — 8 September 2026

The sentence above rests on board 2 knowing whether the platter is still or turning, because
**one mode bit moves both** the `F DISPLAY` source and the gate rate together. The pairing is
what makes the display read `33.3` in either mode:

| Mode | Source | Window | Count |
|---|---|---|---|
| stopped | demand, 1332 Hz | 2 Hz gate → **250 ms** | 333 → `33.3` |
| running | `INV TACH`, 333 Hz | 0.5 Hz gate → **1 s** | 333 → `33.3` |

**Stick that bit and the source and the window mismatch — the reading comes out about 4× wrong.**

⚠ That bit is thrown by board 3's pads 2 and 3, and
[`board-3-fvar-gate.md`](/GT2101/project-notes/board-3-fvar-gate/) §2a now shows those pads
tracing back to the **`ORANGE` post**, which Remora has left open.

⭐ **No extra work is needed to find out.** The display test already at the top of § NEXT *is*
the test: `fvar.rpm(33.3333)`, platter stopped, **expect `33.3`**. **A reading near `133` is
this, not the Pico, not the transistor and not the wire.**

### ❓ It may also dissolve the auto-lock fault — speculation, 6 September 2026

**Labelled a guess, on purpose.** Board 1's power-up phase problem has only ever been seen with
board 1 driven **in isolation**. In a complete tower the gate line free-runs at 2 Hz off board
2, and 4001 D parks the 4013 whenever the gate is low and `Q2` is 0 — so the divider may phase
itself within the first second, unaided. ⭐ The supporting argument: Gale shipped this deck, so
it cannot have needed a lock routine at power-up.

⚠ **Untested, and it changes nothing about what to do next** — the software fix in § NEXT is
still the thing to try, because the bench is where the work is. Full statement, and the caution
against letting it become an assumption, in
[`board-1-display.md`](/GT2101/project-notes/board-1-display/) §6a.

### ✅✅ MEASURED 6 September 2026 — the node is parked, and NO BREAK IS NEEDED

**Board 3 pin 5, tower powered, meter on DC volts, black probe on pin 9 (GND):**

| Condition | Reading |
|---|---|
| Black switch **released (VAR)** | **0.05 V** |
| Black switch **pressed (FIX)** | **0.05 V** |
| Fresh power-up, held and watched | stable — not drifting, not flipping |

⭐ **The XR2207 is not oscillating.** 0.05 V is a definite logic low, not a wandering average,
and it holds in both switch positions across a power cycle.

**So the entire `F VAR` interface is:** one **BC547B**, one **base resistor (1 k–10 k)**, one
wire. **Nothing is lifted, nothing is cut, no track is broken.** The Pico's transistor joins the
XR2207's output node in a wired-OR with a transistor that is permanently off — there is nothing
to fight.

### ⭐ Two things this measurement confirms beyond itself

1. ✅ **The `ORANGE` post finding is confirmed on hardware.** Sheet 3B was read at 400 dpi the
   same morning and predicted exactly this: the Helipot fed the VCO's control input directly by
   a flying lead, that lead is now on the Pico, so **the VCO has no control voltage and does not
   run.** Predicted from pencil, measured on the bench.
2. ✅ **The black switch does not affect board 3's output** — as
   [`flexicon-backplane-map.md`](/GT2101/project-notes/flexicon-backplane-map/) says it should
   not. The switch sits *downstream*, on board 5, choosing between `F VAR` and the fixed
   1332 Hz. Board 3 is upstream of it.

⚠ **A consequence worth knowing:** the test tower therefore has **no speed reference at all in
VAR** right now. If it were put on the deck with a motor, VAR would do nothing. That is not a
fault — it is the hole Remora is going to fill.

### ⚠⚠ Bench warning — pins 8 and 9 are adjacent, and confusing them shifts everything

📄❓ **Not yet confirmed, but it explains three readings taken before the clean one.** Board 3
has **−10 V on pin 8 and GND on pin 9, side by side.** With the black probe on pin 8 instead of
pin 9, every reading gains the whole negative rail — a pin sitting at 0 V reads as about +10 V.
Readings of 13.5 V and "bang on 10 V" were taken before the reference was settled and are
almost certainly this.

⭐ **The lesson is general: on this board, check the black probe is on pin 9 before believing
any number.** One reading of **pin 8 to pin 9** would confirm it and would also give the real
negative rail, which the archive only has on paper.

### ✅✅ BUILT AND PROVEN ON THE BENCH — 7 September 2026

**The transistor exists, it works, and it was built from salvage before the order arrived.**
Bench only — nothing has touched board 3.

| | |
|---|---|
| **Transistor** | an **NPN desoldered from a Quad FM4 board**. ⚠ Exact type not written down at the time — the candidates on the bench were **BC183L**, **BC413** and **ZTX650**. ⭐ **Write it on the part** |
| **Base** | **GP16**, through **10 kΩ** |
| **Collector** | **GP17** |
| **Emitter** | the ground pin adjacent to GP17 |

**The proof, from the Thonny shell:**

```
scan()            ->  LOW pins: [16]
find_collector()  ->  collector at: [17]
test()            ->  off -> 1
                      on  -> 0
```

⭐ **`off -> 1, on -> 0` is the whole requirement**: the transistor sits out of the way while the
Pico is idle, and pulls a pulled-up node down when the Pico says so. That is exactly what it will
do to the XR2207's output node.

⭐⭐ **The polarity works out with nothing to configure.** The NPN inverts, board 3's 4011
inverts it back, so **board 3 pin 5 follows GP16 directly.** Whatever square wave the Pico emits
is the square wave `F VAR` sees.

⚠ **GP16 is now spoken for** and belongs in `config.py` as the `F VAR` pin, alongside `POT_PIN`
and `LED_PIN` — which § FIRMWARE records as still hard-coded in `main.py`.

#### ⚠⚠ What went wrong first, and what it teaches

The evening produced two clean failures before it produced a result — `test()` returning
`on -> 1`, and `scan()` returning `LOW pins: []`. ⚠⚠ **Three things then changed at once, so the
cause was never isolated by experiment.** ✅ **Matt's own account, and it is first-hand: the
resistor in circuit was the wrong one.** Recorded as the cause. But all three of the following
are *sufficient* on their own, and each is worth knowing:

**1. ⭐ The base resistor was 960 kΩ, not 10 kΩ.** The Pico's internal pull-up is only ~50–80 kΩ,
so nearly a megohm in series leaves the base pin sitting around **3.1 V — a solid HIGH**. `scan()`
therefore cannot see the base **however good the transistor is and however good the contact**.
⭐⭐ **Use 10 kΩ or less for any discovery scan**, whatever the final circuit wants.

**2. The base is an OUTER leg on this transistor, not the middle one.** `L`-suffix parts
(BC182L/183L/184L) and Zetex E-line parts deliberately use a different lead order from the BC547,
and datasheet pages found by search **contradicted each other** about which.

**3. A BC214C was on the bench, and it is a PNP.** Every test here drives the base *up*, which
holds a PNP hard off — so it reads exactly like a dead transistor. ⚠ Not established as the part
actually in circuit when the tests failed, but it is the complement of the BC184 and it cannot
work as the `F VAR` sink, so it is worth knowing before it is reached for again.

⚠⚠ **The general lesson is the change discipline, not any one of the three.** Two hours went on
readings taken while the resistor, the transistor and the pin position were all uncertain
together. **Change one thing at a time, and re-run the scan after each.**

⭐⭐ **The test that settles species and base leg in a minute.** Meter on the **diode** range,
probes on the **bare legs**, ⚠ **never through a resistor** (a meter cannot push its test current
through 10 kΩ, so a good junction reads `0.L`). The base is the one leg reading ~0.65 V to
**both** others:

| Which probe sits on the base leg | Verdict |
|---|---|
| **Red** | **NPN** — usable |
| **Black** | **PNP** — wrong species |

Then swap the probes: both readings should be `0.L`. Four readings, no assumptions.

⭐ **And then let the Pico find the wiring**, rather than counting pins — `scan()` for the base,
`find_collector()` for the collector. On 7 Sept the base was assumed to be on GP15 and the scan
returned **GP16**: "bottom-left corner pin" flips depending on which face of the Pico is up.
**Never name a Pico pin by a corner or a direction.**

⚠ **Use a base resistor of 10 kΩ or less for the scan.** The Pico's internal pull-up is only
~50–80 kΩ, so with 960 kΩ in series the base pin sits near 3.1 V and reads HIGH — the scan
returns empty even with a perfect transistor and perfect contact.

### ✅✅ THE INJECTION POINT, FOUND AND MEASURED ON A SPARE BOARD — 7 September 2026

Done on **spare board 3 "B"**, unpowered, with a meter. Nothing connected, nothing risked. ⭐ The
whole `F VAR` path is now confirmed on hardware end to end, with no ❓ left in the middle — the
first chain in this project of which that is true.

#### ⚠⚠⚠ THE XR2207 IS A 14-PIN CHIP, NOT 16

**This cost an hour and it must not be rediscovered.** Counting the legs in a photograph settled
it: **seven per row.** Sheet 3B agrees — it draws pins 1–7 along the top edge and 14, 13, 12 …
along the bottom. So does the datasheet, whose highest pin is 14 (triangle out, marked NC here).

**Orientation: printing upright, notch on the LEFT.** Then:

| Row | Pins, left → right |
|---|---|
| **bottom** | 1, 2, 3, 4, 5, 6, 7 |
| **top** | 14, **13**, 12, 11, 10, 9, 8 |

⭐⭐ **`SQUARE OUT` pin 13 is the SECOND leg from the left along the top row.**

⚠⚠ Under the wrong 16-pin count it came out as the **fourth** from the left — which is **pin 11**,
and one leg beyond that is **pin 12, the negative supply**. Bench readings of 5.34 MΩ and
10.66 MΩ were correct measurements of the wrong leg, taken on my instruction.

⚠ **Ignore the round dimples.** Both chips carry moulding dimples at opposite corners. **The
notch is the index, and nothing else is.**

#### The MC14011CP numbers itself, by its own strapping

Found without counting anything: the **only adjacent pair that beeps to each other** are the
strapped inputs of gate B — **pins 5 and 6**. They sit **fifth and sixth from the left along the
bottom row**, so that chip is also **pin 1 bottom-left** with the printing upright, the same way
round as the XR2207. ⭐ Confirms the copper is un-mirrored even though two of the four sheets are.

#### ✅ The two resistors that never had values

| | Measured in circuit | |
|---|---|---|
| **pull-up** — XR2207 pin 1 (`+V`) → pin 13 | **10.66 kΩ** | almost certainly a 10 kΩ part |
| **`R`** — pin 13 → 4011 pins 5+6 | **10.16 kΩ** | likewise |

⭐ **Both are 10 kΩ. Both ❓ on sheet 3B are closed.**

⭐⭐ **What that means for the injection.** `+V` is the zener-regulated node, so the Pico's
transistor pulls pin 13 down through **well under 1 mA**. The 4011's input is CMOS and draws
nothing, so `R` carries no signal current at all — it is protection, not drive. **Nothing on
board 3 will notice the Pico arriving.**

#### ✅ The chain, link by link

```
XR2207 pin 13 ──┬─ 10.66 kΩ ─ +V                            ✅ measured
                └─ 10.16 kΩ ─ 4011 pins 5+6 (strapped)      ✅ measured
                                  └─ 4011 pin 4 ─ edge pin 5 = F VAR   ✅ beeps
```

⚠⚠ **Edge pin 5 is the 4011's OUTPUT** — the far end of this chain, not a place to inject.
**The transistor goes on XR2207 pin 13 and nowhere else.**

### ✅✅✅ THE GENERATOR — `firmware/fvar.py`, 7 September 2026

**The Pico now produces `F VAR`.** PIO, not a timer — rock steady and independent of the CPU.

| | |
|---|---|
| **Pin** | **GP16**, the transistor's base, through the 10 kΩ |
| **33⅓ rpm** | **1333.3334 Hz** — ⭐ *exact*. 125 MHz ÷ 93750 = 4000/3 with nothing left over |
| **45 rpm** | 1800 Hz, within ~0.001 % |
| **78 rpm** | 3120 Hz, within ~0.001 % |
| **Proof** | `fvar.check()` counted **2665 edges on GP17 in 2 s = 1332.5 Hz** ✅ |

⭐ **That reading proves two things at once:** the Pico's frequency, *and* that the salvaged FM4
transistor switches cleanly 1,333 times a second. Base and collector both verified at working
speed. ⚠ The 0.06 % shortfall is `time.sleep()` and the interrupt handler — **the measurement,
not the oscillator.** The PIO output is exact by construction.

**API:** `fvar.start(hz)` · `fvar.rpm(33.3333)` · `fvar.check()` · `fvar.stop()`.

⚠⚠ **ORDER OF OPERATIONS — this cost twenty minutes on 7 Sept.**

1. **Bench: three wires.** GP16 → 10 k → base, **GP17 → collector**, GND → emitter. `fvar.check()`
   needs GP17 to see anything.
2. **Then, and only then, remove the GP17 wire** — the tower node idles at **+10 V** and would
   destroy that pin.
3. Then the collector goes to XR2207 pin 13.

⚠ With GP17 removed, `check()` returns **0 edges**, `watch()` returns **all 1s** and `test()`
returns `on -> 1`. **That is a correctly working circuit with no collector wire**, not a fault.
`scan()` still returning `[16]` is the tell — the base side is independent of GP17.

### ✅✅✅ PROVEN LIVE IN THE POWERED TOWER — 7 September 2026, evening

**Board 3 pad 5 follows GP16 with the whole tower powered.** The `F VAR` chain is confirmed end
to end on hardware — Pico, transistor, XR2207 pin 13, the 4011, out to pad 5 — with **nothing
cut, nothing lifted, and no break in the flexicon.** ⭐ This is the measurement the whole
§ `F VAR` plan was waiting for.

**How it was proven.** GP16 held statically LOW then HIGH, five seconds each in a loop; meter on
DC volts, black probe on **board 3 pin 9**. Pad 5 clicks between its two levels in step with the
Pico.

### ✅✅ THE TWO LEVELS, MEASURED — 8 September 2026

**Board 3 pad 5 to pin 9, black switch RELEASED (VAR), GP16 on the 5-second loop:**

| GP16 | Pad 5 |
|---|---|
| LOW | **0.0071 V** — 7.1 mV, i.e. hard down |
| HIGH | **10.75 V** — the rail |

⭐⭐ **Rail to rail, and the healthy answer.** This closes the open item *"is the low end 0.73 V
or 7.3 V?"* — it is **7 millivolts**, better than either.

⭐ **And 10.75 V corroborates board 5 from an unrelated direction.**
[`board-5-power.md`](/GT2101/project-notes/board-5-power/) concluded the rails sit nearer
**±11 V** than the ±10 V the archive carries on paper. A 4011 output driven to 10.75 V says the
same thing, measured on a different board for a different reason. ⚠ **Worth remembering when any
figure on this deck is quoted as "10 V" — it is a nominal, not a measurement.**

⭐ **A meter reading of ~650 Ω to ground in the low state is the same fact, not a fault.** Seen
first on an auto-selecting meter that flipped to ohms when the voltage went away. A few hundred
ohms is what a CMOS output looks like pulling down at a 10 V supply; **open circuit or megohms
would have been the bad answer**, meaning the pin was floating rather than driven.
⚠⚠ **Lock the meter into DC volts rather than let it choose** — and never select ohms by hand on
a powered tower: the reading is meaningless and it can cost the meter's fuse. The 4011's output is switching cleanly, so what leaves board 3 is a
proper logic swing that board 4 can count, not a wobble in the middle that would read as a
constant high. ⭐ **The transistor, the base resistor and all three legs are confirmed correct by
this alone** — no leg needed counting.

⚠ **First reading of the session was 7.5 V, and it was the black switch.** ⭐ **This is a new
fact:** with the button **pressed (FIX)** pad 5 does not swing cleanly; released (VAR) it does.
📄 6 September recorded *"the black switch does not affect board 3's output"* — true then,
because the XR2207 was parked and there was nothing to affect. **With the Pico driving, the
switch position changes what pad 5 reads.** Not a fault and not a problem — in FIX the deck
ignores `F VAR` by design — but ⚠⚠ **every future reading on pad 5 must record the switch
position**, and any measurement that looks wrong should have the switch checked first.

⭐ **Refinement for the permanent joint:** land the wire on **the lead of the 10 kΩ pull-up
resistor** rather than the XR2207's leg. Same electrical node, and it keeps the iron off a
50-year-old chip — the same instinct as the flexicon's *solder to the brass staple, never the
pad* rule.

#### ⚠⚠ Two false alarms that cost an evening — neither was a fault

**1. `fvar.check()` returning 0 edges is CORRECT.** It counts on **GP17**, and GP17 comes off as
soon as the collector goes to board 3 (step 2 of the order of operations above). It cannot see
the tower node and was never meant to. ⭐ **The tell that all is well is `scan()` still returning
`[16]`** — the base side is independent of GP17.

**2. A multimeter cannot see `F VAR`.** At 1333 Hz a meter reads an average — roughly half the
rail, drifting — which looks exactly like a dead circuit. ⭐ **Hold the pin statically and watch
the reading move**, or use a scope. Never judge this circuit from a meter on a running square
wave.

⚠⚠ **And the rule this project already knew, broken again: a REPL snippet that toggles an output
needs a delay or a loop.** `p.value(0)` and `p.value(1)` pasted as a block run microseconds
apart — the LOW state is never measurable and the pin simply ends up HIGH. The working form:

```python
import time
from machine import Pin
p = Pin(16, Pin.OUT)
while True:
    p.value(0); print("LOW"); time.sleep(5)
    p.value(1); print("HIGH"); time.sleep(5)
```

#### ⭐ The divide-and-conquer test — keep this for any future injection fault

Black probe on **board 3 pin 9** throughout, GP16 toggling slowly on the loop above. Three
points; **the first one that does not flip is the fault.**

| Probe on | GP16 LOW | GP16 HIGH | If it does not flip |
|---|---|---|---|
| **A.** GP16 on the Pico | 0 V | 3.3 V | The Pico is not driving — most likely `main.py` grabbed the boot and is sat in its display loop |
| **B.** the transistor's collector | ~8–10 V | ~0.1 V | The transistor or one of its three wires. ⚠ The base is an **outer** leg on the salvaged FM4 part, not the middle one |
| **C.** board 3 pad 5 ⚠ **switch in VAR** | **0.007 V** ✅ | **10.75 V** ✅ | On a leg but not into the 4011 — power down, then check ~10 kΩ from that leg to the 4011's strapped pair |

⚠ **The pin-11 trap caught us again in conversation, not on the bench.** Recalled from memory
hours later, `SQUARE OUT` was reported as pin 11. It is **pin 13, second leg from the left along
the top row.** Pin 11 is BIAS and pin 12 next door is the negative supply — confirmed against the
Exar datasheet. ⭐ **The wire was on the right leg all along**; only the recollection was wrong.

### ⚠⚠ The black switch is NOT Remora's fallback — decided 7 September 2026

**Matt's decision: the black switch stays original.** It is the deck's 33⅓ / FIX selector and the
green LED's ground, exactly as Gale built it. **It is given no Remora role, nothing is wired to
it, and the safety case for `F VAR` injection does not rest on it.**

⭐ **What remains true, as original behaviour rather than as a feature:** board 5's black switch
selects between `F VAR` (row 5 pad 4) and the fixed 1332 Hz (pad 7), returning the choice to
board 4 pad 3 — so **in FIX the deck does ignore the Pico.** Worth knowing so it does not surprise
anyone at the bench. It is not a designed escape hatch and must not be written up as one.

⚠ **This withdraws the "one-button fallback" framing**, which stood in this file in four places:
§ What two wires buys, this section's old heading *"The fallback that makes the whole idea
safe"*, § NEXT, and § Open items. All four are corrected.

⚠ **The consequence is real.** The open question *"what does the deck do if the Pico stops
mid-record"* now stands on its own, with no button behind it. ⭐ **It is a question, not an
alarm** — that state is already the deck's resting condition, because the XR2207 has been parked
at 0.05 V since the Helipot's orange lead moved to the Pico, and nothing has misbehaved.

### ⭐ The session that settles it — needs no parts

**One goal: a frequency, or nothing.**

Scope on **board 3 pin 5**, deck powered, black switch released (VAR).

| Reading | Meaning |
|---|---|
| A steady square wave | The XR2207 is free-running. Plan on lifting pin 13 |
| Nothing, or a flat DC level | The node is free. No break needed — one transistor and a wire |

⚠ **Finding pin 5.** Board 3's pin 1 is +10 V and pin 9 is GND. Find the pin that beeps to
+10 V, call that 1, and count along. **Do not count legs from a moulding dimple** — these
packages have several.

⚠ **Scope, not a meter.** A meter on a 1.3 kHz square wave reads an average and tells you
nothing useful.

**What is *not* being done in that session:** nothing is unsoldered, nothing is lifted, no wire
is added and the flexicon is not touched. It is one probe on one pin.

---

## ⚠⚠ THE TOWER'S DISPLAY IS DEAD — and it is NOT Remora — 8 September 2026

**Found while running the `33.3` display test.** The display sits at **`00.0`** and nothing the
Pico does changes it. ⭐ **The cause is upstream of everything Remora touches, and it was in this
tower before today.**

### The measurements, in the order they were taken

Black probe on **board 2 pin 14 (GND)** throughout — ⭐ **ground is common across the tower, so
one ground point serves every board and you never have to re-find it.** ⚠ That also sidesteps the
row 3 / row 4 trap, where GND moves from pin 9 to pin 8.

| Pin | Reading | Meaning |
|---|---|---|
| board 2 **pin 7** | **~4–5 V** | ✅ the Pico's demand frequency has arrived — across board 3, board 5 and the black switch |
| board 2 **pin 8** | **~4–5 V** | ✅ `F DISPLAY` is live — board 2's MC14016 mux is passing the demand on to board 1 |
| board 2 **pins 3, 4** | **10 V** both | ✅ the STILL state, correct for a stopped platter |
| board 2 **pin 10** | **0.261 V, steady** | ❌ **the gate is dead** |
| board 2 **pin 13** | **0.007 V** | ✅ `RESET` from board 1 resting low, as designed |
| board 2 **pin 2** | **10.71 V, parked** | ❌ **no crystal arriving** |
| board 2 **pin 1** | 10 V | ✅ the rail |

**The chain: no crystal → the MC14521 has no clock → no gate on pin 10 → board 1 never opens a
counting window → it counts nothing → `00.0`.**

⭐ **It also explains why FIX made no difference.** Board 2 makes the fixed 1332 Hz from that same
clock. **One dead signal accounts for every symptom of the evening.**

### ✅ The backplane is cleared — continuity, powered down

| Probes | Result |
|---|---|
| board 4 pin 1 ↔ board 2 pin 1 | **beeps** — the control, both on the `+10 V` rail |
| board 4 pin 2 ↔ board 2 pin 2 | **beeps** — the crystal link is intact |

⭐ **The control test is what makes the second trustworthy** — without it, "no beep" could just
mean a miscount. **Use this pattern for any continuity check on this deck:** find a pair that
*must* be connected, prove the probes first, then move to the pair in question.

⚠⚠ **So the 1.048711 MHz is not being generated on board 4.** The link is fine; the source is not
producing. This is a **new fault on board 4**, whose page
([board 4 study](/GT2101/technical-notes/board-4-servo/)) is otherwise the cleanest in the archive.

### ⭐ What this does NOT stop

**The servo may be entirely unaffected.** Board 4 derives `F REF` by dividing the incoming `4×F`
(pin 3 → ÷4 → pin 9), **not** from the crystal. The crystal is generated on board 4 and *consumed
by board 2*, for the display timebase and the FIX reference. **So Remora's speed command can still
reach the motor with the crystal dead** — only the deck's own display and its FIX mode are out.

📄 Reasoning from the sheets, not yet measured. **The one reading that would settle it is board 4
pin 9** — see § NEXT.

### ⚠ Two suspects eliminated on evidence, not argument

1. **The reset-deadlock theory.** Boards 1 and 2 are a loop, so a jam looked plausible: board 1
   holds `RESET`, board 2's divider freezes, no gate, board 1 never advances. **Board 2 pin 13
   reads 0.007 V** — resting low, exactly as designed. **Withdrawn.**
2. **The `ORANGE` post consequence** (§ `F VAR`, and
   [`board-3-fvar-gate.md`](/GT2101/project-notes/board-3-fvar-gate/) §2a). Pads 2 and 3 read
   **10 V**, which sheet 3C annotates as `STILL` — correct for a stopped platter — **and pin 8 is
   carrying the demand**, which is what a working mux does. ⭐ **So the mux is not stuck and this
   is not the cause of `00.0`.** ⚠ The wiring finding stands and stays open; **its predicted
   consequence did not appear.** It should be re-tested once the display works.

⚠⚠ **A caution worth keeping.** The morning's paper audit predicted a display fault and named a
cause; the evening found a display fault with a *different* cause. **A prediction that half comes
true is the most misleading kind.** Had the gate not been metered, the `00.0` would have been
filed against the `ORANGE` post and the real fault would still be here.

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

> ⭐ **The two-wire build needs one of these: the `F VAR` shifter**, and that one is unusually
> easy — see § `F VAR`. Everything else below belongs to a later phase. **Read it before
> building anything for phase 2, not before phase 1.**

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

### ⚠⚠ Green LED — the 10 V install needs an NPN, and the bench does not

The 1 kΩ series resistor is on Board 1, so on the bench a Pico pin sinks connector pin 8
directly with no parts. **That does not survive the move to 10 V** — and the difference is the
*off* state, not the on state:

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

⚠ **Read `folder-findings.md`'s *"9.18 V selected / 0 not"* the right way round:** **~9 V is
LED OFF** (board 1's own pull-up, read back through the LED) and **0 V is ON**. A passive
switch and GP5 open-drain are both sinks — **there is nothing for the Pico to fight.**

⭐ **GP5 in session 6 was standing in for the black switch** — same node, same direction. That
is why one wire and no components worked.

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

### ⚠ There is no DC-DC converter — it is the LM7805, on a new input

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

### ⚠⚠ Switching noise — an open concern, and the one that could spoil the deck

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

⚠⚠ **It is not that simple on a Pico W** — and the older "quiet supply *or* WiFi, not both"
line in this file was too absolute. 📄 On a Pico W, **GP23 is reassigned to `WL_ON`** (wireless
power on) and **the SMPS mode pin moves to `WL_GPIO1`, a pin on the CYW43 wireless chip.** So it
is still reachable, but only after powering up and initialising the radio — i.e. you would be
switching on a radio SoC inside the plinth in order to make the power supply quieter.
❓ Whether MicroPython exposes `WL_GPIO1` conveniently has not been checked.

### ✅✅ DECIDED 6 September 2026 — plain Pico for phase 1

**Build phase 1 on the plain Pico. Buy the W anyway and keep it in the drawer for phase 2.**

The two-wire architecture settled this, because it removed the W's entire reason for being on
the list:

- ⭐ **On the two-wire build the Pico is blind, so a web monitor has nothing to show.** It knows
  the pot position and the frequency it just commanded — and the deck's own display already
  shows both, on the turntable, better. **The page would be a worse copy of the front panel.**
  The monitor earns its keep the moment `TACH` comes in, and not before.
- **This is a turntable, and Howie's tower is local evidence that modern electronics in this
  tower can be heard.** Given a choice between a quieter supply and a feature that cannot be
  populated yet, quiet wins.
- ⭐ **The decisive one: during bring-up the Pico is on the bench with USB attached, so the
  serial console is already the development instrument** — quieter and simpler than a web page.
  The page only matters once the deck is closed up and playing, **which is exactly when a radio
  in the plinth is least welcome.**
- **It is a genuine drop-in, so this is reversible.** GP numbering is identical and none of the
  wires in use clash. Swapping later is a swap, not a redesign.

⭐ **And the Pico 2 / RP2350 argument is void too.** `parts-to-order.md` justified it as giving
"the servo loop more headroom" — but **on the two-wire build there is no servo loop in the
Pico.** It emits a square wave between 1.3 and 3.1 kHz. That is a **PIO** job: rock-steady,
jitter-free and independent of whatever the CPU is doing. An RP2040 will not notice it is
happening.

100 µF + 100 nF across the 7805's input and output remains ordinary good practice, and keep
the Pico away from the `TACH` wiring when it is mounted.

✅ **Side effect: row 5 pad 9 = `GND` is now confirmed.** It was 📄 from the FANATSON sheet
and had never been checked against the part. Carrying the Pico's supply return proves it.
First of row 5's pads 3–9 to be confirmed — see `flexicon-backplane-map.md` §7.

❓ **Not yet recorded: where the 5 V lands on the Pico.** It must be **VSYS (pin 39)**, not
VBUS (pin 40). VBUS is the USB rail and an external supply on it fights the cable. Confirm
and record.

### The +15 V input — superseded as to its INPUT only

Kept because it is how the +10 V question came to be asked, and because the reasoning about
the deck's rails is still correct.

`GaleTT5Schem.pdf` shows +10 V made from +15 V via a 560R and a shunt zener — that alone
gives only ~9 mA, far less than the display needs, so **+15 V** was first taken straight off
the 4700µF reservoir. ±15 V is unregulated and may sit at 16–18 V unloaded.

Built: **+15 V → LM7805 → Pico VSYS (pin 39) / GND (pin 38)**. Heatsink **cold** at the
Pico's ~25 mA (≈0.25 W). Rule of thumb for Matt: too hot to keep a finger on = needs help.
The LED display runs from the deck's own +10 V rail, not from the 7805.

✅ **The tower's +10 V rail carries it.** The 7805 is fed from the backplane now, and sheds
half the heat doing it.

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

✅ **The green LED already has a job: it is the 33⅓ / FIX indicator**, grounded by the black
switch — see **§ THE GREEN LED above.** A lock indicator (out when stopped, flashing through
the 4 s soft-start ramp, steady once the tacho says the platter is in tolerance) is the obvious
second job, but ⚠ it only works while the black switch is in **VAR**, and it overrides an
original function.

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
| 13 | **8 Sept** | ⭐⭐⭐ **`F VAR` PROVEN END TO END ACROSS THE TOWER — and a pre-existing tower fault found.** Pad 5 measured **10.75 V / 0.0071 V** ✅, and the Pico's signal traced as far as **board 2 pin 7 and pin 8**, both showing a mid-rail average — so it crosses board 3, board 5, the black switch and board 2's mux. ⚠⚠ **But the display sits at `00.0`.** Cause found and it is nothing to do with Remora: **board 2 pin 2 has no crystal** (parked at 10.71 V), so its MC14521 has no clock, so the gate on pin 10 is dead (**0.261 V**, steady), so board 1 never opens a counting window. ✅ **Backplane cleared** — board 4 pin 1 ↔ board 2 pin 1 and board 4 pin 2 ↔ board 2 pin 2 both beep, powered down. **So the 1.048711 MHz is not being produced on board 4.** See § THE TOWER'S DISPLAY IS DEAD. ⭐ Two suspects eliminated on evidence: board 1's RESET rests correctly at **0.007 V** (no reset deadlock), and pads 2/3 read **10 V = STILL**, correct for a stopped platter |
| 9 | **6 Sept** | ⭐⭐ **`F VAR` measured on board 3 pin 5 — the node is parked at 0.05 V**, stable, in both black-switch positions and across a power cycle ✅. **So the two-wire injection needs no break**: one BC547B, one base resistor, one wire. ✅ Confirms on hardware that the XR2207 has no control voltage, which sheet 3B had predicted that morning. ✅ Confirms the black switch is downstream of board 3. ⚠ Three earlier readings (13.5 V, 10.0 V, 0.4 V) are attributed to the black probe sitting on pin 8 (−10 V) instead of pin 9 (GND) — 📄❓ not confirmed. **Also: all four Pico firmware files copied off the Pico into the repo**, and the pin map found to be split between `config.py` and `main.py` |
| 12 | **7 Sept** | ⭐⭐⭐ **THE PICO EMITS `F VAR`.** PIO square wave on **GP16** at **1333.3334 Hz** — exact, because 125 MHz divides into 4000/3 with nothing left over — and **GP17 counted 2665 edges in 2 s = 1332.5 Hz** ✅, so the salvaged FM4 transistor is switching cleanly at working speed. The 0.06 % shortfall is the software stopwatch, not the oscillator. `firmware/fvar.py` written. ⚠ Twenty minutes lost to my own instruction: GP17 had been correctly removed ready for the tower, and I then asked for tests that watch GP17. **Bench-verify with three wires; remove GP17 only as the last act before the tower** |
| 11 | **7 Sept** | ⭐⭐ **The whole `F VAR` path confirmed on a spare board 3, unpowered** — pin 13 identified, **pull-up 10.66 kΩ**, **`R` 10.16 kΩ**, 4011 pin 4 beeps to edge pin 5 ✅. Both resistor ❓ closed. ⚠⚠ **And the XR2207 found to be a 14-PIN chip, not 16** — my count had sent the probe to pin 11, one leg from the negative supply |
| 10 | **7 Sept** | ⭐⭐ **The `F VAR` transistor built and proven on the bench** — base **GP16** through 10 kΩ, collector **GP17**, emitter to GND; `off -> 1`, `on -> 0` ✅. Built from an **NPN salvaged off a Quad FM4**, because the September order had still not arrived. ⚠ Two earlier failures (`on -> 1`, then `LOW pins: []`) are attributed by Matt to **the wrong base resistor being in circuit — 960 kΩ, which the Pico's own pull-up cannot overcome.** Two other sufficient causes were live at the same time and none was isolated: the base is an **outer** leg on this part, and a **BC214C (a PNP)** was on the bench. ⭐ The Pico self-discovery scans found the wiring with no pin counted, and corrected a base assumed to be on GP15 to **GP16** |
| 8 | **3 Sept** | ⭐ **The Pico runs on the tower's own power.** +10 V off **board 5 pad 2**, GND off **pad 9**, into the **LM7805**, 5 V out to the Pico; the regulator sits in the void under board 5. Self-starting, LED blinking, no bench supply to the Pico ✅. **Confirms row 5 pad 9 = GND** — the first of that row's pads 3–9 off the sheet ✅. **Green LED net metered end to end** (board 5 pad 1 → board 1 pad 5) and confirmed to have nothing else on it — not GND, not the +10 V rail ✅. **Both rebuilt supply rails on the flexicon mapped pad by pad** ✅. All three display digits good |

---

## STATUS, 6 September 2026

**Bench sessions 1–8 complete.** The deck's speed pot reads into the Pico, the Pico runs on the
tower's own power, all five boards are identified from their own etched part numbers and studied
from their own drawings, and — on the bench, board 1 alone — the display and the green LED both
answer to the Pico.

⭐⭐ **The architecture changed on 6 September 2026 and got much smaller.** See § ARCHITECTURE:
**Remora is two signal wires** — the Helipot's orange wiper in, `F VAR` out. The Pico is a
digital replacement for the XR2207 and nothing else.

⚠ **What that does to the eight bench sessions.** Nothing is wasted, but the display and green
LED work is now **a proven bench capability rather than part of the build** — in the tower those
boards do their own jobs. The Helipot work and the power work are directly on the critical path.

✅ **The parts are ordered — 4 September 2026, awaiting delivery.** ⚠⚠ **Most of them are now
phase 2 or later.** See § the parts, below, and
[`parts-to-order.md`](/GT2101/project-notes/parts-to-order/). **Log what is actually in the box
before anything is built.**

Equipment: spare boards 1–5, a spare motor PCB, a spare motor, a DMM, bench supply and scope.
✅ **And two towers** — Howie's on the deck, Alex's on the bench. See § THE DECK.

### The parts, against the two-wire build

| | |
|---|---|
| **Needed now** | ✅✅ **SATISFIED 7 September 2026, from salvage** — an NPN off a Quad FM4 and a 10 kΩ. The `F VAR` interface is **built and proven**. The BC547B and the E12 assortment are still wanted, but nothing is blocked on them |
| **Still missing and still wanted** | the **E12 assortment** — you need that one base resistor, and it is one of the things that did not arrive |
| **Phase 2** | the **J113** ×5, for `TACH` in |
| **Not needed at all now** | the **LM358**, its two-stage RC filter and its 10 kΩ pull-down. That circuit existed to inject the drive voltage, which the two-wire build does not do |
| **Not needed yet** | the touch divider (27 k + 10 k + 1 k), the display level shifters, the green-LED NPN, most of the perfboard |

⭐ **The Kapton tape is still the most useful thing in the order** — see
[`parts-to-order.md`](/GT2101/project-notes/parts-to-order/).

---

## NEXT

**One session, one goal, one measurable outcome.**

### ~~The critical path~~ — ✅✅ BOTH HALVES DONE

- ✅ **6 Sept: board 3 pin 5 measured at 0.05 V**, stable, both switch positions. The node is
  parked, the XR2207 is not running, **the injection needs no break.**
- ✅ **7 Sept: the transistor is built and proven** — base GP16 through 10 kΩ, collector GP17.
  See § `F VAR`.

### ⭐⭐⭐ THE NEXT SESSION — **board 4 pin 9, one reading** — set 8 September 2026

✅✅ **The wire is in and proven.** § THE TOWER'S DISPLAY IS DEAD has the evening's full trace:
the Pico's `F VAR` reaches **board 2 pin 8** in good order, across three boards and the black
switch, with nothing cut. **Everything below this heading is finished work, kept for the record.**

**One goal: does board 4 act on the Pico's signal?**

The deck's display cannot answer that any more — board 4's crystal has stopped, so board 1 counts
nothing and shows `00.0` whatever anyone does. ⭐ **But board 4 pin 9 can answer it, and it needs
no display, no scope and no new parts.**

1. `import fvar` · `fvar.rpm(33.3333)`. Black switch **released (VAR)**.
2. Black probe on **board 2 pin 14** — ⭐ ground is common; do not go hunting for board 4's, which
   is on **pin 8**, not pin 9 like board 3's.
3. Red probe on **board 4 pin 9**.

| Reading | Meaning |
|---|---|
| **~5 V**, mid-rail | ⭐⭐ **Board 4 is receiving the Pico's `F VAR` and dividing it.** The deck's servo half is obeying Remora — the two-wire architecture demonstrated without a working display |
| **parked at a rail** | It stops at board 4. A separate chase, and the crystal fault is then the first suspect |

⚠ **Mid-rail means a signal, parked means nothing** — the opposite of the usual intuition,
because the meter is showing the average of a square wave.

### Then, separately — board 4's crystal

A **tower repair**, not a Remora job, and worth its own session. Cheap first checks: board 4
**pin 1** for the rail, whether the board is fully seated, then the oscillator itself.
⚠ **Do not pull boards to reseat them casually** —
[`flexicon-backplane-map.md`](/GT2101/project-notes/flexicon-backplane-map/) §8: the stiffened
film should come on and off *less* now, not more.

### ~~The old next session~~ — ✅ DONE 8 September 2026



✅ **The generator is done** (7 Sept, § THE GENERATOR) and ✅ **the injection point is measured**
(7 Sept, § THE INJECTION POINT). Everything below is the last step.


**One goal: the deck's own display reading `33.3` off the Pico's crystal.**

1. ⚠⚠ **The collector goes onto XR2207 pin 13 — NOT board 3 pin 5.** ⚠ **Corrected 7 September
   2026; this step said "onto board 3 pin 5" and that is wrong and would risk the 4011.** Pad 5
   is the **4011's push-pull output**, so a transistor there fights a 50-year-old CMOS driver.
   The injection node is the **open-collector node upstream of the 4011** — XR2207 pin 13, with
   the board's own pull-up on it. ⭐ **This is what "the board supplies the pull-up" and "the
   polarities cancel" have always meant**: the NPN inverts, the 4011 inverts back, so **pad 5
   follows GP16**. Injecting at pad 5 would give neither.
2. **A common ground** between Pico and tower — board 3 **pin 9** (⚠ pin 8 alongside it is
   −10 V), or the LM7805's own ground if the Pico is already running off board 5 pad 9.
   ⚠⚠ **Take the GP17 wire off first.** That node idles at **+10 V** and would destroy the pin;
   GP17's only job was the bench proof and it is finished.
3. **A square wave out of GP16 — 1333 Hz for 33⅓.** ⭐ A **PIO** job, not a timer: rock-steady
   and independent of whatever the CPU is doing.
4. **Watch the deck's own display.** ⭐ **The display is the instrument** — board 1 counts
   `F DISPLAY` over a 250 ms window, so it reads `F VAR` straight back to you. No scope needed
   to know whether this worked.
   ⚠⚠ **Read the wrong answers properly — added 8 September 2026.** `33.3` is the pass.
   **Something near `133`, or a digit pattern 4× out, is not a Pico fault** — it is board 2's
   display mux stuck, because board 3's STILL/TURNING pads are fed from the now-open `ORANGE`
   post. See § `F VAR` and [`board-3-fvar-gate.md`](/GT2101/project-notes/board-3-fvar-gate/)
   §2a. **Blank or unchanging digits** is the old power-up phase problem, also not this wire.

⚠ **Black switch in VAR**, or the fixed reference is selected and the Pico is ignored.
⚠ **Not a fallback** — the switch stays original and Remora's safety case does not rest on it.
See § `F VAR`.

⚠ **Finding board 3 pin 5:** pin 1 is +10 V and pin 9 is GND. Find the pin that beeps to +10 V,
call that 1, and count along. **Do not count legs from a moulding dimple** — these packages have
several. ⚠⚠ And **pin 8 is −10 V, adjacent to pin 9** — check the black probe before believing
any number.

### Also needs nothing

1. ~~Copy `config.py` into `firmware/`~~ — ✅✅ **done 6 September 2026.** All four files that
   exist on the Pico are now in the repo. ⚠ **And `config.py` turned out not to be the whole pin
   map** — `POT_PIN` and `LED_PIN` are hard-coded in `main.py`. Moving them into `config.py` is
   two lines and makes its own header honest. See
   [`firmware/`](/GT2101/project-notes/firmware/).
2. ~~Confirm the VAR/FIX selector~~ — ⚠ **No longer load-bearing, 7 September 2026.** The black
   switch stays original and is not Remora's fallback (§ `F VAR`), so this stopped being the
   safety argument for anything. 📄 For the record only: the flexicon map's signal chain has the
   **black switch on board 5** selecting between `F VAR` (pad 4) and the fixed 1332 Hz (pad 7),
   returning the choice to board 4 pad 3.
3. ⭐ **One reading whenever convenient: board 3 pin 8 to pin 9.** Gives the real negative rail,
   and confirms the pin-8/pin-9 probe trap in § `F VAR`.
3. **Does the test tower have a flexicon of its own?** One look, and it decides whether the
   restored film can come out of the tower that is about to be experimented on.
4. **Measure the tacho frequency** on the deck as it stands — one scope probe, and it confirms
   the `F VAR` table from the other end. ⚠ Scope, not a meter: it swings 0 to −10 V.

### ⚠ Demoted by the two-wire architecture

**Board 1 auto-lock** was the most annoying recurring fault. On the two-wire build the display
runs on its own original chain, so **the fault may not exist in a complete tower at all** —
see [`board-1-display.md`](/GT2101/project-notes/board-1-display/) §6a. ❓ Speculation. Still
worth trying the free software fix on the bench, but it is no longer on the critical path.

---

## Open items

**Measurements that turn 📄 into ✅ — in value order**

- ⭐ **Board 3 pin 7 on the running deck**, at each speed. Four numbers that are the whole
  specification for `drive.nominal_drive()` and the safety ceiling. **The most valuable
  measurement left in the project.**
- ⭐ **The tacho pulses per revolution** — expect ~600 per platter turn, ~333 Hz at 33⅓.
  `bench.tacho()` settles it in five minutes and nothing else changes the answer.
- ~~Board 3 pin 5 with the XR2207's control input open~~ — ✅✅ **CLOSED 6 September 2026:
  0.05 V, parked, both switch positions. No break needed.** And ✅✅✅ **the injection itself is
  proven live in the powered tower, 7 September 2026** — see § `F VAR`.
- **Board 2 pad 6's real swing** — one DC-volts reading decides whether that pad is dangerous
  or ordinary logic. The ☠ warning stands until it is taken.
- The tower gap the Pico has to straddle (~12 mm for a socketed Pico). **Nothing is printed
  until that number exists.**
- Display current with all eights lit.
- The Helipot's resistance — label says 1 kΩ, one bench reading said 10 kΩ. Affects no wiring.
- Board 5's etched part number; issue letters on boards 1, 2 and 5.
- ⚠ **The spare motor's suspected fault.** ⭐ Check the encoder disc by eye *before* reaching for
  the meter — a shattered disc explains a dead motor completely, and the archive already holds a
  photograph of a shattered one. See § THE DECK.
- ❓ **Confirm the spare board 5 exists** — recorded on Matt's own hedge, not on a look.

**Decisions nobody has taken**

- ~~Plain Pico or Pico W~~ — ✅✅ **decided 6 September 2026: plain Pico for phase 1**, W in the
  drawer for phase 2. See § POWER. ⭐ The Pico 2 / RP2350 case is void with it — there is no
  servo loop in the Pico on the two-wire build.
- ⚠⚠ **Switching noise on the +10 V rail is an open concern**, not a closed one. The Pico
  carries its own buck-boost converter on VSYS, and Howie's tower is evidence that a
  microcontroller inside a GT2101 tower can be audible. See § POWER.
- Which of the three touch options to use.
- The speed range the ten Helipot turns map onto — full 30–80 rpm, or a trim band around the
  three standard speeds.
- ⭐ **What the deck does if the Pico stops mid-record.** `F VAR` vanishes and board 4's PLL
  loses its reference. **This replaces the withdrawn "confirm the VAR/FIX selector" item**, which
  only mattered while the black switch was being treated as a fallback (§ `F VAR`, 7 Sept 2026).
  ⭐ Not urgent — that is already the deck's resting state today.
- ~~The values of board 3's series `R` and the XR2207 pin 13 pull-up~~ — ✅✅ **CLOSED
  7 September 2026: both 10 kΩ** (pull-up 10.66 kΩ, series 10.16 kΩ), measured on spare
  board B. See § `F VAR`.

**Housekeeping**

- ⚠ **Log what the parts box actually contains** against
  [`parts-to-order.md`](/GT2101/project-notes/parts-to-order/), **before anything goes on the
  perfboard.**
- ⚠⚠ **The order is back-to-front against the work.** Every active device arrived; almost none
  of the passives did. **One E12 resistor assortment and five J113s unblock the entire build**,
  and both are pennies.
- **Record where the Pico's 5 V lands** — VSYS (pin 39), not VBUS (pin 40).
- **Copy `config.py` into [`firmware/`](/GT2101/project-notes/firmware/).** Eight of the nine
  firmware files exist nowhere but on the Pico, and `config.py` is the only record of which GP
  pin goes to which wire.

### ✅ Closed

Parts ordered (4 Sept) · the tacho front-end is a **J113 JFET** · the Helipot is **ten turns**
and **electrically off board 2** · the Pico **can** drive the green LED, and **what it
indicates is already decided** (33⅓ / FIX) · **board 5 does not ground the LED net** — the
black switch does · the **+10 V rail can carry the Pico** through the LM7805, no wire to the
reservoir.

*Accounts of the wrong answers along the way:*
[`corrections-log.md`](/GT2101/project-notes/corrections-log/).
