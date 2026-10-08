# GT2101 Debugging Reference

Facts-only technical reference for the Gale GT2101 control tower: board functions, signal
chain, and pin-to-pin test points. No history, no provenance, no attribution, bench use only.

---

## 1. System overview

Five PCBs in the control tower (Board 1 through Board 5), connected by a single flexible
backplane film ("the flexicon"). One motor PCB inside the motor pod, wired to the tower via
the flexicon.

Signal chain, demand side (speed-setting):
Helipot (3-wire pot) -> Board 3 (XR2207 VCO) -> F VAR output -> Board 5 (black switch,
VAR/FIX select) -> Board 4 -> Board 5 pad 4 (selected x40 demand) -> feeds both the servo
and the display.

Signal chain, feedback side (actual speed):
Motor optical encoder -> motor PCB (LM339 tacho comparator) -> TACH -> Board 4 -> compared
against demand -> drive correction back to motor PCB -> motor windings.

Display chain:
Board 2 divides a 1.048711 MHz crystal (arriving from Board 4) with an MC14521 24-stage
divider, producing a gating signal. A 4016 switch selects between two divider outputs for the
gate rate, and separately selects F DISPLAY between demand (F VAR/FIX) and actual (INV TACH).
Board 1 counts F DISPLAY pulses during the gate window and drives the LED digits.

---

## 2. Board 1, Display logic

Counts F DISPLAY pulses over the gate window and drives the LED digits.

