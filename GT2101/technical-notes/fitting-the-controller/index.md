---
layout: bare
title: "GT2101 — Fitting a Controller to the Backplane"
permalink: /GT2101/technical-notes/fitting-the-controller/
description: "How to fit a modern controller into the Gale GT2101's control tower using the original backplane as the wiring loom — no cuts, no solder joints on any original board, fully reversible."
show_archive_banner: true
archive_note: >
  A method rather than a finished build. Working figures come from the 2015 traced connector
  tables, not from a meter — the two measurements that would confirm them are named at the end.
---

# Fitting a controller to the backplane

The GT2101's control tower holds five boards on a flexible backplane. Replacing the 1970s
control logic with a microcontroller means getting perhaps ten signals in and out of that
stack — and the obvious way to do it, running flying leads to each board's connector, means
soldering to fifty-year-old boards that are effectively irreplaceable.

There is a much better way, and it falls out of the architecture rather than being invented.

Status markers as elsewhere on this site: ✅ confirmed against the hardware · 📄 from a
document · ❓ unverified.

---

## The principle: the backplane is the loom

Two of the five boards are pure logic and leave together — board 4 generates the drive
voltage, board 3 decides whether it reaches the motor, and both become software. See
[the board 4 page](/GT2101/technical-notes/board-4-servo/) and
[the modern controller project](/GT2101/technical-notes/pico-controller/).

**Their departure frees two edge sockets** — and almost everything the new controller needs
already terminates on the fingers of those two slots. A signal reached through a socket costs
no wire, no solder joint on an original board, and reverses by pulling a card.

So the controller does not get wired *into* the tower. It gets **plugged into it**, on carrier
cards cut to the original board outline, using the sockets the removed boards vacated.

---

## What each vacated slot gives you, free

📄 Both tables are read from the 2015 traced layout sheets.

### Slot 3 — the `3275ST` position

| Finger | Signal | Use |
|:--:|---|---|
| 1, 8, 9 | +10 V, −10 V, GND | all three supply rails |
| 4 | start/stop pulse, 0 → +10 V | the capacitive touch disc, arriving from board 2 |
| **7** | **drive voltage out** | **to the motor**, through the original loom via board 5 |
| 6 | *(dead)* | was board 4's output — now a free channel between the two slots |
| 2, 3 | *(dead)* | were STILL/TURNING status to board 2 |
| 5 | *(dead)* | was `F VAR` |

### Slot 4 — the `3276ST` position

| Finger | Signal | Use |
|:--:|---|---|
| 1, 7, 8 | +10 V, −10 V, GND | all three supply rails |
| **5** | **`TACH` from the motor** | 0 to −10 V. **The only place it appears in the tower** |
| **9** | **`F REF`** | lands directly on the display board's clock input |
| 3 | `4×F` | the front-panel speed switch's VAR/FIX selection, as a frequency |
| 2, 4 | *(dead)* | were the 1.048 MHz clock and `INV TACH` into board 2 |
| 6 | *(dead)* | the free channel to slot 3 |

⚠ **Note the split.** The tachometer and the display clock appear *only* at slot 4. The touch
pulse and the motor drive output appear *only* at slot 3. **Neither slot alone will do**, which
is the single most important fact for anyone planning this.

⚠ **The two slots do not share a pinout.** Slot 3 has −10 V on 8 and GND on 9; slot 4 has
−10 V on 7 and GND on 8. A card built for one slot will short its supply rails in the other.
Legend both cards clearly.

---

## The arrangement

```
  ┌─ slot 1 ── DISPLAY BOARD 3155ST ──────────── stays ─┐
  │                        ▲                            │
  │                        │ F REF, via the backplane   │
  ├─ slot 2 ── TOUCH BOARD 3272ST ─────────────  stays ─┤
  │                        │ touch pulse                │
  │                        ▼                            │
  ├─ slot 3 ── CARRIER B ──────────────────────── new ──┤
  │              · touch divider  (finger 4)            │
  │              · link 6 → 7     (drive to motor)      │
  │                        ▲                            │
  │                        │ one jumper + the dead net  │
  │                        ▼                            │
  ├─ slot 4 ── CARRIER A ──────────────────────── new ──┤
  │              · the microcontroller                  │
  │              · JFET tacho inverter (finger 5)       │
  │              · F REF driver       (finger 9)        │
  │              · op-amp + RC filter → finger 6        │
  │                                                     │
  └─ slot 5 ── POWER SUPPLY 3285NH ───────────── stays ─┘
```

**Carrier A, slot 4** holds the controller itself, the JFET tacho front-end with its gate
straight onto finger 5, the `F REF` level shifter onto finger 9, and the op-amp and filter
that turn PWM into a drive voltage. That voltage leaves on finger 6 — the net that used to
carry board 4's output to board 3, now carrying the new controller's output the same way.

**Carrier B, slot 3** is nearly empty: a link from finger 6 to finger 7, so the drive voltage
reaches the motor by its original path, and a two-resistor divider bringing the +10 V touch
pulse down to logic level.

**One short jumper** between the two cards carries that divided touch pulse back to the
controller. It is the only wire the arrangement itself requires.

Both cards take all three supply rails from their own fingers. **Nothing contends:** with
boards 3 and 4 removed, the touch output drives nothing, the display's clock input is driven
by nothing, and the motor drive net has no other source.

---

## What the backplane cannot give you

Three signals have no route to a vacated slot, because they run board-to-board between two
boards that stay:

| Signal | Why | Cost |
|---|---|---|
| `F DISPLAY` and the count gate | Generated on board 2, consumed on board 1 | 2 wires |
| The display's own `RESET` output | Board 1 → board 2 | 1 wire, and only needed for automatic start-up |
| The green indicator LED | Board 1 → board 5 | 1 wire |

Add an optional supply wire if the tower's +10 V rail cannot carry the controller, and the
whole installation comes to **one jumper and three or four flying leads** — against **zero
modifications to any original board**. Reversing it is pulling two cards and plugging boards
3 and 4 back in.

---

## One circuit point worth deciding early

With board 3 removed, nothing in hardware mutes the motor drive at standstill any more —
that gate was board 3's job, and the 1975 design never let full demand reach a stationary
motor. Software becomes the only protection.

**Give the output op-amp a pull-down resistor to ground.** A single-supply op-amp will not
settle at a true zero unaided, and the pull-down means the drive is zero by hardware if the
PWM stops, the firmware hangs, or the controller has not booted yet. Using the negative rail
to reach zero instead works, but it puts a negative-voltage failure mode directly in front of
the motor drive — not a good trade.

---

## The two measurements that would confirm all this

Everything above is 📄 — traced connector tables, not meter readings. Two checks settle it:

1. **Continuity from each named signal to its slot finger**, tower unpowered. The traced
   sheets give board pin numbers, which is the easier end to work from; the backplane drawing
   gives only positions along the ribbon.
2. **The +10 V rail under load** — how far it sags with roughly 50 mA drawn. This decides
   whether the controller can take its supply from a slot finger or needs a lead to the
   reservoir capacitor.

Neither requires the deck to be running, and neither requires anything to be soldered.

---

*The full working record behind this page — board-by-board studies, connector maps and the
bench sessions — is in [Project Notes](/GT2101/project-notes/).*
