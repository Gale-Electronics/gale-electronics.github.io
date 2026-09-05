---
layout: bare
title: "GT2101 — Project Memory"
permalink: /GT2101/project-notes/project-memory/
description: "The bootstrap document for the GT2101 Remora project — the principle, where the work lives, what is settled, and where every other note is."
---

*A working note — part of the GT2101 project's live record. The polished write-ups live in
[Technical Notes](/GT2101/technical-notes/).*

---

# GT2101 — project memory

**The project is called Remora.** A remora rides on a whale shark: it takes nothing, damages
nothing, and detaches without leaving a mark. The Pico rides on the GT2101 the same way — all
five original boards stay in the tower, powered and running, and the Pico helps them rather
than replacing them.

⚠ The old name **PICOMOD is retired.** *Mod* means modification, and nothing here is modified.
The name argued against the principle, and it is how the remove-the-boards plan crept in.

---

## ⚠⚠ WHAT THIS DOCUMENT IS — rewritten 4 September 2026

**This is a bootstrap document. It is the map, not the territory.**

Until today it was 679 lines and contained two circuit schematics, a firmware specification,
a toolchain guide and a full bench log — all of which also existed, in most cases word for
word, in [`pico-controller-notes.md`](/GT2101/project-notes/pico-controller-notes/). **That
duplication produced three live contradictions**, found on 4 September:

| Contradiction | This file said | The build record said |
|---|---|---|
| `V_IDLE` / board 3 | *"with Board 3 out, firmware is the only thing holding it there… the case that cooks the BD675A/676A"* — **the withdrawn plan** | corrected 29 Aug: board 3 stays, its hardware gate stays |
| Touch divider | 22k/10k, in two places | 27k/10k + 1k — 22k/10k explicitly superseded |
| Parts ordered | ✅ ordered 4 Sept | "nothing has been ordered yet" |

The `V_IDLE` one was bad enough that the bench-order note had to carry a standing
caution amounting to *don't believe the memory doc on this point*. **A bootstrap document
that needs a warning label attached to it elsewhere in the repo has stopped doing its job.**

### ⭐ The rule that keeps it short

> **Nothing in this file may contain a pin number, a voltage, a part number, a resistor
> value or a firmware setting.** Anything that can go stale lives in exactly one specific
> document, and this file points at it.

The one exception is the board table below, because without it this file cannot orient
anybody — and those part numbers were read off etched copper and are not going to change.

**If you find yourself adding circuit detail here, you are putting it in the wrong file.**

---

## ⚠ WHERE THE WORK LIVES — settled 25 August 2026

**One folder. Everything in it. Nothing anywhere else.**

    C:\Users\User\Documents\GitHub\gale-electronics.github.io

That folder is a real git clone of the published site. Everything — schematics, board
photos, technical notes, these working notes, findings, decisions — lives inside it and is
pushed to GitHub at the end of every session, so it is online, backed up and readable by
anyone.

**Order of authority:**

1. **The hardware in front of you.** A measurement beats every document anywhere.
2. **This repository.**
3. Nothing else.

⚠ **This replaces the earlier arrangement**, in which notes were split between the repo, a
claude.ai project and a separate working folder. On 24 August the claude.ai project emptied
without warning and took twenty-one documents with it; seven were recovered from a live
session's context and the rest were lost. **Do not keep the only copy of anything outside
this repository.**

⚠ **There is no second folder, and no other copy of this archive.** Earlier ZIP downloads and
scratch folders contained no `.git` and never reached GitHub. They are struck from the record.
If a note, an instruction or a session points anywhere else, that pointer is wrong and should
be corrected, not followed.

### End of every session

GitHub Desktop → check the changed-file list → summary line → **Commit to main** →
**Push origin**. Twenty seconds, and the work is off the disk.

### ⚠ Start every session like this

1. Connect this repository folder. Folder access is granted per session and does not carry
   over.
2. Read this file.
3. **Check the other notes in `GT2101/project-notes/` for anything written since.** This
   project often moves two or three times in a day, and the documents written *earlier today*
   are the ones most likely to change your answer.
4. Only then start.

On 22 August a full board analysis was delivered without reading two documents written that
same morning, and three of its conclusions were already out of date. Step 3 exists because of
that.

