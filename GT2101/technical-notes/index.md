---
title: "GT2101 — Technical Notes"
layout: bare
permalink: /GT2101/technical-notes/
nav_exclude: true
description: "Service documentation, diagnostic field reports, board-by-board analysis and restoration insight for the Gale GT2101 turntable and its servo control system."
---

# Technical Notes

Curated service data, measurement maps and modern analysis for the **Gale GT2101**.

Every claim in this section carries a status marker: ✅ confirmed against the hardware,
📄 from a document, ❓ unverified. Nothing is deleted for being unverified — it is labelled.
Where a note contradicts the inherited descriptions elsewhere in this archive, the note is
the later work and says why.

## The boards

- [**Disk 4 — the servo board**](/GT2101/technical-notes/board-4-servo/) — `GT201/3276ST ISSUE C`.
  The crystal reference, the JFET tacho front-end and the MC14046 phase-locked loop that generates
  the motor drive voltage. Not merely a reference oscillator.
- [Board register and drive-voltage figures](/GT2101/engineering-drawings-schematics/#register) —
  what each of the five boards does, with the corrections to the inherited descriptions.

## Signals

- [Motor & PCB Signal Map](/GT2101/technical-notes/motor-signal-map/)

## Restoration

- [**A modern controller**](/GT2101/technical-notes/pico-controller/) — an ongoing project to
  replace the 1970s control logic with a microcontroller while keeping every other original part,
  including driving the 1975 display without modifying it.

---

*Still to be written up here: the display board, the touch-sensor board, the `F VAR` and
drive-gate board, and a note on the provenance of the archive's drawings.*
