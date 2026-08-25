---
layout: bare
title: GT2101 — A Modern Controller
permalink: /GT2101/technical-notes/pico-controller/
description: "Rebuilding the Gale GT2101's control logic on a Raspberry Pi Pico while keeping the original display, power supply, controls and motor — an ongoing restoration record."
show_archive_banner: true
archive_note: >
  An ongoing project to replace the GT2101's 1970s control logic with a microcontroller while
  leaving every other original part in place. Recorded as it happens, including the wrong turns.
---

# A modern controller for the GT2101

An ongoing attempt to put new control logic into a GT2101's control tower using a Raspberry Pi
Pico, while keeping **everything else original** — the original power supply, the original LED
display, the original front-panel controls, the original motor and motor PCB, the original wiring.

This page is written as the work happens, and it includes the mistakes. Status markers as
elsewhere on this site: ✅ confirmed against the hardware · 📄 from a document · ❓ unverified.

---

## The principle: the Pico is brains only

The five boards in the tower divide cleanly into logic and everything else.

| Board | What it is | In the rebuild |
|:--:|---|---|
| 1 | Display — a three-digit frequency counter | **stays**, driven directly by the Pico |
| 2 | Capacitive touch start/stop; also the display's timing | **stays**, as the touch sensor |
| 3 | `F VAR` oscillator and the drive-voltage gate | **removed** |
| 4 | Crystal, reference divider, tacho front-end, the servo | **removed** |
| 5 | Power supply and the interface to the motor | **stays** |

**Boards 3 and 4 are one servo split across two boards** — board 4 decides the drive voltage,
board 3 decides whether it is allowed out — so they leave together. Neither is modified. They
unplug, and they can be plugged back in at any time; the deck can be returned to 1976 in about a
minute.

The Pico's carrier board takes slot 3, where its edge fingers meet the original backplane.

### Where the Pico connects

| Job | Where | How |
|---|---|---|
| Speed setting | the Helipot on board 2 | passive — straight into an ADC pin ✅ working |
| Start/stop | board 2's touch pulse | two-resistor divider, edge interrupt |
| Display | board 1, three signals | ✅ working |
| Tacho | the `TACH` net | JFET inverter — see below |
| Drive out | board 3's output net | op-amp buffering filtered PWM |

---

## Driving a 1975 display without modifying it

✅ **Achieved August 2026.** Board 1 is a frequency counter: an MC14553 counts pulses for a gated
window, an MC14511 decodes the total, and the decimal point is hardwired so it can only ever read
`NN.N`.

The obvious approach — emit a frequency and let the board measure it — requires knowing the gate
window exactly. The approach that works is to take the board's own clock line as well, and drive
the whole counting cycle deliberately: close the gate, command a latch and reset, open the gate,
send *a counted number of pulses*, close the gate, command the latch. The displayed value is then
exact by construction, with no dependence on window length at all.

Two things learned on the bench that are not in any drawing:

- ✅ **The board counts while its gate line is LOW.**
- ✅ **The latch/reset chain runs a four-state cycle**, one state per clock pulse: latch, hold,
  reset, hold. **The reset is a state, not a pulse** — while the chain sits in it, the counter is
  held clear and cannot count. Anything loaded during that state is discarded. That behaviour cost
  an hour to find and is the single most useful thing known about this board.
- ✅ The digits going dark during the reset state is a usable landmark: once the controller has
  seen it, it knows where it is in the cycle and stays in step indefinitely.

❗ The cycle's phase is lost at every power-up, since the flip-flop chain comes up in a random
state and nothing on the board resets it. Reading the board's own `RESET` output back into an
input fixes this — one wire and one resistor.

✅ The display's green LED already has its 1 kΩ series resistor on the board (measured 966 Ω in
circuit), about 8 mA at 10 V, so a microcontroller pin can sink it directly with no driver.

---

## Levels: 3.3 V against 10 V CMOS

The original boards run 10 V CMOS. Useful findings:

