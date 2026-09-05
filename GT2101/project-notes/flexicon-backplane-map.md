---
layout: bare
title: "GT2101 — The Flexicon Backplane — Pad Map and Repair Record"
permalink: /GT2101/project-notes/flexicon-backplane-map/
description: "The GT2101's flexible backplane mapped pad by pad: orientation, row order, which pad carries which signal, and the record of the 2026 repairs."
---

*A working note — part of the GT2101 project's live record, written as the work happens and including the wrong turns. The polished write-ups live in [Technical Notes](/GT2101/technical-notes/).*

---

# The flexicon backplane — `GT201/3281NH`

**Written 26 August 2026**, after the part was removed, repaired, stiffened and
continuity-tested. **All five rows are mapped.**

✅✅ **CONFIRMED IN SERVICE, 26 August 2026 — bench session 7.** Board 1 was reconnected to
row 1 and driven by the Pico *through the repaired backplane*, at 5 V, with no other board
connected. **The display works.** Row 1's map below is no longer read off the film — it is
proven by function.

⚠ **AMENDED 3 September 2026 — row 5 pads 1 and 2 were the wrong way round.** See §7. The
green LED is on **pad 1**, the `+10 V` rail on **pad 2**, and row 5 is the one row that does
not carry `+10 V` on pad 1. Anything written before this date that relies on row 5 pad 1
being the rail is wrong.

✅✅ **ROW 5 CONFIRMED IN SERVICE, 3 September 2026 — bench session 8.** The Pico was powered
from **row 5 pad 2 (`+10 V`) and row 5 pad 9 (`GND`)** through an **LM7805**, and ran.
⚠ *This line said "a DC-DC converter" until 4 September 2026. There is no DC-DC converter in
the deck — it is the LM7805, fed from +10 V instead of the +15 V reservoir.*
**Pad 9 is the first of row 5's pads 3–9 to come off the sheet and onto the hardware.** The
same session metered the green LED net end to end and cleared it of a short to the rail
(§7), and identified both rebuilt supply rails pad by pad (§8).

**Provenance:** ✅ read off the part · 📄 from the FANATSON backplane sheet (12.9.2015) or
the per-board connector tables · ❓ unverified.

---

## ⭐ The signal chain — how the tower works as one system

**Merged in from `backplane-signal-map.md`, 4 September 2026**, which was deleted the same day.
That file and this one were the same map twice — logical and physical — and their per-board pin
tables were straight duplicates. **This is everything from it that lived nowhere else.**

📄 Its source was `GaleTTbackplane.pdf`, a hand-traced sheet titled *"GALE GT2101 BACKPLANE
SOLDER SIDE (TOWER)"*, signed **FANATSON, 12.9.2015**. ⭐ It is laid out as **five numbered
rows, PCB 1 to PCB 5** — independent confirmation that the tower holds five boards.

```
                    1.048 MHz crystal  ──────────────┐
                         (Board 4)                   │
                                                     ▼
   Helipot ──► Board 2 ──► Board 3 XR2207 ──► F VAR ──► Board 2 ──► ×40 ──► Board 5
   (on Bd 2)                                                                  │
                                                        black switch VAR/FIX ─┤
                                                                              ▼
                                          Board 4 pin 3  ◄──── 4×F (40–3996 Hz)
                                                │
                                          ÷4 ───┼───► pin 9 ──► Board 1 pin 7 (F REF)
                                                │
                                                ▼
   motor TACH (0/−10 V) ──► Board 4 E113 ──► 4046 PLL ──► 1747 ──► pin 6
                                    │                                 │
                                    └──► pin 4 INV TACH ──► Board 2    ▼
                                                              Board 3 pin 6
                                                                      │
                                                     STILL/TURNING gate│
                                                                      ▼
                                                              Board 3 pin 7 ──► motor

   touch disc ──► Board 2 555 ──► pin 5 (0→+10 V pulse) ──► Board 3 pin 4 ──► the gate
```

**The black speed switch**, on board 5: **VAR released** selects `F VAR` (the Helipot speed);
**FIX pressed** selects the fixed 1332 Hz. The selected frequency returns to board 4 pin 3 as
`4×F`.

### ⭐ What this settles

**There is no motor power stage in the tower.** The tower's output to the motor is a
low-voltage control signal of about **1.2–2.4 V**. The power electronics — the BD675A/676A
Darlingtons — are on the **separate motor controller PCB**. ⭐ That is the finding which
unmasked the inherited `Disk2BPowerDriver.pdf` as a description of the motor board, misfiled
as a tower disk.

