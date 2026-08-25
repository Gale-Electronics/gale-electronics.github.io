---
layout: bare
title: GT2101 — Disk 4, the Servo Board
permalink: /GT2101/technical-notes/board-4-servo/
description: "Gale GT2101 board 4 (GT201/3276ST) — crystal reference, JFET tacho front-end and the MC14046 phase-locked servo that generates the motor drive voltage."
show_archive_banner: true
archive_note: >
  A full reading of board 4 from its 2015 hand-traced schematic and layout sheets, checked against
  photographs of a spare board. Board 4 is the GT2101's servo, not merely its reference oscillator.
---

# Disk 4 — the servo board

`GT201/3276ST` · **ISSUE C** · ✅ read off the etched copper

The inherited description of this board calls it a *reference oscillator*. That is roughly a
quarter of what it does. Board 4 carries the crystal timebase, the reference divider, the
tachometer front-end **and the phase-locked servo that generates the motor's drive voltage**. It
is the closest thing the GT2101 has to a brain.

Status markers used throughout: ✅ confirmed against the hardware · 📄 from a document ·
❓ unverified.

---

## What is on the board

| Part | Job | Date code ✅ |
|---|---|---|
| **MC14011CP** | Quad NAND — buffers and squares the crystal oscillator | AA 7537 |
| **MC14520CP** | Dual binary counter — the ÷4 reference divider | AA 76-02 |
| **MC14046CP** | CMOS phase-locked loop — the phase comparator | AA 7549 |
| **MC1747CL** | Dual op-amp on ±10 V — loop integrator and error output stage | 520 |
| **1.048 MHz crystal** | Master timebase, with a ceramic trimmer beside it | can marked `1048.00` |
| **E113** N-channel JFET | Tacho front-end — see below | — |

Precision RN55 metal-film resistors (`44K8 F`, `4642 B` and others) set the scaling around the
op-amp, which is what fixes the drive voltages listed further down.

✅ **Built no earlier than January 1976.** The MC14520's `A76-02` date code is week 2 of 1976,
making board 4 the latest-dated board yet examined for this archive — boards 1 and 3 are 1975.
A round `OK ELEC` inspection sticker sits on the component side, of the same family as the
`OK NOV 81` service label found on board 2.

---

## The connector — nine pins

✅ Nine pins are fitted in twelve hole positions, and the 2015 tracer numbered exactly nine
signals, so signal *n* is physical pin *n*. The layout sheet is headed **component side**, so the
pins run 1 → 9 left to right with the parts towards you and the connector at the bottom.

| Pin | Signal | Direction | Other end |
|:--:|---|---|---|
| 1 | `+10 V` | in | board 5 |
| 2 | 1.048 MHz | out | board 2 |
| 3 | `4×F` — 40–3996 Hz, i.e. 40 × rpm | in | board 2 / board 5 speed switch |
| 4 | `INV TACH` — 0/+10 V, open drain | out | board 2 |
| 5 | `TACH` — **0 V to −10 V** | in | the motor |
| 6 | **drive voltage** | out | **board 3 pin 6** |
| 7 | `−10 V` | in | board 5 |
| 8 | `GND` | in | board 5 |
| 9 | `1×F` — 10–999 Hz, i.e. 10 × rpm | out | board 1 pin 7 |

⚠ **Boards 3 and 4 do not share a pinout.** Board 4 has −10 V on pin 7 and ground on pin 8;
board 3 has −10 V on pin 8 and ground on pin 9. Both have +10 V on pin 1. A board pushed into the
wrong slot will see its supplies reversed.

---

## How the servo works

```
  pin 3   4×F (40–3996 Hz)  ──►  MC14520 ÷4  ──┬──►  pin 9   1×F (10–999 Hz)  to board 1
                                               │
                                               └──►  4046 SIG IN      (the reference)

  pin 5   TACH (0/−10 V)  ──►  E113 JFET  ──┬──►  pin 4  INV TACH (0/+10 V)  to board 2
                                open drain   │
                                             └──[R]──►  4046 COMP IN   (the feedback)

  4046 phase comparator ──► RC low-pass ──► 1747 A (integrator) ──► 1747 B ──► pin 6
                                                                    the drive voltage
```

