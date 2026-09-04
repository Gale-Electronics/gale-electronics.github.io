---
layout: bare
title: "GT2101 — Fitting the Remora"
permalink: /GT2101/technical-notes/fitting-the-controller/
description: "How the Remora is fitted to the Gale GT2101's control tower without removing a single original board — cable-tied to the pillars, reading the original backplane, fully reversible."
show_archive_banner: true
archive_note: >
  A method rather than a finished build. Signal positions are confirmed on the part; the
  voltages behind them are still 2015 traced figures, and the measurements that would confirm
  them are named at the end.
---

# Fitting the Remora to the backplane

**Rewritten 29 August 2026.** ⚠ An earlier version of this page described removing boards 3
and 4 and plugging carrier cards into the sockets they vacated. **That approach is withdrawn.
No original board is removed.** What follows replaces it completely.

Status markers as elsewhere on this site: ✅ confirmed against the hardware · 📄 from a
document · ❓ unverified.

---

## The principle: the remora

The GT2101's control tower holds five boards on a flexible backplane. The obvious way to add
a microcontroller is to decide which boards it makes redundant, pull them, and take their
place. That is what this page used to describe, and it is the wrong instinct for a deck with
sixty to two hundred survivors and no spare parts in existence.

It is also the wrong instinct for what the object is. A GT2101 with its original electronics
replaced is a Gale box, not a Gale — the same way a pair of 401s rebuilt with modern drivers
keeps the cabinet and loses the character. **Anything added has to be sympathetic to what is
already there.**

The better model is a **remora** — the fish that rides on a whale shark. It takes nothing,
damages nothing, and detaches without leaving a mark. It gets a free ride on a working
animal.

So: **all five boards stay in the tower, powered and running.** The original servo keeps
turning the platter. The controller rides alongside on the same backplane, reads what the
original logic is already doing, and helps where help is wanted — supplying a cleaner speed
reference, driving the display, and taking over a function only where taking over is clearly
better than assisting.

Three properties fall out of this, and they are the whole argument for it:

- **The deck never stops being a GT2101.** At every stage it is a complete, original,
  functioning machine with something extra attached.
- **The original hardware stays in the safety chain.** Board 3's gate still mutes the motor at
  standstill; board 4's servo still closes the loop. Those are not obstacles to work around,
  they are fifty-year-old protections that cost nothing to keep.
- **Reversal is untying two cable ties.**

---

## Mounting: tape and two cable ties

✅ **Decided 29 August 2026.** The controller is a Raspberry Pi Pico. It mounts inside the
tower on the **pillars between the boards** — the tower's own standoffs — with a pad of
adhesive tape behind it and a cable tie at each end.

That is the entire mechanical specification. **No glue, no drilling, no bracket, no
modification to anything.**

⚠ **Nothing touches the flexible backplane.** The Pico straddles the film with clearance and
is anchored only to the pillars. The flexicon is 1975 film, it has already been repaired in
several places, and **no spare exists anywhere**. A cable tie around it would be a clamp on a
fold zone carrying every signal in the deck. Anchor beside it, never to it.

⚠ **Check the tape is not electrically conductive.** Some thermal tapes are aluminium-backed
or carbon-loaded, and this one sits behind a bare board with exposed solder joints. Kapton or
a plain silicone pad is safe. The tape's job here is insulation and padding, not cooling — the
Pico draws about 25 mA and needs no heat sinking.

⚠ Two things to confirm before fitting: that the Pico can never flex down onto the film, and
that its USB socket stays reachable for reprogramming once mounted. ❓ The gap it has to
straddle is **not yet measured** — roughly 12 mm is expected, and nothing is committed until
that number exists.

---

## Where the signals are

✅ Everything the controller needs terminates on the backplane, which is why nothing has to be
soldered to an original board. The pad map is confirmed — it was read optically from both
faces of the translucent film, checked on a meter, and then **proven in service**, with the
display driven through the repaired backplane in bench session 7.

| What the controller needs | Where it appears | Note |
|---|---|---|
| +10 V, −10 V, GND | pad 1 and the last two pads of every row | all three rails available at every row |
| **`TACH` from the motor** | **row 4 pad 5**, also row 5 pad 5 | swings 0 to −10 V |
| **Touch start/stop pulse** | **row 2 pad 5** | 0 → +10 V ☠ see the warning below |
| **Demand** — board 4's drive voltage out | **row 4 pad 6** = row 3 pad 6 | |
| **Drive out to the motor** | **row 3 pad 7** | the calibration prize |
| `F REF` to the display | row 4 pad 9 → row 1 pad 7 | |
| `F DISPLAY`, count gate | row 2 pads 8 and 10 → row 1 pads 3 and 4 | |
| Speed switch VAR/FIX selection | row 4 pad 3 | passive, no level shifting |

⚠ **Rows 3 and 4 do not share a pinout.** Row 3 has −10 V on pad 8 and GND on pad 9; row 4 has
−10 V on pad 7 and GND on pad 8. Never carry an assumption from one to the other.