**The servo lives on boards 4 and 3, in that order.** Board 4 compares and amplifies; board 3
gates. The old description of board 2 as "Servo Motor Drive" is wrong on both counts.

**The display maths.** `4×F` = 40 × rpm (1332 Hz at 33⅓); `1×F` = 10 × rpm (333 Hz). `F VAR`
at 3996 Hz is **99.9 rpm × 40** — the top of the variable range, because the display has three
digits and a fixed decimal point.

---

## 1. What it is

✅ A flexible printed backplane by **flexicon**, legended `GT201/3281NH` on the film. It is
the only electrical path between the five tower boards, and there is no spare of it in the
archive.

✅ **The connection method.** Each board carries a row of pins soldered along its edge. The
flexicon carries **five rows of brass staple pins** clamped over the film and soldered to
the pads, lying at right angles to the board's pins. The two sets **cross** where they meet.

✅ **One staple = one solder blob** on the reverse — Matt, 26 August 2026. Blob count is
therefore pin count directly, with no doubling. This is what unlocked rows 2, 4 and 5.

✅ **The film is translucent**, so the copper reads from both faces under a light. The whole
map below was made optically and then confirmed on the meter.

---

## 2. Orientation — how to hold it ⭐

Everything downstream depends on this, so it is stated once, exactly.

✅ **Solder side** = the face where the legend `GT201/3281NH  flexicon` reads the right way
round. This is the face the FANATSON sheet draws — it is headed *BACKPLANE SOLDER SIDE
("TOWER")*.

✅ **Pin side** = legend mirrored.

Hold it **solder side towards you, the five rows running horizontally**. Then:

| Row | Board | Pads |
|:--:|---|:--:|
| **top** | 1 — display `3155ST` | **8** |
| 2 | 2 — touch `3272ST` | **14** |
| 3 *(close below row 2)* | 3 — `3275ST` | **9** |
| 4 *(wide gap below row 3)* | 4 — `3276ST` | **9** |
| **bottom** *(widest gap of all)* | 5 — power `3285NH` | **9** |

✅ **Every count matches its board's documented connector.** Row 1's eight are board 1's
eight used signals (the board has 12 pins fitted of 19 positions, but only eight reach the
backplane).

✅ **The row spacing is a fingerprint** — rows 2 and 3 sit close together, row 5 is far below
row 4 — and it matches the sheet's row pitch. That is how row order was confirmed rather
than assumed.

✅ **Left-to-right on this face = ascending connector pin number.** `−10 V` and `GND` are at
the **right** end of every row. Confirmed two ways: the sheet labels them that way, and the
bottom row's distinctive layout — two isolated pads at the far left, a wide gap, one lone
pad, then a tight group of six — appears identically on the part and on the sheet.

⚠ **`+10 V` is on pad 1 for rows 1–4 only. Row 5 has the green LED on pad 1 and `+10 V` on
pad 2** — see §7. This is the second offset trap on this part, alongside the row 3 / row 4
`−10 V`/`GND` shift in §6. **Never carry a pad-1 assumption onto row 5.**

---

## 3. Row 1 — board 1, the display ✅✅

Signature: a **wide gap between pads 5 and 6**, then three pads close together at the right.

✅✅ **Proven in service, bench session 7** — the Pico drove the original display through
this row, on the repaired backplane. Pads 1, 3, 4, 7 and 8 are confirmed by function, not
just by inspection.

| Pad | Signal | Board 1 pin | Direction |
|:--:|---|:--:|---|
| 1 | **+10 V** | 1 | in ← board 5 |
| 2 | **BLANK** (start/stop LO) | 3 | in ← board 2 pad 6 |
| 3 | **`F DISPLAY`** | 6 | in ← board 2 pad 8 |
| 4 | **~1 Hz gate** | 7 | in ← board 2 pad 10 |
| 5 | **GREEN LED** | 8 | out → **board 5 pad 1** ✅ |
| 6 | **`RESET`** | 10 | out → board 2 pad 13 |
| 7 | **`F REF`** | 11 | in ← board 4 pad 9 |
| 8 | **GND** | 12 | in ← board 5 |

---

## 4. Row 2 — board 2, touch and display timing ✅