⚠ **The schematic PDFs are image-only scans** — a text read returns empty. That is how
Boards 1–4 were worked out, from PDFs attached to the chat. ✅ **Since 5 September 2026,
connecting the `engineering-drawings-schematics` folder is enough** — a session can render a
sheet and read it directly. See
[`archive-provenance.md`](/GT2101/project-notes/archive-provenance/).

---

## ⚠ Scope — PICO ONLY

The project is **only** this: adding new control logic to the GT2101's control tower using a
Raspberry Pi Pico. Everything else on the deck stays original.

**The replacement controller is out of scope entirely.** It is not being reverse-engineered,
recloned, dated or written about. Its firmware, its part numbers and the manufacturing
enquiry that went with it are all dropped. See the inventory note below for which tower it is
actually in — this was misdescribed until 4 September.

### Why — the principle behind the whole project

A GT2101 with its original electronics replaced is a Gale box, not a Gale. The same is true of
a pair of 401s rebuilt with modern drivers: the cabinet is still Gale, but the character the
company built into it has gone, and nobody paying Gale money is paying for a box. **Everything
added has to be sympathetic to what is already there.**

That is why the Pico rides alongside the original boards instead of replacing them. It is also
the test to apply to any future decision: does this keep the deck a Gale, or does it quietly
turn it into something wearing a Gale's clothes?

⚠ **The distinction that follows from it, and it is the editorial rule for this archive:**
what previous owners and engineers *found out* is kept — their testimony, their measurements,
their mistakes, their dead ends. What they *bolted on* is not. **Findings are the archive;
non-original hardware is not.**

---

## THE HARDWARE — inventory, 4 September 2026

⚠⚠ **There are two towers, and until 4 September this archive did not know it.** Every
document in the repo was written as though there were one deck, one tower and one set of
boards. The bench order still reads, in places, as if a modern board is being taken out of
the only tower Matt owns. **It is not.**

### The two towers

| | What it is | Where it is right now |
|---|---|---|
| **Howie's tower** | Built by **Howie** — his own PCBs and his own parts throughout. Modern microcontroller, its own supply, new segment LEDs, a rotary control | ⭐ **Fitted to the working GT2101 and driving it.** It drives the motor well and works well. **The deck is playable because of this tower** — which is why none of the Pico work is under time pressure |
| **Alex's tower — "the test tower"** | A working original tower, obtained from **Alex** | ⭐ **The bench subject.** Every photograph and every bench session in this repo is this tower. Currently carries the restored flexicon and the LM7805, and is ready to start testing |

⚠ ❓ **Howie's tower puts a small amount of audible noise through the speakers.** Minor, not a
fault, cause unknown — but see the note in
[`pico-controller-notes.md`](/GT2101/project-notes/pico-controller-notes/) § POWER, because it
is the project's only empirical data point on what modern electronics inside a GT2101 tower
does to the audio, and Remora is about to put a microcontroller inside a tower too.

### ⭐⭐ Howie is already in this archive — connected 4 September 2026

**The tower on the deck is the output of a restoration this archive already documents as a
source.** [`folder-findings.md`](/GT2101/project-notes/folder-findings/) describes **"Howie" —
Australian owner who restored a GT2101 with a university student team, active 2015**, and
records him as *"kept as a source, not as a subject."* Nobody had noticed that the tower Matt
is running **is that project's output.** Four things in the repo come from him:

- **The control-tower IC lists by board**, credited to him on the site.
- **The discovery of the flaw in the flexible strap.**
- **The account that the original boards still worked** — *"hey presto …. it works … dial
  speed on the led, touch the top to rotate."* This is the documentary premise for the whole
  restoration plan, and it is about **these exact boards.**
- ⚠ **The undiagnosed "really jerky" rotation** on a repaired flexicon — *"the cro shows the
  signal is being turned on and off repeatedly by something and we don't know what."*

✅ **His stated intention was carried out.** He wrote that he would *"keep the original and now
working parts as backup"*, and Matt has them. That is why the restoration is possible at all.

⚠ **His rebuild was a project decision, not a repair of a dead deck.** New PCBs were already
on order before the strap flaw was found, driven by faster sampling, replaceable parts, and a
wanted feature — the perspex dial stepping 33.3 → 45 → 78 on the lock button.

### The boards

✅ **Every original board that came out of Howie's tower was kept.** ⭐ **They are the boards
every Pico bench session has used** — the Helipot, board 1's display, the green LED. Nothing
was scrapped to build Howie's tower.