☠ **Row 2 pads 5 and 6 are adjacent, and one of them will destroy a GPIO.** Pad 5 swings
0 → +10 V and is the touch pulse you want. Pad 6 swings 0 → −10 V. **A divider does not make
pad 6 safe** — dividing a negative voltage just gives a smaller negative voltage, still below
ground, straight into the input's lower clamp diode. Getting the right pad is what protects
the controller; the resistors are not what protects it. Confirm with a meter on the powered
deck: touch the disc, and watch which pad kicks positive.

⚠ **The tacho needs a JFET, not a divider and not a MOSFET.** It sits at 0 V or −10 V, so an
enhancement MOSFET would be off in both states. The right answer is the one Gale used in 1976:
an N-channel JFET in common source, gate to the tacho, source to ground, drain pulled up to the
logic rail. See [the board 4 page](/GT2101/technical-notes/board-4-servo/).

---

## Listen before driving

This is the rule that makes the remora work, and it is not optional.

⚠ **Boards 2 and 4 are alive and pulsing.** If the controller drives a net that one of them is
already driving, the result is not a clean failure — it is continuous, dynamic contention that
would *partially* work, which is the hardest kind of fault to diagnose and the kind most likely
to be blamed on something else.

So the order is: **every wire is an input first.** Tacho, demand, drive voltage and the touch
pulse all go in as reads, and the log answers the questions that the archive cannot:

- Does the original servo hold 33⅓, and if it wanders, by how much?
- What is the tacho's real pulse rate? 📄 expected ~333 Hz at 33⅓, i.e. 600 pulses per
  platter revolution.
- What is the drive voltage at each speed, and does board 3's gate really mute it to 0 V at
  standstill?

Only when those are measured does anything get driven — and then one connection at a time.

### When a connection does have to be broken

Assisting needs no breaks. **Overruling does** — you cannot drive a net another board is
holding. So the remora eventually bites, in exactly the places where taking over is better
than assisting, and nowhere else.

⭐ **Breaks are made at the brass staples on the solder side, never at a pad.** The film never
sees the iron. Wires that are only added go to **board connector pins**, where spare boards
exist for all five positions. Every break is reversible by re-making one joint.

---

## Why the motor makes this practical

📄 From the 2015 tracing of the motor PCB, and it is the finding that decides the whole shape
of the project.

The motor's own PCB is a **self-contained three-phase brushless commutator**: comparators
reading the rotor sensors, a JFET shunt per phase, buffers, and a complementary Darlington
output pair driving the three windings. Commutation happens there, autonomously, on the motor
board.

It takes **one analogue input**, marked `SPEED IN`.

So a controller for this deck never has to become a motor controller. It has to produce **one
voltage**. Had the motor needed three-phase commutation from scratch, replacing the original
electronics would have been the only route and the boards really would have had to come out.
They don't.

⚠ Note that the motor board has **its own gating** on all three phases off `SPEED IN` — a
second gate, separate from board 3's. If drive is present and the platter does not turn,
board 3 is only one of two suspects.

⚠ The motor PCB runs on **±15 V** with a −10 V reference. The tower runs **+11.9 / −10.9 V**.
They are not a common rail.

---

## The safety point, and how the remora changes it

📄 The drive voltage is proportional to speed — 1.2 V, 1.6 V and 2.4 V for 33⅓, 45 and 78 rpm
— but with the platter stopped the servo's demand rails to **10 V**, and **board 3 mutes it to
0 V** before it can reach the motor.

Anyone reading this archive should note that the widely repeated "10 V at standstill" figure is
the *input* to that gate, not what the motor receives.

Under the old remove-the-boards plan, taking board 3 out took that protection with it, and
firmware became the only thing standing between a stationary platter and full demand — the
failure that destroys the motor board's output transistors.

**Keeping board 3 keeps the protection.** That is not a small consolation prize for a more
conservative approach; it is one of the better reasons to prefer it. Firmware still holds an
idle value of 0 V and a hard ceiling, but they are a second line of defence again rather than
the only one.

If an op-amp does eventually buffer the drive output, give it a pull-down resistor to ground:
a single-supply op-amp will not settle at a true zero unaided, and the pull-down means zero by
hardware if the PWM stops or the controller has not booted. Reaching zero using the negative
rail works but puts a negative-voltage failure mode directly in front of the motor drive —
a bad trade.

---

## What is still 📄 and not ✅

The pad *positions* are confirmed. The *voltages* on several of them are still 2015 traced
figures on sheets marked preliminary. Three measurements settle almost everything, and none
requires anything to be cut:

1. **Row 3 pad 7 at each speed on the running deck.** Four 📄 figures become ✅, and it is the
   single most valuable measurement left in the project.
2. **Row 3 pad 7 with the platter stopped.** Proves board 3's gate really does mute to 0 V.
3. **The +10 V rail under load** — how far it sags at roughly 50 mA. This decides whether the
   controller can take its supply from the backplane or needs a lead to the reservoir
   capacitor.

---

*The full working record behind this page — board-by-board studies, the backplane pad map,
the bench order and the running project memory — is in
[Project Notes](/GT2101/project-notes/).*
