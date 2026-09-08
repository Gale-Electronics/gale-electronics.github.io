# GT2101 - Board 1 (Display) - bench tests
# ---------------------------------------------------------------------------
# From the Thonny Shell:
#
#   import bench
#   bench.lock()        <- FIRST, every time the board has been powered up
#   bench.digits()      <- then this: every segment, then real numbers
#   bench.sweep()       <- counts 0.0 to 99.9 so you can watch it run
#   bench.hold()        <- shows a number, then the Pico stops entirely
#
# Nothing here can hurt the board.
# ---------------------------------------------------------------------------

import time
import config
import display


def lock():
    """Find the board's reset state, so the Pico knows where it is in the lap.

    The board's 4013 free-runs and starts in a random state, so this has to be
    done once after every power-up. It takes at most four Enter presses.

    All you have to spot is the moment THE DIGITS GO DARK.
    """
    display.unlock()
    display.init()

    print()
    print("Press Enter to send one F REF pulse at a time.")
    print("Watch the display. You are looking for the moment the DIGITS GO DARK")
    print("- all three of them, completely blank. That happens once every four.")
    print()

    found = False
    for n in range(1, 10):
        input("   Enter for pulse %d ... " % n)
        display.fref_pulse()
        time.sleep_ms(config.RESET_SETTLE_MS)
        answer = input("      are the digits DARK now?  y/n > ").strip().lower()
        if answer.startswith("y"):
            found = True
            break
        print()

    if not found:
        print()
        print("Never went dark in nine pulses. Tell me what it did show and")
        print("we will look at it again - do not change any wiring.")
        return False

    display.mark_at_reset()
    print()
    print("Good - the counter is empty and we know where we are. Testing...")
    print()

    ok = True
    for value, name in ((123, "12.3"), (450, "45.0"), (780, "78.0")):
        display.show(value)
        answer = input("   does it read %s ?  y/n > " % name).strip().lower()
        if not answer.startswith("y"):
            ok = False
            break

    print()
    if ok:
        display.show_rpm(33.3)
        print("=" * 58)
        print("LOCKED. The display is yours - it should be showing 33.3")
        print("Run  bench.digits()  next.")
        print("=" * 58)
    else:
        display.unlock()
        print("That did not come out right. Run bench.lock() again - if it")
        print("fails the same way twice, tell me what it showed instead.")
    return ok


def digits():
    """Light every segment of every digit, then show a few real numbers."""
    if not display.is_locked():
        print("Run bench.lock() first.")
        return

    print("888 - every segment on. Check none are missing.")
    display.show(888)
    time.sleep(3)

    for n in (0, 111, 222, 333, 444, 555, 666, 777, 888, 999):
        print("   %d  ->  %04.1f" % (n, n / 10.0))
        display.show(n)
        time.sleep(1)

    print()
    print("The three real speeds:")
    for rpm in (33.3, 45.0, 78.0):
        print("   %.1f rpm" % rpm)
        display.show_rpm(rpm)
        time.sleep(2)

    display.show_rpm(33.3)
    print("Left showing 33.3")


def sweep(step=1, pause_ms=20):
    """Count 0.0 up to 99.9 and back down. Ctrl-C to stop."""
    if not display.is_locked():
        print("Run bench.lock() first.")
        return
    try:
        while True:
            for n in range(0, config.MAX_COUNT + 1, step):
                display.show(n)
                time.sleep_ms(pause_ms)
            for n in range(config.MAX_COUNT, -1, -step):
                display.show(n)
                time.sleep_ms(pause_ms)
    except KeyboardInterrupt:
        display.show_rpm(33.3)
        print("Stopped. Left showing 33.3")


def hold(count=333):
    """Show one number, then do nothing at all."""
    if not display.is_locked():
        print("Run bench.lock() first.")
        return
    display.show(count)
    print("Showing %04.1f - and the Pico is now doing nothing whatsoever." % (count / 10.0))
    print("It stays lit because the board's own 1975 latches are holding it.")


def steps(load_value=123, how_many=8):
    """Diagnostic: load a number, then step F REF and report what you see.

    Only needed if lock() misbehaves.
    """
    display.unlock()
    display.init()
    display.load(load_value)
    print("Loaded %d without latching. Stepping F REF:" % load_value)
    seen = []
    for n in range(1, how_many + 1):
        display.fref_pulse()
        time.sleep_ms(config.RESET_SETTLE_MS)
        what = input("   pulse %d - what does it show? > " % n).strip()
        seen.append(what)
    print()
    print("pulse : " + " ".join("%2d" % (i + 1) for i in range(len(seen))))
    print("shows : " + " ".join("%2s" % s[:2] for s in seen))
    return seen