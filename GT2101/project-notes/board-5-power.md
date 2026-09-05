---
layout: bare
title: "GT2101 — Board 5 — Power and the outside world (3285NH)"
permalink: /GT2101/project-notes/board-5-power/
description: "Working study of the GT2101's bottom board: the triac mains front end, the ±10 V rails, and the passive interface that carries the switches, the pot and the motor leads into the tower."
---

*A working note — part of the GT2101 project's live record, written as the work happens and including the wrong turns. The polished write-ups live in [Technical Notes](/GT2101/technical-notes/).*

---

# GT2101 Board 5 — `GT201/3285NH`

**Written 5 September 2026.** Board 5 was the only board in the tower with no study of its
own — what was known about it lived scattered across the backplane map, the build record and
the folder findings. This page was made during the board-by-board audit, from
`Board-5-Schem.pdf` and `Board-5-Layout.pdf` (FANATSON, 08/2015 and 01.09.2015) read at
400 and 300 dpi, plus the material already in the archive.

**Provenance:** ✅ read off the hardware · 📄 from the FANATSON tracings or the folder
transcription · ❓ unverified.

⚠ **This page does not own the pad map.** The one home for every backplane pad is
[`flexicon-backplane-map.md`](/GT2101/project-notes/flexicon-backplane-map/) §7. What is
here is the *board* — what the copper does — plus the two things board 5's own sheets add to
that map.

---

## 1. What board 5 actually is

**A linear power supply and a passive interface. There is no logic on it at all.**

That single sentence does more work than it looks like it should, because three separate
worries in this project have dissolved on it: whether board 5 drives the green LED net
(it does not), whether the Pico would be fighting an output there (it would not), and whether
anything on board 5 needs to be understood before the Pico is powered from it (it does not).

📄 The parts, from the folder transcription: **BTB08 8 A triac · 10DB1A bridge rectifier ·
TIS91 600 mW · 1N5761A diac · one unidentified device under the heat sink.** The two
schematic sheets add **2 × 4700 µF 25 V** reservoir capacitors, two **560 R** resistors, two
zeners and a **PNP series pass transistor**.

⚠ It is the **bottom** board of the tower and the widest gap in the flexicon sits above it.

---

## 2. The two rails, as the sheet draws them

📄 All of this is from `Board-5-Schem.pdf`, headed `PWR SUPPLY · FANATSON 08/2015`.

```
   mains ──[triac + diac trigger]──► transformer ──► 10DB1A bridge ──┬── +15 V ──[4700µ]── 0V
                                                                     └── −15 V ──[4700µ]── 0V

   +15 V ──┬──[560R]──┬──[100µ]── 0 V          ──►  pad 2   "+10 V"
           │          └──[zener Z]── 0 V              through a three-terminal device
           └──────────────────────────────────────────┘   (drawn dashed — see below)

   0 V  ────────────────────────────────────────────►  pad 9   "0 V"

   −15 V ──┬──[560R]──┬──[100µ]── 0 V
           │          └──[zener Z, "BLAU", ≈ −11.45 V]──┐
           │                                            │ base
           └──[diode ≈0.3 V, "Ge?"]── C ── PNP ── E ───►  pad 8   "−10 V"
                                          hFE = 283
                                          VBE = 0.69 V
```

⭐ **The two rails are not made the same way, and that is worth knowing.** The negative rail
is a straightforward zener-referenced **series pass** stage built from a discrete PNP — the
tracer even measured that transistor and wrote its gain and V<sub>BE</sub> on the sheet. The
positive rail's 560 R and zener are only the *reference*; the actual path from the +15 V
reservoir to pad 2 runs through a **three-terminal device the tracer drew as a dashed outline
with three terminals and did not label.**

❓ **That dashed device is almost certainly the "one unidentified device under the heat sink"**
in the folder transcription. A heat sink implies a pass element, and a pass element is exactly
what the dashed outline is standing in for. Nobody has read the part number off it. ⚠ It is
worth a look next time the tower is open, because it is the component the whole tower's
positive rail — and therefore the Pico's supply — depends on.

### The rails are nearer ±11 V than ±10 V

📄 The sheet's zener annotations are around **11.2 V** and **−11.45 V**, and
[`folder-findings.md`](/GT2101/project-notes/folder-findings/) §2.3 independently gives
pad 2 as **+11.9 V** and pad 8 as **−10.9 V**. Two unrelated sources agreeing that the rails
called "±10 V" throughout this archive actually sit a volt or so higher.

