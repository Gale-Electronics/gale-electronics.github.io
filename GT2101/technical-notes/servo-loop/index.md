---
layout: bare
title: GT2101 — How the Speed Servo Works
permalink: /GT2101/technical-notes/servo-loop/
description: "A plain-language explanation of the Gale GT2101's closed-loop speed control: the Helipot speed demand, the optical tacho feedback, the phase-locked servo on board 4 and the motor drive."
show_archive_banner: true
archive_note: >
  A reconstruction of the GT2101's speed-control system from the surviving electronics, the 2015
  hand-traced schematics and the archive's documentation. It is not Gale or DCA factory
  documentation. The simplified explanation is a functional interpretation; the detailed signal
  path is taken from tracings marked PRELIMINARY by their author.
---

# How the GT2101's speed servo works

This page explains, without assuming any background in servo engineering, how the GT2101 holds
its platter at the speed you ask for. The board-by-board detail lives on other pages; this one
puts the pieces together.

Status markers used throughout, as elsewhere in Technical Notes: ✅ confirmed against the
hardware · 📄 from a document, including the archive's own 2015 hand-traced schematics · ❓
unverified or inference.

> **Status of this page: a reconstruction.** No Gale or DCA circuit description survives. What
> follows is built from the physical boards, the FANATSON tracings of 2015 (one person's reverse
> engineering, several sheets marked **PRELIMINARY**) and the archive's other documentation. The
> [summary table at the end](#what-is-established-and-what-is-reconstruction) separates what is
> well supported from what is interpretation.

⚠ **This page describes the surviving production electronics**, whose boards carry date codes
from 1974 to 1976. The prototype shown at the 1974 Audio Fair was reported with a **5.0 MHz**
crystal reference, against the 1.048 MHz crystal on the surviving board 4, so the early machine
may have differed in detail (see the [research notes](/GT2101/research-notes/#what-the-1974-machine-was-reported-to-do)).

⚠ **It also describes the circuit as originally built.** The archive's own deck has since been
modified as part of the [Remora](/GT2101/technical-notes/pico-controller/) project, which moves
the Helipot's wiper lead to a microcontroller. None of that is described here.

---

## 1. The basic idea

The GT2101 does not simply put a fixed voltage across its motor and hope the platter turns at
the right speed. Friction, stylus drag, temperature and the mains supply would all make it drift.
Instead it uses a **closed-loop servo**: it keeps measuring what the motor is actually doing and
keeps correcting it.

The whole idea fits on one line:

```
  desired speed  →  compare with actual speed  →  correct the motor  →  measure again  →  repeat
```

There are three parts to it:

- a **demand** — the speed you have asked for;
- a **measurement** — the speed the motor is actually turning at;
- a **comparison** that turns the difference between the two into a correction.

The rest of this page goes through each part in turn.

---

## 2. Speed demand: the Helipot and `F VAR`

The large speed control on the control tower is a **Helipot**, a precision multi-turn
potentiometer. ✅ The part in the archive's photographs is marked `R 1K`, with date code 7603.

The Helipot does **not** drive the motor. It carries no motor current, and nothing in the
tracings connects it to the motor. Its only job is to tell the electronics what speed is wanted.

In outline:

```
  Helipot  →  F VAR  →  servo
```

📄 The tracings fill in one important step. The Helipot's wiper sets the control input of an
**XR2207 voltage-controlled oscillator** on board 3, and the XR2207 turns that setting into a
**frequency**: a stream of pulses whose rate represents the requested speed. That pulse stream
leaves board 3 as **`F VAR`**.

```
  Helipot wiper  ──►  XR2207 oscillator (board 3)  ──►  F VAR, a pulse stream at 40 × the requested rpm
```

📄 So `F VAR` is a frequency, not a voltage: **40 pulses per second for every rpm requested**.
That is 1,332 Hz at 33⅓ rpm and 3,996 Hz at 99.9 rpm, the top of the variable range. This
matters for everything that follows. The demand and the measurement arrive in the same form, as
pulse streams, so the servo can compare them pulse against pulse.

📄 **The fixed 33⅓ setting.** A black switch on board 5 chooses between `F VAR` (switch released)
and a **fixed 1,332 Hz** reference generated on board 2 (switch pressed), which is the
33⅓ rpm demand. Board 2 also receives the 1.048711 MHz crystal signal, and 1,332 Hz is the
frequency the sheets record. ❓ Exactly how board 2 derives 1,332 Hz from the crystal is not yet
settled from the tracings (see [board 2's open questions](/GT2101/project-notes/board-2-touch/)).

📄 Whichever source the switch selects, the same frequency goes to the servo on board 4 and to
the display on board 2. Board 4 divides it by four, giving a **reference at 10 pulses per second
per rpm** (333 Hz at 33⅓ rpm).

Further detail: [Board 3 — `F VAR` and the drive gate](/GT2101/project-notes/board-3-fvar-gate/)
· [Backplane map](/GT2101/project-notes/flexicon-backplane-map/).

---

## 3. Actual speed: the optical encoder and `TACH`

The GT2101's motor is a ✅ **three-phase brushless DC motor, coupled directly to the platter
spindle**, with no belt or idler. On its shaft is an ✅ **optical encoder**: a rotating optical
disc read by a fixed optical pickup (the readout or photohead). As the shaft turns, the pattern
on the disc passes the pickup and the encoder produces a pulse for each step of movement.

The GT2101's documentation gives the feedback as **600 counts per revolution** ✅. 📄 The servo
arithmetic on board 4 independently predicts the same figure.

⚠ This archive records the figure as **counts** per revolution. It does not establish how many
lines are on the disc. Depending on how the pickup decodes the pattern, a number of counts can
come from fewer physical lines, so do not read "600 counts" as "600 lines".

The pulse stream leaves the motor's own circuit board as **`TACH`**, swinging between ✅ 0 V and
−10 V, and goes up the curly cable to the control tower.

```
  motor shaft  →  optical disc and pickup  →  pulse train  →  TACH  →  servo
```

It helps to think of the encoder as **counting** shaft movement. It does not estimate the speed.
Every fraction of a turn produces a pulse, so the pulse stream is a repeatable, fine-grained record
of how the shaft is actually moving. At 33⅓ rpm with the platter locked, the tacho runs at about
333 pulses per second (📄 derived from the drawings, not yet measured on a running deck).

❓ **One link is not yet traced end to end.** On the motor PCB tracing, `TACH` is produced by a
comparator fed from a wire labelled `BROWN`, and where that wire goes at the motor end is not
drawn. The optical encoder is by far the most likely source: it is the only speed-sensing device
found, and its 600 counts match the loop arithmetic. A continuity check on the motor pod would
confirm it.

Further detail: [The motor](/GT2101/technical-notes/motor-findings/).

---

## 4. The control tower: comparing demand with actual speed

The servo receives both sides of the equation:

- **`F VAR`** (or the fixed 33⅓ reference): *what speed is wanted*;
- **`TACH`**: *what the motor is actually doing*.

It compares them and produces a correction. If the motor is running too slowly, the correction
increases the drive. If it is running too fast, the correction moves the other way and reduces it.
The important point is that this never stops. It is a **continuous feedback loop**, not a single
adjustment made when you set the speed.

### The simplified picture

```
       HELIPOT
          │
          │ F VAR  (speed demand)
          ▼
     ┌─────────┐
     │  SERVO  │ ◄──────────────────────┐
     │ CONTROL │                        │
     └────┬────┘                        │
          │                             │
          │ correction                  │
          ▼                             │
     MOTOR DRIVE                        │
          │                             │
          ▼                             │
   BRUSHLESS MOTOR                      │
          │                             │
          ▼                             │
   OPTICAL ENCODER                      │
          │                             │
          │ TACH  (measured speed)      │
          └─────────────────────────────┘
```

⚠ **This is a simplified functional diagram.** It shows what the system does. It is not a
reproduction of the original factory circuit, and several stages are left out.

### The same loop, as the tracings draw it

📄 For readers who want the actual boards, this is the path as reconstructed from the 2015
tracings and the backplane sheet:

```
  Helipot ──► board 3: XR2207 oscillator ──► F VAR (40 × rpm)
                                                │
              board 2: fixed 1,332 Hz ──────────┤  black switch on board 5 (VAR / FIX)
                                                ▼
                                   board 4: ÷4 ──► reference (10 × rpm) ──┐
                                                                          ▼
  motor TACH ──► board 4: JFET level shifter ────────────────────► MC14046 phase comparator
                                                                          │
                                                       filter and integrator (MC1747 op-amp)
                                                                          │
                                                               drive voltage, board 4 pin 6
                                                                          │
                                                 board 3: STILL/TURNING gate (mutes at rest)
                                                                          │
                                                       board 3 pin 7 ──► motor PCB "SPEED IN"
                                                                          │
                                        commutation and linear push-pull output stage ──► motor
```

What each stage does, in plain terms:

1. 📄 **The comparison is a phase-locked loop.** Board 4's **MC14046** compares the *timing* of
   the reference pulses with the *timing* of the tacho pulses. This is stricter than comparing
   two speeds. In principle, if the platter falls even slightly behind, its pulses start arriving
   late relative to the reference, and the error grows for as long as it stays behind. A
   phase-locked loop therefore corrects not only the speed but any accumulated slip, so while it
   stays locked the platter makes the number of turns the reference calls for. (This is how
   phase-locked servos behave in general. It has not been measured on a GT2101.) 📄 There is no divider inside the
   loop: the tacho is compared one-for-one with the reference.
2. 📄 **Filter and integrator.** The comparator's raw output is a series of pulses. A low-pass
   filter and an integrator built round an **MC1747** op-amp smooth it into a steady voltage. The
   integrator lets the loop settle on whatever drive voltage the motor needs at that speed and
   hold it there.
3. 📄 **The drive voltage.** The result leaves board 4 as a single DC voltage. The tracings record
   it as **1.2 V at 33⅓ rpm, 1.6 V at 45 and 2.4 V at 78**, figures written in four separate
   places in the archive but not yet measured on a running deck. With the platter stopped the loop
   demands full drive, and the voltage rises to about 10 V.
4. 📄 **The start/stop gate.** Board 3 decides whether that voltage is allowed out. With the
   platter at rest it holds its output at 0 V, so full drive never reaches a stationary motor.
   Touching the start/stop disc opens the gate.
5. ✅ **The motor PCB.** The tower does not send the motor power. It sends a low-voltage command,
   and the circuit board in the motor pod does the work. Three position sensors tell it where the
   rotor is, and it steers that one command to each of the three windings in turn
   (commutation). Six power transistors then amplify it in **linear class-AB push-pull**, not
   by switching.

Further detail: [Disk 4 — the servo board](/GT2101/technical-notes/board-4-servo/).

---

## 5. The power rails: what ±15 V and ±10 V are for

It is tempting to describe the motor supply as "+15 V speeds it up, −15 V slows it down". **That
is not how the GT2101 works**, and it is not what the rails are for.

The surviving schematics allow a more precise description:

- 📄 **Board 5 makes two unregulated rails, nominally +15 V and −15 V**, from the mains
  transformer and bridge rectifier, each with a 4,700 µF reservoir capacitor.
- 📄 **The tower's electronics run on regulated rails of about ±10 V** derived from those, and
  called ±10 V throughout the tracings. Board 5's sheet and an independent reading both suggest
  they sit nearer +11.9 V and −10.9 V. The servo's op-amp on board 4 runs on these.
- 📄 **The motor PCB's output transistors run from ±15 V.** Its comparators and op-amps sit on a
  −10 V rail.

The positive and negative rails are there because analogue circuits need room to swing both
ways, and because a **push-pull** output stage needs a supply on each side. That lets it drive
current through a motor winding in either direction as the rotor turns, which is part of
commutation, not of speed control. Neither rail on its own means "faster" or "slower".

📄 **The speed correction is a single control voltage.** On the tracings, the drive voltage from
board 4 to the motor sits between 0 V and about 10 V. Its size sets how hard the motor is driven,
and the servo raises it if the platter is slow and lowers it if the platter is fast. ❓ Whether
the original electronics can actively brake the motor, rather than simply reducing drive, is
not established by the tracings.

Further detail: [Board 5 — power](/GT2101/project-notes/board-5-power/) ·
[The motor's commutation PCB](/GT2101/technical-notes/motor-findings/#the-commutation-pcb).

---

## 6. The loop, step by step

1. The user selects a speed with the Helipot, or presses the fixed 33⅓ setting.
2. The Helipot's setting becomes the `F VAR` reference frequency.
3. The motor turns.
4. The optical encoder produces feedback pulses from the motor shaft.
5. The feedback arrives at the servo as `TACH`.
6. The servo compares the requested and measured pulse streams.
7. A correction is generated: the drive voltage moves up or down.
8. The motor drive responds, and the platter speeds up or slows down.
9. The encoder measures the result again.
10. The process repeats continuously for as long as the deck is running.

**How often the comparison happens.** The phase comparator works on the pulse streams
themselves, which the drawings put at about 333 pulses per second at 33⅓ rpm. How quickly the
loop as a whole *responds* to a disturbance is a different question. It is set by the filter
and integrator component values, and the archive has no source or measurement for it, so this
page does not give a figure.

---

## 7. Why this matters in the context of Dennis Arnall

The 1 November 1974 *Felix* report on the Audio Fair states:

> "The designer of the turntable, Dennis Arnall, is a former gyroscope designer…"

This page does **not** offer that as evidence that Arnall designed the GT2101's servo
electronics. **We do not know that.** Nigel Hobden credits Paul Ramsden at DCA with the GT2101's
electronic and electrical design, and Ramsden recalls an unnamed outside consultant being brought
in to stabilise the PLL. See [Dennis Arnall](/GT2101/research-notes/#dennis-arnall) for the
evidence and the unproven hypothesis that he may have been that consultant.

There is a conceptual connection, but it needs stating carefully. Gyroscope and
inertial-control systems are built on feedback: measure the system's actual state, compare it
with the desired state, apply a correction, and repeat. The GT2101 applies the same broad
philosophy to rotational speed:

| | |
|---|---|
| **A gyroscope or inertial control system** | measure → compare → correct → repeat |
| **The GT2101** | measure motor speed → compare with the speed demand → correct the motor → repeat |

The sensors and physical quantities are different, and the GT2101's servo is **not** "the same
technology as a gyroscope". The accurate statement is that both belong to the **same broad
family of closed-loop control systems**.

### Closed-loop control was not unusual in 1974

⚠ **That family resemblance does not, by itself, point to a gyroscope designer.** By the time of
the 1974 Audio Fair, closed-loop electronic control was well established across engineering:

- **In aircraft.** NASA's [F-8 Digital Fly-By-Wire](https://www.nasa.gov/centers-and-facilities/armstrong/flying-with-nasa-digital-fly-by-wire)
  research aircraft first flew in 1972. It used a computer to make repeated corrections to its
  control surfaces in place of mechanical linkages, and analogue autopilots and stability
  augmentation systems were older still.
- **In industry.** Servo motors with electronic feedback were routine in machine tools,
  instruments and tape transports.
- **In turntables.** Servo-controlled direct-drive decks were already on the market. The
  Technics SP-10, which [the motor page](/GT2101/technical-notes/motor-findings/#signals)
  mentions for comparison, is one example.

So any competent electronics engineer of the period could have designed a closed-loop speed
servo, including Paul Ramsden's group at DCA. Felix's description of Arnall as a gyroscope
designer does not become significant just because the GT2101 uses feedback.

### What remains worth investigating

The narrower question is whether the GT2101's **particular** choices drew on precision
instrument practice:

- 📄 a **phase-locked** loop, which holds the platter's position against the reference rather
  than just its speed;
- ✅ high-resolution optical feedback at **600 counts per revolution**;
- ✅ **linear class-AB** commutation instead of switched drive, which the motor page describes
  as closer to precision instrument servo practice than to consumer hi-fi (engineering
  judgement, not sourced history);
- the **PLL stabilisation** that, according to Paul Ramsden, DCA brought in an outside
  consultant to handle.

That is the kind of specialist servo work a gyroscope or inertial-instrument engineer would have
had direct experience of. Two contemporary or near-contemporary strands also point at that world.
The 1974 Fair programme described the deck's technology as having "more in common with inertial
guidance systems" than with conventional record players. Two later secondhand accounts say the
motor was adapted from a shipboard gyro design, but that remains unconfirmed narrative (see
[The motor](/GT2101/technical-notes/motor-findings/#sourcing--who-made-it)).

None of this shows who designed what. It gives a plausible reason to investigate Arnall's
background in relation to the **specialist** parts of the GT2101's servo, and in particular the
PLL stabilisation, while recognising that closed-loop control in general was commonplace by
1974.

---

## What is established, and what is reconstruction

**Confirmed or well supported**

| Claim | Basis |
|---|---|
| The GT2101 uses a closed-loop servo to hold platter speed | ✅ The servo board, tacho and drive path are present in the hardware; 📄 traced on board 4 |
| The Helipot provides the speed-control input | ✅ Photographed; its three leads match the three posts on board 3's tracing |
| `F VAR` belongs to the speed-demand side | 📄 Named on the board 3 and backplane tracings; ✅ measured on a spare board, pad to pad |
| The motor has optical shaft feedback | ✅ Optical disc and fixed pickup seen in the motor pod |
| The feedback is identified as `TACH` | 📄 Named on the board 4 and motor PCB tracings; ✅ 0 V / −10 V swing recorded |
| The encoder is associated with 600 counts per revolution | ✅ Documented; 📄 independently predicted by the board 4 loop arithmetic |
| Crystal-referenced timing | ✅ A 1.048 MHz crystal on board 4 times the display; 📄 the fixed 33⅓ reference comes from board 2, which receives that crystal signal. ⚠ In **variable** mode the tracings make the XR2207 oscillator the speed reference, not the crystal |
| Analogue supply rails on both sides of 0 V | 📄 Unregulated ±15 V on board 5 and the motor PCB's output stage; regulated ≈±10 V for the tower's servo and logic |

**Reconstruction or functional interpretation**

| Claim | Why it is interpretation |
|---|---|
| The simplified "`F VAR` against `TACH`" picture of the comparison | A functional summary of the traced circuit, which actually compares a divided-down reference with the tacho in a phase comparator |
| The exact internal processing of the error signal | Read from tracings marked PRELIMINARY; component values and the 4046's operating mode have not been checked on a running deck |
| The drive voltages (1.2 V, 1.6 V, 2.4 V, about 10 V at rest) | 📄 On four tracings, not yet measured |
| How fast the loop responds | No source or measurement in the archive |
| How board 2 derives the fixed 1,332 Hz from the crystal | An open question in the tracings |
| That `TACH` comes from the optical encoder | Strongly indicated, but the wire has not been traced end to end |
| Who designed each part of the system | Not established by the electronics. See the [research notes](/GT2101/research-notes/#people-and-attribution) |
