# GT2101 - Board 1 (Display) - driver
# ---------------------------------------------------------------------------
# Board 1 is a three-digit frequency counter: an MC14553 counts pulses on the
# F DISPLAY line for as long as the GATE line is open, and an MC14511 shows the
# total. The decimal point is hardwired, so a count of 333 reads "33.3".
#
# The trick this driver uses: the Pico owns the F REF line as well, and F REF is
# what clocks the 4013 that produces the board's own latch and reset pulses. So
# we do not have to guess the deck's timing window - we send an exact number of
# pulses, close the gate, and then TELL the board to latch. The number on the
# display is then exact by construction, and the speed we send the pulses at
# does not matter at all.
#
#   show(333)  ->  "33.3"
#
# The 4553 latches hold their value, so once shown, a number stays on the
# display with no further work. You only call show() when the value changes.
# ---------------------------------------------------------------------------

from machine import Pin
import time
import config

_f_display = None
_gate = None
_f_ref = None
_blank = None

# These are worked out from config.py every time init() runs, so bench.auto()
# can change the settings and just call init() again.
_gate_shut = 1
_gate_open = 0
_blank_off = 1
_blank_on = 0


def init():
    """Set up the pins and leave the board's counter cleared."""
    global _f_display, _gate, _f_ref, _blank
    global _gate_shut, _gate_open, _blank_off, _blank_on

    _gate_shut = 1 if config.GATE_COUNTS_WHEN_LOW else 0
    _gate_open = 1 - _gate_shut
    _blank_off = 1 if config.BLANK_ACTIVE_LOW else 0   # level meaning "digits lit"
    _blank_on = 1 - _blank_off

    _f_display = Pin(config.PIN_F_DISPLAY, Pin.OUT, value=0)
    _gate      = Pin(config.PIN_GATE,      Pin.OUT, value=_gate_shut)
    _f_ref     = Pin(config.PIN_F_REF,     Pin.OUT, value=0)

    if config.PIN_BLANK is None:
        _blank = None
    else:
        _blank = Pin(config.PIN_BLANK, Pin.OUT, value=_blank_off)

    latch()          # clear whatever the counter powered up holding


def fref_pulse():
    """One pulse on F REF. This is what advances the board's 4013 timing chain."""
    w = config.FREF_PULSE_US
    _f_ref.value(1)
    time.sleep_us(w)
    _f_ref.value(0)
    time.sleep_us(w)


def latch():
    """Latch whatever the counter holds onto the display, then clear the counter.

    That is one full trip round the board's own 4013 / 4001 housekeeping chain.
    FREF_EDGES in config.py says how many F REF pulses that takes.
    """
    for _ in range(config.FREF_EDGES):
        fref_pulse()
    time.sleep_ms(config.RESET_SETTLE_MS)


def load(count):
    """Send `count` pulses into the counter, but do NOT latch them yet.

    Only useful for bench work. Normal code calls show().
    """
    if count < 0:
        count = 0
    elif count > config.MAX_COUNT:
        count = config.MAX_COUNT

    p = _f_display
    w = config.PULSE_US
    us = time.sleep_us

    _gate.value(_gate_open)
    for _ in range(count):
        p.value(1)
        us(w)
        p.value(0)
        us(w)
    _gate.value(_gate_shut)

    return count


# --- phase lock ------------------------------------------------------------
# The board's 4013 is a free-running divider. Nothing resets it, so at power-up
# it sits in whichever of its four states it feels like, and it only moves when
# WE pulse F REF. So "send a couple of pulses and hope" lands somewhere
# different every time - which is exactly what the bench showed.
#
# Measured on the board, the four states are:
#
#     LATCH  -> counter value captured and shown
#     hold
#     RESET  -> counter cleared, and THE DIGITS GO DARK
#     hold
#
# The dark state is the landmark. Once we have seen it we know the counter is
# empty and we know where we are in the lap, and since the Pico is the only
# thing driving F REF we stay in step from then on. Every update is deliberate:
#
#     2 pulses -> reset, counter cleared
#     load N   -> counter holds N
#     2 pulses -> back to the latch, N appears
#
# bench.lock() finds the dark state. It calls mark_at_reset() when you see it.

_locked = False
_at_reset = False


def mark_at_reset():
    """Tell the driver 'the digits just went dark', i.e. we are at the reset state."""
    global _locked, _at_reset
    _locked = True
    _at_reset = True


def unlock():
    global _locked, _at_reset
    _locked = False
    _at_reset = False


def is_locked():
    return _locked


def _show_locked(count):
    global _at_reset

    if not _at_reset:
        for _ in range(config.FREF_LATCH_TO_RESET):
            fref_pulse()                          # -> round to the reset state
    _at_reset = False

    # IMPORTANT: the reset is a STATE, not a brief pulse. While the 4013 sits in
    # it, the 4553's reset line is held and the counter simply cannot count - so
    # anything loaded here is thrown away and the display comes up as 0.0. Step
    # out of the reset state first, then load.
    fref_pulse()                                  # -> out of reset, into hold
    time.sleep_ms(config.RESET_SETTLE_MS)         # let the RC chain let go

    count = load(count)                           # counter now holds count

    for _ in range(config.FREF_CYCLE - config.FREF_LATCH_TO_RESET - 1):
        fref_pulse()                              # -> on to the latch state
    time.sleep_ms(1)
    return count


def show(count):
    """Put a number on the display. 0 to 999, shown as 0.0 to 99.9.

    Needs the phase lock. Run bench.lock() once after every power-up.
    """
    if _locked:
        return _show_locked(count)

    # Not locked yet: old blind behaviour, kept so bench.lock() can use it.
    count = load(count)
    latch()
    return count


def show_rpm(rpm):
    """Put a platter speed on the display. 33.333 -> "33.3"."""
    return show(int(round(rpm * 10.0)))


def blank(off=True):
    """Turn the digits off (True) or back on (False).

    Does nothing unless PIN_BLANK is wired up in config.py.
    """
    if _blank is None:
        return False
    _blank.value(_blank_on if off else _blank_off)
    return True


# --- raw line control, for poking at the board by hand -----------------------

def set_gate(open_it):
    """Force the gate line open (True) or shut (False), and leave it there."""
    _gate.value(_gate_open if open_it else _gate_shut)


def set_fref(level):
    """Force F REF to 0 or 1 and leave it there."""
    _f_ref.value(1 if level else 0)


def set_fdisplay(level):
    """Force F DISPLAY to 0 or 1 and leave it there."""
    _f_display.value(1 if level else 0)