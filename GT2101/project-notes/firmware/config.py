# GT2101 - Board 1 (Display) - SETTINGS
# ---------------------------------------------------------------------------
# This is the only file you should ever need to edit.
#
# WIRING, bench setup (Board 1 running at 5 V from the Pico's USB supply)
#
#   Hold Board 1 component side towards you, displays at the top.
#   The connector row along the bottom is: seven pins, a gap, one lone pin,
#   a gap, one lone pin, a bigger gap, then three pins at the right-hand end.
#   Count the twelve pins you can see, left to right.
#
#     Board 1 pin        Signal        Pico
#     ------------------------------------------------------------
#     1  (1st of seven)  +10 V    <--  pin 40  VBUS   (5 V from USB)
#     6  (6th of seven)  F DISP   <--  GP2
#     7  (last of seven) GATE     <--  GP3
#     11 (middle of 3)   F REF    <--  GP4
#     12 (last pin)      GND      <--  pin 38  GND
#
#   Leave everything else unconnected. In particular:
#     - pin 3  (BLANK)      has a pull-up on the board, so unconnected = display ON
#     - pin 8  (GREEN LED)  leave alone for now
#     - pin 10 (RESET out)  is an OUTPUT from the board. Never drive it.
#
#   ONE POWER SOURCE AT A TIME. On the bench that is the USB lead, nothing else.
# ---------------------------------------------------------------------------

# ---- Pico pins (GP numbers, the ones printed on the board, not 1-40) -------
PIN_F_DISPLAY = 2
PIN_GATE      = 3
PIN_F_REF     = 4
PIN_BLANK     = None      # None = not wired. Set to a GP number to control blanking.

# ---- Which way round the signals are ---------------------------------------
# Sheet 1A says the 4011 passes the clock through while the gate line is LOW.
# If the display never counts, try setting this to False.
GATE_COUNTS_WHEN_LOW = True

# The 4511's BLANK input is active low: pulling it low turns the digits off.
BLANK_ACTIVE_LOW = True

# ---- Timing ----------------------------------------------------------------
# How many F REF pulses complete one "latch the value, then clear the counter"
# cycle. The 4013 is a two-stage divider so this is probably 2 or 4, but it has
# never been measured. Run bench.fref_hunt() to find it, then put the answer here.
FREF_EDGES = 2

# The board's four-state cycle, measured on the bench 21 Aug 2026:
#
#     pulse 1  LATCH   - counter value captured, appears on the display
#     pulse 2  hold    - display unchanged
#     pulse 3  RESET   - counter cleared, DIGITS GO DARK for this state
#     pulse 4  hold    - display unchanged
#     ...and round again
#
# FREF_CYCLE      = pulses for one full lap
# FREF_LATCH_TO_RESET = pulses from the latch state to the reset state
FREF_CYCLE = 4
FREF_LATCH_TO_RESET = 2

PULSE_US        = 5    # half-period of each F DISPLAY pulse (microseconds)
FREF_PULSE_US   = 50   # half-period of each F REF pulse (microseconds)
RESET_SETTLE_MS = 5    # pause for the RC reset chain on the board to finish

# ---- Range -----------------------------------------------------------------
# Three digits with a fixed decimal point, so 0 to 999 counts = 0.0 to 99.9
MAX_COUNT = 999