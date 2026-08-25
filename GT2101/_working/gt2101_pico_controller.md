---
name: gt2101-pico-controller
description: Adding a Raspberry Pi Pico as the new control logic in the Gale GT2101's control tower — the only active GT2101 workstream
type: project
---

# GT2101 — the Pico controller

**Rewritten 22 August 2026.** The previous version dated from the morning of 20 August,
before the board register and before Boards 1, 2, 3 and 4 were each studied from their own
drawings. Most of its open questions are now answered and several of its statements were
wrong. Write bench instructions per [[explanation-level]].

**Updated 24 August 2026** after bench session 5 — the Helipot turn count is settled and the
pot now drives the display end to end.

**Updated again 24 August 2026** after bench session 6 — **the Pico drives Board 1's green
LED** (§ BENCH LOG), the "no driver transistor needed" claim in § INTERFACING is corrected,
the Helipot's electrical relationship to Board 2 is settled (§ THE CONTROLS), and the
minimum-intrusion wiring plan is written down for the first time (§ HOW THE PICO MEETS
THE TOWER).

**Scope:** Matt is adding new control logic to the GT2101's control tower using a Pico and
a handful of small parts. Everything else on the deck stays original.

Dropped and not to be revived unless Matt says so: reverse-engineering or recloning the
locked 2009 "Howie board", chasing its ATmega88PA firmware, and the Walkbury Electronics
manufacturing enquiry.

---

## THE DECK

Gale **GT2101**, late-1970s acrylic-plinth turntable. The project folder holds the original
Gale schematic and layout PDFs (TT1–TT5, backplane, motor PCB) plus a parts list.

⚠ **Those PDFs are image-only scans** — `project_read` returns empty text. A cloud session
cannot read them from the project. **Attach a PDF directly to the chat instead** and Claude
can render and read it visually. That is how Boards 1–4 were worked out.

⚠ **They are also not Gale factory drawings.** Every schematic and layout in the archive is
hand-drawn reverse-engineering by one person (FANATSON) in 2015. The typed prose pages are
worse — four have been checked against the hardware and four were substantially wrong. See
`gt2101_archive_provenance.md`.

The control tower currently runs a board someone else remade with modern parts around
2009–2010 (ATmega88PA, four SN74AHC594 shift registers, three 7-segment displays). **It
works well** — the deck is playable as it stands, so none of this is under time pressure.

---

## THE FIVE BOARDS — and which ones stay

Numbered 1 at the top to 5 at the bottom. Full detail in
`control_tower_board_register.md`; signals in `gt2101_backplane_signal_map.md`.

| Board | Gale no. | What it does | In the Pico build? |
|---|---|---|---|
| 1 (top) | `3155ST` | Display | **stays** — the Pico drives it ✅ working |
| 2 | `3272ST` | Touch start/stop, display timing, carries the Helipot | **stays** — as touch sensor and pot bracket only |
| 3 | `3275ST` | `F VAR` generator + drive-voltage gate | ❌ **out** |
| 4 | `3276ST` C | Crystal, reference divider, tacho front-end, **the servo** | ❌ **out** |
| 5 (bottom) | `3285NH` | Power supply + external interface | **stays** |
| backplane | `3281NH` | Flexible ribbon by *flexicon* | stays |

**Boards 3 and 4 are one servo split over two boards** — 4 decides the drive voltage, 3
decides whether it is allowed out. They leave together. Neither is modified: they unplug,
reversibly, and go to the spares box.

⚠ **This supersedes the old "do not plan to unplug boards" rule**, which was written when
Board 2 was believed to be the "Servo Motor Drive" and Board 3 was believed to produce the
drive voltage. Both beliefs came from the defunct website and both are wrong.

---

## ARCHITECTURE — Pico is brains only

Matt's stated goal: **"all the logic from the Pico, everything else original."** Original
power supply, original LED display, original front-panel controls, original motor PCB,
original wiring loom.

**The Pico's carrier board sits in slot 3** — the corroded ISSUE B spare of `3275ST` is the
leading candidate, since its edge fingers already fit the backplane socket and its three pot
eyelets are in the right place.

### Where the Pico connects