| Pad | Signal | Direction |
|:--:|---|---|
| 1 | **+10 V** | in |
| 2 | 1.048 MHz | in ← board 4 pad 2 |
| 3 | STILL/TURNING | in ← board 3 pad 2 |
| 4 | STILL/TURNING | in ← board 3 pad 3 |
| 5 | ⭐ **START/STOP PULSE HI — 0 → +10 V** | out → board 3 pad 4 |
| 6 | ☠ **START/STOP PULSE LO — 0 → −10 V** | out → board 1 pad 2 |
| 7 | `F REF ×40` | in ← board 4 |
| 8 | 🔧 **`F DISPLAY`** | out → board 1 pad 3 |
| 9 | `INV TACH` | in ← board 4 pad 4 |
| 10 | 🔧 **~1 Hz gate** | out → board 1 pad 4 |
| 11 | 1332 Hz FIX | out → board 5 |
| 12 | **−10 V** | in |
| 13 | **`RESET`** | in ← board 1 pad 6 |
| 14 | **GND** | in |

### ☠ Pads 5 and 6 are next door to each other and one of them will destroy a GPIO

**Pad 5 swings 0 → +10 V. Pad 6 swings 0 → −10 V.** Pad 5 is the touch pulse the Pico wants,
through a divider. Pad 6 is the display-blanking pulse and **a divider does not make it
safe** — dividing −10 V just gives a smaller negative voltage, still below ground, straight
into the Pico's lower clamp diode.

**Getting pad 5 rather than pad 6 is the thing that protects the Pico, not the resistors.**
Confirm with the meter before soldering: deck powered, touch the disc, pad 5 kicks positive
and pad 6 kicks negative.

Divider for pad 5: **27 kΩ + 10 kΩ** gives 2.70 V from a 10 V rail — a solid logic high with
headroom if the rail sits high. (The 22 k/10 k in `parts-to-order.md` gives 3.13 V, which
works but leaves little margin.) Add 1 kΩ in series into the GPIO.

---

## 5. Row 3 — board 3 ✅

| Pad | Signal | Direction |
|:--:|---|---|
| 1 | **+10 V** | in |
| 2 | STILL/TURNING | out → board 2 pad 3 |
| 3 | STILL/TURNING | out → board 2 pad 4 |
| 4 | **start/stop pulse**, 0 → +10 V | in ← board 2 pad 5 |
| 5 | **`F VAR`** | out → board 2 |
| 6 | **drive voltage IN** | in ← board 4 pad 6 |
| 7 | ⭐ **drive voltage OUT → the motor** | out |
| 8 | **−10 V** | in |
| 9 | **GND** | in |

⚠ Pad 7 is the calibration prize. `board-3-fvar-gate.md` §5: measure it at each speed on the
running deck, and four 📄 figures become ✅.

---

## 6. Row 4 — board 4 ✅

| Pad | Signal | Direction |
|:--:|---|---|
| 1 | **+10 V** | in |
| 2 | 1.048 MHz | out → board 2 pad 2 |
| 3 | `4×F` — black switch VAR/FIX selection | in |
| 4 | `INV TACH` | out → board 2 pad 9 |
| 5 | ⭐ **`TACH` from the motor**, 0 to −10 V | in |
| 6 | drive voltage out | out → board 3 pad 6 |
| 7 | **−10 V** | in |
| 8 | **GND** | in |
| 9 | 🔧 **`F REF`** | out → board 1 pad 7 |

⚠ **Rows 3 and 4 do not share a pinout** — row 3 has −10 V on 8 and GND on 9; row 4 has
−10 V on 7 and GND on 8. Never carry an assumption between them.

⚠ `TACH` on pad 5 swings **0 to −10 V** and needs the **J113 JFET** inverter, not a divider
and not a MOSFET. See `parts-to-order.md`.

---

## 7. Row 5 — board 5, power and the outside world ✅

Signature: two pads at the far left, a wide gap, one lone pad, then a group of six.

⚠⚠ **CORRECTED 3 September 2026 — pads 1 and 2 were previously listed the wrong way round.**
This section used to give pad 1 as `+10 V` and pad 2 as the green LED. **It is the other way
round.** The error came from applying §2's "`+10 V` on pad 1" rule, which holds on rows 1–4
and does not hold here.

