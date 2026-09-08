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

---

## ⚠ Scope — PICO ONLY

The project is **only** this: adding new control logic to the GT2101's control tower using a
Raspberry Pi Pico. Everything else on the deck stays original.

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

⚠ The Pico is added alongside the original logic, not in place of
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

⚠ **The four most valuable things still unmeasured**, all of which turn 📄 into ✅:

1. **Board 3 pin 7 on a running deck**, at each speed. Four numbers that are the entire
   specification for `drive.nominal_drive()` and the safety ceiling.
2. **The tacho pulses per revolution.** Expect ~600, ~333 Hz at 33⅓.
3. **The tower gap** the Pico has to straddle. Nothing gets printed until that number exists.
4. ⚠ **Board 3 pads 2 and 3, platter stopped then turning** — added 8 September 2026. They tell
   board 2 whether the deck is moving, and the 8 September audit found them fed from the
   `ORANGE` post, which Remora has left open. **If they do not move, the display can read about
   4× out and it is not the Pico's fault.** See
   [`board-3-fvar-gate.md`](/GT2101/project-notes/board-3-fvar-gate/) §2a and
   [`corrections-log.md`](/GT2101/project-notes/corrections-log/) §17.

---


### Needs the parts box

Log what actually arrived against
[`parts-to-order.md`](/GT2101/project-notes/parts-to-order/) **before building anything** — that
list has been amended three times. Then the perfboard interface card, the tacho JFET front-end,
the touch wire (☠ row 2 pad 5, **never** pad 6), and the 10 V level shifters. Detail in
[`pico-controller-notes.md`](/GT2101/project-notes/pico-controller-notes/).


⚠ **There is no hurry. The deck plays.** Do everything above first.