| Job | Where | How |
|---|---|---|
| **Speed setting** | Helipot, mounted on Board 2 but wired only to the Pico | passive, straight to GP26. ✅ working |
| **Start/stop** | Board 2 pin 5 — a 0 → +10 V pulse | 22k/10k divider into a GPIO, rising-edge interrupt |
| **Display** | Board 1 pins 6, 7, 11 (+3, 10 optional) | ✅ working at 5 V; needs level shifting at 10 V |
| **Green LED** | Board 1 pin 8 | ✅ working at 5 V, open-drain on GP5. **NPN driver required at 10 V** |
| **Tacho in** | the `TACH` net, 0/−10 V | **J113 JFET inverter** — see below |
| **Drive out** | Board 3's pin-7 net | LM358 buffering filtered PWM |

**The Pico holds start/stop state in software.** Board 2 only ever emits an edge, so each
pulse toggles — which is what `controls.py` was going to do anyway.

---

## HOW THE PICO MEETS THE TOWER — minimum intrusion

**Written 24 August 2026.** 📄 throughout — built on the traced connector tables in the
board studies, not on a meter. The two checks at the end turn most of it ✅.

### The principle: the backplane is the loom

Boards 3 and 4 leaving frees **two edge sockets**, and most of what the Pico needs already
terminates on their fingers. Anything reached through a socket costs no wire, no solder
joint on an original board, and reverses by pulling a card.

**Slot 3 fingers (`3275ST` pinout) give, free:**

| Finger | What the Pico gets |
|---|---|
| 1, 8, 9 | +10 V, −10 V, GND |
| 4 | the touch pulse from Board 2 pin 5 — 0→+10 V, needs the 22k/10k divider |
| 7 | **drive voltage out to the motor**, through the original loom via Board 5 |
| 6 | now a dead net (was Board 4 pin 6) — a free signal channel between the two slots |

**Slot 4 fingers (`3276ST` pinout) give, free:**

| Finger | What the Pico gets |
|---|---|
| 1, 7, 8 | +10 V, −10 V, GND |
| 5 | **`TACH` from the motor** — the only place it appears |
| 9 | **`F REF` straight to Board 1 pin 11** — a backplane path to the display |
| 3 | the black switch's VAR/FIX selection, as a frequency |
| 2, 4 | channels *into* Board 2 (its 1.048 MHz and INV TACH inputs), now unused |

⚠ The tacho and the display clock are **only** at slot 4; the touch pulse and the motor
output **only** at slot 3. Neither slot alone does the job.

### Suggested arrangement — Pico on the slot-4 card

- **Card A, slot 4:** the Pico, the J113 tacho inverter (gate straight to finger 5), `F REF`
  out on finger 9, the green-LED NPN, and the LM358 + RC filter. The filtered drive voltage
  leaves on **finger 6**, the dead net.
- **Card B, slot 3:** almost nothing — a link from finger 6 to finger 7 (drive to the motor)
  and the 22k/10k touch divider off finger 4.
- **One short jumper** between the two cards carries the divided touch pulse back to the
  Pico. That is the only wire the architecture itself forces.

Both cards take all three rails from their own fingers. **No contention anywhere:** with
Boards 3 and 4 out, Board 2 pin 5 drives nothing, Board 1 pin 11 is driven by nothing, and
the motor drive net has no other source.

⚠ Slot 3 has −10 V on 8 / GND on 9; slot 4 has −10 V on 7 / GND on 8. **The two cards are
not interchangeable and must be legended.**

### What is still not reachable — the real wire count

| Need | Wires | Notes |
|---|---|---|
| Helipot | **0** | ✅ its three leads are already a free tail going straight to the Pico. Board 2 holds it mechanically and nothing else |
| Board 1 `F DISPLAY`, gate (pins 6, 7) | 2 | + level shifters |
| Board 1 `RESET` in, for auto-lock (pin 10) | 1 | board-to-board net, no route to a vacated slot |
| Board 1 green LED (pin 8) | 1 | could share the display card's route |
| +15 V for the 7805 | 0–1 | ❓ if the +10 V rail can supply ~50 mA, take it from finger 1 and this wire disappears — and the regulator runs cooler |