| Pad | Signal | |
|:--:|---|---|
| **1** | **GREEN LED** ← board 1 pad 5 / board 1 pin 8 | ✅ |
| **2** | **+10 V** | ✅ |
| 3 | to the **black speed switch** (VAR released / FIX pressed) | 📄 |
| 4 | `F VAR` / 3996 Hz (×40) | 📄 |
| 5 | **`TACH`** from the motor | 📄 |
| 6 | **SPEED OUT** to the motor | 📄 |
| 7 | 1332 Hz FIX | 📄 |
| 8 | **−10 V** | 📄 |
| **9** | **GND** | ✅ |

✅ Pad count and positions read off the part. **Pads 1, 2 and 9 are ✅. Pads 3–8 remain 📄
from the sheet** and are still unconfirmed against the part.

✅ **The pad grouping is confirmed on paper too — 5 September 2026.** `Board-5-Layout.pdf`
draws the connector row and marks its ends `LEFT` and `RIGHT`: from the `LEFT` end, two pads
(1, 2), a wide gap, one lone pad (3), then a group of six (4–9). That is the signature above,
read from the other side, and it is an independent confirmation of both the count and the
grouping. The board study is [`board-5-power.md`](/GT2101/project-notes/board-5-power/).

### ✅ Pad 9 = `GND`, confirmed in service 3 September 2026

Bench session 8. The Pico's **LM7805** was fed from **pad 2 and pad 9** and the Pico
ran — self-starting, LED blinking, with the tower supplying it. The regulator sits in the
void at the bottom of the tower stack, underneath board 5. Function confirms both pads
at once: pad 2 was already ✅ from the repair-wire reasoning below, and **pad 9 now joins it,
the first of pads 3–9 to be proven against the hardware rather than read off the sheet.**

⚠ Still 📄 and still worth care: **pad 8 = `−10 V`**, immediately beside the pad now known to
be ground. Nothing has confirmed it, and it is the pad a slip off 9 lands on.

### How pads 1 and 2 were settled ✅

Three independent lines, all agreeing:

1. ✅ **Matt, 3 September 2026 — the green LED is board 5 pin 1**, called without qualification
   off the hardware.
2. ✅ **The repair wiring says which pad is the rail.** Of the two pads at this end, the
   **inner** one carries the orange repair wire that then chains down the film row to row to
   row 1. A wire that touches every row is a supply rail. The **outer** pad is a bare blob —
   **the only pad in row 5 with no repair wire on it**, so its copper is original Gale
   routing and not a 2026 shortcut. That answers one entry on §8's open list.
3. ✅ **The trace route, Matt, 3 September 2026 —** *pin 1 goes underneath pins 2, 3 and 4,
   then travels up the centre of the film to the green LED at board 1 pin 8.* Visible on
   `outside-trace.jpeg` as a single trace leaving the outer pad, running horizontally back
   beneath the pad row, then turning across the film. **Row 1 pad 5 sits at the physical
   centre of its row**, so the described route and the destination corroborate each other.

4. ✅✅ **METERED, 3 September 2026 — bench session 8.** Matt: *"pin 1 on board 5 and pin 5 on
   board 1 beep."* Continuity confirmed end to end, so the route above is no longer an
   inference from three converging arguments — it is a measurement.

   ⭐ **And it is one of the few readings on this part that is guaranteed to be original
   copper.** §8 warns that a repair wire and an etched trace are indistinguishable on a
   meter. Row 5 pad 1 is the one pad in the row with **no repair wire on it**, so this beep
   cannot be a 2026 bridge.

   *(On the numbering: board 1's connector has no used pin 5 — only pins 1, 3, 6, 7, 8, 10,
   11 and 12 reach the backplane — so "board 1 pin 5" is **row 1 pad 5**, which is board 1
   pin 8. Same node.)*

**The net, end to end, closed and measured:**

```
board 5 pin 1 ──┬─ under row 5 pads 2, 3, 4
                └─ up the centre of the film
                   └─ row 1 pad 5 ── board 1 pin 8 ── GREEN LED
```

**It is a clean point-to-point run.** Nothing else joins it on the backplane.

### ☠ The pads 2–4 hazard

**The green LED trace passes beneath pads 2, 3 and 4, and pad 2 is the `+10 V` rail.** That
is the tightest copper on the part. Any bridge, slip or staple work on pads 2, 3 or 4 lands
on a net that runs — via board 1 pin 8 — **straight to a Pico GPIO** in the stage-1 plan.

Treat this end of row 5 as no-go unless the job is specifically on it, and meter pad 1 to
pad 2 for shorts after any work in that area.

