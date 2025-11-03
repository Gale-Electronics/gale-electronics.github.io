---
layout: bare
title: GT2101 — Motor & PCB Signal Map
permalink: /GT2101/technical-notes/motor-signal-map/
show_archive_banner: true
archive_note: >
  Consolidated probe map reconstructed from the original galeaudio.com technical notes and modern restoration data.
  This record documents the expected signal behaviour across the GT2101’s control tower and motor stack for future diagnosis and preservation.
---

# GT2101 — Motor & PCB Signal Map

A consolidated probe map for the **Gale GT2101**’s logic and motor-drive boards, compiled from bench measurements and archived notes.  
This table records typical signal behaviour across the control stack and motor assembly — forming a foundation for reverse engineering, repair, and historical documentation.

> **Diagnostic Tips**
> - “Drops to 0 when Start/Stop pressed” = momentary, edge-triggered control line.  
> - **Clock lines** (1.048 MHz / 10 Hz / 1 Hz) drive timing and display multiplexing.  
> - **Tach** = motor feedback. **Speed Ref** = user-set frequency from the main dial.

---

## Top PCB

| Pin | Name / Function | Notes |
|:--:|------------------|-------|
| 1 | Positive Supply | + V rail |
| 2 | Drops to 0 when Start/Stop pressed | Edge control |
| 3 | Display-generation frequency (tach ↔ desired) | Higher when showing desired speed and not running |
| 4 | 1 Hz / 10 Hz display-refresh clock | Motor/desired display timing |
| 5 | LED signal | 7-segment display driver |
| 6 | 1 Hz / 10 Hz display-refresh clock (duplicate) | Redundant feed |
| 7 | **Speed Reference (10 Hz – 999 Hz)** | Main pot setpoint |
| 8 | Ground | 0 V reference |

---

## 2nd PCB

| Pin | Name / Function | Notes |
|:--:|------------------|-------|
| 1 | Positive Supply | + V rail |
| 2 | **1.048 MHz Clock** | Master timebase |
| 5 | Pulse High when Start/Stop pressed | Edge command |
| 6 | Drops to 0 when Start/Stop pressed | Complement control |
| 7 | Return for 33⅓ Select Switch |  |
| 8 | Display Frequency (tach / desired multiplex) | Matches Top Pin 3 |
| 9 | **Inverted Tach Signal** | Phase-inverted feedback |
| 10 | 1 Hz / 10 Hz Display Clock | Multiplex timing |
| 11 | **Fixed 33⅓ × 40 = 1332 Hz** | Reference for locked speed |
| 12 | Negative Supply | – V rail |
| 13 | 1 Hz / 10 Hz Display Clock (duplicate) | Redundant feed |
| 14 | Ground | 0 V reference |

---

## 3rd PCB (Middle)

| Pin | Name / Function | Idle V | Active V | Notes |
|:--:|------------------|:--:|:--:|--|
| 1 | Positive Supply | – | – |  |
| 4 | Pulse High when Start/Stop pressed | 0 | 10 | Command edge |
| 5 | Pot Signal × 4 (40 Hz – 3996 Hz) | 0 | 10 | Derived setpoint |
| 6 | Unknown | – | – | To be confirmed |
| 7 | **Speed Signal** | – | – | Control to motor drive |
| 8 | Negative Supply | – | – | – V rail |
| 9 | Ground | 0 | – | Reference |

---

## 4th PCB (Near Bottom)

| Pin | Name / Function | Idle V | Active V | Notes |
|:--:|------------------|:--:|:--:|--|
| 1 | Positive Supply | – | – | + V rail |
| 2 | **1.048 MHz Clock Signal** | 0 | 10 | Timebase |
| 3 | Return from 33⅓ Select Switch | – | – |  |
| 4 | **Inverted Tachometer Signal** | 0 | 10 | Feedback (inverted) |
| 5 | **Tachometer Signal** | 0 | –10 | Feedback (non-inverted) |
| 6 | Unknown | – | – |  |
| 7 | Negative Supply | – | – | – V rail |
| 8 | Ground | – | – | 0 V |
| 9 | **Speed Reference (10 Hz – 999 Hz)** | 0 | 10 | User setpoint |

---

## Bottom PCB (Power Section)

| Pin | Name / Function | Idle V | Active V | Notes |
|:--:|------------------|:--:|:--:|--|
| 1 | 33⅓ Indicator (selected / not) | 9.18 | 0 | Mode lamp logic |
| 2 | Positive Supply | 11.9 | – | + rail |
| 3 | Return from 33⅓ Select (Freq = Pin 4 or 7) | 0 | 10 | Mode return |
| 4 | Frequency Set by Pot (0.1 – 99.9 × 40 → 4–3996 Hz) | 0 | 10 | Main setpoint |
| 5 | **Tach Signal** | 0 | –10 | Motor feedback |
| 6 | **Speed Signal** | 0 | 5 | Drive control |
| 7 | **Fixed 33⅓ × 40 = 1332 Hz** | 0 | 10 | Reference |
| 8 | Negative Supply | –10.9 | – | – rail |
| 9 | Ground | 0 | – | 0 V reference |

---

## Motor DIN Connector (Brushless DC Motor)

| Pin | Function | Notes |
|:--:|--|--|
| – | Run / Stop | Start/Stop control |
| – | V Speed | Control voltage input |
| – | PG OUT | Pulse Generator (tach) output |
| – | AGND | Analogue ground |
| – | PGND | Power ground |
| – | Vin | Motor supply voltage |

---

### Troubleshooting Cues

- **No start or frozen display** → Check the 1.048 MHz clock (2nd / 4th PCB Pin 2) and ± supply rails (+11.9 V / –10.9 V).  
- **Speed hunting** → Compare **Speed Ref** (Top 7, 4th 9) vs **Tach** (Bottom 5, 4th 4 & 5). A large phase error indicates comparator or trace fault.  
- **33⅓ lamp stuck** → Inspect Bottom Pin 1 and select returns (Pins 3 & 7).  
- **Display incorrect but speed OK** → Check multiplex clocks (Top 4/6, 2nd 10/13) and display-frequency line (Top 3, 2nd 8).

> Contributions from bench measurements and archival records.  
> If you verify unknown pins or capture oscilloscope traces, please add them here to extend the archive.
