# GT2101 Restoration Shopping List

Parts required to repair and service the original boards for the Gale GT2101 turntable control tower.

Last updated: 7 October 2026.

---

## 1. Board 4 (Original Tower Board — Early Revision)

**Target Board:** Original in-tower Board 4 (the revision with the 14-pin 4013 divider).  
**Circuit Function:** Generates `F REF` / `1×F` reference clock on Pad 9 (divides Pad 3 demand by 4) to drive Board 1 display latch.  
**Fault:** Dead original IC causing flat 0 V on Pad 9 (stuck display `00.0`).

| Item | Description & Recommended Part No. | Package / Spec | Qty | Notes / Search Terms |
|---|---|---|---|---|
| **Dual D-Type Flip-Flop IC** | **CD4013BE** (Texas Instruments)<br>*Alternates:* HEF4013BP, MC14013BCP, HCF4013BEY | **DIP-14** (Through-hole)<br>CMOS, rated up to 18 V | 2–5 | Buy brand new standard modern CMOS stock (Mouser, RS, DigiKey, or eBay). Avoid 74HC74/74HCT74 (5 V parts). |
| **14-Pin IC Socket** | **14-Pin DIL / DIP Turned-Pin Socket** (Machined round hole) | 0.3" row spacing (standard narrow DIP) | 2–5 | Turned-pin (machined round pin) sockets provide superior grip, long-term corrosion resistance, and prevent iron heat damage to the new IC. |

---

## 2. Optional Bench Spares for Board 4 (Later / Issue C Revision)

**Target Board:** Spare Board 4 (`GT201/3276ST ISSUE C` currently running in the tower).  
**Circuit Function:** Modern factory revision using 16-pin dual binary up-counter for the ÷4 divider.

| Item | Description & Recommended Part No. | Package / Spec | Qty | Notes / Search Terms |
|---|---|---|---|---|
| **Dual Binary Up-Counter IC** | **MC14520BCP** (ON Semi) or **CD4520BE** (TI) | **DIP-16** (Through-hole)<br>CMOS, rated up to 18 V | 1–2 | Handy spare if you ever need to service the Issue C spare board. |
| **16-Pin IC Socket** | **16-Pin DIL / DIP Turned-Pin Socket** (Machined round hole) | 0.3" row spacing | 1–2 | Machined pin socket for 16-pin DIP footprint. |

---

## 3. Recommended Tools / Consumables for the Swap

| Item | Purpose |
|---|---|
| **Desoldering Braid / Wick** (2.0 mm or 2.5 mm) | For cleanly lifting solder off the original 14-pin IC pads without tearing the delicate 1970s copper traces. |
| **60/40 Leaded Rosin Core Solder** | Melts at a lower temperature (~183 °C) than lead-free solder, minimizing heat risk to vintage PCB copper pads. |
| **Flux Pen / Rosin Flux** | Makes desoldering the original chip pins much faster and cleaner. |
