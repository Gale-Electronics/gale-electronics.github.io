# GT2101 — Claude project memory (portable copy)

**Rewritten 19 August 2026**, replacing the export made earlier the same day.
**Updated 21 August 2026** after the Board 1 display work.
**Updated 22 August 2026** after the Board 2, Board 3 and Board 4 studies — the
architecture is now settled and several long-standing numbers changed. See §"What changed
on 22 August" below if you already know the earlier version.
**Updated 24 August 2026** — the speed disc is tinted, not clear (§ THE CONTROLS), and the
suspension has its own document for the first time (§ OUTSIDE THE CONTROL TOWER).
**Updated again 24 August 2026** after bench sessions 5 and 6 — the Helipot is **electrically
off Board 2** (§ THE CONTROLS), the Pico now drives **Board 1's green LED** (§ INTERFACING,
and the claim there is corrected), and the minimum-intrusion wiring plan is written up in
`gt2101_pico_controller.md` § HOW THE PICO MEETS THE TOWER.

> ## ⚠ AUTHORITATIVE LOCATION — CHANGED 22 AUGUST 2026
>
> **The website repository is the source of truth**: the folder
> `gale-electronics.github.io-main` on Matt's desktop PC, published at
> `gale-electronics.github.io/GT2101/`.
>
> Order of authority:
>
> 1. **The hardware in front of you.** A measurement beats every document anywhere.
> 2. **The website repository.**
> 3. This document and the rest of the claude.ai project notes.
> 4. The working folder `Desktop\GT2101` — firmware and original scans only. It used to
>    claim authority and no longer does.
>
> **Ask to connect the repo folder before starting technical work.** Folder access is
> granted per session and does not carry over.

### ⚠ Start every session like this

1. **Call `project_info` and look at the timestamps.** This project often moves two or three
   times in a day. The documents written *earlier today* are the ones most likely to change
   your answer, and they are the ones easiest to miss.
2. Read this file.
3. Ask to connect the repo folder if the work touches the archive.
4. Only then start.

On 22 August a full board analysis was delivered without reading two documents written that
same morning, and three of its conclusions were already out of date. Step 1 exists because
of that.

**What this is:** the bootstrap document for a new session — the only file at the root of
the claude.ai project, with everything else under `claude/`. It is a summary of the project,
not the record of it. The record is the published site.

---

## ⚠ Scope — PICO ONLY

The project is **only** this: adding new control logic to the GT2101's control tower
using a Raspberry Pi Pico. Everything else on the deck stays original.

**Dropped, and not to be revived unless Matt says so:** reverse-engineering or recloning
the locked 2009 "Howie board", chasing its ATmega88PA firmware, and the Walkbury
Electronics manufacturing enquiry.

---

## What changed on 22 August 2026

Four things that supersede anything written earlier:

1. **Boards 3 and 4 come out.** They are one servo split across two boards. Boards 1, 2 and
   5 stay, and the Pico's carrier takes slot 3. The old rule "do not plan to unplug boards"
   was based on a wrong description of Boards 2 and 3 from the defunct website.
2. **The tacho runs at ~600 pulses per platter revolution, not 60.** Ten times out.
3. **`V_IDLE` is 0 V, not 10 V** — and with Board 3 out, firmware is the only thing
   enforcing it.
4. **The tacho level-shifter must be a JFET (J113), not the PNP circuit described in
   earlier versions of this file.** The PNP cannot work.

---

## The five boards

| Board | Gale no. | What it does | In the build? |
|---|---|---|---|
| 1 (top) | `3155ST` | Display | **stays** — Pico drives it ✅ working |
| 2 | `3272ST` | Touch start/stop, display timing, holds the Helipot | **stays** — touch sensor and pot bracket only |
| 3 | `3275ST` | `F VAR` generator + drive-voltage gate | ❌ **out** |
| 4 | `3276ST` ISSUE C | Crystal, ÷4 reference, tacho front-end, **the servo** | ❌ **out** |
| 5 (bottom) | `3285NH` ❓ | Power supply + external interface | **stays** |
| backplane | `3281NH` | Flexible ribbon by *flexicon* | stays |

✅ All part numbers except Board 5's were **read off the etched copper**. The sequence
3155 · 3272 · 3275 · 3276 · 3281 · 3285 ascends down the stack, which corroborates the
whole register. Boards carry **ISSUE letters** — a previously unrecorded revision axis.

