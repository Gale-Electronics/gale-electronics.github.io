---
layout: bare
title: "GT2101 — Project Notes"
permalink: /GT2101/project-notes/
description: "The working record of the GT2101 restoration and Pico controller project — board studies, bench sessions, decisions and open questions, written as the work happens."
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
  Where the work lives, what has been settled, what has changed, and what is next. Read this
  first.

## The build

- [**Pico controller — working notes**](/GT2101/project-notes/pico-controller-notes/) —
  the live record of replacing the 1970s control logic with a Raspberry Pi Pico: which
  boards stay, where the Pico connects, interfacing, firmware, and the bench log.
- [**Parts list**](/GT2101/project-notes/parts-to-order/) — what the build needs and what
  each item unblocks.

## The boards, studied

- [**Board 1 — Display**](/GT2101/project-notes/board-1-display/) `3155ST` — a three-digit
  frequency counter. Complete connector pin map, the four-state latch/reset cycle, and the
  sessions that drove it from a Pico without modifying it.
- [**Board 2 — Touch and display timing**](/GT2101/project-notes/board-2-touch/) `3272ST` —
  the capacitive touch start/stop circuit, and the 14-pin connector.
- [**Board 3 — `F VAR` and the drive gate**](/GT2101/project-notes/board-3-fvar-gate/)
  `3275ST` — the variable-speed oscillator and the gate that mutes the motor at rest.
- [**Backplane signal map**](/GT2101/project-notes/backplane-signal-map/) — what travels
  between all five boards, pin by pin.

---

## A note on sources

The inherited prose pages copied from the defunct *galeaudio.com* have not held up. Four
have been checked against the hardware and all four were substantially wrong about what
their board does. The 2015 hand-traced schematics by FANATSON, by contrast, have held up
well — but they are one person's reverse engineering, some sheets are marked preliminary,
and **there are no Gale factory drawings in this archive at all**.

The boards themselves are the only primary source. Etched copper beats everything.
