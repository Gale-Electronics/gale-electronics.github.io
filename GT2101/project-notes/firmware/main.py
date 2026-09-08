# main.py - session 8: standalone display + pot + green LED
import time
from machine import Pin, ADC
import config, display

POT_PIN     = 26        # GP26, Helipot wiper (orange)
LED_PIN     = 5         # GP5, Board 1 pin 8
RPM_MIN     = 30.0      # pot at one end
RPM_MAX     = 80.0      # pot at the other end
STEP_COUNTS = 1500      # pot movement that sends one F REF pulse (~1/4 turn)
STILL_MS    = 3000      # stay still this long to say "that's the dark one"

led = Pin(LED_PIN, Pin.OPEN_DRAIN, value=1)   # 0 = lit, 1 = out
pot = ADC(POT_PIN)


def read_pot():
    t = 0
    for _ in range(16):
        t += pot.read_u16()
    return t >> 4


def lock_by_pot():
    display.unlock()
    display.init()
    base = read_pot()
    pulses = 0
    last_move = time.ticks_ms()

    while True:
        now = read_pot()
        if abs(now - base) > STEP_COUNTS:
            base = now
            display.fref_pulse()
            time.sleep_ms(config.RESET_SETTLE_MS)
            pulses += 1
            last_move = time.ticks_ms()

        led.value(0 if (time.ticks_ms() // 250) % 2 else 1)   # flashing = not locked

        if pulses and time.ticks_diff(time.ticks_ms(), last_move) > STILL_MS:
            display.mark_at_reset()
            led.value(0)                                      # steady = locked
            return
        time.sleep_ms(20)


lock_by_pot()

last = None
while True:
    rpm = RPM_MIN + (read_pot() / 65535.0) * (RPM_MAX - RPM_MIN)
    count = int(round(rpm * 10.0))
    if count != last:
        display.show(count)
        last = count
    time.sleep_ms(100)