**Board 4 is the latest-dated board** (MC14520 date code A76-02 = January 1976).

Detail lives in `control_tower_board_register.md`, `gt2101_backplane_signal_map.md`, and one
document per board: `gt2101_board1_display.md`, `_board2`, `_board3`, `_board4`.

**Published equivalents, which outrank them:** the board register and drive-voltage figures at
`/GT2101/engineering-drawings-schematics/`, and the per-board notes at
`/GT2101/technical-notes/`. Board 4 and the modern-controller project are published; boards 1,
2 and 3 and the drawings-provenance note are still to be written up there.

⚠ **The project's schematic PDFs are image-only scans** — `project_read` returns empty. A
cloud session must have them **attached directly to the chat** to read them. That is how
Boards 1–4 were worked out.

⚠ **They are also not factory drawings** — all are one person's 2015 hand tracings, and the
four typed prose pages checked against hardware were all substantially wrong. See
`gt2101_archive_provenance.md`.

---

## ARCHITECTURE — keep ALL original hardware, Pico is brains only

Matt's stated goal: **"all the logic from the Pico, everything else original."** Original
power supply, original LED display, original front-panel controls, original motor PCB,
original wiring loom.

Boards 3 and 4 are pure logic, so they leave — unmodified and reversibly. The Pico's
carrier goes in slot 3 (the corroded ISSUE B spare of `3275ST` is the leading candidate:
its edge fingers already fit and its pot eyelets are in the right place).

### Where the Pico connects

| Job | Where | How |
|---|---|---|
| Speed setting | Helipot, on Board 2 mechanically only | passive, straight to GP26 ✅ working |
| Start/stop | Board 2 pin 5 — a 0 → +10 V pulse | 22k/10k divider, rising-edge interrupt |
| Display | Board 1 pins 6, 7, 11 (+3, 10 optional) | ✅ working at 5 V |
| Green LED | Board 1 pin 8 | ✅ working at 5 V, open-drain on GP5. **NPN driver required at 10 V** |
| Tacho in | the `TACH` net, 0/−10 V | **J113 JFET inverter** |
| Drive out | Board 3's pin-7 net | LM358 buffering filtered PWM |

The Pico holds start/stop state in software — Board 2 only ever emits an edge, so each
pulse toggles.

### ⭐ Minimum-intrusion wiring — the backplane is the loom

Written up in full in `gt2101_pico_controller.md` § HOW THE PICO MEETS THE TOWER. Short
version: Boards 3 and 4 leaving frees **two edge sockets**, and most of what the Pico needs
already terminates on their fingers — power, the touch pulse and the motor drive at slot 3;
the tacho, `F REF` to Board 1 and the black switch's selection at slot 4. Neither slot alone
does the job, so the plan is two cards with one jumper between them. **Total: one jumper
plus three or four flying wires, and no modification to any original board.**

---

## THE CONTROLS — confirmed by Matt on the deck

| Control | Where | What it does |
|---|---|---|
| **Red switch** | bottom of tower | mains power on/off. Out of scope entirely |
| **Black switch** | bottom of tower | VAR released = speed set by the disc; FIX pressed = locked 33⅓. Plain passive switch |
| **Tinted disc, turned** | top of tower | sets the speed. **Beckman Helipot 7286, 0.25%**, bolted to Board 2 |
| **Tinted disc, touched** | top of tower | **starts/stops the platter, and is CAPACITIVE.** Responds to a finger, not a plastic pen |

✅ **The disc is smoke-tinted, not clear and not red — Matt, 24 August 2026.** Earlier
versions of this file called it the "Clear disc" twice. The red seen through it comes from
the LEDs behind, on both the original boards and the Howie tower. This matters for the OLED
overlay plan: a neutral tint supplies density but **no colour**, so a white module behind it
reads white. See `gt2101_board1_display_device.md` §5.

A tap under `TAP_MAX_MS` (600 ms) toggles start/stop; a sustained touch is treated as
adjusting speed and ignored.

✅ **The original touch sensor is confirmed** — a bent copper tab beside the Helipot bush
into a 555, out as a pulse on Board 2 pin 5. Reading that pulse is the cheapest of the three
options; the others are sensing the tab directly through 1 MΩ, or a TTP223 module.