✅ **Checked and clear, 3 September 2026.** After the Pico's supply wire was soldered to
pad 2, Matt metered pad 1 against pad 2: **not connected.** The green LED net is isolated
from the `+10 V` rail at the backplane. This is the check to repeat after any future work
on pads 2, 3 or 4.

### ✅ The net is clean — nothing else on it, 3 September 2026

Matt, swept against the part: *"it only beeps pin 1 board 5 and pin 5 board 1."*

**That is the whole net.** Not `GND`, not `+10 V`, not any other pad. §7's "clean
point-to-point run" was an inference from the trace route; it is now a measurement, and it
**answers the long-standing open question of whether board 5 grounds the green LED net.
It does not. The Pico owns it.**

### ⭐⭐ What the net IS — settled against hardware, 3 September 2026

**The green LED is the 33⅓ / FIX indicator, and the black switch grounds it. Board 5 has no
circuitry on it at all.**

✅ **Matt, bench session 8:** press the black button and the LED lights. ✅ And **pad 1 beeps
to deck `GND` with the black switch held pressed**, open with it released — which is why the
first sweep showed nothing.

```
board 1: +10 V ── green LED ── 1 kΩ ── board 1 pin 8
                                          │
                       row 1 pad 5 ── the centre run ── row 5 pad 1
                                          │
                        board 5 pin 1 ── black switch ── 0 V
```

⭐⭐ **And two drawings confirm it outright — found 5 September 2026.** This section was built
on three lines of hardware reasoning plus a confirmation by omission. There were two documents
saying it in writing the whole time:

- **`Board-5-Layout.pdf`** labels the connector row, and under pad 1 the tracer wrote
  **`LED GRÜN`**. See [`board-5-power.md`](/GT2101/project-notes/board-5-power/) §4.
- **`motor-overview/backplane.pdf`** draws it. On row 5 the **outer** pad is labelled
  **`LED GREEN`** and the **inner** one **`+10 V`** — the reverse of rows 1–4 — and the long
  trace running down the centre of the film from row 1's `LED GRÜN` pad lands on that outer
  pad. ⭐ **The backplane sheet shows the exception to the "+10 V on pad 1" rule explicitly.**

⚠ **So the 3 September correction was right, and it need not have taken three lines of
reasoning from the hardware to reach.** Two sheets in this archive already said so. That is the
same lesson as the board 1 timebase alarm, one week apart: *before working something out from
first principles, check whether a drawing already says it.*

✅ **`Board-5-Schem.pdf` confirms it by omission.** Board 5's schematic carries exactly three
outputs — `2 (+10 V)`, `9 (0 V)`, `8 (−10 V)` — and **pin 1 appears nowhere on it** (re-read
at 400 dpi, 5 September 2026 — the silence is real). Board 5
is a power supply plus a passive interface for the external flying leads (`BLU`, `OR`, `GN`,
`WS`, `SW`). No logic, no driver. The `PNP hfe=283` on that sheet is the **−10 V pass
transistor**, not an LED driver.

⚠ **This corrects the `9.18 V` worry, which was wrong.**
[`folder-findings.md`](/GT2101/project-notes/folder-findings/) §2.3's *"9.18 V selected / 0 not"* has its states the wrong
way round: **~9 V is the LED OFF state** — board 1's own pull-up read back through the LED —
and **0 V is ON**. Board 5 does not drive this net and there is nothing for the Pico to fight.
A passive switch to ground and GP5 open-drain are both **sinks**; they OR together.

⭐ **GP5 in bench session 6 was standing in for the black switch** — same node, same job, same
direction. That is why one wire and no components worked.

⚠ **What remains is a functional collision, not an electrical one.** With the black switch in
FIX the LED is lit whatever the Pico wants: **the Pico can turn it on, not off.** Any lock
indicator scheme only works while the switch is in VAR.

⚠ **The 10 V NPN is unaffected** — that hazard is board 1's 1 kΩ pull-up acting on the Pico's
*off* state, nothing to do with board 5.

### What this corrects elsewhere

- **The folder transcription in [`folder-findings.md`](/GT2101/project-notes/folder-findings/) §2.3 was right about the
  order** and this document was wrong. Its board 5 table reads *pin 1 — 33.3 indicator,
  9.18 V selected / 0 not · pin 2 — +supply, 11.9 V*. Pin 1 is the green LED, described by
  what it indicates rather than by its colour. Its pins 4–9 already agreed with this map;
  with 1 and 2 corrected, **the two sources now agree completely on row 5.**