⚠ **This matters for the project's principle**, and it cuts in Howie's favour. The archive's
rule is that what a previous owner *bolted on* is not kept — but Howie kept the originals, so
nothing was destroyed and the deck can be put back exactly as it was. **His tower is a
reversible substitution at the tower level, not a modification of a Gale.** That is a
different thing from replacing a deck's electronics, and the record should say so.

### The flexicon

✅ **The restored flexicon — the one with the orange wires — is Howie's tower's own original
cable.** It became spare when Howie's build replaced it. At least five traces broken, coverlay
peeling; repaired and deliberately stiffened by Matt, then tested pad by pad. Full detail in
[`flexicon-backplane-map.md`](/GT2101/project-notes/flexicon-backplane-map/) §8.

**It goes back into Howie's tower when that tower is restored.** ⚠ **It is currently fitted to
the test tower.**

❓ **Does the test tower have a flexicon of its own?** The last piece of the count, and still
open. Until it is answered, **treat the restored flexicon as the only one** and keep the rule:
**solder to the brass staple, never to a pad.**

### ❓⚠ Is the restored flexicon the one that ran jerky?

**A question worth answering before step 4, and nobody has asked it.** Howie's team *"fitted a
replacement flex strap"*, after which the deck ran but with **"really jerky"** rotation that
they never diagnosed and the record simply stops on.

So there may be **two** straps in that tower's history — the original, and Howie's
replacement. **Which one does Matt have, and is the orange-wired repair on the strap that
misbehaved?**

⭐ **It changes what the precedent means.** As currently written,
the bench notes recorded jerky rotation as *"precedent on a repaired flexicon, not a new fault
of yours."* **If
it is the same physical part, it is not precedent — it is an undiagnosed fault still present
in the component**, and the right response is to look for it rather than to accept it.

### ⚠⚠ The restored flexicon is in the wrong tower

**The least replaceable part in the project is currently installed in the tower that is about
to receive a breadboard, a Pico and experimental connections.**

Two things make this worse than it looks:

1. It is the part the **Howie restoration depends on**. If it is damaged during Pico bring-up,
   the restoration loses its backplane, not just the bench.
2. §8 of the flexicon map records that stiffening moved the stress to the **ends of the orange
   wires**, so each refit loads the pads harder than before — and this one already has to come
   out of the test tower and go into Howie's tower at least once more.

⭐ **If the test tower has its own flexicon, put it back in and box the restored one until the
Howie restoration.** The test tower's job is to be experimented on; the restored film's job is
to survive.

### The plan

Howie's tower is eventually restored — modern parts out, its own original boards back in, on
its own restored flexicon, with the Pico inside. **Not yet, and not urgent.** The bench work
happens on the test tower first, precisely so the restoration target is not the test subject.

---

## The five boards

Numbered 1 at the top of the stack to 5 at the bottom.

| Board | Gale no. | What it does |
|---|---|---|
| 1 (top) | `3155ST` | Display — a three-digit frequency counter |
| 2 | `3272ST` | Capacitive touch start/stop, display timing, carries the Helipot |
| 3 | `3275ST` | `F VAR` generator + the drive-voltage gate |
| 4 | `3276ST` ISSUE C | Crystal, ÷4 reference, tacho front-end, **the servo** |
| 5 (bottom) | `3285NH` ❓ | Power supply + passive external interface. ⚠ **Carries mains** |
| backplane | `3281NH` | Flexible printed film by *flexicon* |

✅ All part numbers except Board 5's were **read off the etched copper**. The sequence
3155 · 3272 · 3275 · 3276 · 3281 · 3285 ascends down the stack, which corroborates the whole
register. Boards carry **ISSUE letters** — a revision axis nobody had recorded.

**Boards 3 and 4 are one servo split across two boards** — 4 decides the drive voltage,
3 decides whether it is allowed out.

⚠ **All five boards stay.** The Pico is added alongside the original logic, not in place of
any of it. It listens first, and only once the tacho, the demand and the drive are logged and
understood does anything get injected — at the backplane, one connection at a time.

---

## ⭐ WHERE EVERYTHING IS

**The build**

| Document | What is in it |
|---|---|
| [Remora — working notes](/GT2101/project-notes/pico-controller-notes/) | ⭐ **The build record and the single source for all of it:** where the Pico connects, interfacing and level shifting, the green LED, the tacho JFET, power, firmware, toolchain, and the full bench log |
| [Parts list](/GT2101/project-notes/parts-to-order/) | What the build needs and what each item unblocks |

