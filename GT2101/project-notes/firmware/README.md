---
layout: bare
title: "GT2101 — Remora Firmware"
permalink: /GT2101/project-notes/firmware/
description: "The MicroPython running on the GT2101's Pico — what is in the repository, and what is still only on the Pico itself."
---

*Part of the GT2101 project's live record. See
[Project Notes](/GT2101/project-notes/) for the working record and
[`pico-controller-notes.md`](/GT2101/project-notes/pico-controller-notes/) § FIRMWARE for the
design.*

---

# Remora firmware

**Created 4 September 2026**, replacing a folder called `Claude outputs` that held one file.
The old name credited the tool rather than describing the contents, and the space in it made
an awkward URL. More to the point, **this is where the bench order says the firmware is
supposed to live.**

> *"Copy `config.py` (the GP2/GP3/GP4 assignment) from the Pico into this repo. After the
> 24 August loss, the Pico's filesystem must not be the only record of which wire goes
> where."* — the bench-order note, 26 August 2026

---

## ⚠⚠ What is actually here — and what is not

**One file out of nine.** Everything else exists **only on the Pico's own filesystem.**

| File | In the repo? | What it does |
|---|---|---|
| `blink.py` | ✅ **yes** | Power-up proof. Blinks the onboard LED and touches nothing else |
| `config.py` | ❌ **no** | ⚠⚠ **Every setting, and the record of which wire goes where.** The most important file in the build |
| `main.py` | ❌ no | Entry point — MicroPython auto-runs this filename and nothing else |
| `display.py` | ❌ no | Board 1's counted-pulse driver, rewritten from scratch 21 Aug |
| `bench.py` | ❌ no | The bring-up harness — `blink` · `lock` · `digits` · `green` · `controls` · `tacho` · `drive` · `loop` |
| `tacho.py` | ❌ no | Edge timestamping and the ring buffer |
| `controls.py` | ❌ no | Touch pulse, start/stop state |
| `drive.py` | ❌ no | PWM, the RC filter and the hard ceiling |
| `controller.py` | ❌ no | The servo loop |

⚠ **This is the exact exposure the 24 August loss was about.** That day a claude.ai project
emptied without warning and took twenty-one documents with it; seven were recovered and the
rest were not. The rule written the next day was *"do not keep the only copy of anything
outside this repository"* — and eight of nine firmware files are currently outside it, on a
microcontroller that gets reflashed, unplugged and carried between towers.

⭐ **`config.py` is the one to copy first.** It is the only record of the GP2 / GP3 / GP4 /
GP5 / GP26 assignment, and that mapping is not written down anywhere else in the repo. If the
Pico's filesystem is lost, the wiring has to be traced again from the hardware.

**Copying is a two-minute job in Thonny:** *File → Open → Raspberry Pi Pico*, then
*File → Save as → This computer*, into this folder.

---

## `blink.py`

Proves the Pico boots and runs on tower power with no USB attached. Drives no GPIO, involves
no board. This is what confirmed the LM7805 supply in bench session 8.

⚠ Note the `Pin("LED")` fallback — the onboard LED is on GP25 on a plain Pico but moves to the
wireless chip on a Pico W. Relevant to the plain-Pico-versus-Pico-W decision still open in
[`parts-to-order.md`](/GT2101/project-notes/parts-to-order/).