- ⚠ **`9.18 V` implies board 5 *drives* this net**, rather than grounding it or leaving it
  open. That figure is 📄 and unconfirmed, but if it holds it is the least convenient of the
  three possibilities for the Pico taking the LED — see §10.

---

## 8. The repairs, August 2026 ✅

✅✅ **The repairs are Matt's own work — confirmed 4 September 2026.** This section used to
read as though the wires had been found on the part, and §10 asked for detail *"from the
person who fitted them"* as if an earlier restorer had to be tracked down. **There is no such
person.** Matt fitted them, and can answer any question about them directly.

✅ **At least five traces were broken** — Matt, 4 September 2026. Firmer than the "several"
this section carried before.

✅ **Why they broke: the coverlay was peeling.** The amber film was lifting away — adhesive
failure after fifty years, not a single mechanical injury. ⭐ **That mechanism is what makes
bridging the right repair rather than a bodge:** a delaminated coverlay cannot be re-bonded
reliably, so the copper beneath it cannot be trusted even where it still reads continuous.

**Orange PVC wire soldered on the solder side**, bridging the breaks **and deliberately
stiffening the film across the fold zones**. ⚠ The stiffening was a stated aim, not a side
effect: the traces broke *because* the film flexes there, so taking the flex out of the fold
zones protects the traces that are still intact.

✅ **Continuity tested by Matt, 26 August 2026 — all connections read as they should.** The
backplane is electrically sound, and has since been proven in service twice (see the header).

### ⚠ Where it will fail next — added 4 September 2026

**Stiffening does not remove stress from a flex circuit. It moves it.** The new weak points
are at the **ends of the orange wires**, where stiffened film meets unstiffened film — that
boundary is now the sharpest bend in the part.

⚠ **The practical consequence runs opposite to the intuition.** The repair makes the backplane
much more robust *in service*, but a stiffened flex resists conforming to the tower, so every
refit loads the pads harder than it used to. **Take it on and off less now, not more.**

### ✅ Still one part, and still no spare — confirmed 4 September 2026

The two sets of photographs in `engineering-drawings-schematics/flexicon-connector/` show the
**same** flexicon from its two faces, not two backplanes:

| Face | How to tell | What you see |
|---|---|---|
| **Pin side** | legend **mirrored** | green oxidised traces, fine red wires |
| **Solder side** | legend reads **right way round** | the thick orange repair wires |

**There is no second backplane.** The rule that follows from it is unchanged and is the most
important rule on this part: **solder to the brass staple, never to a pad.**

### ⚠ The folder itself needs a tidy — 5 September 2026

Checked by content, not by name. Two pairs in
`engineering-drawings-schematics/flexicon-connector/` are **byte-identical duplicates** — same
MD5, same size — filed under two names each:

| Kept | Duplicate of it | Bytes |
|---|---|---|
| `remora.jpeg` | `raymon.jpeg` | 1 822 277 |
| `top-pico-mount-front.jpeg` | `IMG_0275.jpeg` | 2 256 158 |

⚠ **`raymon.jpeg` is the one to be careful about.** A file named after a person reads like
provenance — *this photograph came from Raymon* — and it is in fact a byte-for-byte copy of
`remora.jpeg`. Nothing in this archive cites it, and nothing should start to: it carries no
information the other file does not, and its name implies a source it does not have.

⚠ **`flexicon-1.2` has no file extension at all** and sits beside `flexicon-1.1.png`,
`flexicon-1.3.jpeg` and `flexicon-1.4.jpeg`. It is about 2 MB and is presumably the missing
`.jpeg`, but a file with no extension will not render on the published site and will be
skipped by anything walking the folder.

**None of this affects a conclusion on this page.** It is recorded because the next person to
cite a photograph from that folder should know which names point at the same image.

### ⭐ But the two-tower situation may change the break calculus — 4 September 2026

⚠ **That "no spare" claim was verified about two photo sets, not about the whole workshop.** It
is now known there are **two towers** — Howie's, on the deck, and Alex's, on the bench — and the
restored film in the photographs is **Howie's tower's own original cable**, currently fitted to
the test tower.

❓ **So the open question is: does the test tower have a flexicon of its own?** One look answers
it, and it decides more than tidiness:

