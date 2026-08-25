---
name: gt2101-board2
description: Board 2 (GT201/3272ST) — the touch start/stop circuit, the F DISPLAY generator, and the full 14-pin connector map
type: reference
---

# GT2101 Board 2 — `GT201/3272ST`

**Studied 22 August 2026** from sheets `2ASchem`, `2BSchem` and `2Layout` (FANATSON,
17.09.2015), plus photographs of the spare board.

**Provenance:** ✅ read off the board · 📄 from the FANATSON tracings · ❓ unverified.

---

## 1. ✅ THE TOUCH SENSOR IS CONFIRMED

Sheet 2A is drawn around an electrode explicitly labelled **`TOUCH SENSOR`**. The
touch-sense hypothesis in `control_tower_board_register.md` — the bent copper tab beside
the Helipot bush, a 555 centimetres away — is no longer a hypothesis.

**The chain, 📄 from sheet 2A:**

```
TOUCH SENSOR ─ 10n ─ 10k ─→ MC1455P1 (=NE555) TRIGGER (pin 2)
                              │  220k / 270k / diode across DISCHARGE + THRESHOLD
                              ↓
                       T1 ─ 220k / 0.47µ ─ 1µ ─ T2  (1M bias to −10 V)
                              ↓
                       MC1748CP1 op-amp   (inverting, 1M feedback, 15k on +)
                              ↓
                       ¼ MC14011 NAND, inputs tied = inverter
                              ↓
                  connector pin 5 (HI)  and  pin 6 (LO)
```

⚠ The tracer's own warning on the sheet: **"T1, T2: types, values, pinouts only educated
guess. NO REFERENCES ON MY UNIT, NOT MEASURED!"** The 555 and the 4011 output stage are
drawn confidently; the two transistors are not.

### The output is a PULSE, not a level and not a latch

📄 Both waveforms are drawn on sheet 2A:

| Pin | Name | Waveform | Goes to |
|---|---|---|---|
| **5** | `START/STOP PULSE` **HI** | 0 V → **+10 V** pulse | PCB **3** |
| **6** | `START/STOP PULSE` **LO** | 0 V → **−10 V** pulse | PCB **1** |

Pin 5 arrives at Board 3's connector pin 4, which feeds the 4011 that clocks the 4013
that drives the BC214 / J113 drive gate. So **the touch pulse is what opens and closes
the motor drive** — sheets 2A and 3A agree end to end.

### Consequence for the Pico — this is the easy case

- **Tap pin 5.** It swings 0 → +10 V, so a two-resistor divider and a rising-edge
  interrupt on a GPIO. Pin 6 swings **negative** and would need the PNP-inverter
  treatment; there is no reason to use it.
- **With Board 3 removed, pin 5 drives nothing.** Nothing to lift, nothing to cut, no
  contention. Board 3's departure frees the exact signal the Pico wants.
- **The Pico holds the start/stop state in software**, since the hardware only emits an
  edge. Each pulse toggles. That is what `controls.py` would have done anyway.
- **The touch chain is self-contained** — it needs only +10 V, −10 V and GND, and nothing
  from Boards 3 or 4. It keeps working with Board 3 out of the stack.

---

## 2. The connector — 14 pins, mapped

📄 From the layout sheet's footer, cross-checked against sheet 2B. Arrows are the
tracer's; a circled number is the board at the other end.

| Pin | Signal | Direction |
|---|---|---|
| 1 | **+10 V** | in |
| 2 | 1.048 MHz crystal ← ④ | in |
| 3 | ← ③ (STILL/TURNING status) | in |
| 4 | ← ③ (STILL/TURNING status) | in |
| 5 | **`START/STOP PULSE` HI** → ③ | out |
| 6 | **`START/STOP PULSE` LO** → ① | out |
| 7 | `F REF ×40` ← ④ | in |
| 8 | **`F DISPLAY`** → ① | out |
| 9 | `INV TACH` ← ④ | in |
| 10 | → ① — almost certainly the **~1 Hz gate** | out |
| 11 | `1332 Hz FIX` (= 333 × 40) → ⑤ | out |
| 12 | **−10 V** | in |
| 13 | **`RESET` ← ①** | in |
| 14 | **GND** | in |