- ✅ **The Helipot and the speed switch need no level shifting at all** — both are passive.
- ✅ **Both display boards examined work at 5 V**, so bench work can be done with the display
  driven directly from the microcontroller and no level shifters anywhere. Level shifting is only
  needed for the final 10 V installation.
- Going up (3.3 V → 10 V) is a handful of NPN inverters. Coming down (+10 V → 3.3 V) is a divider.
- ⚠ **Do not reach for an off-the-shelf level-shifter module.** The common ones top out at 5.5 V.

### The tacho input — a trap worth documenting

The tacho swings **0 V to −10 V**. It will destroy a 3.3 V input if connected directly.

The plan first written down for this project was a PNP inverter with its emitter at 3.3 V and the
tacho brought to the base through a resistor. **It cannot work**: at 0 V *and* at −10 V the base
sits well below the emitter, so the transistor conducts in both states and the output never
changes. It would have wasted a bench session.

The correct answer is the one Gale used in 1976 — a single N-channel JFET in common source, gate
to the tacho, source to ground, drain pulled up to the logic supply. On at 0 V, pinched off at
−10 V. See [the board 4 page](/GT2101/technical-notes/board-4-servo/) for the original circuit.

---

## The safety issue at the centre of this rebuild

📄 The drive voltage is proportional to speed — 1.2 V, 1.6 V, 2.4 V for 33⅓, 45 and 78 rpm — but
with the platter stopped the servo's demand rails to **10 V**, and board 3 mutes it to **0 V**
before it can reach the motor.

⚠ **Removing board 3 removes that protection.** The 1975 design never let 10 V reach a stationary
motor; software now has to be the thing that doesn't. The idle drive value and a hard ceiling on
the output stop being a second line of defence and become the only one. This is the failure that
would destroy the motor PCB's output transistors.

Anyone attempting a similar rebuild should note that the widely repeated figure of "10 V at
standstill" is the *input* to that gate, not what the motor receives.

---

## Firmware shape

Eight modules, so each subsystem can be brought up on its own, with a single settings file that is
meant to be the only one edited: tacho, display, controls, drive, controller, main, and a bench
module that exercises each part separately. Notes that may be useful to others:

- Tacho edges are timestamped into a ring buffer one revolution long, and the measurement window
  is **chosen by state** — short while spinning up, longer while running, a full revolution for
  the display. A single long window makes the loop oscillate; lag is the problem, not noise.
- The integral term is clamped harder during start-up so the proportional term supplies the
  acceleration and the integral does not wind up and overshoot.
- Fault codes distinguish *pulses seen then lost* from *no pulses ever*. A seized platter triggers
  both conditions, and the distinction is what tells you whether to look at the platter or at the
  wiring.

---

## Progress

| Date | Outcome |
|---|---|
| 19 Aug 2026 | Microcontroller programmed and self-starting ✅ |
| 19 Aug 2026 | Regulator from the deck's own +15 V rail; runs on deck power, regulator cold ✅ |
| 20 Aug 2026 | The deck's Helipot read into an ADC input, full sweep ✅ |
| 21 Aug 2026 | **`12.3`, `45.0`, `78.0` and `33.3` on the original 1975 display**, board otherwise untouched ✅ |
| 22 Aug 2026 | Boards 2, 3 and 4 read from their drawings; the architecture settled |

**Next:** the display's auto-lock wire, then the touch input, then the tachometer.

---

## What this exercise has been good for

Rebuilding the logic has meant reading every board properly, and that has corrected a good deal of
what this archive previously said — that board 2 was a servo, that board 3 generated the drive
voltage, that board 3 was an optical sensor, that "disk 2" was two boards. **Every one of those
came from inherited prose with no stated source, and every one fell over on contact with the
hardware.** The 2015 hand tracings, by contrast, have held up.

The deck being rebuilt still has its original 2009-era replacement controller fitted and working,
so none of this is being done under pressure. That is the only reason it has been possible to stop
and check each claim rather than guess.