- **If no** — nothing changes. One film, no spare, and every rule above stands at full strength.
- **If yes** — ⭐ **breaks stop being unrecoverable.** Every argument in this project about
  cutting a trace has assumed a single irreplaceable film. With a second one, a scheme can be
  proven on the test article while the restoration target stays untouched. That reopens the
  "stage 1 = the Pico takes the display, three breaks" plan that was shelved as too risky, and
  it is the only thing that would.

⚠ **Until it is answered, assume no spare and keep soldering to the staples.**

⚠ **And regardless of the answer, the restored film is in the wrong tower.** It is the part the
Howie restoration depends on, and it is currently in the tower about to receive a breadboard and
experimental wiring. If the test tower has its own, swap it back and box the restored one — the
test tower's job is to be experimented on; the restored film's job is to survive.

⚠ **A repair wire is indistinguishable from an etched trace on a meter.** Anyone buzzing this
part in future will read the repairs as original routing unless this section says otherwise.

❓ On row 1 the repaired pads appear to be **1, 4 and 8** — `+10 V`, the **~1 Hz gate**, and
`GND`. The gate matters: it is one of the three signals stage 1 drives.

✅ **Row 5 pad 1 carries no repair wire at all** — bare blob, original copper.

### ✅✅ Both rebuilt rails, mapped pad by pad — 3 September 2026

Matt read both chains off the part in bench session 8. **These are the two long repair wires,
and they are now fully recorded.**

**The `+10 V` rail** — the run of four wires at the far left edge:

```
row 5 pad 2 ── row 4 pad 1 ── row 3 pad 1 ── row 2 pad 1 ── row 1 pad 1
```

This confirms and completes the earlier partial identification. `+10 V` lands on **pad 1 of
every row except row 5**, exactly as §2 states, and row 5's offset is why the chain starts on
pad 2.

**The `GND` rail** — the run at the far right end:

```
row 5 pad 9 ── row 4 pad 8 ── row 3 pad 9 ── row 1 pad 8
```

⭐ **This chain independently confirms the row 3 / row 4 offset in §6.** The wire lands on
**9, then 8, then 9** — because row 3 carries `−10 V` on 8 and `GND` on 9, while row 4 carries
`−10 V` on 7 and `GND` on 8. Anyone assuming the two rows shared a pinout would have run this
wire onto `−10 V`. Whoever fitted it read the rows individually, and so did Matt.

❓ **Row 1's landing needs one more look.** Matt gave it as pad 9, but **row 1 has only eight
pads** — board 1 has 12 pins fitted of 19 positions and only eight reach the backplane, with
`GND` on pad 8, the last one. Recorded above as **pad 8**, on the assumption that the count
carried over from the two nine-pad rows before it. If row 1 turns out to have a ninth pad, that
matters considerably more than this wire does, and §3 needs reopening.

❓ **Row 2's landing is not recorded.** Matt's account goes row 5 → row 4 → row 3 → row 1. Row
2's `GND` is **pad 14**, the last of its fourteen. Whether the chain reaches it, or row 2 takes
ground by original copper, is unrecorded.

⭐ **Still to record — and Matt is the person who can, with the part in his hands:** the
remaining shorter wires. Which two pads each one joins, and whether it follows the original
path or shortcuts across the film. Shortcuts are the dangerous ones — correct electrically,
wrong topologically, and topology is what this archive is for.

⚠ **This is now the highest-value job left on this part.** Not because anything is at risk
electrically — it is tested and working — but because of the warning immediately above: an
unrecorded repair silently becomes a false map the moment anyone else buzzes the backplane,
including a future session of this project.

---

## 9. Stage 1 — the Pico takes the display 🔧

The whole of stage 1 is now locatable on the part. Three connections broken, five wires on,
nothing on any board touched, and the deck's own servo still running the platter.

**Break three** (marked 🔧 above):

| Break | Row | Pad | Stops |
|---|:--:|:--:|---|
| `F DISPLAY` | 2 | **8** | board 2 driving it |
| ~1 Hz gate | 2 | **10** | board 2 driving it |
| `F REF` | 4 | **9** — the rightmost pad on that row | board 4 driving it |

**Five wires, all onto row 1:**

| Row 1 pad | Signal | Pico |
|:--:|---|---|
| 3 | `F DISPLAY` | output |
| 4 | gate | output |
| 7 | `F REF` | output |
| 5 | GREEN LED | open-drain at 5 V; **low-side NPN at 10 V** |
| 6 | `RESET` | **input only — never drive it** |

