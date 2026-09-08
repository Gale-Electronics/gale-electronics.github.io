---
layout: bare
title: "GT2101 — Corrections Log"
permalink: /GT2101/project-notes/corrections-log/
description: "Every withdrawn claim, superseded value and corrected mistake in the GT2101 archive, with the date and the reason — kept out of the working notes so those can state what is true now."
---

*A working note — part of the GT2101 project's live record. The polished write-ups live in
[Technical Notes](/GT2101/technical-notes/).*

---

# GT2101 — corrections log

**Opened 6 September 2026.** The working notes had reached the point where the corrections
were louder than the facts: a reader could not tell what was true now without reading the
history of everything that had once been believed. **This file is where that history lives.**

## The rule this file exists to serve

> **The notes say what is true. This file says what we used to think and why we stopped.**

What stays in the working notes:

- **Guard rails** — anything that stops a wrong action at the moment you would take it.
  ☠ row 2 pad 5 never pad 6 · sheets 3C and 3D are mirrored · rows 3 and 4 do not share a
  pinout · not a MOSFET · solder to the brass staple never a pad · never drive board 1's
  pin 10 · do not disturb the Helipot's brass nut. **These are not history, they are safety.**
- **Negative facts that prevent a rebuild of a wrong thing** — "not X, it is Y" in one line,
  with the story here.
- **The ✅ 📄 ❓ provenance markers.** They are the discipline, not clutter.

What moves here: withdrawn alarms, superseded values, audit trails, and every sentence of the
form *"this section previously read…"*.

⚠ **Nothing is deleted from the archive by this file's existence.** If a fact was removed from
a working note and is not recorded here, that is a bug — see § verification at the end.

⚠⚠ **The pre-tidy state is in git.** Everything below can be read in full in the repository
history at the commit before 6 September 2026.

---

## 1. The remove-the-boards plan — WITHDRAWN 29 August 2026

**The single most damaging wrong idea in the project's history, because it kept coming back.**

An early architecture removed **boards 3 and 4** and put the Pico in a vacated slot. It was
withdrawn in full on 29 August 2026: **all five boards stay.** But the withdrawal landed only
in the files being edited that day, and passages reasoning from "with board 3 out" survived in
other files for another week.

| Where it survived | What it said | Found |
|---|---|---|
| `project-memory.md` | *"with Board 3 out, firmware is the only thing holding `V_IDLE` there… the case that cooks the BD675A/676A"* | 4 Sept |
| `parts-to-order.md` | board 3 *"out of the architecture"*; board 4 *"leaves with Board 3"*; the J113 needed because board 4's E113 *"goes out with the board"* | 5 Sept |
| `board-2-touch.md` | *"With Board 3 removed, pin 5 drives nothing… Board 3's departure frees the exact signal the Pico wants"* | 5 Sept |
| `board-3-fvar-gate.md` | *"with Board 3 out of the architecture, that protection leaves with it"* — called the single biggest risk of the build | 5 Sept |

⭐ **The lesson, and it is the one this archive keeps relearning:** *a correction lands in the
file being edited, not in the files that repeat the claim.* **After correcting anything, grep
the whole folder for the old claim.**

⭐ **The J113 is still required and the quantity is unchanged** — only the reason was wrong.
Board 4 stays, so its E113 tacho front-end stays with it, but that front-end feeds board 4's
own PLL. The Pico taps `TACH` in parallel at the backplane and needs a front-end of its own.

---

## 2. `V_IDLE` — "STILL = 10 V" was a misread, not a gap

**Settled 29 August 2026; the account of *why* was itself corrected on 5 September 2026.**

`V_IDLE` is **0 V, not 10 V.** Board 4's loop rails to maximum demand at rest and board 3's
gate mutes it. The drive table's home is
[`board-3-fvar-gate.md`](/GT2101/project-notes/board-3-fvar-gate/) §4.

⚠⚠ **The archive had written itself a false account of its own mistake.** Several files said
*"the backplane sheet only ever recorded one column, and it was the input one."* Read at
400 dpi on 5 September, `motor-overview/backplane.pdf` records **both columns side by side**,
and the second reads **`STILL: 0 V`** in the tracer's own hand.

