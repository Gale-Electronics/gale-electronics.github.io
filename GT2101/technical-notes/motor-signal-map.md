---
title: GT2101 — Motor & PCB Signal Map
layout: default
nav_order: 10
permalink: /GT2101/technical-notes/motor-signal-map/
---

# GT2101 Motor & PCB Signal Map

A consolidated probe map for the **Gale GT2101**’s logic and motor-drive boards, compiled from bench measurements and original notes.  
This table documents expected signal behaviour across the control stack and motor assembly, forming the basis for diagnostic or restoration work.

> **Diagnostic tip**  
> • “Drops to 0 when Start/Stop pressed” = a momentary, edge-triggered control line.  
> • **Clock lines** (1.048 MHz / 10 Hz / 1 Hz) drive timing and display multiplexing.  
> • **Tach** = motor feedback. **Speed Ref** = user-set frequency from the main pot.

---

## Top PCB

| Pin | Name / Function | Notes |
|:--:|------------------|-------|
| 1 | Positive Supply | + V rail |
| 2 | Drops to 0 when Start/Stop pressed | Momentary control |
| 3 | Display-generation frequency (switches between tach & desired) | Higher when showing desired speed and not running |
| 4 | 1 Hz / 10 Hz display-refresh clock | Switches between motor / desired display |
| 5 | LED signal | Drives 7-segment display |
| 6 | 1 Hz / 10 Hz display-refresh clock (duplicate) | Redundant feed |
| 7 | **Speed Reference** (10 Hz – 999 Hz) | Main pot setpoint |
| 8 | Ground | 0 V |

---

## 2nd PCB

| Pin | Name / Function | Notes |
|:--:|------------------|-------|
| 1 | Positive Supply |  |
| 2 | **1.048 MHz** clock signal | Master timebase |
| 3 | – |  |
| 4 | – |  |
| 5 | Pulse high when Start/Stop pressed | Edge command |
| 6 | Drops to 0 when Start/Stop pressed | Complement control |
| 7 | Return for 33⅓ select switch |  |
| 8 | Display frequency (tach/desired multiplex) | Matches Top Pin 3 |
| 9 | **Inverted tach** signal | Phase-inverted feedback |
| 10 | 1 Hz / 10 Hz display clock | Multiplex timing |
| 11 | **Fixed 33⅓ × 40 = 1332 Hz** | Reference for 33⅓ mode |
| 12 | Negative Supply | – V rail |
| 13 | 1 Hz / 10 Hz display clock (duplicate) | Redundant feed |
| 14 | Ground | 0 V |

---

## 3rd PCB (Middle)

| Pin | Name / Function | Idle V | Active V | Notes |
|:--:|------------------|:--:|:--:|--|
| 1 | Positive Supply | – | – |  |
| 2 | – | – | – |  |
| 3 | – | – | – |  |
| 4 | Pulse high when Start/Stop pressed | 0 | 10 | Command edge |
| 5 | Pot signal × 4 (40 Hz – 3996 Hz) | 0 | 10 | Derived setpoint |
| 6 | Unknown | – | – | To be confirmed |
| 7 | **Speed Signal** | – | – | Control to drive |
| 8 | Negative Supply | – | – |  |
| 9 | Ground | 0 | – |  |

---

## 4th PCB (Near Bottom)

| Pin | Name / Function | Idle V | Active V | Notes |
|:--:|------------------|:--:|:--:|--|
| 1 | Positive Supply | – | – |  |
| 2 | **1.048 MHz** clock signal | 0 | 10 | Timebase |
| 3 | Return from 33⅓ select switch | – | – |  |
| 4 | **Inverted tachometer** signal | 0 | 10 | Feedback (inverted) |
| 5 | **Tachometer** signal | 0 | –10 | Feedback (non-inverted) |
| 6 | Unknown | – | – |  |
| 7 | Negative Supply | – | – |  |
| 8 | Ground | – | – | 0 V |
| 9 | **Speed Reference** (10 Hz – 999 Hz) | 0 | 10 | Setpoint |

---

## Bottom PCB (Power Section)

| Pin | Name / Function | Idle V | Active V | Notes |
|:--:|------------------|:--:|:--:|--|
| 1 | 33⅓ indicator (selected / not selected) | 9.18 | 0 | Mode lamp logic |
| 2 | Positive Supply | 11.9 | – | + rail |
| 3 | Return from 33⅓ select (Freq = Pin 4 or 7) | 0 | 10 | Mode return |
| 4 | Frequency set by pot (0.1 – 99.9 × 40 → 4 – 3996 Hz) | 0 | 10 | Main setpoint |
| 5 | **Tach** signal | 0 | –10 | Motor feedback |
| 6 | **Speed Signal** | 0 | 5 | Drive control |
| 7 | **Fixed 33⅓ × 40 = 1332 Hz** | 0 | 10 | Reference |
| 8 | Negative Supply | –10.9 | – | – rail |
| 9 | Ground | 0 | – | 0 V |

---

## Motor DIN (Brushless DC Motor)

| Pin | Function | Notes |
|:--:|--|--|
| – | Run / Stop | Start/Stop control |
| – | V Speed | Control voltage / speed input |
| – | PG OUT | Pulse Generator (tach) output |
| – | AGND | Analogue ground |
| – | PGND | Power ground |
| – | Vin | Motor supply |

---

### Troubleshooting Cues

- **No start or frozen display** → Check the 1.048 MHz clock (2nd / 4th PCB Pin 2) and ± supply rails (+11.9 V / –10.9 V).  
- **Speed hunting** → Compare **Speed Ref** (Top 7, 4th 9) vs **Tach** (Bottom 5, 4th 4 & 5). A large phase error or missing inverted tach suggests a faulty comparator or open trace.  
- **33⅓ lamp stuck** → Inspect Bottom Pin 1 and 33⅓ return (Pins 3 & 7).  
- **Display wrong but speed OK** → Check multiplex clocks (Top 4/6, 2nd 10/13) and the display-frequency line (Top 3, 2nd 8).

> If you confirm unknown pins or capture oscilloscope traces, add them to this page to keep the archive living and accurate.
