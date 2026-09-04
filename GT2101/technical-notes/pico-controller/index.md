---
layout: bare
title: "GT2101 — The Remora"
permalink: /GT2101/technical-notes/pico-controller/
description: "Adding a Raspberry Pi Pico to the Gale GT2101's control tower without removing a single original board — an ongoing restoration record."
show_archive_banner: true
archive_note: >
  An ongoing project to add a microcontroller to the GT2101's control tower while leaving every
  original board in place and running. Recorded as it happens, including the wrong turns.
---

# The Remora

**Remora** is the name of this project. A remora rides on a whale shark — it takes nothing,
damages nothing, and detaches without leaving a mark. That is the whole design brief.

An ongoing attempt to add a Raspberry Pi Pico to a GT2101's control tower while keeping
**everything original** — every one of the five boards, the power supply, the LED display, the
front-panel controls, the motor and its PCB, and the wiring.

⚠ **Rewritten 29 August 2026.** An earlier version of this page had boards 3 and 4 removed and
the Pico taking a vacated slot. **That is withdrawn. No board is removed.**

This page is written as the work happens, and it includes the mistakes. Status markers as
elsewhere on this site: ✅ confirmed against the hardware · 📄 from a document · ❓ unverified.

---

## Why not simply modernise it

A GT2101 with its original electronics replaced is a Gale box, not a Gale. The same is true of
a pair of 401s rebuilt with modern drivers — the cabinet is still Gale, but the character the
company built into it has gone, and nobody paying Gale money is paying for a box.

That is the whole argument for the approach below. Everything added has to be sympathetic to
what is already there. This deck currently runs a well-made modern replacement controller; it
is being removed and the original five boards refitted, because a working deck that is no
longer original is not the thing worth preserving.

It also sets the editorial rule for this archive: **what previous owners and engineers found
out is kept — their testimony, their measurements, their dead ends. What they bolted on is
not.** Several of the most useful facts on this site came from a previous restorer, and they
are recorded here with his name on them; the hardware he had made is not part of this deck's
future and is not documented.

---

## The principle: the remora

The Pico rides on the deck the way a remora rides on a whale shark — it takes nothing, damages
nothing, and detaches without leaving a mark.

| Board | What it is | In the build |
|:--:|---|---|
| 1 | Display — a three-digit frequency counter | **stays**, and the Pico drives it ✅ |
| 2 | Capacitive touch start/stop; also the display's timing | **stays** |
| 3 | `F VAR` oscillator and the drive-voltage gate | **stays** |
| 4 | Crystal, reference divider, tacho front-end, the servo | **stays** |
| 5 | Power supply and the interface to the motor | **stays** |

**All five boards stay in the tower, powered and running.** The original servo keeps turning the
platter; the Pico reads what it is doing and helps where help is wanted. Boards 3 and 4 are one
servo split across two boards — board 4 decides the drive voltage, board 3 decides whether it is
allowed out — and both stay in the safety chain.

✅ **Mounting, decided 29 August 2026:** adhesive tape behind the Pico and a cable tie at each
end, onto the **pillars between the boards**. No glue, no drilling, no bracket, no modification
to anything. ⚠ Nothing touches the flexible backplane — that film is irreplaceable and the Pico
straddles it with clearance. ⚠ Check the tape is not electrically conductive; it sits behind a
bare board.

⚠ **Listen before driving.** Boards 2 and 4 are alive and pulsing. Driving a net one of them is
already holding gives continuous, dynamic contention that would *partially* work — the worst kind
of fault. Every wire goes in as an input first. See
[Fitting a controller to the backplane](/GT2101/technical-notes/fitting-the-controller/).

### Where the Pico connects

| Job | Where | How |
|---|---|---|
| Speed setting | the Helipot on board 2 | passive — straight into an ADC pin ✅ working |
| Start/stop | board 2's touch pulse | two-resistor divider, edge interrupt |
| Display | board 1, three signals | ✅ working |
| Tacho | the `TACH` net | JFET inverter — see below |
| Drive out | board 3's output net (row 3 pad 7) | op-amp buffering filtered PWM — ⚠ read-only until the gate is proven |

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
circuit), about 8 mA at 10 V — and ✅ a microcontroller can drive it, confirmed on the bench.

⚠ **But mind the off state, not the on state.** An earlier version of this page said a pin could
sink that LED directly with no driver. That is true at 5 V on the bench, where the pin floats to
about 3 V when it lets go and nothing conducts. **At the deck's 10 V it is wrong**: released, the
pin is pulled toward 8 V through that 1 kΩ, the microcontroller's input clamp diode conducts, and
several milliamps are injected into its own 3.3 V rail — continuously, from the instant the deck is
switched on and before any firmware has run. The 10 V installation needs a low-side NPN. On the
bench, configure the pin as **open-drain**, never as a plain output, so the same code survives the
move.

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

⭐ **Keeping board 3 keeps that protection**, and it is one of the better arguments for the remora
approach. An earlier plan removed board 3, which would have left firmware as the only thing between
a stationary platter and full demand — the failure that destroys the motor PCB's output
transistors. With the board in place, the idle value and the hard ceiling in software are a second
line of defence again rather than the only one.

⚠ Note also that the motor's own PCB has **a second gate** on all three phases, separate from
board 3's. If drive is present and the platter does not turn, board 3 is only one of two suspects.

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
| 22 Aug 2026 | Boards 2, 3 and 4 read from their drawings |
| 24 Aug 2026 | The speed pot drives the display end to end — turn the disc, the digits follow ✅. The pot is a ten-turn Helipot, using the full ADC span |
| 24 Aug 2026 | **The original green LED lit and extinguished on command** — one wire, no components ✅ |

| 26 Aug 2026 | The flexible backplane mapped pad by pad, repaired and continuity-tested; the display driven **through** it ✅ |
| 29 Aug 2026 | Motor PCB tracing read: it commutates autonomously from one analogue `SPEED IN` net, so the Pico needs to produce one voltage, not three-phase drive. Architecture settled as the remora — **all five boards stay** |

**Next:** measure the deck running completely original, then the tachometer as a listen-only
wire. See [the bench order](/GT2101/project-notes/next-steps-bench-order/).

The full working record — board-by-board studies, bench procedures, the parts list and the running
project memory — is kept in [Project Notes](/GT2101/project-notes/).

---

## What this exercise has been good for

Rebuilding the logic has meant reading every board properly, and that has corrected a good deal of
what this archive previously said — that board 2 was a servo, that board 3 generated the drive
voltage, that board 3 was an optical sensor, that "disk 2" was two boards. **Every one of those
came from inherited prose with no stated source, and every one fell over on contact with the
hardware.** The 2015 hand tracings, by contrast, have held up.

The deck being worked on still has a later replacement controller fitted and working, so none
of this is being done under pressure. **That board is being removed and the original five
refitted**; it is not part of this project and is not documented here. That is the only reason it has been possible to stop
and check each claim rather than guess.