### ✅ The Helipot is electrically OFF Board 2 — Matt, 24 August 2026

**All three pot leads go directly to the Pico; nothing else connects to it.** The pot is held
to Board 2 by a **brass nut and washer** only — Board 2 is its bracket, not its circuit.

- This closes an open question in `gt2101_board3.md` about what drove the XR2207's control
  voltage "presumably via Board 2". That path is already broken.
- **Board 2's remaining jobs are exactly two:** the touch sensor, and holding the pot.
- ⚠ **Do not disturb the brass nut and washer.** The touch electrode is a bent tab beside
  that bush and the sensitivity depends on what the bush and shaft are tied to. No ground
  strap, no steel replacement, no cleaning under the washer. If touch behaviour changes
  after reassembly, that hardware is the first suspect.
- For the final build: **100 nF from the wiper to AGND at the Pico end** — the wiper runs
  through the tower alongside the motor drive line.

✅ **Helipot wiring, bench 20 Aug:** **orange = wiper** → GP26_A0 (pin 31); **red** → 3V3(OUT)
pin 36; **yellow** → AGND pin 33. ❓ Resistance unresolved — label says 1 kΩ, one bench
reading said 10 kΩ. Doesn't affect the wiring.

✅ **TEN TURNS — 24 August 2026.** Full ADC span 160–65535. A reading stuck low is far more
likely to be an unfinished turn than a broken wire; that is what the "pot appears dead"
report of 24 August turned out to be. ⚠ Ten turns is very fine control — about 3 rpm per
turn if mapped 30–80 rpm. Decide deliberately whether the whole range is wanted or a trim
band around the three standard speeds.

---

## DRIVE VOLTAGE — proportional, with a hard mute at rest

📄 Board 3's layout sheet tabulates **both sides** of its gate:

| Condition | Board 4 pin 6 (demand in) | Board 3 pin 7 (out to motor) |
|---|---|---|
| **STILL** | 10 V | **0 V** |
| 33⅓ | 1.2 V | 1.2 V |
| 45 | 1.6 V | 1.6 V |
| 78 | 2.4 V | 2.4 V |

Lowest speed is lowest voltage, rising roughly through the origin — what a brushless motor
needs, since back-EMF rises with speed. "STILL = 10 V" is Board 4's loop railing to maximum
demand with the platter stopped, and **Board 3 mutes it to 0 V.**

⚠ The backplane sheet only ever recorded the input column. That is where the old
"STILL: 10 V" came from, and it was being read as though it reached the motor.

⚠⚠ **`V_IDLE` = 0 V, and with Board 3 out, firmware is the only thing holding it there.**
The 1975 design never let 10 V reach a stationary platter. The idle value and the hard
ceiling in `drive.set_drive()` stop being belt-and-braces and become the only braces — this
is the case that cooks the BD675A/676A. Give the LM358 a **10 kΩ pull-down on its output**
so idle is 0 V by hardware as well.

📄 not ✅ — the tracer's figures, on a sheet marked PRELIMINARY. **Measuring Board 3 pin 7 on
the running deck is the most valuable measurement left in the project.**

---

## TACHO — ~600 pulses per platter revolution

Board 4's 4046 locks the tacho to `1×F` with **no divider in the loop**, so the tacho runs
at **10 Hz per rpm** — 333 Hz at 33⅓ rpm, i.e. **600 pulses per platter revolution**.

⚠ **Supersedes "60 pulses/rev"**, which assumed the PLL reference was the ×40 frequency.
It is the ×10 frequency.

Re-scale `TACHO_PPR`, the ring buffer (one revolution = 600 entries), and the measurement
windows. `bench.tacho()` hand-turning 10 revolutions should show **~6000** edges.

---

## INTERFACING

Pico is 3.3 V; the original boards run 10 V CMOS.

- **Helipot and black switch need NO level shifting** — both passive. ✅ proven.
- **Shift up (3.3 → 10 V):** `F DISPLAY`, `F REF`, gate, `BLANK`. ~4 NPN circuits.
  ⚠ **A common-emitter NPN inverts** — `GATE_COUNTS_WHEN_LOW`, the `F REF` pulse polarity
  and the `F DISPLAY` pulse shape all flip when the 5 V bench wiring becomes the 10 V
  wiring. Invert in `config.py` or use two transistors per line, but decide it deliberately.
