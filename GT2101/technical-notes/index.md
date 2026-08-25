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
- [Backplane signal map](/GT2101/project-notes/backplane-signal-map/) — what travels between
  all five boards of the control tower, pin by pin.

## Motor

- [Motor findings](/GT2101/technical-notes/motor-findings/)

## Restoration

- [**A modern controller**](/GT2101/technical-notes/pico-controller/) — an ongoing project to
  replace the 1970s control logic with a microcontroller while keeping every other original part,
  including driving the 1975 display without modifying it.

---

## The working record

These pages are the finished write-ups. The **[Project Notes](/GT2101/project-notes/)**
section holds the working record behind them — the full board studies for boards 1, 2 and 3,
the bench sessions, the parts list, and the running project memory. That is where a claim
made here can be traced back to the measurement that produced it.

Still to be written up on this page in finished form: the display board, the touch-sensor
board, the `F VAR` and drive-gate board, and a note on the provenance of the archive's
drawings. All four exist in draft in the project notes.