So: **one jumper plus three or four flying wires**, against zero modifications to any
original board. Reversal is pulling two cards and putting Boards 3 and 4 back.

### One circuit point to decide now

`V_IDLE` = 0 V is firmware's only protection with Board 3 out, and an LM358 on a single
supply will not sit at a true 0 V unaided. Run it from the backplane's +10 V (no wire) with
a **10 kΩ pull-down on its output**, so idle is 0 V by hardware even if the PWM stops or the
Pico hangs. Using −10 V as its negative rail gives a cleaner zero but puts a
negative-voltage fault mode in front of the motor drive — not worth it.

### The two checks that settle it

1. **+10 V rail under load** — how far it sags with ~50 mA drawn. Decides whether the Pico's
   supply needs a wire to the reservoir.
2. **Board 1 pin 8 to deck GND, unpowered, in the assembled tower** — silence means Board 5
   does not ground the green LED net and the Pico owns it.

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

- **This closes an open question in `gt2101_board3.md`**, which still asks what drove the
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
- Board 2 sits next to slot 3, so the pot's tail stays short whichever slot the Pico takes.
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

📄 From Board 3's layout sheet, which tabulates **both sides** of its gate:

| Condition | Board 4 pin 6 (demand in) | Board 3 pin 7 (out to motor) |
|---|---|---|
| **STILL** | 10 V | **0 V** |
| 33⅓ rpm | 1.2 V | 1.2 V |
| 45 rpm | 1.6 V | 1.6 V |
| 78 rpm | 2.4 V | 2.4 V |

Lowest speed is lowest voltage, rising roughly through the origin — which is what a
brushless motor needs, since back-EMF rises with speed. **"STILL = 10 V" is Board 4's loop
railing to maximum demand with the platter stopped, and Board 3 mutes it to 0 V.**

⚠ **The backplane sheet only ever recorded the input column.** That is where the project's
long-standing "STILL: 10 V" came from, and it was being read as though it reached the motor.

### ⚠ The single most important consequence of the architecture

**`V_IDLE` is 0 V, not 10 V** — and with Board 3 out, **firmware is the only thing holding
it there.** The 1975 design never let 10 V reach a stationary platter; the hard drive
ceiling in `drive.set_drive()` and the idle value stop being belt-and-braces and become the
only braces. This is the case that cooks the BD675A/676A.

📄 not ✅ — these are the tracer's figures on a sheet marked PRELIMINARY. **Measuring Board 3
pin 7 on the running deck is the most valuable measurement left in the project.**

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

- **Helipot and black switch need NO level shifting** — both passive. ✅ proven on the bench.
- **Shift up (3.3 → 10 V):** `F DISPLAY`, `F REF`, gate, `BLANK`. ~4 NPN circuits.
  ⚠ **A common-emitter NPN inverts.** `GATE_COUNTS_WHEN_LOW`, the `F REF` pulse polarity and
  the `F DISPLAY` pulse shape all flip when the bench 5 V wiring becomes the 10 V wiring.
  Either invert them in `config.py` or use two transistors per line — but decide it
  deliberately rather than meeting it as a surprise.
- **Shift down (+10 V → 3.3 V):** Board 2's start/stop pulse. Two resistors, 22k/10k.
- **Speed voltage out:** LM358 on +10 or +15 V, PWM 30 kHz + two-stage RC (10k/1µF ×2),
  10 kΩ pull-down on the output.

### ⚠ Green LED — correction, 24 August 2026

Earlier versions of this file said the 1 kΩ series resistor is on Board 1, so a Pico pin can
sink connector pin 8 directly, **"no driver transistor needed."** That is true on the bench
and **false in the deck** — and the difference is the *off* state, not the on state:

| Supply | Sinking (LED lit) | **Not** sinking (LED out) |
|---|---|---|
| 5 V bench | ~3 mA. Fine | the pin floats to 5 − 2 = **3 V**. Nothing conducts. Fine |
| 10 V deck | ~8 mA. Fine | the pin is pulled toward **8 V** through 1 kΩ; the Pico's clamp diode conducts and dumps ~4 mA into its own 3V3 rail, continuously, from the instant the deck is switched on |

**So the 10 V installation needs the low-side NPN** that `gt2101_parts_to_order.md` has
always listed for it. The two documents disagreed; the parts list was right.