- Pad 2, BLANK
- Pad 3, F DISPLAY (in, from Board 2 pad 8)
- Pad 4, GATE (in, from Board 2 pad 10)
- Pad 6, RESET (out, to Board 2 pad 13, drives the MC14521's R pin; listen-only from Board 1's side, never drive this pin, it re-zeroes the tower's display timebase)
- Pad 7, F REF (in, from Board 4 pad 9, the MC14520 divide-by-4 output)
- Pad 12, ground

Internal logic: 4001 gate D = NOR(4013 Q2, GATE) feeds 4013 R1/R2, so GATE parks the display's
internal divider during the count window and releases it when the window closes. Released,
F REF walks the 4013 through four states, state B = latch (4011 gate C = NAND(Q1, NOT-Q2)),
state D = reset (4001 gate C = NOR(NOT-Q1, NOT-Q2)).

Count arithmetic: 1332 Hz x 0.25 s window = 333 counts -> displays "33.3".

---

## 3. Board 2, Timebase and mode switching

- Pad 2, crystal signal in (1.048711 MHz, from Board 4), measures 5.2 V DC on a meter (it's
  a square wave, meter reads half the 10.7 V rail)
- Pad 3, Pad 4, STILL / TURNING inputs (from Board 3's LM3900, via the flexicon)
- Pad 6, logic node behind a 10k and a clamp diode; Board 1's end has a pull-up to +10 V;
  rests high, pulses low (unconfirmed by meter as of last audit)
- Pad 7, F VAR/FIX demand in
- Pad 8, F DISPLAY out (to Board 1 pad 3)
- Pad 9, INV TACH in
- Pad 10, GATE out (to Board 1 pad 4)
- Pad 11, MC14521 Q19 output, measures 3.7 V (not 50% duty, correct for a divider with a
  NAND reset)
- Pad 13, RESET in (from Board 1 pad 6), drives the MC14521's R pin; rests low, pulsed high
- Pad 14, ground reference for this board

ICs: MC14521 (24-stage divider off the crystal; Q21 = 0.4999 Hz, Q19 = 2.000 Hz) and a 4016
two-way switch (selects which divider output becomes GATE, and separately selects F DISPLAY
between demand and actual, both switched together by the same STILL/TURNING control bit from
Board 3 pads 3/4).

Known fault signature: pad 2 reads 5.2 V (crystal present) and pad 11 reads 3.7 V (first
divider stage running) but pad 10 reads near 0 V, the MC14521 or the 4016 channel feeding
pad 10 is faulty; connector pins alone can't distinguish which.

---

## 4. Board 3, Speed demand (Helipot / XR2207 VCO)

Takes the Helipot's wiper voltage and converts it to a frequency (F VAR) for the servo and
display.

Helipot wiring (3-wire pot, legend R 1K, L .25, code 7603):
- RED post, pot's CCW leg, board 3 GND
- ORANGE post, pot's wiper (S), XR2207 pin 6 (timing resistor terminal) AND, via a capacitor,
  LM308 pin 3 (+ input), this post does two jobs
- YELLOW post, pot's CW leg, board 3 negative rail (nominally −10 V)

XR2207 (14-pin VCO):
- Pin 6, timing resistor terminal, fed from the ORANGE post through a resistor (pins 4, 5, 7
  are NC, so pin 6 is the only timing resistor, open circuit here means zero timing current)
- Pin 13, SQUARE OUT (second pin from the left, top row); 10.66 kOhm pull-up, 10.16 kOhm
  series resistor to a 4011 inverter (pins 5+6 in, pin 4 out) -> pad 5
- Pin 11, BIAS (not SQUARE OUT, do not confuse)
- Pin 12, negative supply

LM308 (fed by the same ORANGE post via a capacitor, AC-coupled):
- Pin 3 (+ in), from ORANGE post
- Pin 6 output, through a resistor to LM3900 "1+ IN" and "2− IN" (same wire, both inputs)

LM3900 (quad op-amp, two independent pairs):
- Amps 1 and 2, window comparator off the LM308; "2 OUT" -> pad 2, "1 OUT" -> pad 3 (STILL/
  TURNING lines to Board 2)
- Amps 3 and 4, separate pair, senses pad 7 net (IN 3−, pin 8), drives 4011 -> 4013 -> BC214
  -> J113, i.e. motor mute / touch-pulse latch / 0V-at-rest. This pair is independent of the
  ORANGE post and the window comparator.

Backplane routing (confirmed on backplane.pdf): pad 5 (VAR, F VAR output) runs straight to
Board 5 row 5 pad 4. It does NOT pass through Board 2, and there is no x40 multiplication on
this leg, it leaves Board 3 already scaled at 40 Hz per rpm (3996 Hz = 99.9 rpm x 40; 1332 Hz
FIX = 33.3 rpm x 40).

Test points:
- Pad 5 to pin 9 (ground), black switch released (VAR position): should swing rail-to-rail,
  0 V low to 10 V high. If stuck around 7.5 V, the black switch is pressed (FIX), not a fault.
- A multimeter cannot resolve F VAR directly, at ~1333 Hz it reads a drifting average
  indistinguishable from a dead line. Use a scope, or hold the probe still and watch for
  movement.

Transistor leg identification (when fitted as a salvage part, not from a datasheet pinout ,<br>
TO-92 pinouts mirror depending on which face you read): identify by function, not position ,<br>
base = control leg (gets the drive resistor), emitter = return leg (to ground), collector =
working leg (to the circuit). Confirm by testing for off->1, on->0 switching, not by counting
legs.

---

## 5. Board 4, Servo / tacho front end

- Pad 2, crystal distribution point (1.048711 MHz out to Board 2 pad 2)
- Pad 3, selected x40 demand in (same net as Board 5 pad 3 and Board 2 pad 7)
- Pad 8, common ground reference point for cross-board continuity checks
- Pad 9, F REF out (MC14520 divide-by-4 output) -> Board 1 pad 7
- Row 4, pad 5, TACH in point (listen-only tap point for an external monitor)

Crystal: 1.048711 MHz, confirmed running. ~600 ppr (counts per revolution) encoder resolution
figure appears on this board's documentation.

Known-good reading: Board 4 pad 2 and Board 2 pad 2 should read identically (both ~5.2 V) when
ground is common between the two boards. If they read differently despite both beeping
continuous on a continuity test, ground is NOT actually common, stop and re-establish ground
before trusting any other voltage on either board.

---

## 6. Board 5, Power supply and mode switching

Two independent rails, made differently:
- Positive rail: through a 3-terminal device (location: under the heat-sink bracket, corner of
  board, NOT confirmed to be the same part position on every board; verify by eye for each
  physical board). Nominal ≈ +11.2 to +11.9 V. Pad 2 is the positive rail test point.
- Negative rail: zener + discrete PNP pass transistor (PNP hfe=283 per schematic). Nominal
  ≈ −10 to −11 V. Pad 8 is the negative rail test point. PNP pinout viewed from the top, flat
  edge: pins are B, C, E in that order.

Common ground: pad 9.

Other components on this board: triac 2N6342 (TO-220, free-standing, middle of board beside
the diac and a white trimmer, NOT the part under the heat-sink bracket), diac 1N5761A (2
legs), bridge rectifier 10DB1A (+ corner marked), 2x 100 uF 25 V blue axial capacitors, 560 ohm
resistor (regulator section).

Row 5 / pad map (backplane):
- Pad 1, LED GREEN
- Pad 2, +10 V (nominal; measures ~11.7 V in practice)
- Pad 3, black switch common (VAR/FIX selector, shared net with Board 4 pad 3 and Board 2
  pad 7, this is the selected x40 demand signal)
- Pad 4, F VAR in (direct from Board 3 pad 5, no intermediate board)
- Pad 7, fixed 1332 Hz (FIX reference)
- Pad 8, negative rail (should read approximately −10 to −11 V to ground at pad 9; a reading
  near +1.6 to +1.7 V indicates the negative rail is not being generated, check pad 2 for
  +11.7 V first to rule out a blown fuse as the cause)
- Pad 9, ground reference for this board

Standard reading table, positive rail healthy:
- Pad 2 to pad 9: +11.7 V
- Bridge + terminal to pad 9: approximately 1.1 MOhm (both probe directions)

Fault isolation note: a dead negative rail (pad 8 near +1.6 V instead of −10 V) will starve
both Board 3's XR2207 (no negative supply for the VCO) and Board 3's LM3900 (no negative
supply for the STILL/TURNING window comparator) simultaneously, both faults can share one
root cause.

Black switch (VAR/FIX): a passive mechanical switch physically located in the tower base
casting, not on Board 5 itself, Board 5 pads 3/4/7 are only the route out to it. Two switch
positions select between F VAR (pad 4, variable) and the fixed 1332 Hz reference (pad 7).
Also grounds the green LED in one position. EAO type 01-272 pushbutton, contacts rated 300 Vac
5/250, lamp rating 60 V / 1.2 W.

---

## 7. Motor PCB (inside motor pod)

Single analogue input net: SPEED IN, arriving from the control tower. This is one analogue
amplitude command, the motor PCB itself handles commutation. No three-phase PWM is needed
from outside; one analogue voltage level is sufficient.

SPEED IN reaches each of three phase chains through 47 kOhm + 47 kOhm (two resistors in
series), with a capacitor to ground at the junction between them. Each phase chain has an
N-channel JFET (type J113, substitution for an original E113) shunting that junction to
ground, gated by that phase's own comparator output.

LM339 (quad comparator), all four sections in use:
- Position sensor GREEN: inputs pins 8, 9 -> output pin 14
- Position sensor YELLOW: inputs pins 6, 7 -> output pin 1
- Position sensor VIOLET: inputs pins 10, 11 -> output pin 13
- Each of the above three has 470 kOhm feedback from output to the + input (positive feedback
  = hysteresis, for clean squaring of the sensor signal)
- Fourth section: inputs pins 4, 5 -> output pin 2, this is the TACH comparator. Its input is
  a wire labelled BROWN. The tacho's open-collector output pulls to ground through 4.7 kOhm;
  the chip's own negative rail is −10 V, which is why TACH swings between 0 V and −10 V.

LM324 (quad op-amp), three sections in use, positioned after the JFET gating network:
- Section: inputs 6, 5 -> output 7
- Section: inputs 2, 3 -> output 1
- Section: inputs 13, 12 -> output 14
- Each drives an output pair through a 560 ohm resistor to the motor windings
- Fourth section (inputs 9, 10 -> output 8) is drawn NC, unused spare on this board

Winding pairs (three), each pair color-coded: green/white, red/white, black/white, these
terminate at the LM324 output stages.

Rails on this board: output Darlington transistors run on +/-15 V. Both the LM339 and LM324
run on a −10 V negative rail (shared with the tower's negative rail). Sensor bias bus reaches
that negative rail through 180 kOhm.

TACH signal: the wire labelled BROWN feeds the LM339's fourth (tacho) comparator section
directly, it is NOT derived from any of the three winding pairs.

---

## 8. Flexicon / backplane, key cross-references

The backplane is a single flexible film connecting all five boards. Always solder to the
brass staples, never directly to a pad.

Confirmed single-net groupings (same electrical net, multiple pad numbers across boards):
- Board 5 pad 3 = Board 4 pad 3 = Board 2 pad 7, one net, the selected x40 demand signal
  (output of the VAR/FIX switch, feeds both servo and display)
- Board 3 pad 5 (VAR output) -> Board 5 row 5 pad 4 directly, no intermediate board, no
  multiplication on this leg

Ground continuity reference chain (prove common before trusting any voltage reading): Board 5
pad 9 -> Board 4 pad 8 -> Board 3 pad 9 -> Board 2 pad 14 -> Board 1 pad 12.

Scaling reference: F VAR leaves Board 3 already at 40 Hz per rpm of platter speed.
- 33.3 rpm -> 1332 Hz (FIX reference value)
- 99.9 rpm -> 3996 Hz

---

## 9. Quick fault-to-pin lookup

| Symptom | Check first |
|---|---|
| Display dead / reads garbage | Board 2 pad 2 (crystal in, expect 5.2 V) then pad 11 (expect 3.7 V) then pad 10 (gate out, near 0 V here with the first two present means MC14521 or 4016 fault) |
| Speed control (knob) has no effect | Board 3 ORANGE post (Helipot wiper) for a smooth sweep; then XR2207 pin 6 for timing current; then pin 13 for SQUARE OUT swing |
| VAR mode won't engage / sticks in FIX | Check the base casting's black switch (VAR/FIX) and its two contact pairs, one pair is lamp, one is contacts, not yet distinguished by position |
| Everything analogue dead at once (VCO, STILL/TURNING, servo) | Board 5 pad 8 to pad 9, if near +1.6 V instead of −10 V, the negative rail is down; check pad 2 first (+11.7 V) to rule out a blown fuse |
| No drive to motor at all | Confirm SPEED IN is present at the motor PCB; then check each phase's JFET gate (comparator output) is toggling |
| TACH reads nothing | LM339 fourth section, pins 4/5 in, pin 2 out, on the motor PCB; confirm the BROWN wire is intact to pin 4/5 |
| Two boards "beep continuous" on continuity but read different voltages | Ground is not actually common between them, stop, re-establish a verified common ground before taking any further reading |

---

*Facts only, pin numbers, nets, components and measured/predicted values as documented and
bench-verified. No restoration history, provenance or attribution included.*