- **Shift down (+10 V → 3.3 V):** Board 2's start/stop pulse. Two resistors, 22k/10k.
- **Speed voltage out:** LM358 on +10 or +15 V, PWM 30 kHz + two-stage RC (10k/1µF ×2),
  10 kΩ pull-down.

### ⚠ Green LED — corrected 24 August 2026

The 1 kΩ series resistor is on Board 1, ≈8 mA at 10 V. Earlier versions of this file
concluded from that: *"a Pico pin can sink connector pin 8 directly. No driver transistor
needed."* **True on the bench, false in the deck** — the difference is the *off* state:

| Supply | Sinking (lit) | **Not** sinking (out) |
|---|---|---|
| 5 V bench | ~3 mA. Fine | pin floats to 3 V. Nothing conducts. Fine |
| 10 V deck | ~8 mA. Fine | pin pulled toward **8 V** through 1 kΩ; the Pico's clamp diode dumps ~4 mA into its own 3V3 rail, continuously, from switch-on |

**The 10 V install needs the low-side NPN** that `gt2101_parts_to_order.md` always listed.
The two documents disagreed; the parts list was right.

✅ **Bench session 6, 24 Aug: working at 5 V with no components at all** — one wire, Board 1
pin 8 → GP5, `Pin.OPEN_DRAIN`. ⚠ **`OPEN_DRAIN`, never `OUT`** — the pin must pull low or
let go, never drive high.

### ⚠ Tacho input — a JFET, not a PNP

```
        +3.3 V
          │
         10k
          │
  TACH ──[10k]──┤ G   ┌─── to a Pico GPIO   (inverted)
  0/-10V        │  J113 JFET
                └── S ── GND
```

TACH at 0 V → JFET conducts → pin LOW. TACH at −10 V → pinched off → pin HIGH.

**This is Gale's own circuit** — an E113 in exactly this configuration is Board 4's tacho
front-end, and sheet 3A records a defective E113 on Board 3 *"replaced by J113 (RS
Components)"*.

⚠ **Not a MOSFET** — a 2N7000/BS170 needs a positive gate, so with a signal that only sits
at 0 V or −10 V it would be off in both states.

⚠ **The PNP circuit described in earlier versions of this file cannot work** — "22k base
series, 100k to GND, emitter 3V3" leaves the base below the emitter at *both* tacho levels,
so the PNP conducts always and the output sits high permanently. Do not build it.

**Bench shortcut, used successfully 21 Aug:** the display boards work at **5 V**, so on the
bench the Pico drives them **directly, with no level shifters**. The transistors on order
are only needed for the final 10 V installation.

---

## POWER — LM7805 from +15 V, built and working

`GaleTT5Schem.pdf` shows +10 V made from +15 V via a 560R and a shunt zener — that alone
gives only ~9 mA, far less than the display needs, so take **+15 V** straight off the
4700µF reservoir. ±15 V is unregulated and may sit at 16–18 V unloaded.

Built: **+15 V → LM7805 → Pico VSYS (pin 39) / GND (pin 38)**. Heatsink **cold** at the
Pico's ~25 mA (≈0.3 W). Rule of thumb for Matt: too hot to keep a finger on = needs help.
The LED display runs from the deck's own +10 V rail, not from the 7805.

❓ **Worth re-testing:** if the tower's +10 V rail can supply ~50 mA, the 7805 can be fed
from a slot finger instead — one fewer wire and less heat.

Safety rule used throughout: **one power source at a time** — USB out when the 15 V is on.

⚠ **Do not put board 5 in the bench chain** — it takes AC from the mains transformer and
carries mains; a DC bench supply can't drive it.

---

## FIRMWARE — MODULAR

Eight files so each subsystem can be brought up alone. **`config.py` holds every setting —
it should be the only file Matt ever edits.**

`config.py` · `tacho.py` · `display.py` · `controls.py` · `drive.py` · `controller.py` ·
`main.py` · `bench.py`

**`main.py` is the entry point — MicroPython auto-runs that filename and nothing else.**

Bring-up order from the REPL: `bench.blink()` → `bench.lock()` / `bench.digits()` →
`bench.green()` → `bench.controls()` → `bench.tacho()` → `bench.drive(confirm=True)` →
`bench.loop()`. `bench.drive()` refuses to run without `confirm=True`.

