---
layout: bare
title: "GT2101 — Remora Firmware"
permalink: /GT2101/project-notes/firmware/
description: "The MicroPython running on the GT2101's Pico — every file that exists, the pin map it encodes, and what is still only planned."
---

*Part of the GT2101 project's live record. See
[Project Notes](/GT2101/project-notes/) for the working record and
[`pico-controller-notes.md`](/GT2101/project-notes/pico-controller-notes/) § FIRMWARE for the
design.*

---

# Remora firmware

## ✅✅ EVERYTHING ON THE PICO IS NOW IN THE REPOSITORY — 6 September 2026

**Copied straight off the Pico's filesystem via Thonny.** The exposure this folder was created
to close is closed.

| File | What it does |
|---|---|
| `config.py` | ⚠⚠ **Board 1's settings and part of the pin map.** See the warning below — it is *not* the whole pin map |
| `main.py` | Entry point — MicroPython auto-runs this filename and nothing else. Session 8: display + pot + green LED, standalone |
| `display.py` | Board 1's counted-pulse driver |
| `bench.py` | The bring-up harness |
| `blink.py` | Power-up proof. Blinks the onboard LED and touches nothing else. This is what confirmed the LM7805 supply in bench session 8 |

### ⭐ And the exposure was smaller than this page claimed

**This page used to say "one file out of nine" and list `tacho.py`, `controls.py`, `drive.py`
and `controller.py` as existing only on the Pico.** ✅ **They do not exist at all** — the Pico
carries four files, and all four are now here. Those four were **planned, never written**.

⭐ **And on the two-wire architecture, two of them are never going to be written:**
`drive.py` and `controller.py` existed to inject the drive voltage and close a servo loop, and
**the Pico does neither.** `tacho.py` and `controls.py` become phase-2-or-optional. See
[`pico-controller-notes.md`](/GT2101/project-notes/pico-controller-notes/) § ARCHITECTURE.

---

## ⚠⚠ `config.py` IS NOT THE WHOLE PIN MAP — found 6 September 2026

Its own header says *"This is the only file you should ever need to edit."* **That is not
true**, and it matters, because this repo has been treating `config.py` as *the* record of
which GP pin goes to which wire.

| GP pin | Goes to | Declared in |
|---|---|---|
| **GP2** | Board 1 pin 6 — `F DISPLAY` | `config.py` ✅ |
| **GP3** | Board 1 pin 7 — `GATE` | `config.py` ✅ |
| **GP4** | Board 1 pin 11 — `F REF` | `config.py` ✅ |
| **GP26** | **Helipot wiper (orange)** | ⚠ **`main.py`, hard-coded** — `POT_PIN = 26` |
| **GP5** | **Board 1 pin 8 — green LED** | ⚠ **`main.py`, hard-coded** — `LED_PIN = 5` |

⭐ **Fix: move `POT_PIN` and `LED_PIN` into `config.py`.** Two lines, and it makes the header's
claim true. Until then, **read both files** before believing any pin map.

### ✅ The bench wiring, verbatim from `config.py`

Board 1 held **component side towards you, displays at the top**; the connector row is seven
pins, a gap, one lone pin, a gap, one lone pin, a bigger gap, then three at the right-hand end.
Count the twelve pins you can see, left to right.

| Board 1 pin | Signal | Pico |
|---|---|---|
| 1 (1st of seven) | +10 V | pin 40 **VBUS** (5 V from USB) |
| 6 (6th of seven) | `F DISPLAY` | GP2 |
| 7 (last of seven) | `GATE` | GP3 |
| 11 (middle of three) | `F REF` | GP4 |
| 12 (last pin) | GND | pin 38 GND |

⚠ **Leave everything else unconnected.** Pin 3 (`BLANK`) has a pull-up on the board, so
unconnected = display ON. Pin 10 (`RESET` out) is an **output from the board — never drive it.**

⚠⚠ **VBUS and VSYS are two different things and this project uses both.** `config.py` takes
5 V *out* of **VBUS (pin 40)** to power board 1 on the bench. The LM7805's 5 V goes *into*
**VSYS (pin 39)** in the tower. **Both are correct; do not swap them.**

⚠ **ONE POWER SOURCE AT A TIME.** On the bench that is the USB lead and nothing else.

---

## What the code already does that the notes did not record

⭐ **`main.py` already solves the auto-lock problem, using the pot.** `lock_by_pot()` steps
`F REF` one pulse per ~quarter-turn of the Helipot, flashing the green LED while unlocked, and
when the pot has been still for 3 s it takes that as the dark state and marks it — then the LED
goes steady. **That is the "human watching for the digits to go dark" step, done through the
pot instead of the keyboard.**

⭐ It is what the free software fix would replace: hold `GATE` low, send up to four `F REF`
pulses, no watching at all. See
[`board-1-display.md`](/GT2101/project-notes/board-1-display/) §6a.

⚠ **`main.py` maps the pot to the FULL 30–80 rpm range** (`RPM_MIN = 30.0`, `RPM_MAX = 80.0`).
The open question *"full range or a trim band around the three standard speeds?"* is therefore
**already answered in code, by default rather than by decision.** Ten turns across 50 rpm is
about 5 rpm per turn.

---

## ⚠ Stale comments inside `config.py`

- `FREF_EDGES = 2` carries the comment *"it has never been measured. Run `bench.fref_hunt()` to
  find it"* — but **the four-state cycle WAS measured on 21 August 2026** and is written out
  four lines below it (`FREF_CYCLE = 4`, `FREF_LATCH_TO_RESET = 2`). The comment is stale and
  `FREF_EDGES` duplicates `FREF_LATCH_TO_RESET`.
- `GATE_COUNTS_WHEN_LOW = True` is correct and ✅ confirmed on the bench, not a guess.

⚠ **When the display moves from the 5 V bench to the 10 V tower, the NPN level shifters
invert**, so `GATE_COUNTS_WHEN_LOW` and the `F REF` / `F DISPLAY` pulse polarities all flip.
Decide that deliberately in this file rather than meeting it as a surprise.

---

## `blink.py`

Proves the Pico boots and runs on tower power with no USB attached. Drives no GPIO, involves no
board.

⚠ Note the `Pin("LED")` fallback — the onboard LED is on GP25 on a plain Pico but moves to the
wireless chip on a Pico W. ✅ **The plain Pico is decided for phase 1** (6 September 2026), so
the fallback is insurance rather than a live requirement.

---

## The rule this folder exists for

⚠ **Do not keep the only copy of anything outside this repository.** On 24 August 2026 a
claude.ai project emptied without warning and took twenty-one documents with it; seven were
recovered and the rest were not. **A microcontroller that gets reflashed, unplugged and carried
between towers is exactly the kind of place that rule is about.**

⭐ **Re-copy after any bench session that changes a file on the Pico.** In Thonny: select the
files in the *Raspberry Pi Pico* pane, right-click, **Download to** this folder.
