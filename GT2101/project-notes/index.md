---
layout: bare
title: "GT2101 — Project Notes"
permalink: /GT2101/project-notes/
description: "The working record of the GT2101 restoration and the Remora project — board studies, bench sessions, decisions and open questions, written as the work happens."
---

# Project Notes

The **working record** of the GT2101 project, as opposed to the finished write-ups in
[Technical Notes](/GT2101/technical-notes/).

These pages are written while the work is happening. They contain bench procedures, part
numbers, wiring decisions, things that turned out to be wrong, and lists of what is still
unknown. They are kept public deliberately: the reasoning behind a conclusion is often more
useful than the conclusion, and a note about a wrong turn saves the next person an evening.

Status markers are used throughout, as elsewhere on this site:
✅ confirmed against the hardware · 📄 from a document · ❓ unverified.

---

## Start here

- [**Project memory**](/GT2101/project-notes/project-memory/) — the bootstrap document.
  The principle, where the work lives, what is settled, and an index of everything else.
  Read this first.

## The build

- [**Remora — working notes**](/GT2101/project-notes/pico-controller-notes/) — ⭐ **the build
  record, and the single source for all of it**: where the Pico connects, interfacing, the
  green LED, the tacho front-end, power, firmware, toolchain and the full bench log.
- [**Parts list**](/GT2101/project-notes/parts-to-order/) — what the build needs and what
  each item unblocks.
- [**Firmware**](/GT2101/project-notes/firmware/) — the MicroPython on the Pico. ⚠ **Eight of
  the nine files are still only on the Pico itself**, `config.py` included.

## The boards, studied

- [**Board 1 — Display**](/GT2101/project-notes/board-1-display/) `3155ST` — a three-digit
  frequency counter. Complete connector pin map, the four-state latch/reset cycle, and the
  sessions that drove it from a Pico without modifying it.
- [**Board 2 — Touch and display timing**](/GT2101/project-notes/board-2-touch/) `3272ST` —
  the capacitive touch start/stop circuit, and the 14-pin connector.
- [**Board 3 — `F VAR` and the drive gate**](/GT2101/project-notes/board-3-fvar-gate/)
  `3275ST` — the variable-speed oscillator and the gate that mutes the motor at rest.
- [**Board 4 — the servo**](/GT2101/technical-notes/board-4-servo/) `3276ST ISSUE C` — the
  crystal reference, the JFET tacho front-end and the PLL. Written up in Technical Notes.
- [**Board 5 — Power and the outside world**](/GT2101/project-notes/board-5-power/) `3285NH` —
  the triac mains front end, the two ±10 V rails and how differently they are made, and the
  passive interface that carries the switches, the pot and the motor leads into the tower.
- [**Flexicon backplane map**](/GT2101/project-notes/flexicon-backplane-map/) — ⭐ **the one
  backplane document**: the signal chain through the whole tower, the physical pad map row by
  row, the 2026 repairs, and where the film will fail next.

## Outside the control tower

- [**Mechanical — bearing, suspension, rumble**](/GT2101/project-notes/mechanical-and-suspension/)
  — the three springs are different rates and had been fitted on the wrong legs; the bearing and
  its 0.004″ clearance; why the lubricant was a rumble decision; and John Daly's first-hand
  contradiction of the "rumble is zero" claim.

---

## A note on sources

- [**Archive provenance**](/GT2101/project-notes/archive-provenance/) — where the drawings
  came from, which inherited pages have failed against the hardware, and the ✅ 📄 ❓
  discipline used throughout this site.
- [**Folder findings and leads**](/GT2101/project-notes/folder-findings/) — the technical
  yield of the offline *galeaudio.com* mirror: the motor PCB reading, the connector pin-table
  transcription, the frequencies and rails, the live contradictions over the motor's origin,
  the people still worth contacting, and the encoder-disc suppliers.

The inherited prose pages copied from the defunct *galeaudio.com* have not held up. **All six
have now been checked** against the hardware and **five were substantially wrong** about what
their board does; the sixth describes board 5, the one board whose function can be guessed
correctly from its parts list. The 2015 hand-traced schematics by FANATSON, by contrast, have
held up well — a board-by-board audit on 5 September 2026 found their connector maps and
voltage tables accurate throughout — but they are one person's reverse engineering, some
sheets are marked preliminary, several are marked mirrored, and **there are no Gale factory
drawings in this archive at all**.

The boards themselves are the only primary source. Etched copper beats everything.
