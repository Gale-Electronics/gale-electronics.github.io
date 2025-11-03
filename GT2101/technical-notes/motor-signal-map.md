---
title: GT2101 — Motor & PCB Signal Map
layout: default
nav_order: 10
---

# GT2101 Motor & PCB Signal Map

Measured functions and expected behaviours for each GT2101 logic/drive board.  
Use this as a guided probe map when diagnosing **speed errors, non-start, or unstable display**.

> **Tip:** “Drops to 0 when Start/Stop pressed” indicates a momentary control line (edge-triggered).  
> **Clock lines** (1.048 MHz / 10 Hz / 1 Hz) drive timing and display multiplexing.  
> **Tach** = motor feedback. **Speed Ref** = user-set frequency from the main pot.

---

## Top PCB

| Pin | Name / Function                                                                 | Notes |
|-----|----------------------------------------------------------------------------------|-------|
| 1   | Positive Supply                                                                  |      |
| 2   | Drops to 0 when Start/Stop pressed                                               | Momentary control line |
| 3   | Frequency to generate display (switches between motor tach and desired signal)   | Higher frequency when showing **desired speed** and not running |
| 4   | 1 Hz / 10 Hz clock for display refresh                                           | “showing motor / showing desired” |
| 5   | LED signal                                                                       | Display LED drive |
| 6   | 1 Hz / 10 Hz clock for display refresh (duplicate of Pin 4)                      | Redundant feed |
| 7   | **Speed Reference** signal (10 Hz–999 Hz), set by main pot                       | User setpoint |
| 8   | Ground                                                                           | 0 V |

---

## 2nd PCB

| Pin | Name / Function                                                                 | Notes |
|-----|----------------------------------------------------------------------------------|-------|
| 1   | Positive Supply                                                                  |      |
| 2   | **1.048 MHz** clock signal                                                       | Master timebase |
| 3   | –                                                                                |      |
| 4   | –                                                                                |      |
| 5   | Pulse high when Start/Stop pressed                                               | Edge/command pulse |
| 6   | Drops to 0 when Start/Stop pressed                                               | Complementary control |
| 7   | Return for 33⅓ select switch                                                     |      |
| 8   | Frequency to generate display (tach/desired multiplex)                           | Matches Top PCB Pin 3 |
| 9   | **Inverted tach** signal                                                         | Phase-inverted feedback |
| 10  | 1 Hz / 10 Hz clock for display refresh                                           | Mux timing |
| 11  | **Fixed 33⅓ × 40 = 1332 Hz**                                                    | Reference for 33⅓ mode |
| 12  | Negative Supply                                                                  |      |
| 13  | 1 Hz / 10 Hz clock for display refresh (duplicate)                               | Redundant feed |
| 14  | Ground                                                                           | 0 V |

---

## 3rd PCB (Middle)

| Pin | Name / Function                                   | Idle V | Active V | Notes |
|-----|----------------------------------------------------|:------:|:--------:|-------|
| 1   | Positive Supply                                    |   –    |    –     |      |
| 2   | –                                                  |   –    |    –     |      |
| 3   | –                                                  |   –    |    –     |      |
| 4   | Pulse high when Start/Stop pressed                 |   0    |    10    | Command edge |
| 5   | Pot signal frequency ×4 (40 Hz–3996 Hz)            |   0    |    10    | Derived setpoint |
| 6   | ???                                                |   –    |    –     | Unknown (document when determined) |
| 7   | **Speed Signal**                                   |   –    |    –     | Control to drive section |
| 8   | Negative Supply                                    |   –    |    –     |      |
| 9   | Ground                                             |   0    |    –     | 0 V |

---

## 4th PCB (Near Bottom)

| Pin | Name / Function                                   | Idle V | Active V | Notes |
|-----|----------------------------------------------------|:------:|:--------:|-------|
| 1   | Positive Supply                                    |   –    |    –     |      |
| 2   | **1.048 MHz** clock signal                         |   0    |    10    | Timebase |
| 3   | Return from 33⅓ select switch                      |   –    |    –     |      |
| 4   | **Inverted tachometer** signal                     |   0    |    10    | Feedback (inverted) |
| 5   | **Tachometer** signal                              |   0    |   −10    | Feedback (non-inverted, negative swing) |
| 6   | ???                                                |   –    |    –     | Unknown |
| 7   | Negative Supply                                    |   –    |    –     |      |
| 8   | Ground                                             |   –    |    –     | 0 V |
| 9   | **Speed Reference** (10 Hz–999 Hz; main pot)       |   0    |    10    | Setpoint |

---

## Bottom PCB (Power PCB)

| Pin | Name / Function                                                     | Idle V | Active V | Notes |
|-----|----------------------------------------------------------------------|:------:|:--------:|-------|
| 1   | 33⅓ indicator (selected / not selected)                              |  9.18  |    0     | Mode lamp logic |
| 2   | Positive Supply                                                      |  11.9  |    –     | + rail |
| 3   | Return from 33⅓ select (Freq = Pin 4 or Pin 7)                       |   0    |    10    | Mode return |
| 4   | Frequency set by pot (0.1–99.9 × 40 → 4–3996 Hz)                     |   0    |    10    | Main setpoint |
| 5   | Tach Signal                                                          |   0    |   −10    | Motor feedback |
| 6   | **Speed Signal**                                                     |   0    |    5     | Control to drive |
| 7   | **Fixed 33⅓ × 40 = 1332 Hz**                                        |   0    |    10    | 33⅓ reference |
| 8   | Negative Supply                                                      | −10.9  |    –     | − rail |
| 9   | Ground                                                               |   0    |    –     | 0 V |

---

## Motor DIN (Brushless DC Motor)

| Pin | Function  | Notes |
|-----|-----------|-------|
| –   | Run/Stop  | Start/Stop control line |
| –   | V Speed   | Control voltage / speed input |
| –   | PG OUT    | Pulse Generator (tach) output |
| –   | AGND      | Analogue ground |
| –   | PGND      | Power ground |
| –   | Vin       | Motor supply |

---

### Troubleshooting cues

- **No start / display frozen:** Verify 1.048 MHz (2nd/4th PCBs Pin 2). If missing, trace back to clock generator and its supply rails (+11.9 V / −10.9 V).
- **Speed hunts:** Compare **Speed Ref** (Top Pin 7 / 4th Pin 9) vs **Tach** (Bottom Pin 5, 4th Pins 4/5). Large phase error or missing inverted tach often points to a failed comparator or broken trace.
- **33⅓ lamp stuck:** Check Bottom Pin 1 logic and the 33⅓ return path (Pins 3 & 7).
- **Display wrong but speed OK:** Multiplex clocks (1 Hz/10 Hz on Top Pins 4/6 and 2nd Pins 10/13) or the “display frequency” line (Top Pin 3 / 2nd Pin 8).

> If you refine unknown pins or capture scope images, add them here to keep the archive living and exact.
