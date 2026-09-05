---
layout: bare
title: "GT2101 — Archive Provenance"
permalink: /GT2101/project-notes/archive-provenance/
description: "Where the GT2101 drawings and descriptions came from, which of them have failed against the hardware, and the status discipline used throughout this archive."
---

*A working note — part of the GT2101 project's live record. The polished write-ups live in
[Technical Notes](/GT2101/technical-notes/).*

---

# Archive provenance

**Extracted 4 September 2026** from `project-memory.md`, where it had been stapled to the end
of the file as *"File 3"* since the 24 August recovery. Several notes across the repo cite a
document called `gt2101_archive_provenance.md` that never existed as a file — **this is it.**

---

## The status discipline

This archive was built by copying a now-defunct enthusiast site whose sources are unknown.
**It is being turned into a single point of truth**, and every claim carries a visible status:

| | Meaning |
|---|---|
| ✅ | Confirmed against the hardware — measured, read off the part, or proven by function |
| 📄 | From a document. Says which document |
| ❓ | Unverified, or inherited from the defunct site |

⚠ **Nothing is deleted for being unverified. It is labelled.** An inherited claim that turns
out to be wrong is more useful marked wrong than removed, because the next person will
otherwise find the same claim elsewhere and believe it.

### ⚠ A second, finer scheme exists — and it is not a rival

[`folder-findings.md`](/GT2101/project-notes/folder-findings/) tags its claims `[HW]`, `[1st]`,
`[2nd]` and `[SITE]`. **That is deliberate, not an inconsistency**, and the two map onto each
other:

| Fine (folder-findings) | Coarse (everywhere else) | |
|---|---|---|
| `[HW]` read off hardware or a tracing of it | ✅ | |
| `[1st]` first-hand from a named participant | 📄 | ⭐ **the distinction the coarse scheme cannot make** |
| `[2nd]` relayed through an intermediary | 📄 | ⭐ |
| `[SITE]` unsourced galeaudio.com prose | ❓ | |

⭐ **Testimony has degrees, and ✅ 📄 ❓ cannot express them.** Whether a claim about the motor
came from Paul Ramsden directly or reached us through two people changes what it is worth, and
that file is almost entirely oral history. **Use the fine scheme when handling testimony, the
coarse one everywhere else.**

---

## ⚠ There are no Gale factory drawings in this archive

**Every schematic and layout here is one person's hand-traced reverse engineering**, signed
FANATSON and dated 2015. Several sheets are marked **PRELIMINARY**. They are not, and have
never been, manufacturer documentation.

**They have nonetheless held up well.** The sheet numbering and the circled destination
numbers on the layout footers turned out to be trustworthy, and they are what allowed boards
1–4 to be joined into a single signal chain. Where a tracing has been checked against
hardware it has generally been right.

⚠ **The tracings are image-only scans.** A text read returns nothing. ✅ **But they can be
read by a connected session — corrected 5 September 2026.** With the
`engineering-drawings-schematics` folder connected, rendering a sheet to PNG at ~400 dpi and
zooming reads the pencil annotations directly. That is how the drive-voltage **two-column**
table and Board 1's 4013 wiring were settled on 5 September. **Attaching the PDF to the chat
is no longer the only way**, and three files in this repo said it was.

---

## ⚠ The inherited prose pages have failed, five out of six

**Completed 5 September 2026.** All six are now checked. Typed descriptions copied from the
defunct site, no stated sources.

| Page | What is wrong with it |
|---|---|
| `Board-1-Display-Logic-Interface.pdf` | ⚠ **Added 5 Sept 2026.** Calls the **MC14001 an "OR gate"** and the **MC14011 an "AND gate"** — they are a NOR and a NAND, and board 1's whole latch/reset decode only works because they are. Also claims the board shows speed "derived from tach feedback", which nothing on either sheet supports |
| `Disk-3-Optical-Sensor.pdf` | Calls board 3 a tachometer processor "mounted close to the motor's photodiode assembly". There is no photodiode, no encoder input, and nothing on the connector that could be one. Board 3 is a **VCO and a drive gate** — the opposite of a tacho processor |
| `Disk-2A-Servo-Control.pdf` | Lists two ICs that are not on the board, omits four that are, puts the PLL on the wrong board, and **does not mention the touch sensor at all** — the most distinctive circuit on it |
| `Disk-2B-Power-Driver.pdf` | Describes the **separate motor controller PCB**, not a tower board. Misfiled. This is where the "is disk 2 one board or two?" confusion came from |
| `Disk 4 — Reference Oscillator.pdf` | Board 4 is a crystal reference, a tacho front-end **and the servo**. Calling it a reference oscillator misses what it is for |
| `Disk-5-Power-Supply.pdf` | ⭐ **The exception. Broadly holds.** Its component list matches the sheets, and "both positive and negative linear regulation stages" is exactly what board 5 draws. Only two details are unsupported: the rails are **not** isolated from each other, and its "early units / later revisions" history is corroborated by nothing. See [`board-5-power.md`](/GT2101/project-notes/board-5-power/) §6 |