On the bench, open-drain and no parts at all — ✅ proven, bench session 6.

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

## POWER — LM7805 from +15 V, built and working

`GaleTT5Schem.pdf` shows +10 V made from +15 V via a 560R and a shunt zener — that alone
gives only ~9 mA, far less than the display needs, so take **+15 V** straight off the
4700µF reservoir. ±15 V is unregulated and may sit at 16–18 V unloaded.

Built: **+15 V → LM7805 → Pico VSYS (pin 39) / GND (pin 38)**. Heatsink **cold** at the
Pico's ~25 mA (≈0.3 W). Rule of thumb for Matt: too hot to keep a finger on = needs help.
The LED display runs from the deck's own +10 V rail, not from the 7805.

❓ **Worth re-testing:** if the tower's +10 V rail can supply ~50 mA, the 7805 can be fed
from a slot finger instead — one fewer wire, and less heat to shed. See § HOW THE PICO MEETS
THE TOWER.

Safety rule used throughout: **one power source at a time** — USB out when the 15 V is on.

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
counted-pulse scheme in `gt2101_board1_display.md`. The old frequency-emitting `display.py`
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

**What the LED should indicate is undecided.** It has no job of its own now that Boards 3
and 4 are leaving. The obvious use is a lock indicator — out when stopped, flashing through
the 4 s soft-start ramp, steady once the tacho says the platter is in tolerance — which also
makes the servo visible during the tacho bring-up.

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

---

## STATUS, 24 August 2026

Bench sessions 1–6 complete. **Board 1 is done apart from auto-lock**: the display, the
green LED, and the deck's speed pot all answer to the Pico, and the pot drives the display
in real time.

**All five boards have now been identified from their own etched part numbers and studied
from their own drawings.** The architecture is settled: Boards 3 and 4 come out, Boards 1,
2 and 5 stay, and the Pico takes slot 3 (or slot 4 — see § HOW THE PICO MEETS THE TOWER).

Matt has spare boards 1–5, a spare motor PCB, a spare motor, a DMM, bench supply and scope;
prefers to leave the working deck shut. Nothing has been ordered yet — see
`gt2101_parts_to_order.md`.

---

## NEXT

**Board 1's only remaining job is auto-lock, and it is now the project's most annoying
recurring fault, not a nicety.** The board's 4013 comes up in a random state at every
power-up, so `bench.lock()` needs a human watching for the digits to go dark — and every
time that step is skipped, the display looks broken. Wiring connector pin 10 (`RESET` out)
into a Pico input lets the Pico find that state by itself. One wire and one resistor —
anything from about 47 kΩ to 470 kΩ at 5 V. **Check the drawer before ordering; this may
not be blocked at all.**

Otherwise the next subsystem is **controls** (Board 2 pin 5, two resistors) or **tacho**
(needs the J113).

---

## Open items

- **Order the parts.** See `gt2101_parts_to_order.md`.
- **Confirm the tacho pulses per revolution** — expect ~600 per platter turn.
- **Measure Board 3 pin 7 on the running deck** at each speed. Four numbers that are
  currently 📄 become ✅, and they are the whole specification for `drive.nominal_drive()`.
- **Settle the Helipot's resistance** — label says 1 kΩ, one bench reading said 10 kΩ.
- ~~Helipot turn count~~ — ✅ **settled 24 Aug: ten turns.**
- ~~Whether the Helipot is still electrically on Board 2~~ — ✅ **settled 24 Aug: it is not.**
- ~~Can the Pico drive the green LED~~ — ✅ **settled 24 Aug: yes.**
- **Decide what the green LED should indicate.**
- **Decide the speed range the ten turns map onto** — full 30–80 rpm, or a trim band.
- Decide which of the three touch options to use.
- **Does Board 5 ground the green LED net?** Beep test in the assembled tower, unpowered.
- **Can the tower's +10 V rail supply ~50 mA?** Decides whether the 7805 needs a wire to the
  reservoir.
- Measure display current with all eights lit.
- Read Board 5's etched part number, and check Boards 1, 2 and 5 for issue letters.
- Measure the tower gap height (a socketed Pico needs ~12 mm).