📄 **There is no divider inside the loop** — the platter and its tachometer are the oscillator the
4046 is steering. The loop therefore locks the tacho frequency directly onto the ×10 reference.

---

## The tachometer runs at about 600 pulses per revolution

Because the loop compares the tacho against `1×F` one-for-one, in lock the tacho produces
**10 Hz per rpm** — 333 Hz at 33⅓ rpm. Expressed per turn of the platter, that is roughly
**600 pulses per revolution**.

📄 Derived from the drawings, not yet measured on a running deck. It is recorded here because it
is easy to arrive at a figure ten times smaller by assuming the loop compares the ×40 frequency
(1332 Hz at 33⅓) instead of the ×10 one.

---

## The tacho front-end — and why it has to be a JFET

The motor's tachometer signal swings between **0 V and −10 V**, which no CMOS input can read.
Gale solved it with a single N-channel JFET in common source:

```
        +10 V
          │
         [R]
          │
  TACH ───┤ G   ┌─── INV TACH out (0 / +10 V)
  0/−10V  │  E113
          └── S ── GND
```

With the gate at 0 V the JFET conducts and the output is pulled low; at −10 V it is pinched off
and the pull-up takes the output to +10 V. **A JFET is essential here** — an ordinary enhancement
MOSFET needs a *positive* gate voltage, so on a signal that only ever sits at 0 V or −10 V it
would remain off in both states and never switch.

📄 Sheet 3A records a defective E113 on board 3 being *"replaced by J113 (RS Components)"*, so a
modern substitution for this part is already proven on this equipment.

---

## Where its outputs go

- **Pin 2, 1.048 MHz** → board 2, which divides it down for the display timing.
- **Pin 4, `INV TACH`** → board 2.
- **Pin 9, `1×F`** → board 1 pin 7, the display's latch-and-reset clock. The motor signal map's
  entry for that pin — *"speed reference, 10–999 Hz"* — is word for word the label the tracer
  wrote against board 4 pin 9, so three separate documents agree on this connection.
- **Pin 6, the drive voltage** → board 3 pin 6, where a window comparator and a JFET switch
  decide whether it reaches the motor.

📄 The drive voltages: **33⅓ rpm = 1.2 V · 45 rpm = 1.6 V · 78 rpm = 2.4 V · stationary = 10 V**.
The 10 V is the loop railing to full demand with the platter stopped, and board 3 mutes it to
0 V — see [the drawings page](/GT2101/engineering-drawings-schematics/#drive-voltage).

---

## A discrepancy worth recording

📄 The 2015 schematic draws the ÷4 divider as a **4013** dual D flip-flop. ✅ The board carries an
**MC14520** dual binary counter instead. Both can divide by four, and the frequencies quoted on
the sheets (1332 Hz in, 333 Hz out) confirm the ratio is four — but the tracer either worked from
a different issue of the board or wrote the wrong part number. Anyone relying on that stage should
check it against the board in front of them.

---

## Correction to the inherited description

❓ The page `Disk 4 — Reference Oscillator.pdf`, inherited from the defunct *galeaudio.com*, says
the board "generates the stable frequency reference" and that its output "feeds the servo control
board (Disk 2A)".

- It omits the tacho front-end and the phase-locked servo — most of the board.
- It omits the MC14520 divider and the E113 JFET.
- It calls the quad NAND an AND gate, and gives the PLL as an MC4046 rather than an MC14046.
- The board's outputs go to boards 1, 2 and **3**. There is no "Disk 2A" board; 2A and 2B are two
  schematic sheets of board 2.

That page should be read as ❓ disputed. It is the fourth of four inherited board descriptions to
fail a check against the hardware.