⭐ **So it was never a gap in the source. It was a misreading of a source that had both
numbers on it.** A missing column is bad luck; a misread column is a habit. The drive table is
now recorded in **four** independent places, all agreeing.

---

## 3. Board 1's display timebase alarm — RAISED AND WITHDRAWN, 5 September 2026

**Raised in the morning, withdrawn the same day by the audit that read sheet 1A properly.
Kept in full because the failure is more instructive than the fact.**

**What the alarm said.** `F REF` sets the count window and `F DISPLAY` is counted, so if both
scale with speed the display would read the same number at every speed. Therefore board 1's
timebase must be fixed and crystal-derived, and the two archive sources calling board 1 pad 7
speed-proportional — the backplane sheet's `F REF ×1`, and `folder-findings.md` §2.3's
*"10–999 Hz set by main pot"* — must **both** be mis-recorded.

⭐ **The premise was false.** `F REF` does **not** set the count window. The **gate** line on
pad 4 does, holding the 4013 in reset through **4001 D** for as long as the window is open —
a gate no version of the page had ever mentioned. `F REF` only runs the latch–hold–reset–hold
housekeeping lap *after* the window closes. The two are not in the same equation at all.

| | at 33⅓ rpm |
|---|---|
| `F DISPLAY` | 1332 Hz |
| gate window | 250 ms open → count = 333 → reads `33.3` |
| `F REF` | ~333 Hz (`×1`) → the four-pulse lap takes ~12 ms, comfortably inside the closed part |
| gate repetition | ~1 Hz — the display refreshes about once a second, which is what the tracer's "1Hz?" described |

**Both archive sources were right, the tracer was right, and §5's fallback plan was never in
danger.** 📄 A third source that would have killed the alarm was sitting unread:
`folder-findings.md` §2.3 calls pad 4 the *"1/10 Hz display refresh clock"* and pad 7 the
*"speed reference 10–999 Hz"* — exactly the arrangement sheet 1A draws.

⚠⚠ **The lesson.** The alarm was raised from **a sentence in the notes**, not from the
drawing, and a third source that contradicted it was never opened. **Before declaring that the
archive contradicts itself, re-read the primary drawing and grep the archive for the same
pad.**

⚠ **One live disagreement survives from that transcription** and is *not* resolved: it calls
board 1 pad **6** a *"duplicate of 4"*, where sheet 1A is unambiguous that it is `RESET` out to
PCB 2 (4001 pin 10 → pad 6). **The sheet wins, but the two records disagree.**

---

## 4. The Pico's supply — there is no DC-DC converter

**Corrected 4 September 2026.** Three repo documents said the Pico's supply was a DC-DC
converter that had *"retired the LM7805"*. Matt said it was the LM7805, and he was told on the
strength of the notes that he had the part name wrong. **He did not.**

**What had actually changed on 3 September was the regulator's *input*** — from the +15 V
reservoir to the +10 V backplane rail — and someone had written that up as a different part.

⭐ **The distinction to hold:** he does misremember component names recalled in the abstract
(an LM7805 once became a "step-down"), **but believe him about the part in his hand.**
Correcting a person from a document is how a wrong document survives.

⚠ **A second error rode on the first.** The switching-noise concern was briefly closed on the
grounds that "the LM7805 is linear, so there is no switching". **Wrong twice over:** the Pico
carries its own buck-boost converter on VSYS, and Howie's tower is direct evidence that a
microcontroller inside a GT2101 tower can be audible. **The concern is reopened and stands.**

---

## 5. The motor PCB — LM324 and LM339 were the wrong way round

**Corrected 5 September 2026** against `motSchem.pdf` at 400 dpi.

The page had the position sensors feeding **LM324** stages with 470 kΩ feedback, and a
separate **LM339** squaring the tacho. The sheet shows the opposite:

- **LM339 quad comparator, all four sections.** Three take the position sensors `GREEN`,
  `YELLOW`, `VIOLET`, each with **470 kΩ from output to the + input** — positive feedback,
  i.e. hysteresis, which is what squaring wants. The fourth is the **tacho** comparator.
- **LM324 quad op-amp, three sections**, *after* the gating network, each driving an output
  pair through 560 Ω. The fourth is drawn `NC` — a spare op-amp on the board.

The 470 kΩ figure was right; it just belongs to the LM339.

⚠ **A ❓ that moved.** *"Tacho reference derived from the motor's own winding"* — the sheet
does not draw that. The tacho comparator takes a wire labelled **`BROWN`**; the three winding
pairs terminate at the output stages and go nowhere near it.

---

## 6. The tacho figure — wrong twice, each time by a factor of ten

**~600 pulses per platter revolution**, i.e. ~333 Hz at 33⅓ rpm, i.e. 10 Hz per rpm.

- **60/rev** — inferred from the assumption that the PLL reference was the ×40 frequency. It
  is the ×10 frequency. Ten times out.
- **2400/rev** — the same error in the other direction.

⚠ **Still 📄, not ✅.** `bench.tacho()` settles it in five minutes and nothing else in the
project changes the answer.

---

## 7. The touch divider — 22k/10k is superseded

**Corrected 4 September 2026.** The divider for board 2 pin 5's 0 → +10 V pulse into a GPIO is
**27 kΩ + 10 kΩ, with 1 kΩ in series at the Pico end.** 27k/10k gives 2.70 V from a 10 V rail;
**22k/10k gives 3.13 V, which works but leaves almost no margin.**

⚠ The old figure stood in two places at once, which is how it survived.

---

## 8. The tacho level shifter — three wrong answers before the right one

The tacho swings **0 V to −10 V**, so it needs an **N-channel JFET (J113)**, gate to `TACH`,
source to GND, drain pulled to 3V3 through 10 kΩ.

| Wrong answer | Why it cannot work |
|---|---|
| A resistor divider | Dividing −10 V gives a smaller *negative* voltage, still below ground and straight into the Pico's clamp diode |
| A MOSFET (2N7000/BS170) | Needs a **positive** gate. With a signal that only sits at 0 V or −10 V it is off in both states |
| The PNP circuit in the old notes — *"22k base series, 100k to GND, emitter 3V3"* | The base is below the emitter at **both** tacho levels, so the PNP conducts always and the output sits high permanently |

⭐ **This is Gale's own circuit.** An E113 in exactly this configuration is board 4's tacho
front-end, and sheet 3A records a defective E113 *"replaced by J113 (RS Components)"*.

---

## 9. Board 2 — the timing chain was attributed to the wrong chip

**Corrected 5 September 2026.** The page said the display gate came from *"the 4040's Q21 and
Q19"*. The 4040 is a 12-stage counter and **has no Q21**. `Q21` and `Q19` are on the
**MC14521** 24-stage divider, clocked by the 1.048711 MHz crystal signal arriving on pin 2
from PCB 4.

⭐ **The arithmetic is what settled it, beyond argument:**

| | |
|---|---|
| 1 048 711 Hz ÷ 2²¹ | **0.4999 Hz** — the sheet's `Q21 = 0.5 Hz` |
| 1 048 711 Hz ÷ 2¹⁹ | **2.000 Hz** — the sheet's `Q19 = 2 Hz` |

Board 1's `RESET` output likewise resets the **MC14521**, not the 4040.

⭐ **Arithmetic is the strongest evidence available on a hand-traced sheet.** It proved a chip
identity that pencil could not.

⚠ **`(= 333 × 40)` was the page's own transcription error, not the tracer's.** The layout
footer reads `= 33,3 × 40`, which is correct: 33.3 × 40 = 1332.

---

## 10. Board 3 — two pins were called "unnamed" and are not

**Corrected 5 September 2026.** Board 3's connector pins 2 and 3 were listed as *"unnamed on
the drawing"*. They are named — on **sheet 3C** rather than on the layout, which is where the
table had been built from. They are the LM3900 window comparator's `OUT 2` (its pin 4 → pad 2)
and `OUT 1` (its pin 5 → pad 3), annotated `STILL` / `TURNING`.

