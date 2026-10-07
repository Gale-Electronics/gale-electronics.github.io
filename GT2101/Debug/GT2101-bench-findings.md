# GT2101 Bench Findings

Companion to GT2101-debugging-reference.md. A dated record of what has been measured, ruled out and
fixed on the bench. NOTE FOR A NEW CHAT: treat sections 2 and 3 as settled and do not re-test them.
Start from section 5 (checks still to record). Facts as stated or measured by Matt; items marked
TO CONFIRM are not yet settled. Last updated 7 Oct 2026.

---

## 1. Current status (7 Oct 2026)

Control tower fixed. Original fault: display showed only zeros (`00.0`).

Cause: a dead 4013 dual flip-flop on the original in-tower Board 4, so no F REF signal went from
Board 4 to Board 1 (Board 4 pad 9 -> Board 1 pad 7). Without F REF, Board 1's 4013 never steps
through its states, so the latch never fires and the digits stay at zero.

Fix: swapped in a spare Board 4 (the MC14520CP revision). Display immediately came back to life
and now latches properly.

---

## 2. Dated log

**6 Oct 2026**
- Display showing zeros. Started debugging at Board 1 and Board 2.
- Tools: multimeter and FNIRSI 2C23T scope/meter. Spare Board 1, 2, and 4 available outside the tower.
- A spare Board 1 fitted in the tower also showed only zeros.
- Board 2 pads 2, 10 and 11 read good. Pad 11 about 3.8 V with the black switch off, 5.6 V on.
- Board 2 pad 13 to ground: 1M.
- Board 4 pad 3 live on the scope: ~1.8 kHz in VAR (follows the Helipot), ~1.03–1.33 kHz in FIX.
- Board 4 pad 9 / Board 1 pad 7 (F REF): flat 0 V, continuity good between the two pads.
- Motor disconnected during testing. Preferred not to pull boards from the tower yet.

**7 Oct 2026**
- Standalone bench testing of spare Board 4 with bench PSU:
  - Pad 2 confirmed healthy: master crystal oscillating at 1.05 MHz.
  - Fault on the tower's original Board 4 isolated: Pad 3 receiving demand clock, but Pad 9 output completely flat (0 V).
- Solved Board 4 revision discrepancy:
  - Tower's original Board 4 uses a **4013 (14-pin dual D flip-flop)** for the ÷4 divider.
  - Spare Board 4 uses an **MC14520CP (16-pin dual binary counter)** for the ÷4 divider.
- Swapped spare Board 4 into the tower. Pad 9 restored. Display un-froze and is now working.

---

## 3. Ruled out (do not re-test)

- Board 2 timebase and gate: crystal in, MC14521 first stage and gate out all read good (6 Oct).
- Board 1: a spare Board 1 gave the same zeros, and the fix was on Board 4.
- Speed demand path: Board 4 pad 3 live in both VAR and FIX (6 Oct).
- Flexicon between Board 4 pad 9 and Board 1 pad 7: continuity good (6 Oct).
- Motor: disconnected throughout, not involved in the display fault.

---

## 4. Confirmed: two Board 4 revisions (÷4 divider)

The GT2101 documentation records two distinct revisions of Board 4 for generating F REF (Pad 9):

1. **Older Revision (Original Tower Board):**
   - Uses a **4013** (MC14013 / CD4013, 14-pin DIP) dual D-type flip-flop configured as a ÷4 ripple counter.
   - Matches the 2015 hand-traced `Board-4-Layout.pdf` where "4013" is handwritten on the chip.
   - Failure mode: dead 4013 IC (flat Pad 9 output). Replacement part: CD4013BE / MC14013B.

2. **Later Revision (Spare Board, Issue C):**
   - Uses an **MC14520CP** (16-pin DIP) dual binary up-counter using the Q1 output for ÷4.
   - Matches the `GT201/3276ST ISSUE C` board description.
   - Replacement part: MC14520BCP / CD4520BE.

**Cross-compatibility:**
- Both revisions are **100% pin-compatible** drop-in replacements on the 9-pin edge connector.
- Pin 3 is always 4×F in; Pin 9 is always 1×F out (÷4).

---

## 5. Checks still to record after the repair

- Board 4 pad 9 and Board 1 pad 7: square wave present (~333 Hz in FIX), same amplitude at both.
- FIX position: display reads 33.3 (1332 Hz x 0.25 s = 333 counts).
- VAR position: display follows the Helipot smoothly.
- Board 4 pad 2: still about 5.2 V (crystal signal not loaded down).
- Board 4 pad 6 (Drive voltage out): check stationary DC voltage to verify servo output.

---

*Facts only. No restoration history, provenance or attribution.*