**The boards and the wiring**

| Document | What is in it |
|---|---|
| [Board 1 — Display](/GT2101/project-notes/board-1-display/) | Pin map, the four-state latch/reset cycle, the sessions that drove it from a Pico |
| [Board 2 — Touch](/GT2101/project-notes/board-2-touch/) | The capacitive touch circuit and the 14-pin connector |
| [Board 3 — `F VAR` and the gate](/GT2101/project-notes/board-3-fvar-gate/) | ⭐ **Home of the drive-voltage table** — 0 V still, 1.2 / 1.6 / 2.4 V |
| [Board 4 — the servo](/GT2101/technical-notes/board-4-servo/) | Crystal, tacho front-end, the PLL. Written up in Technical Notes |
| [Flexicon backplane map](/GT2101/project-notes/flexicon-backplane-map/) | ⭐ **The one backplane document.** The signal chain, the physical pad map, the repairs, and where the film will fail next |

**Outside the control tower**

| Document | What is in it |
|---|---|
| [Mechanical — bearing, suspension, rumble](/GT2101/project-notes/mechanical-and-suspension/) | ✅ The three springs are different rates and were on the wrong legs. Plus the bearing, the lubricant and why it was chosen, the foam, and the unresolved rumble contradiction. ⚠ **Restored 4 Sept after this file's own de-duplication pass deleted it** |

**Practice and provenance**

| Document | What is in it |
|---|---|
| [Archive provenance](/GT2101/project-notes/archive-provenance/) | Where the drawings came from, which inherited pages are disputed, and the ✅ 📄 ❓ discipline |
| [Folder findings and leads](/GT2101/project-notes/folder-findings/) | The galeaudio.com mirror's technical yield: the motor PCB reading, the pin-table transcription, the live contradictions, and the contact list |
| [Firmware](/GT2101/project-notes/firmware/) | What is in the repo and what is still only on the Pico. ⚠ Eight of nine files are outside the repository |

---

## Settled — do not reopen without new evidence

Each of these was argued out, and re-litigating one costs a session.

- **All five boards stay.** An earlier plan removed boards 3 and 4 and put the Pico in a
  vacated slot. **Withdrawn in full.** Any note reasoning from "with board 3 out" is stale.
- **Boards 3 and 4 are one servo split across two boards** — this corrected a wrong
  description of boards 2 and 3 inherited from the defunct website.
- **The tacho runs at ~600 pulses per platter revolution, not 60 and not 2400.** The figure
  has been wrong twice, each time by assuming the wrong reference frequency.
- **`V_IDLE` is 0 V, not 10 V** — and board 3's hardware gate enforces it. Firmware agrees
  with the hardware rather than substituting for it.
- **The tacho level shifter is a JFET.** Not a divider, not a MOSFET, and not the PNP circuit
  in the old notes, which cannot work in either state.
- **The replacement controller is out of scope**, and what previous restorers found out is
  kept while what they bolted on is not.
- **The repo is the only folder.**

---

## ⚠ Open challenges — nobody has answered these

**The counterweight to the list above.** Rescued on 4 September 2026 from the fresh-eyes brief —
a document written to be handed to a sceptic, retired once the rest of it had been absorbed
elsewhere. These four were the only part of it that lived nowhere else. They are
deliberately uncomfortable and they should stay that way.

**1. Is "listen to everything first, break nothing" actually the cheapest order — or
procrastination dressed as caution?**

⭐ **Partly answered on 4 September, against us.** The bench order had the project's single most
valuable measurement — the tacho frequency — sitting behind five steps and a parts delivery,
when it needed nothing but a scope on a deck that was already turning. **Some of the caution was
self-imposed.** Worth re-asking of every remaining step: what does this genuinely depend on?

**2. Is there a reading of the archive in which the tacho figure is neither 333 nor 1332 Hz?**

Still open — and now cheap to settle empirically. See § NEXT below: it needs one scope probe on
the deck as it stands.

**3. Is keeping board 3 in circuit genuinely safer — or does having two gates in series, board
3's and the motor board's, make a fault harder to localise than one would be?**