⚠ **`display.py` and `bench.py` were rewritten from scratch on 21 August 2026** for the
counted-pulse scheme described in `gt2101_board1_display.md`. The old frequency-emitting
`display.py` and the old `bench.display()` are superseded and should not be revived.

Design points:

- Tacho edges timestamped into a ring buffer one revolution long. **Window chosen by
  state**: ~6 pulses spinning up, ~10 running, a full revolution for the display. One long
  window makes the loop oscillate — lag is the problem, not noise. ⚠ **Re-scale for 600 ppr.**
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
- **Nothing may call `display.show()` before the phase lock exists** — unlocked it falls
  back to blind mode and lands somewhere different at every power-up. This is the failure
  reported as "the display stopped working" on 24 August.
- **Average the ADC (16 reads) and only call `show()` when the value changes** — a raw
  `read_u16()` flickers the last digit continuously. ✅ proven.
- ⚠ **Any bench step that toggles an output needs a delay or a loop.** Four REPL lines run
  back to back light the green LED for microseconds and look exactly like a dead circuit.

Superseded: `tacho_count.py` — `bench.tacho()` does the same job and reads `config.py`.

---

## TOOLCHAIN

**Thonny 5.0.0** on Windows. MicroPython installed from inside Thonny (bottom-right corner
→ *Install MicroPython…*) — no separate UF2 download. **No drivers needed**; Windows 10/11
handle both the BOOTSEL drive and the serial port. Working pattern: File → Open (This
computer) → green play to test → red Stop → File → Save as (Raspberry Pi Pico).

⚠ **After saving a changed file to the Pico, press the red Stop button before re-running.**
MicroPython keeps the previously imported module in memory, so without the reboot you get
the old code with the new file on disk. This caused an hour of confusing results on
21 Aug. Do **not** "run config.py" to reboot — the red Stop button is the way.

⚠ **But the red Stop button also throws away the display's phase lock.** Once `bench.lock()`
has been run, break loops with **Ctrl-C**. For the same reason, type one-off experiments
into the **Shell pane**, not the editor — the green play button reboots the Pico.

**Meter note:** Matt's DMM shows **`0.L`** for open circuit. It does not go blank.

---

## OUTSIDE THE CONTROL TOWER — the suspension

⚠ Out of the PICO scope above, but recorded because the archive had **nothing at all** on it
until 24 August 2026. See `gt2101_suspension.md`.

Short version: the acrylic sub-chassis rides on three towers, each a coil spring inside a
plastic tube plunging into an aluminium cup. ✅ **The three springs are not the same rate,
and the odd one belongs at the arm corner** — that is the heaviest corner. They were fitted
wrong, which made the sub-chassis sit crooked and the tubes rub in their cups. Matt swapped
them on 24 August and the deck now floats freely.

Open: the resonant frequency has never been measured, and the bounce count went from 3–4
(friction, not damping) to 12 (too little damping) once the rubbing stopped. Target 4–6.

---

## STATUS, 24 August 2026

| Bench session | Date | Outcome |
|---|---|---|
| 1 | 19 Aug | Pico programmed and self-starting from `main.py` ✅ |
| 2 | 19 Aug | +15 V → LM7805 → Pico, runs on deck power, heatsink cold ✅ |
| 3 | 20 Aug | Helipot read into the Pico on GP26, full sweep ✅ |
| 4 | 21 Aug | **Board 1 display driven by the Pico** — `12.3`, `45.0`, `78.0`, `33.3` ✅ |
| 5 | 24 Aug | **Helipot drives the display end to end**; pot confirmed ten turns ✅ |
| 6 | 24 Aug | **Board 1's green LED driven by the Pico** — one wire, GP5, open-drain, no parts ✅ |

**All five boards are now identified from their own etched part numbers and studied from
their own drawings.** The architecture is settled. Board 1 is done apart from auto-lock.

Matt has spare boards 1–5, a spare motor PCB, a spare motor, a DMM, bench supply and scope;
prefers to leave the working deck shut. **Nothing has been ordered yet** — see
`gt2101_parts_to_order.md`.

---

## NEXT

**Board 1's only remaining job is auto-lock.** The board's 4013 comes up in a random state
at every power-up, so `bench.lock()` currently needs a human watching for the digits to go
dark. Wiring connector pin 10 (`RESET` out) into a Pico input lets the Pico find that state
by itself. One wire and one resistor — anything from about 47 kΩ to 470 kΩ at 5 V, so
**check the drawer before assuming this is blocked.**

