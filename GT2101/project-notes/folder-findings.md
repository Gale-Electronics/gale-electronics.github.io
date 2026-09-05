---
layout: bare
title: "GT2101 — Folder Findings and Leads"
permalink: /GT2101/project-notes/folder-findings/
description: "Technical data, live contradictions, people and document leads extracted from the offline galeaudio.com mirror and the FANATSON tracings — every claim weighted by how it is sourced."
---

*A working note — part of the GT2101 project's live record. The polished write-ups live in
[Technical Notes](/GT2101/technical-notes/).*

---

# GT2101 — Folder findings: technical material and leads

⚠ **Renamed and given frontmatter, 4 September 2026.** This file was
`GT2101_interview_extraction_1.md` and **had no frontmatter at all** — no layout, no title, no
permalink — so it was the only document in `project-notes/` that did not publish as a page.
`index.md` could only link to the containing folder, because there was no URL to point at.
Twenty-one kilobytes of the best provenance material in the project was effectively invisible
on the site.

The old name was misleading too: this is not an interview transcript. It is the technical and
documentary yield of the whole offline folder, and the name now says so. ⚠ **Two notes
elsewhere in the repo cited it as `GT2101_interview_extraction.md`, without the `_1` — a
filename that never existed.** Those references are corrected.

**Source:** an offline mirror of galeaudio.com plus the FANATSON tracings, since folded into this repository.
**Revised:** 28 August 2026. Supersedes the earlier interview-extraction version.
**Removed in this pass:** Ira Gale biography, Warhol/*Pork*, celebrity owners, dealer and showroom history, speaker restoration threads, for-sale classifieds, and the general people index. None of it bore on the deck.

---

## 1. Source reliability — read before using anything below

**The galeaudio.com prose has a directional bias toward US manufacture.** Its author, John Mayberry ("emmaco", Southern California), asserted US origin for the GS401 bass drivers and continued asserting it publicly after being shown otherwise — the first run was US, later production was in-house in London, confirmed with **David Lyth**, who oversaw production. Every unsourced origin claim on that site is therefore suspect **in a known direction**, and the motor origin claims below are tagged accordingly.

Note the bias does not discriminate between his two candidates: Inland Motor (Radford, Virginia) and Litton Industries are both American. Where it bites is one level up — the assumption that the whole motor assembly arrived complete from America.

**Weighting used throughout:**

- `[HW]` read off hardware or off a tracing of hardware — strongest
- `[1st]` first-hand from a named participant, hedges preserved
- `[2nd]` relayed through an intermediary
- `[SITE]` galeaudio.com prose, unsourced — treat as a hypothesis only

**Third numbering system warning.** The folder's pin tables are an independent transcription and disagree with the board studies in places (they mark board 4 pin 6 "???" where the board study has row 4 pad 6 = demand). Use them to cross-check, never as bench authority — **the board studies are the physical-pin reference.** Full detail in [`archive-provenance.md`](/GT2101/project-notes/archive-provenance/) § three numbering systems, which is that warning's home.

---

## 2. Hard technical data

### 2.1 Motor PCB — from `jpg\GaleTTmotSchem_1.jpg` (FANATSON, 10.9.2015) `[HW]`

Read directly from the tracing this session. **This is the most useful single document in the folder** and it changes the shape of the Pico problem.

**Topology.** A self-contained three-phase brushless commutator with a separate tach channel:

- **LM339 quad comparator**, four sections in use:
  - **BROWN** (with a second input marked M) → out pin 2 = **TACH**, 4k7 pull-up
  - **GREEN** → 10K in, pins 8/9 → out 14
  - **YELLOW** → 10K in, pins 6/7 → out 1
  - **VIOLET** → 10K in, pins 10/11 → out 13
  - Each of the three sensor sections carries **470K feedback** (hysteresis). A 180K sits to −10 V.
- Each phase then: **47K + 47K** in series, an **N-channel JFET (E113/J113) shunt to ground**, and a capacitor to ground
- **LM324** buffer per phase (sections 6/5→7, 2/3→1, 13/12→14; the fourth section 9/10→8 is unused, NC, pin 11 to −10 V)
- **560R** into a complementary Darlington output pair — the sheet annotates **BD675A** and **BD676A** (one label partly cut; BD675A is NPN and BD676A PNP in standard datasheets)
- **Outputs: green/white, red/white, black/white** — the three motor phases
- **Rails: ±15 V**, with a **−10 V** reference

**The consequence for the Remora.** There is a single analogue net marked **"SPEED IN"** running down the sheet, feeding all three phase chains through the 47K resistors and the JFET shunts. Commutation is handled autonomously on this board from the three sensor lines. So **driving the motor requires one analogue amplitude command, not three-phase PWM** — provided the motor PCB is retained. That is a very different and much smaller job for the Pico than commutating from scratch.

Note also this board has **its own JFET gating** on all three phases off SPEED IN — a second gate, distinct from the still-gate you're investigating on board 3.

### 2.2 Control tower ICs by board `[HW]`, credited on the site to Howie

⚠ **Two part descriptions corrected 5 September 2026.** The site's own list called the
MC14011 a "quad AND" and the MC14001 a "quad OR". They are a quad **NAND** and a quad
**NOR**; the whole of Board 1's latch/reset decode only works if they are. The same two
errors appear in `engineering-drawings-schematics/board-1-display/Board-1-Display-Logic-Interface.pdf`,
which suggests that page was written from this list rather than from the board. The board-1
row below is corrected; the other rows are left as transcribed.

| Board | Devices |
|---|---|
| **Top (1)** | MC14511CP BCD→7-seg · MC14553CP BCD decade up counter · MC14011CP quad **NAND** · MC14001CP quad **NOR** · MC14013CP dual D · 3 × TIS61 PNP 300 mW · BC214 PNP 625 mW |
| **2nd** | MC1748CP1 op-amp · MC1455P1 timer (555) · **MC14521CP 24-stage divider** · MC14016CP quad analog switch · MC14040CP 12-bit counter · MC14011CP · MC14001CP · BC184 NPN |
| **3rd** | MC14011CP · LM3900N quad op-amp · **XR2207P VCO** · LM308N precision op-amp · MC14013CP dual D · MC1747CL dual op-amp · BC214 · **2N4393 N-JFET** |
| **4th** | MC14011CP · **MC14520CP dual binary up counter** · **MC14046CP PLL** · MC1747CL · BC184C · "Vishay W300A 7709" N-JFET · **2N4392 N-JFET** |
| **Power (5)** | BTB08 8 A triac · 10DB1A bridge rectifier · TIS91 600 mW · 1N5761A diac · one unidentified device under the heat sink |

### 2.3 Ribbon connector pin tables — folder transcription, cross-check only

**Board 1, top (8-way):** 1 +supply · 2 drops to 0 on Start/Stop · 3 display frequency, switches between motor tach and demand · 4 1/10 Hz display refresh clock · 5 LED signal · 6 duplicate of 4 · 7 speed reference 10–999 Hz set by main pot · 8 GND
*Source note: pin 3 runs at a much higher frequency when showing demand and not running.*

**Board 2 (14-way):** 1 +supply · 2 **1.048 MHz clock** · 3 – · 4 – · 5 pulse high on Start/Stop · 6 drops to 0 on Start/Stop · 7 return for 33.3 select · 8 display frequency · 9 inverted tach · 10 display refresh clock · 11 **fixed 33.3 × 40 = 1332 Hz** · 12 −supply · 13 duplicate of 10 · 14 GND

**Board 3, middle (9-way):** 1 +supply · 2 – · 3 – · 4 pulse high on Start/Stop, 0→10 V · 5 **pot frequency × 4, 40–3996 Hz**, 0→10 V · 6 **???** · 7 speed signal · 8 −supply · 9 GND

**Board 4, near bottom (9-way):** 1 +supply · 2 1.048 MHz, 0→10 V · 3 return from 33.3 select · 4 inverted tach, 0→10 V · 5 tach, 0→−10 V · 6 **???** · 7 −supply · 8 GND · 9 speed reference 10–999 Hz

**Board 5, power (9-way):** 1 33.3 indicator, **9.18 V** selected / 0 not · 2 +supply **11.9 V** · 3 return from 33.3 select, freq = pin 4 or pin 7, 0→10 V · 4 **pot 0.1–99.9 × 40 = 4–3996 Hz**, 0→10 V · 5 tach, 0→−10 V · 6 **speed signal, 0→5 V** · 7 fixed 1332 Hz, 0→10 V · 8 −supply **−10.9 V** · 9 GND

**Motor DIN, brushless DC motor:** Run/Stop · V Speed · PG OUT · AGND · PGND · Vin — **no voltages given for any of the six.**

### 2.4 Frequencies and rails

- Crystal reference **1.048 MHz** — appears in prose and independently on two boards' pin tables
- Fixed 33.3 lock reference **1332 Hz** (33.3 × 40)
- Pot demand expressed two ways: **×10** (10–999 Hz) and **×40** (4–3996 Hz)
- Tower rails **+11.9 V / −10.9 V**; logic swings 0→10 V; tach 0→−10 V; **speed signal 0→5 V**
- Motor PCB rails **±15 V**, −10 V reference
- Quoted spec `[SITE]`: 10–99.9 rpm variable, 33.3 quartz lock, 10 ppm

### 2.5 Mechanical `[2nd]` unless marked

- **Bearing:** ground stainless spindle in a phosphor-bronze bush, matched pair, **0.004″ clearance**, clock/watch oil `[SITE]` — corroborated independently by Hobden via Simon Y
- **Lubricant:** chosen by **Leicester University Department of Tribology**; watch oil, originally sperm-whale derived; Ira also approached **BP Advance Fluids** about space-programme oils. Nigel's stated reason: anything else introduces rumble; watch oil doesn't oxidise and stays put
- **Motor suspension:** samarium-cobalt magnets in repulsion inside a **5 mm Swedish soft-iron cylinder** to keep the field off the cartridge `[SITE]`
- **Suspension foam:** **C.B. Frost Ltd, Birmingham**; Gale selected by trial and error from samples. Correct foam in good condition should mean no wobble. Ira considered and rejected silicone damping
- **Suspension height:** top tri-plexi should sit **midpoint between the upper and lower metal parts of the tower**
- **Encoder:** 600-line glass disc, described as rotating between an electro-optic reading assembly; accessed through an opening at the bottom of the motor windings. A **photograph of a shattered disc** is in the archive with a shipping warning

---

## 3. Findings that bear directly on the work

⚠ **Re-headed 4 September 2026.** These were written against the numbered steps 3 to 8 of a
separate bench-order note, **which no longer exists** — the work is now grouped in
[`project-memory.md`](/GT2101/project-notes/project-memory/) § NEXT by what each job needs
rather than by step number. The findings below are unchanged; only their labels were tied to
something that has gone.

**Refitting the original boards — the "most important unknown" is answered from documents.**
Howie's own account: the new PCBs were **already on order** — "the new pcb's are still on order from the supplier, but some of the new modern ESC bits and pieces have arrived" — and only then, "**in the meantime**, one of the guys found an interesting flaw in the flexible 'strap'." The rebuild was a project decision ahead of any board failure, driven by faster sampling, replaceable parts, and a wanted feature (perspex dial stepping 33.3→45→78 on the lock button). He intended to **"keep the original and now working parts as backup."** After the strap repair the originals ran: "hey presto …. it works … dial speed on the led, touch the top to rotate."
**Reading: Level A is live, not dead on arrival.** `[1st]`

**Running the deck original — the pass criterion may be softer than it looks.** Simon Y, Gale audio Google group, **21 Dec 2010**, relaying Nigel Hobden: the deck has "fluctuating speed which according to Nigel and one other person is an **inherent issue due to the configuration of the circuitry**." If that holds, a deck that doesn't lock perfectly is not necessarily faulty. Counter-evidence in the same thread: **John Mayberry, 23 Dec 2010** — "No, I've had no electronic issues. It has always turned on/off and adjusted to speed quickly." `[2nd]` / `[1st]`

**Running the deck original — a known prior failure mode on a repaired flexicon.** Howie's team fitted a replacement flex strap; the deck ran but with "**really jerky**" rotation. "The cro shows the signal is being turned on and off repeatedly by something and **we don't know what**." **They never diagnosed it and the record stops there.** If you see that behaviour it is precedent, not a new fault. `[1st]`

**The tacho — ⚠ this paragraph's conclusion was withdrawn, and it is kept for its reasoning.**

*As written, 28 August:* the fixed reference is **1332 Hz at 33⅓ rpm**. 33⅓ rpm = 0.5556 rev/s,
so 1332 Hz implies **2400 pulses/rev** — 600 lines × 4, i.e. quadrature. Boards 2 and 4 both
carry dividers (MC14521, MC14520), so a division may sit between disc and comparison.
*"Go in expecting 1332 Hz and be surprised by 333 Hz, not the reverse."*

⚠⚠ **The 2400 figure is withdrawn.**
[`project-memory.md`](/GT2101/project-notes/project-memory/) settles it: **~600 ppr, not 60 and
not 2400.** Board 4's 4046 locks the tacho to `1×F` with **no divider in the loop**, so the
tacho runs at 10 Hz per rpm — **333 Hz at 33⅓**. This figure has now been wrong twice, once low
and once high, each time by assuming the wrong reference frequency.

⭐ **But the arithmetic above is not wrong — it is measuring a different point.** Both
frequencies are real. **1332 Hz is genuine and sits *upstream* of board 4's ÷4**; 1332 ÷ 4 = 333.
A 600-line disc read in quadrature gives 2400 edges at the disc, of which the tower's loop uses
600. **So if a probe reads 1332 Hz, you have landed upstream of the divider — not disproved the
600.** That reconciliation is why this paragraph is kept rather than deleted.

**The drive ceiling — an independent number.** Board 5 pin 6 puts the **speed signal at 0→5 V**, not 0→10 V. Consistent with your measured 2.4 V figure and a ceiling well below 10 V.

**The drive gate — a second one exists.** The motor PCB has its own JFET shunt gating on all three phases off SPEED IN, separate from board 3's still-gate. Worth knowing before attributing gate behaviour to board 3 alone.

**The touch wire — nothing new, one caution.** The folder's board 2 table gives pins 5 and 6 as "pulse high on Start/Stop" and "drops to 0 on Start/Stop" with **no voltages**. It does not corroborate your 0→+10 V / 0→−10 V adjacency. Meter before iron, as planned.

---

## 4. Live technical contradictions

**4.1 Motor manufacturer.** `[SITE]` "made by Inland in the USA" · `[SITE]` elsewhere on the same page "adapted from one of the **Inland/Litton Industries (we're tracking it down)** designs used for shipboard gyros" · `[1st]` **Paul Ramsden**, DCA: "**I think** the motors came in as finished units from **Litton Industries** – we had nothing to do with the insides."
Ramsden is the cleanest witness — British, at DCA, no US narrative to serve — but he hedges and speaks only for what arrived at DCA. **Unresolved.**

**4.2 Were the motors ever opened?** `[1st]` Ramsden: "finished units … **we had nothing to do with the insides**." · `[2nd]` Nigel Hobden via Simon Y: "they used a **special clamp when they opened up the motors**. This ensured along with a **special spacer** so that gap could set correctly **between each head**. Knowing the distance was critical. **Each one was set individually?**"
Both can be true if the opening happened **at Gale in London**, not at DCA in Warwick — which would mean in-house work on the motor internals, exactly what the US-origin framing flattens. Simon Y flags his own uncertainty. **This is the single most valuable claim to put back to Hobden verbatim.**

**4.3 Encoder attribution.** The site credits the **motor to Inland** and the **600-line disc to Litton** — two vendors for one assembly, no source for either. Nobody first-hand confirms who made the disc.

**4.4 Rumble.** `[SITE]` "Rumble is zero because there is no mechanical contact surface" · `[1st]` **John Daly**, DCA Design Director, email 1 June 2006: "In the end the turntable was too expensive and **I think it suffered from too much rumble** compared to other high end turntables that were around at the time." **Testable on the bench.**

**4.5 "Top circuit board added by Gale."** A site photo caption — Mayberry conceding that part of the motor assembly is Gale's own work. Consistent with the motor PCB tracing being a 1970s discrete design rather than an OEM sealed unit.

---

## 5. Open questions the folder does not answer

- Which company actually made the motor, and whether the assembly was substantially finished in London
- Whether the disc carries **only** the fine tach track, or **also** the three-phase commutation pattern. The motor PCB has four channels (TACH + three sensors) but the schematic cannot distinguish optical pickups from Hall devices. **Answerable by looking, and it changes any disc-copy spec from one track to two in fixed angular registration**
- Any disc geometry at all: OD, hub bore, track radius, line/space ratio, index mark, glass thickness, chrome side. "600 line" is the only published number and it is unsourced
- Motor DIN voltages — six functions named, none characterised
- Board 3 pin 6 and board 4 pin 6, both marked "???" in the source
- What caused the jerky rotation reported after that strap replacement
- Attribution of the ribbon pin tables — uncredited on the page
- Any GT2101 patent number. The Sao Win / Ira Gale shared-patent claim carries no number anywhere. (The only patent number in the folder is EP0128672, Ira Gale with Michael Shain, computer protection — unrelated)
- Whether original towers were ever replaced in period. Only the one modern rebuild is documented

---

## 6. Leads — people

| Person | Why they matter | Last seen |
|---|---|---|
| **Nigel Hobden** | Origin of the "motors were opened, clamp and spacer, head gap set individually" claim, and of "speed fluctuation is inherent to the circuitry". Everything from him is second-hand via Simon Y. Reported to have **found drawings of the turntable but not opened them**. The highest-value contact in the project | Answering questions via Simon Y, 2010–2012; Lucy Bartlett still in touch Jan 2012 |
| **"Jules"** | **The strongest living first-hand source on the motor question.** At Gale 1974–77; moved "upstairs to build the decks and the deck control units", worked in a dust-free chamber, "calibrating the speeds of the deck using a scope to tweak the crystal". He saw what arrived from America and what was done to it in Bruton Place. No stake in either origin narrative. Surname not given; corresponded with Mayberry | Letter to Mayberry, undated; photographer by trade |
| **"Simon Y"** | Intermediary to Hobden; supplied the `SY_*.jpg` photos in your folder; offered "If we have any more questions I can bundle them up" | 2010–2012 |
| **"Howie"** | Australian owner who restored a GT2101 with a university student team. **Kept as a source, not as a subject** — the IC lists, the flex-strap discovery, the account that the original boards still ran, and the undiagnosed jerky rotation all come from him. The replacement controller he had made is out of scope | Active 2015 |
| **Paul Ramsden** | DCA electronics group. First-hand on the control system and on what DCA did and did not touch. Named **Steve Twitchet** as the man who hand-taped the circular board layouts | Statement solicited and given, undated |
| **"fanatson" (Markus)** | Posts Jan/Feb 2012 as a 401A owner in **A-6020 Innsbruck, Austria**. Same handle as your 2015 FANATSON tracings — and the motor PCB sheet is signed FANATSON 10.9.2015. If it is him, he is the one person who could settle the two-numbering-systems problem directly. **Handle match only; not established** | 2012 |
| **Huub Bouwmeester** | Netherlands. Obtained and preserved the John Daly email; identified the prototype photo by writing to Freivokh directly. Good at getting answers out of people | 2012 |
| **Lucy Bartlett** | Not technical, but in **January 2012 was still in touch with Ray Churchouse, Ian Dampney, Nigel Hobden and David Lyth**. The routing hub | Jan 2012 |
| **Mark Brumby** | Posted the LP12 motor substitution in the Gale audio group, Dec 2010. Knows the deck physically | Dec 2010 |
| **Dr Sao Win** | Shares the (unnumbered) patents; his own machine is claimed by Robin Wyatt of Robyatt Audio | Mayberry spoke with him "a few months" before Sep 2016; retired, Santa Barbara area |

**Ruled out:** David Lyth — speakers only, left before the GT2101.

---

## 7. Leads — documents and objects said to exist

- **Drawings held by Nigel Hobden**, found but unopened as of the Simon Y correspondence. Never described. The most valuable unopened item in the project
- **Wiring diagrams** — Hobden via Simon Y: "may turn up", with the caveat that some parts were custom made
- **A single-sheet GT2101 sales brochure**, printed both sides — **Mark**, 19 Jul 2012, offered a scan. Not in the folder
- **A factory brochure** cited by the site for the "SME 3009 Type II or no arm" spec. Not in the folder
- **Original transparencies** from the *Hi-Fi News & Record Review* article — offered by its author **Adrian Newitt**, 18 Mar 2014, who also complained the site used his material without tracing him. He was ex-DCA and knew editor Steve Harris

**Absent from the folder despite being linked:** all six interview recordings — five Bonnie Gale `.wma` segments and `Ray-Churchouse-Interview-Edited.wav`. The mirror captured the pages, not the media. Exact filenames are recoverable from the page source if any snapshot of the site survives elsewhere.

---

## 8. Suppliers — for the parts that cannot be bought

**Encoder disc.** Custom chrome-on-glass discs are still routine one-off work:

- **Max Levy Autograph** (Philadelphia, now Coherent Aerospace & Defense) — precision encoder scales, **disks and reading reticles**. The reticle matters: your disc rotates *between* a reading assembly
- **Photo Solutions** — custom encoder discs in glass, mylar and aluminium, low volume
- **Optry** (China) — cheaper custom glass code discs

The obstacle is the **specification**, not the manufacture. See §5 — no disc geometry exists anywhere in the archive. **Documenting the disc while it is intact is the highest-value insurance action available**, and there is already a photograph of a shattered one.

**Motor.** No like-for-like exists. The assembly is rotor, stator, integral encoder, samarium-cobalt thrust bearing and the platter interface — the bearing is part of the motor. Options, ranked:

1. **Repair the motor PCB.** The commutation electronics are *outside* the motor and every device on that board is obtainable or substitutable — and you now have the tracing. Much of what would present as a dead motor is board-side. The documented prior restoration took this route and kept motor and encoder original
2. **Re-make the disc** (above)
3. **Rewind the stator** — preserves bearing and geometry
4. **Frameless direct-drive substitute into the existing bearing.** Kollmorgen *is* Inland Motor Division, Radford VA; the modern **RBE** frameless series is the lineal descendant — rotor and stator only, built into your own bearing, commutated by the Pico. Surplus units appear regularly. Blocked as a like-for-like by §4.1: no OEM part number is known, so there is nothing to search NOS stock against
5. **Donor deck.** 60–200 built, 15 located. Whole decks only, at deck prices
6. **LP12 motor** — Mark Brumby, Dec 2010: "you have to get the sub platter turned down a little, about 1.5 mm IIRC." Be clear what this is: an AC synchronous belt-drive **conversion**. It abandons the direct drive, the servo and the encoder. It gets a dead deck spinning and nothing more

---

## 9. What the folder is, in one line

An offline mirror of galeaudio.com stored three times over (`gale website\`, `turntable v2\` — verified byte-identical — and `galeaudio.com\`), plus the FANATSON tracing PDFs and their JPEG renders, board photographs, and six short typed board-summary PDFs dated 3 Nov 2025 which are recent working notes, not period documents. The schematic PDFs are image-only and return no text; the `jpg\` renders can be read directly.