⚠ Sheets 2B and 2Layout disagree slightly on pins 7 and 11 — 2B calls pin 7 "F VAR or FIX
from the speed switch via PCB 4" and pin 11 "1332 Hz FIX 'D'". Same signals, different
descriptions. Not resolved.

⚠ The layout sheet is headed **"② MIRRORED"** — the opposite of Board 3's sheet, which is
not. Do not carry an orientation habit between them.

### What this settles about Board 1

- `F DISPLAY` reaches Board 1 from **Board 2 pin 8**.
- The gate reaches Board 1 from **Board 2 pin 10**, derived from the 4040's Q21 (0.5 Hz)
  and Q19 (2 Hz) through the 4001 / 4016 network. The backplane tracer marked the "~1 Hz"
  gate with a question mark; this is where it comes from.
- **Board 1's pin 10 `RESET` output lands on Board 2 pin 13**, resetting the 4040. That is
  where the display board's reset goes — worth knowing, given `config.py` says "never
  drive it".

---

## 3. ⚠ The archive prose is wrong again — two more pages

Both inherited pages were checked against the drawings and the hardware.

**`Disk2AServoControl.pdf`** — lists **MC14520CP** and **MC14516CP**, neither of which is
on the board; omits the MC14521, MC14011, MC14016 and MC1748 that are; calls the board the
"central element of the phase-lock servo loop" when the 4046 PLL is on Board 4; says it
receives "tach feedback from Disk 3" when `INV TACH` arrives from Board 4 on pin 9. Most
tellingly, it **does not mention the touch sensor at all** — the most distinctive circuit
on the board.

**`Disk2BPowerDriver.pdf`** — describes LM324/LM358 op-amps, BD675A/BD676A power
transistors, TO-220 devices, three-phase drive currents, "mounted directly above the motor
housing". **That is the motor controller PCB, not a tower board.** It has been filed as a
tower disk by mistake.

### This resolves "is disk 2 one board or two?"

**One board.** The archive's "2A" and "2B" are the tracer's **two schematic sheets of one
board**, and the "Disk 2B Power Driver" page is a misfiled description of the separate
motor PCB. That is where the two-board idea came from.

**Recommended: mark both pages ❓ disputed in the archive**, alongside
`Disk-3-Optical-Sensor.pdf`. Three inherited prose pages checked, three substantially
wrong. Treat the whole set as unreliable and prefer the tracings and the hardware.

---

## 4. Chips on the board ✅

Read off the spare, 20 August 2026: **MC1455P1** (7336), **MC14040CP** (M75-39),
**MC14521CP** (7521), **MC14016CP** (M75-04), **MC14011CP** (AA7533), **MC14001CP** (7532),
**MC1748CP1** (M 535 A). Paper sticker reading **"OK NOV 81"** still attached.

---

## 5. Open questions

| ❓ | Why it matters |
|---|---|
| Which Board 1 pin the LO pulse (pin 6) lands on | Decides whether it needs lifting when the Pico takes over Board 1 |
| What the tab actually is — contact or gap to the shaft | Determines whether the sense is conductive or capacitive |
| Whether the 555's threshold is reliable in practice | If not, take the tab straight to a Pico pin instead |
| T1 and T2's real identities | The tracer guessed; nobody has read them off the board |
| Pins 7 and 11 — the two sheets disagree | Minor, but unresolved |

---

## 6. ✅ The Helipot is electrically OFF this board — 24 August 2026

**Matt, on the bench:** all three Helipot leads run directly to the Pico, and **nothing else
is connected to the pot**. It is held to Board 2 by a **brass nut and washer** only.

So Board 2's role in the Pico build is exactly two things: **the touch sensor, and a bracket
for the pot.**

⚠ **Do not disturb the brass nut and washer.** The touch electrode is a bent copper tab
beside that bush, and the sensitivity depends on what the bush and shaft are electrically
tied to. No ground strap, no steel replacement, no cleaning under the washer. If touch
behaviour changes after the tower is reassembled, that hardware is the first suspect.