⚠ **Which state is the high one is still 📄 with a question mark** — the pencil `+` and `≠`
marks do not read cleanly even at 400 dpi. One meter reading on pads 2 and 3, platter stopped
then turning, would close it.

---

## 11. The XR2207's control voltage — "via Board 2" was an assumption

**Corrected 6 September 2026.** `board-3-fvar-gate.md` §6 asked what drove the XR2207's control
voltage, answered *"presumably the Helipot via Board 2"*, and then dismissed the question as
moot because the Helipot now goes to the Pico. `pico-controller-notes.md` repeated it.

📄 **Sheet 3B draws an `ORANGE` post** on board 3, through a resistor, into the XR2207's
control input. **The Helipot fed the VCO directly, by a flying lead onto board 3** — it was
never on board 2's circuit, which is why it could be found "electrically off board 2" without
anything having been disconnected.

⭐ **The consequence is live, not historical:** that control input is now open, and what the
XR2207 does with an open input is the one unknown the `F VAR` injection plan turns on.
✅ **Answered 6 September** (parked at 0.05 V) and **explained 8 September** (§17 — pin 6 is the
only timing terminal, so an open post means zero timing current).

⚠⚠ **And this section is itself incomplete.** *"Into the XR2207's control input"* is half of what
the post does. **See §17.**

⚠ **A wrong wiring instruction was given in conversation before the sheets were read** — to
lift the series resistor `R` between the XR2207 and the 4011. **That would make things worse.**
`R` is on the *input* side of the 4011, so lifting it floats a CMOS input and leaves the 4011
still driving pin 5. **The break, if one is needed, is XR2207 pin 13.** Same failure as always:
reasoning from the connector table instead of opening the sheet.

---

## 12. The green LED — what it is, and two claims that were wrong about it

**Settled 3 September 2026.** It is the **33⅓ / FIX indicator**. The **black switch** grounds
it. Board 5 has no circuitry on pin 1, and `Board-5-Schem.pdf` does not show the pin at all.

| Wrong claim | Correction |
|---|---|
| *"Board 5 may drive the net to 9.18 V and the Pico would be fighting an output"* | `folder-findings.md`'s *"9.18 V selected / 0 not"* has its states **reversed**: ~9 V is LED **off** (board 1's own pull-up read back through the LED), 0 V is **on**. A passive switch and an open-drain GPIO are both sinks — no contention |
| *"No driver transistor needed"* | True on the 5 V bench, **false at 10 V** — and the difference is the *off* state. At 10 V the pin is pulled toward 8 V through 1 kΩ and the Pico's clamp diode conducts continuously. **The low-side NPN is required** |
| *"What it should indicate is open"* | Gale already decided. The open question is whether to **override** a working original function — a decision about the project's principle, not a wiring question. And with the switch in FIX the Pico can turn it **on but not off** |

---

## 13. The inherited prose pages — six checked, five wrong

**Complete 5 September 2026.** The typed prose pages from the defunct website are
**non-evidence**. Prefer the FANATSON tracings and the hardware.

| Page | Verdict |
|---|---|
| `Disk-3-Optical-Sensor.pdf` | ❌ Calls board 3 an "Optical Sensor / Tachometer Processor". There is no photodiode or encoder input anywhere in the tower. Its **chip list is right**; only the function is invented |
| `Disk-2A-Servo-Control.pdf` | ❌ Lists two chips that are not on the board, omits four that are, puts the PLL on the wrong board, and **never mentions the touch sensor** — the board's most distinctive circuit |
| `Disk-2B-Power-Driver.pdf` | ❌ Describes the **motor controller PCB**, not a tower board. Misfiled. ⭐ This is where the "is disk 2 one board or two?" confusion came from — it is **one** board, and 2A/2B are two sheets of it |
| `Board-1-Display-Logic-Interface.pdf` | ❌ Calls the MC14001 an "OR gate" and the MC14011 an "AND gate". A Canva summary from November 2025, not a drawing |
| `Disk 4 — Reference Oscillator.pdf` | ❌ |
| `Disk-5-Power-Supply.pdf` | ✅ **The exception, and broadly holds** — board 5 is the one board whose function you *can* guess from its parts list |

