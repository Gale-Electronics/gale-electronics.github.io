# fvar.py — Remora's F VAR generator
# Emits a crystal-locked square wave on GP16, which is the transistor's base.
# The transistor inverts it; board 3's 4011 inverts it back; so board 3's
# edge pin 5 ends up following GP16 directly.
#
# F VAR is 40 Hz per rpm:
#     33 1/3 rpm -> 1333.333 Hz
#     45    rpm  -> 1800    Hz
#     78    rpm  -> 3120    Hz
#
# Bench use only so far. Nothing here touches the tower.

import rp2
import time
from machine import Pin

FVAR_PIN = 16          # base, through the 10k
SENSE_PIN = 17         # collector — used only to check the output
SM_CLOCK = 125_000_000 # the Pico's system clock


@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW)
def _square():
    # Half-period loop count arrives in the FIFO. pull(noblock) keeps the
    # previous value when nothing new has been pushed, so it free-runs.
    pull(noblock)
    mov(x, osr)

    mov(y, x)
    set(pins, 1)
    label("hi")
    jmp(y_dec, "hi")

    mov(y, x)
    set(pins, 0)          [2]     # [2] balances the 2 extra cycles above
    label("lo")
    jmp(y_dec, "lo")


_sm = None


def _count_for(hz):
    """Loop count for one half period. 10 cycles of fixed overhead per period."""
    n = round(SM_CLOCK / (2.0 * hz)) - 5
    if n < 1:
        raise ValueError("frequency too high")
    return n


def actual_hz(hz):
    """What the hardware will really produce for a requested frequency."""
    return SM_CLOCK / (2.0 * _count_for(hz) + 10.0)


def start(hz=1333.3333):
    """Start (or retune) the square wave on FVAR_PIN."""
    global _sm
    if _sm is None:
        _sm = rp2.StateMachine(0, _square, freq=SM_CLOCK, set_base=Pin(FVAR_PIN))
    _sm.put(_count_for(hz))
    _sm.active(1)
    print("F VAR on GP%d: asked %.4f Hz, actual %.4f Hz  (%.4f rpm)"
          % (FVAR_PIN, hz, actual_hz(hz), actual_hz(hz) / 40.0))


def stop():
    """Stop the square wave and leave the pin low."""
    global _sm
    if _sm is not None:
        _sm.active(0)
    Pin(FVAR_PIN, Pin.OUT, value=0)
    print("F VAR off, GP%d low" % FVAR_PIN)


def rpm(r):
    """Set the speed in rpm rather than Hz."""
    start(r * 40.0)


def check(seconds=2, pin_no=SENSE_PIN):
    """Count edges on the collector to prove the transistor is switching.

    Expect roughly the same figure as the frequency you asked for.
    """
    c = [0]
    p = Pin(pin_no, Pin.IN, Pin.PULL_UP)

    def _tick(_):
        c[0] += 1

    p.irq(trigger=Pin.IRQ_RISING, handler=_tick)
    time.sleep(seconds)
    p.irq(handler=None)
    hz = c[0] / seconds
    print("GP%d saw %d edges in %ds  ->  %.1f Hz  (%.2f rpm)"
          % (pin_no, c[0], seconds, hz, hz / 40.0))
    return hz