**Recommended: the five marked ❓ disputed in the archive, with a pointer to the board study
that supersedes each.**

⭐ **And the exception explains the rule.** Board 5 is the one board whose function you can
guess correctly from its parts list — a bridge rectifier and two 4700 µF capacitors can only
be a power supply. Everywhere else, **the chip lists are often right and the functions are
invented.** That is the signature of pages written from a parts list by someone who never had
a board in front of them, and it is why board 5 passing is not evidence that any of them were
checked against hardware.

⭐ **Treat the whole inherited prose set as unreliable.** Prefer the tracings, and prefer the
hardware over both.

⚠ **Two of the filenames above were cited wrongly across this archive** until 5 September
2026 (`Disk2AServoControl.pdf`, `Disk2BPowerDriver.pdf`, and elsewhere `Disk3OpticalSensor.pdf`
and `5Schem.pdf`). The drawings folders have been tidied at different times and to different
conventions; **check a filename before citing it.**

---

## ⚠ Three numbering systems exist, and they disagree

The board studies, the 2015 tracings, and an independent transcription of the connector
tables. They do not agree — the transcribed tables mark board 4 pin 6 "???" where the board
study has it as the demand output.

**Use the physical-pin tables in the board studies. Cross-check against the others. Never
solder to them.**

---

## ⚠ This project's own notes can contradict each other

Two documented cases, and the lesson is the same both times.

**The green LED, 24 August.** The board notes said *"no driver transistor needed"*; the parts
list had always listed a low-side driver. **Both were written honestly** — one was reasoning
about the 5 V bench, the other about the 10 V deck. The parts list was right.

**The supply regulator, 4 September.** Three documents said a DC-DC converter had replaced the
LM7805. The hardware was an LM7805 throughout; what had changed was its *input*, and somebody
wrote that up as a different part. The error then propagated because the same passage existed
in three files.

⭐ **When two project documents conflict, work out which supply, which board issue, or which
date each was written about before deciding either is wrong.** Usually both were true when
written.

⚠ **And duplication is the mechanism.** The DC-DC error survived because it had been copied
into three files; the `V_IDLE` alarm survived in `project-memory.md` for six days after being
corrected in `pico-controller-notes.md` for the same reason. **One fact, one home, everything
else a pointer** — see [`project-memory.md`](/GT2101/project-notes/project-memory/) § what
this document is.

---

## ⚠ Six times the written record has been wrong about the hardware

**The most useful reliability statistic in this archive**, and the reason for the order of
authority in [`project-memory.md`](/GT2101/project-notes/project-memory/): *the hardware in
front of you, then this repository, then nothing else.*

| Date | What the documents said | What the part said |
|---|---|---|
| — | Three boards in the control tower | **Five** |
| 21 Aug 2026 | *(undocumented anywhere)* | The display runs a **four-state** latch/reset cycle — and the reset is a **state, not a pulse** |
| 24 Aug 2026 | The suspension springs are interchangeable | **Three different rates, and they were fitted on the wrong legs** |
| 24 Aug 2026 | The Helipot drives the XR2207 via board 2 | **Electrically off board 2 entirely** — it is a bracket, not a circuit |
| 3 Sept 2026 | Board 5 may drive the green LED net to 9.18 V | **The black switch grounds it. Board 5 has no circuitry on that pin at all** |
| 4 Sept 2026 | A DC-DC converter had replaced the LM7805 — *in three files at once* | **It was the LM7805 throughout.** Only its input had changed |

⭐ **Not one of these was found by re-reading the documents.** Every one came from looking at,
metering, or handling the part — and in four of the six, the documents were internally
consistent and confidently worded while being wrong.

⚠ **The practical rule that follows:** when a measurement contradicts this archive, **the
archive is what changes.** Confirm a part number recalled from memory if it matters, but never
argue a piece of hardware out of what it is doing on the strength of a note. The 4 September
entry above is exactly that mistake, made against a component somebody was holding at the time.

---

## The boards themselves

**The only primary source in the archive.** Etched copper beats everything: it settled the
five-board count, every part number but board 5's, the ISSUE-letter revision axis, and the
existence of two distinct issues of board 3.