⭐ **The pattern:** these read like **function guessed from a parts list by someone who never
had the board**, and they share errors with the galeaudio.com parts list, which is probably
where they came from.

⚠ **The tally was "four for four" in five files** until the set was completed; all five were
corrected on 5 September.

---

## 14. Smaller corrections

| Subject | Was | Is |
|---|---|---|
| The tinted disc | *"the clear disc"*, twice | **Smoke-tinted.** The red comes from the LEDs behind it. ⚠ Matters for any display-overlay idea: a neutral tint gives density but no colour |
| Boards 2 and 3 | A description inherited from the defunct website | **Boards 3 and 4 are one servo split across two boards** — 4 decides the drive voltage, 3 decides whether it is allowed out |
| The Helipot | Assumed to be on board 2's circuit | **Electrically off board 2.** All three leads go to the Pico; board 2 is its bracket, held by a brass nut and washer |
| Helipot turn count | Unknown; a partial sweep read as a dead pot | **Ten turns**, full ADC span 160–65535. A reading stuck low is an unfinished turn, not a broken wire |
| Board 5's green-LED question | *"This does not clear Board 5"* | Cleared — metered end to end in bench session 8 |
| Auto-lock resistor | Quoted as if 100 kΩ were a requirement | **Anything from ~47 kΩ to 470 kΩ.** It only limits current into the Pico's clamp diode. **Check the drawer before ordering** |
| The LM358's supply | +15 V in one file, +10 V in another | **+10 V, off the backplane.** +15 V would mean a wire across the deck to the reservoir — the exact thing the 3 September supply change removed |
| `§ LIVE MONITOR` | Pointed at by `parts-to-order.md` | **No such section has ever existed.** The web monitor has never been specified anywhere in the repo |
| Two towers | Every document assumed one deck, one tower | **Two.** Howie's on the deck, Alex's on the bench |
| Howie | An anonymous previous owner | ⭐ **Already a documented source in this archive** — `folder-findings.md` records him, and the tower Matt runs is that project's output |

---

## 15. Documents deleted, and what was rescued first

**4 September 2026:** `backplane-signal-map.md`, `next-steps-bench-order.md`,
`fresh-eyes-brief.md`, `working-practice.md`, `GT2101_interview_extraction_1.md`.

⚠⚠ **Before deleting anything, grep for its unique strings.** Four times a file that looked
like a duplicate held something that existed nowhere else. **Orphaned and duplicated look
identical from a distance.**

- `mechanical-and-suspension.md` was deleted by a de-duplication pass and **had to be
  restored** — it was not a duplicate.
- The smoke-tinted disc finding survived only in the fresh-eyes brief.
- The four open challenges in `project-memory.md` were rescued from the same file.

⚠ **Tidying can promote something that was better left buried.** `working-practice.md` was
extracted from the bottom of `project-memory.md`, where nobody would find it, into its own page
with its own URL — making it far more prominent than it had ever been. **Be careful what gets
published about a person while tidying.**

✅ `motor-overview/motor-findings.md` — a saved copy of a published page carrying its own third
confidence scheme — was **retired 5 September 2026**, replaced by a stub pointing at the
canonical page, after a sentence-by-sentence comparison confirmed the live page had lost
nothing.

---

## 16. Filenames that rotted

⚠ **Check before citing.** Board 1's drawings folder was renamed, board 2's half-renamed,
board 3's untouched, board 5 cited as `5Schem.pdf`, board 4's Disk PDF carries spaces and an
em dash. The old `GaleTT1*.pdf` names are dead links.

