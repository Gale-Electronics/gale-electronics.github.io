---
layout: bare
title: "GT2101 — Mechanical: Bearing, Suspension and Rumble"
permalink: /GT2101/project-notes/mechanical-and-suspension/
description: "The GT2101's bearing, lubricant, spring suspension and foam — what is confirmed on the hardware, what comes from the defunct site, and the unresolved rumble question."
---

*A working note — part of the GT2101 project's live record. The polished write-ups live in
[Technical Notes](/GT2101/technical-notes/).*

---

# Mechanical — bearing, suspension, rumble

**Created 4 September 2026**, and overdue. Notes across this repo have cited a file called
`gt2101_suspension.md` since 24 August. **It never existed.** The only account of the
suspension was three paragraphs inside `project-memory.md`, and everything about the bearing,
the lubricant and the foam was sitting inside
[`folder-findings.md`](/GT2101/project-notes/folder-findings/) §2.5 — a document about the
*provenance of a defunct website*, which is not where a bearing clearance belongs.

⚠ **This file exists because of a mistake worth recording.** On 4 September the suspension
paragraphs were **deleted** from `project-memory.md` during a de-duplication pass, on the
assumption that anything in the bootstrap doc was duplicated elsewhere. It wasn't — it was
orphaned, which looks identical from a distance. The content below is restored from that
deletion. **Orphaned and duplicated are not the same thing, and the test is a grep, not a
glance.**

---

## 1. ✅ The suspension — confirmed on the hardware, 24 August 2026

The acrylic sub-chassis rides on **three towers**. Each is a **coil spring inside a plastic
tube, plunging into an aluminium cup.**

✅✅ **The three springs are not the same rate, and the odd one belongs at the arm corner** —
that is the heaviest corner. **They were fitted wrong.** The sub-chassis sat crooked and the
tubes rubbed in their cups. Matt swapped them on 24 August and **the deck now floats freely.**

⭐ That is the kind of finding the archive exists for: nothing in any document says the springs
differ, and a deck with them on the wrong legs would read as a tired suspension rather than a
mis-assembled one.

### ⚠ Still open — and the numbers moved in the wrong direction

| | Before the swap | After | Target |
|---|---|---|---|
| Bounce count | 3–4 | **12** | **4–6** |

**3–4 was friction, not damping** — the tubes rubbing in their cups were absorbing the energy.
Removing the rubbing removed the false damping and revealed how little real damping there is.
**12 is too little.** ❓ **The resonant frequency has never been measured.**

📄 The suspension height is specified: the **top tri-plexi should sit at the midpoint between
the upper and lower metal parts of the tower.**

---

## 2. The bearing

📄 `[SITE]`, but ⭐ **corroborated independently** by Nigel Hobden via Simon Y — which is
unusual for a galeaudio.com claim and worth noting.

- **Ground stainless spindle in a phosphor-bronze bush**
- **A matched pair**, with **0.004″ clearance**
- **Clock/watch oil**

⚠ The bearing is **part of the motor assembly**, not a separate component — rotor, stator,
integral encoder, samarium-cobalt thrust bearing and the platter interface are one unit. That
is why there is no like-for-like replacement; see
[`folder-findings.md`](/GT2101/project-notes/folder-findings/) §8.

### The lubricant, and why it is that lubricant

📄 `[2nd]` The oil was chosen by the **Leicester University Department of Tribology**. Watch
oil, originally sperm-whale derived. Ira Gale also approached **BP Advance Fluids** about
space-programme oils.

**Nigel Hobden's stated reason:** anything else introduces rumble; watch oil does not oxidise
and stays put.

⚠ **So the oil is a rumble decision, not a friction decision** — which matters, because rumble
is the deck's one live performance contradiction (§4). Do not substitute a heavier oil for a
quieter bearing without knowing that the original choice was already optimising for exactly
that.

---

## 3. Magnetic shielding

📄 `[SITE]`, uncorroborated. **Samarium-cobalt magnets in repulsion, inside a 5 mm Swedish
soft-iron cylinder**, to keep the motor's field off the cartridge.

---

## 4. The foam

📄 `[2nd]` **C.B. Frost Ltd, Birmingham.** Gale selected it by trial and error from samples.

**Correct foam in good condition should mean no wobble.** ⚠ Ira Gale **considered and rejected
silicone damping** — worth knowing before anyone proposes adding damping to fix the bounce
count in §1. It was already on the table in period and was turned down.

---

## 5. ⚠ Rumble — the live contradiction

The deck's one unresolved performance claim, and **it is testable on the bench.**

| Source | Claim |
|---|---|
| 📄 `[SITE]` galeaudio.com | *"Rumble is zero because there is no mechanical contact surface"* |
| ⭐ `[1st]` **John Daly**, DCA Design Director, email 1 June 2006 | *"In the end the turntable was too expensive and **I think it suffered from too much rumble** compared to other high end turntables that were around at the time."* |

**Daly is the stronger source** — first-hand, named, and he was the design director of the firm
that styled the deck, with no reason to talk it down. The site's claim is unsourced and reads
like marketing copy.

⚠ **And §1 is now relevant to it.** If the springs have been on the wrong legs for years, and
the tubes have been rubbing in their cups, then any rumble measurement taken on this deck
before 24 August was measuring a mis-assembled suspension. **Whatever Daly heard in 2006 may or
may not have been the design's fault.** That is worth measuring properly now that the
sub-chassis floats.

---

## 6. Provenance

Sections 2 to 5 are extracted from
[`folder-findings.md`](/GT2101/project-notes/folder-findings/) §2.5 and §4.4, where they had
been sitting inside a document about the reliability of a defunct website. The weighting tags
`[SITE]`, `[1st]` and `[2nd]` are that document's, and §1 of it explains why `[SITE]` claims
carry a **known directional bias**. Read them there if a claim here matters to a decision.

Section 1 is ✅ Matt's own work on the hardware, 24 August 2026.