⭐ **Solder to the brass staple, not to the pad.** The film never sees the iron. This applies
to breaking a connection as much as to making one.

Reversal is re-making three joints.

---

## 10. Open questions

| ❓ | Why it matters |
|---|---|
| Whether the crossed pins are **soldered** or friction-fit | Archive value: it is what "reversible" means for anyone who works on the tower later |
| **What is `R` on the board 2 row of the FANATSON sheet?** | Carried over from `backplane-signal-map.md` when it was merged in, 4 Sept 2026. Never identified |
| ~~What board 2 pin 9 does with `INV TACH`~~ — ⭐ **effectively answered, 4 Sept 2026** | It feeds board 2's **MC14016 quad analogue switch**, which selects the `F DISPLAY` source. Board 3's window comparator throws it via the STILL/TURNING lines on row 3 pads 2 and 3 → row 2 pads 3 and 4. **So the display shows commanded speed when the platter is stopped and measured speed when it turns** — which is exactly what the folder transcription meant by *"pin 3 runs at a much higher frequency when showing demand and not running"* (`F VAR` up to 3996 Hz against a 333 Hz tach). Worth confirming on the bench, but three sources already agree |
| ~~Which pads each repair wire joins~~ — **the two long rails are done, 3 Sept 2026** | §8. Both supply chains are mapped pad by pad. ⭐ **The remaining shorter wires are the highest-value job left on this part** — whether any of them shortcut across the film is the question that matters, and ✅ **Matt fitted them, so there is nobody to track down** (4 Sept 2026) |
| ⚠ **Whether a spare flexicon exists — HALF closed, and this row used to say otherwise** | §8. ✅ **Closed:** the two photo sets are the **same part from its two faces** — pin side legend mirrored, solder side carrying the orange repair wires — so there is no second film *in the photographs*. ❓ **Still open, and it is a different question:** *does the test tower have a flexicon of its own?* One look answers it and it decides the whole break calculus. It is [`project-memory.md`](/GT2101/project-notes/project-memory/) § NEXT item 4. ⚠ *This row read "CLOSED — no spare exists" until 5 September 2026, contradicting §8 in this same file.* **Until it is answered, assume no spare: solder to the brass staple, never to a pad** |
| ⚠ **Where the next failure will be** | §8. At the **ends of the orange wires**, where stiffened film meets unstiffened. Stiffening moved the stress rather than removing it — so refit the part as seldom as possible |
| **Does the `GND` rail reach row 2 pad 14?** | §8. Matt's chain runs 5 → 4 → 3 → 1 and skips row 2. Either the wire reaches it and was not mentioned, or row 2 grounds through original copper |
| **Row 1's pad count — eight or nine?** | §8. The `GND` chain was given as landing on row 1 pad 9, and §3 has row 1 with eight pads. Almost certainly a count carried over from the nine-pad rows, but if row 1 has a ninth pad then §3 is incomplete and it is one of the three signals stage 1 drives |
| ~~Whether board 5 grounds the green LED net~~ — ✅✅ **CLOSED 3 Sept 2026** | §7. **The black switch grounds it; board 5 has no circuitry on pin 1 and `Board-5-Schem.pdf` does not show the pin at all.** The LED is the 33⅓/FIX indicator. Confirmed two ways on the hardware: pressing the button lights the LED, and pad 1 beeps to `GND` only with the button held. **Nothing for the Pico to fight** — a passive switch and GP5 open-drain are both sinks |
| ⚠ **The green LED already has a job** | §7. It indicates FIX / 33⅓. With the switch pressed the Pico cannot turn it off, only on. Reusing it as a lock indicator overrides an original function — a deliberate decision, not a default |
| ⚠ **Row 5 pad 8 = `−10 V`** — still 📄 | §7. It sits immediately beside pad 9, which is now confirmed as `GND` and is carrying the Pico's supply return. Nothing has confirmed pad 8, and it is where a slip off 9 lands |
| Whether `BLANK` (row 2 pad 6 → row 1 pad 2) should also be broken | Left connected, touching the disc will blank the display |
| Row 5's signal order, **pads 3–8** | 📄 from the sheet only, not yet confirmed against the part. **Pads 1, 2 and 9 are now ✅** — see §7. Pad 9 was confirmed by carrying the Pico's supply return in bench session 8 |
