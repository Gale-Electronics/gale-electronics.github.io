# GT2101 Bench Findings

Companion to GT2101-debugging-reference.md. A dated record of what has been measured, ruled out and
fixed on the bench. NOTE FOR A NEW CHAT: treat sections 2 and 3 as settled and do not re-test them.
Start from section 5 (checks still to record). Facts as stated or measured by Matt; items marked
TO CONFIRM are not yet settled. Last updated 7 Oct 2026.

---

## 1. Current status (7 Oct 2026)

Control tower fixed. Original fault: display showed only zeros.

Cause: a dead MC chip on Board 4, so no F REF signal went from Board 4 to Board 1 (Board 4 pad 9 ->
Board 1 pad 7). Without F REF, Board 1's 4013 never steps through its states, so the latch never
fires and the digits stay at zero.

---

## 2. Dated log

**6 Oct 2026**
- Display showing zeros. Started debugging at Board 1 and Board 2.
- Tools: multimeter and oscillator. Spare Board 1 and Board 2 available to probe outside the tower.
- A spare Board 1 fitted in the tower also showed only zeros.
- Board 2 pads 2, 10 and 11 read good. Pad 11 about 3.8 V with the black switch off, 5.6 V on.
- Board 2 pad 13 to ground: 1M.
- Board 4 pad 3 live on the scope: 1.8 kHz in VAR (follows the Helipot), 1.33 kHz in FIX.
- Board 4 pad 9 / Board 1 pad 7 (F REF): flat 0 V, continuity good between the two pads.
- Chip marking read off a Board 4: MC14520CP (see TO CONFIRM in section 4).
- Motor disconnected during testing. Preferred not to pull boards from the tower yet.

**7 Oct 2026**
- Fix reported: dead MC chip on Board 4, no signal from Board 4 to Board 1.
- Established that the tower's Board 4 is an older revision from the spare Board 4 (section 4).

---

## 3. Ruled out (do not re-test)

- Board 2 timebase and gate: crystal in, MC14521 first stage and gate out all read good (6 Oct).
- Board 1: a spare Board 1 gave the same zeros, and the fix was on Board 4.
- Speed demand path: Board 4 pad 3 live in both VAR and FIX (6 Oct).
- Flexicon between Board 4 pad 9 and Board 1 pad 7: continuity good (6 Oct).
- Motor: disconnected throughout, not involved in the display fault.

---

## 4. Correction to the reference: two Board 4 revisions

The reference describes Board 4 pad 9 as the MC14520 divide-by-4 output. That only holds for the
later Board 4 revision.

- The Board 4 in the tower is an older revision and has no MC14520.
- The spare Board 4 is the later type and does have the MC14520.
- TO CONFIRM: how F REF is generated on the older board, which chip was dead, and what replaced it.
- TO CONFIRM: the MC14520CP marking logged on 6 Oct may have come from the spare board rather than
  the tower's board.
- TO CONFIRM: whether the spare Board 4 swaps straight into the tower or differs in other ways.

---

## 5. Checks still to record after the repair

- Board 4 pad 9 and Board 1 pad 7: square wave present, same amplitude at both.
- FIX position: display reads 33.3 (1332 Hz x 0.25 s = 333 counts).
- VAR position: display follows the Helipot smoothly.
- Board 4 pad 2: still about 5.2 V (crystal signal not loaded down).

---

*Facts only. No restoration history, provenance or attribution.*