⚠ **Still open, and it is a real objection to the current architecture.** The project decided
all five boards stay, partly because board 3's hardware gate protects the motor at rest. But the
motor PCB has its own JFET gating on all three phases off `SPEED IN`. **If drive is present and
the platter does not turn, there are two candidates and no way to tell them apart from outside.**
Nobody has argued this through.

**4. What has been missed entirely?**

The one that keeps paying. On 4 September alone it produced: **two towers** rather than one,
**Howie already being a documented source** in this archive rather than an anonymous previous
owner, and **the display-source chain** — board 3's window comparator throwing board 2's
analogue switch to show demand when stopped and tach when running — which had been sitting
unnoticed across three board studies.

---

## STATUS — 4 September 2026

**Eight bench sessions complete.** Board 1 is done apart from auto-lock: the display, the
green LED and the deck's speed pot all answer to the Pico, and the pot drives the display in
real time. The Pico runs on the tower's own power. All five boards are identified from their
own etched part numbers and studied from their own drawings. The architecture is settled.

**The full bench log lives in
[`pico-controller-notes.md`](/GT2101/project-notes/pico-controller-notes/) § BENCH LOG.**

✅ **Parts ordered 4 September 2026, awaiting delivery** — for a perfboard interface card
carrying the dividers, level shifters and JFET front-end. Log the box contents against the
parts list before anything is built.

⚠ **The three most valuable things still unmeasured**, all of which turn 📄 into ✅:

1. **Board 3 pin 7 on a running deck**, at each speed. Four numbers that are the entire
   specification for `drive.nominal_drive()` and the safety ceiling.
2. **The tacho pulses per revolution.** Expect ~600, ~333 Hz at 33⅓.
3. **The tower gap** the Pico has to straddle. Nothing gets printed until that number exists.

---

## NEXT

⚠ **The separate bench-order note was deleted on 4 September 2026.** What follows is now the
only statement of what to do next, so it is kept here deliberately. **One session, one goal,
one measurable outcome.**

### ⭐ Needs nothing — available now

**No parts, nothing dismantled, no risk to anything.** Several of these had been sitting behind
blockers they never actually had.

1. ⭐ **Measure the tacho frequency, on the deck as it stands.** The tacho is made by the encoder
   disc and the LM339 on the **motor PCB** — original hardware, turning right now — so **it does
   not care which tower is fitted.** One scope probe. *Measurable outcome: the frequency on
   `TACH` at 33⅓.* ~333 Hz confirms 600 ppr; ~1332 Hz means you have landed upstream of board
   4's ÷4. ⚠ **Scope, not a meter** — it swings 0 to −10 V. This figure has been wrong twice,
   and it sets `TACHO_PPR`, every measurement window and the servo tuning.
2. **Copy `config.py` into [`firmware/`](/GT2101/project-notes/firmware/).** Two minutes in
   Thonny, and it is the only record of which GP pin goes to which wire. Eight of the nine
   firmware files exist nowhere but on the Pico.
3. **Photograph the encoder disc while it is intact.** No disc geometry exists anywhere in this
   archive, and there is already a photograph of a shattered one. While looking: does it carry
   only the tach track, or a commutation pattern as well? Answerable by eye.
4. **Does the test tower have a flexicon of its own?** One look, and it decides the whole break
   calculus — see [`flexicon-backplane-map.md`](/GT2101/project-notes/flexicon-backplane-map/) §8.
5. **Board 1 auto-lock.** One wire and one resistor, anything from about 47 kΩ to 470 kΩ.
   **Check the drawer before assuming it is blocked.** Removes the project's most annoying
   recurring fault.
6. **Measure the tower gap.** One number. Nothing is printed until it exists.

### Needs the parts box

Log what actually arrived against
[`parts-to-order.md`](/GT2101/project-notes/parts-to-order/) **before building anything** — that
list has been amended three times. Then the perfboard interface card, the tacho JFET front-end,
the touch wire (☠ row 2 pad 5, **never** pad 6), and the 10 V level shifters. Detail in
[`pico-controller-notes.md`](/GT2101/project-notes/pico-controller-notes/).

### Needs a tower on the deck — a decision, not a step

Anything needing a turning **original** servo means **displacing Howie's tower from the deck**:
running the restored tower in FIX to see whether it holds 33⅓, and measuring board 3 pin 7 at
each speed — the calibration prize, and the most valuable measurement left in the project.

⚠ **There is no hurry. The deck plays.** Do everything above first.