⚠ **Nothing needs changing, but a few numbers elsewhere are slightly optimistic** — every
calculation in these notes that used "10 V" (the green LED's ≈8 mA, the Pico clamp current in
[`board-1-display.md`](/GT2101/project-notes/board-1-display/) §3, the LM7805's dissipation)
comes out about 20 % larger at 11.9 V. All of them stay comfortably inside their limits, so
this is a note for accuracy rather than an action. 📄 and unmeasured; the meter settles it in
one reading on pad 2.

---

## 3. The mains front end

📄 The sheet draws the incoming mains through a **triac** with a **diac** and an RC network
(**30 K**, **8 K2**) triggering its gate — the classic phase-control arrangement. The tracer
labelled the flying leads by colour in German: **ROT** (red), **SW** (schwarz, black),
**WS** (weiss, white) and **BLAU** (blue).

❓ **What the triac is for has never been established.** Phase control on the primary side is
usually either a soft-start or a way of trimming the supply. The archive mentions a four-second
soft-start ramp on switch-on, which would fit, but nothing has confirmed the connection.

⚠ **Mains is on this board.** Nothing on the Remora plan requires touching board 5's top end,
and nothing should.

---

## 4. What board 5's own sheets add to the pad map

The pad map itself lives in
[`flexicon-backplane-map.md`](/GT2101/project-notes/flexicon-backplane-map/) §7. Two things
found on 5 September 2026 belong to it and are recorded here so they are not lost:

⭐⭐ **`Board-5-Layout.pdf` names pad 1 in writing: `LED GRÜN`.** Section 7 established pad 1
as the green LED three ways — Matt's call off the hardware, the repair-wire reasoning, and the
trace route — and noted that the schematic "confirms it by omission" because pin 1 appears
nowhere on it. **The layout sheet confirms it by name.** That also independently vindicates the
3 September correction that swapped pads 1 and 2 back into the right order.

✅ **The pad-group signature matches exactly.** The layout's connector row reads, from the end
the tracer marked `LEFT`: two pads (**1**, **2**), a wide gap, one lone pad (**3**), then a
group of six (**4**–**9**) running to the end marked `RIGHT`. That is §7's signature read from
the other side, and it is a second, independent confirmation of the pad count and grouping.

✅ **And the schematic's silence is real, not an artefact.** Re-read at 400 dpi on 5 September
2026: `Board-5-Schem.pdf` carries exactly three connector references — `2 (+10 V)`, `9 (0)`
and `8 (−10 V)` — and **pin 1 is not on it anywhere.** The `PNP hFE = 283` on that sheet is
the −10 V pass transistor and nothing else. The claim §7 rests on is sound.

⚠ **Orientation.** `Board-5-Layout.pdf` is headed **`COMPONENT SIDE, MOUNTED UPSIDE DOWN!`** —
the tracer's own exclamation mark. Board 3's layout carries the same warning and boards 1, 2
and 4 do not. **Do not carry an orientation habit between boards in this tower.** The layout
also marks its two connector ends `LEFT` and `RIGHT`, which is the safest way to talk about
pads on this board.

---

## 5. What this means for Remora

- ✅ **The Pico's LM7805 is fed from pad 2 (+10 V) and pad 9 (GND)**, and it runs — bench
  session 8, 3 September 2026. The full arrangement is in
  [`pico-controller-notes.md`](/GT2101/project-notes/pico-controller-notes/) § POWER; this
  page only adds that the rail behind pad 2 is a series-regulated one with an unidentified
  pass device, and sits nearer 11.9 V than 10 V.
- ✅ **Board 5 does not drive the green LED net.** The black speed switch grounds it; board 5
  offers pad 1 as a passive route to that switch and nothing more. There is nothing for the
  Pico to fight.
- ⚠ **Pad 8 is −10 V and sits next to pad 9.** It is 📄, not ✅ — the pad a slip off ground
  lands on, on a board whose negative rail is a real supply with a pass transistor behind it.
  Treat that end of the row with care.
- **Nothing else on board 5 is on the Remora path.** Pads 3–7 carry the switches, the pot and
  the motor leads through to the boards that use them; the Pico meets those signals at the
  boards, not here.

---

## 6. The inherited prose page — the one that largely holds

❓ `Disk-5-Power-Supply.pdf`, from the defunct *galeaudio.com*, is the sixth and last of the
inherited board descriptions. **It is also the only one that broadly survives a check.**

What it gets right: the component list (Siemens 4700 µF / 25 V electrolytics, the 10DB1A
bridge, the BTB08 triac, the diac) matches both the sheets and the folder transcription, and
*"contains both positive and negative linear regulation stages"* is exactly what the schematic
draws.

What is unsupported: *"supplies isolated logic and motor drive rails"* — the rails share the
0 V node and are not isolated from one another; and *"early units used discrete
pass-transistor regulation, later revisions used improved PNP series regulators"* is a
revision history nothing in this archive corroborates, describing two things the one sheet
shows at the same time.

⭐ **This matters for how the whole inherited set should be read.** Five of the six pages were
substantially wrong about what their board does; this one is right, and the difference is that
board 5 is *the board whose function you can guess correctly from its parts list*. A bridge
rectifier and two 4700 µF capacitors can only be a power supply. That is consistent with the
pattern the other audits found: **the chip lists are often right and the functions are
invented** — and on this board, guessing the function from the parts happens to work. It is
not evidence that the author ever had a board in front of them. See
[`archive-provenance.md`](/GT2101/project-notes/archive-provenance/).

---

## 7. Open questions

| ❓ | Why it matters | How to settle it |
|---|---|---|
| **What the device under the heat sink is** | It is the pass element for the tower's entire +10 V rail, and therefore for the Pico's supply | Read the part number off it next time the tower is open. A look, not a measurement |
| **What the triac is actually doing** | Phase control on the mains side is unexplained; a soft-start would fit | Nothing depends on it. ⚠ Mains — leave it alone unless there is a reason |
| The real rail voltages | Every "10 V" calculation in these notes is about 20 % out if the rails are really ±11 V | Two meter readings, pad 2 and pad 8 to pad 9, deck powered |
| ~~Whether board 5 drives the green LED net~~ | ✅✅ **Closed 3 Sept 2026** — the black switch grounds it. See [`flexicon-backplane-map.md`](/GT2101/project-notes/flexicon-backplane-map/) §7 | — |
| Pads 3–8 against the part | They are 📄 from the sheet; only pads 1, 2 and 9 are ✅ | Continuity, one pad at a time, against the switches and the pot |
| Whether the board number is right | Board 5's `3285NH` is the only board number in the tower not read off the etched copper in this archive | Look for the legend on the copper side next time the board is out |