⚠ **Duplicates hide behind names.** `flexicon-connector/` holds two byte-identical pairs —
`raymon.jpeg` ≡ `remora.jpeg` (a person's name implying a provenance it does not have) and
`IMG_0275.jpeg` ≡ `top-pico-mount-front.jpeg` — plus `flexicon-1.2` with no extension. **Check
image duplicates by content, not by name.**

---

## 17. The `ORANGE` post, and where `F VAR` goes — 8 September 2026

**Matt asked for the `F VAR` injection to be double-checked before it is made permanent.** All
four board 3 sheets and `motor-overview/backplane.pdf` were re-read at 350–400 dpi.
⭐ **The injection itself came out sound, and better evidenced than before** — see
`pico-controller-notes.md` § `F VAR`. Two other things did not.

### ⚠⚠ 17a. "The `ORANGE` post is the XR2207's control voltage" — true but incomplete

| What every note said | What the sheets show |
|---|---|
| The `ORANGE` post feeds the XR2207's control input. Full stop. | It feeds **two** things: the XR2207's **pin 6** through a resistor (DC, the frequency control) **and** the **LM308's pin 3** through a capacitor (AC). 📄 Sheet 3A labels that second wire `ORANGE POST` in the tracer's own hand; sheet 3B draws it too |

📄 **And sheet 3C, top left, in block capitals: `FROM LM308 PIN 6`** → the LM3900's `1+ IN` and
`2− IN`, whose outputs are **`2 OUT` → pad 2** and **`1 OUT` → pad 3** — the STILL/TURNING lines
to board 2. **So those pads trace back to a post Remora has left open.**

⭐ **The motor is not affected and this is not an alarm.** The drive gate runs off the LM3900's
*other* pair, amplifiers 3 and 4, which sense the pad 7 net (`IN 3−`, verified on 3C). The mute,
the latch and `V_IDLE = 0 V` are all untouched.

⚠ **What may be affected is board 2's display mux**, and the symptom is specific: a display
reading about **4× out**. Full statement and the two meter readings that close it are in
`board-3-fvar-gate.md` §2a — **kept in the working note, not here, because it is a live guard
rail on a test that has not been run yet.**

⚠⚠ **This one is not fully settled and is not written up as if it were.** A DC pot wiper through
a series capacitor into an amplifier is not a plausible motion detector. The drawing says what it
says; the bench has not spoken.

### ⚠⚠ 17b. `F VAR` does not go to board 2

**Corrected in two files.** `board-3-fvar-gate.md` §3 and `flexicon-backplane-map.md` §5 both
gave board 3 pad 5 as *"out → board 2"*, and the flexicon's merged signal chain drew
`F VAR ──► Board 2 ──► ×40 ──► Board 5`.

📄 `motor-overview/backplane.pdf` draws row 3 pad 5 — labelled **`VAR`** — running **straight
down to row 5 pad 4**, past row 4 with no pad. **There is no `×40` stage anywhere**; `F VAR`
leaves board 3 already at 40 Hz per rpm. The same sheet also sent the Helipot through board 2,
which §11 had already corrected.

⭐ **Board 2's own 14-pin map was the tell all along — it has no `F VAR` input.** The claim
survived because nobody read the two tables against each other.

⭐ **What the sheet gives back for free:** **board 5 pad 3, board 4 pad 3 and board 2 pad 7 are
one net** — the switch-selected demand, feeding the servo and the display together. That closes
the question of how board 2 pad 7 is driven when row 4 has no spare pad for it.

✅ **Nothing built is affected.** The 1333 Hz figure is confirmed twice more on that same sheet
in pencil — `3996 Hz (×40)` at row 5 pad 4 and `1332 Hz` FIX at pad 7.

⚠ **The lesson, and it is [`archive-provenance.md`](/GT2101/project-notes/archive-provenance/)'s
lesson again:** a direction in a connector table is a *claim*, and the cheapest way to test it is
to look for the matching entry at the other end. **Two of the five per-board tables disagreed for
three weeks and nobody put them side by side.**

---

## Verification — 6 September 2026

Every fact removed from a working note during the 6 September tidy is recorded above. The
pre-tidy text of all twelve files is in git at the commit immediately before that date.

⚠ **If you find something that was in a note and is neither in that note nor here, that is a
bug in this tidy.** Say so and put it back.