Otherwise the next subsystem is **controls** (Board 2 pin 5, two resistors) or **tacho**
(needs the J113).

---

## File 2 — `feedback_explanation_level.md`

---
name: explanation-level
description: How Matt wants electronics work explained — start at absolute basics, one goal per session
type: feedback
---

Matt is competent with a soldering iron but **is not an electronics engineer and is not
confident with test equipment**. Given a 7-stage bench plan assuming current-limited
sweeps and scope probing, he replied *"strip this right down to basics as I do not know
what I'm doing."*

**Rule: default to beginner level for anything hands-on. One goal per work session.**

Why: he will say yes to a plan that sounds reasonable and then be unable to start it. He
doesn't push back until he's stuck, so pitching too high wastes his bench time.

How to apply:

- **One session = one measurable outcome.** "The meter reads 5 V."
- **Say which knob, which probe, which leg.** Pinouts in ASCII, pin numbers counted from a
  named physical landmark ("the corner nearest the USB socket").
- ⚠ **Do not tell him to count IC legs from the dot.** These Motorola packages carry
  several moulding dimples that look like a pin-1 mark. Instead: find the leg that beeps to
  +10 V — that is the highest-numbered pin — and pin 1 is the leg directly across the body
  from it. Works on every chip on every board.
- Give a **short table of what the reading means**, including the wrong answers and what
  to do about each.
- **Say explicitly what is NOT being done yet** and why. Reassurance that the deck isn't
  at risk matters to him.
- Ask for **two or three numbers** at the end, never a filled-in worksheet.
- ⚠ **Any step that toggles an output needs a delay or a loop in the snippet given to him.**
  On 24 August four REPL lines run back to back lit an LED for microseconds and read as a
  dead circuit. Never hand over code whose effect is invisible.
- Follow his own mental model where it's sound and change only the unsafe part.
- Conceptual/design discussion can stay at normal level — it's the bench steps that need
  stripping down.
- **He forgets component names** (called the LM7805 a "step-down"). Trust his description
  of *behaviour*; confirm part numbers.
- **He is right about his own hardware.** When he contradicts these notes about what is
  physically in front of him, he wins — that is how the five-board count was corrected, how
  the display board's four-state timing cycle was discovered on 21 Aug, how the suspension
  springs were found to be on the wrong legs on 24 Aug, and how the Helipot was found to be
  electrically off Board 2 the same day.
- **When he says "keep it short", cut to the commands.** No preamble, no reassurance, no
  summary. Two or three lines.
- **Do not tell him when to stop working.** He decides that.
- ⚠ **Read the whole project before answering, including anything written today.** On
  22 Aug a Board 4 answer was given without reading two documents written that morning, and
  three of its conclusions were already out of date. Check `project_info` timestamps first.

---

## File 3 — provenance discipline

Matt's public archive at `https://gale-electronics.github.io/GT2101/` was built by copying
a now-defunct site whose sources are unknown. **He has decided it must become a single
point of truth**, with every claim carrying a visible status: ✅ confirmed against
hardware, 📄 from a document, or ❓ unverified/inherited. Nothing is deleted for being
unverified — it is labelled.

**Four inherited prose pages have now been checked against the hardware, and all four were
substantially wrong**: `Disk-3-Optical-Sensor.pdf`, `Disk2AServoControl.pdf`,
`Disk2BPowerDriver.pdf` (misfiled — it describes the motor PCB) and
`Disk 4 — Reference Oscillator.pdf`. Recommend marking all four ❓ disputed.

By contrast, FANATSON's 2015 hand tracings have held up well, and his sheet numbering and
the circled destination numbers on his layout footers turned out to be trustworthy — they
are what let Boards 1–4 be joined into one signal chain.

Apply the same discipline in conversation: say where a claim comes from, and don't let an
inherited description harden into fact. See `control_tower_board_register.md`.

⚠ **The project's own notes can disagree with each other too.** On 24 August the green LED
was found to be described two ways in two documents — "no driver transistor needed" in the
board notes, "green LED low-side driver" in the parts list. Both were written honestly; one
was reasoning about the bench and one about the deck. When two project docs conflict, work
out which supply, which board issue, or which date each was written about before deciding
either is wrong.
