# blink.py — GT2101 Pico power-up proof
#
# Blinks the Pico's own onboard LED, once a second, forever.
# Purpose: prove the Pico boots and runs on tower power with NO USB attached.
# Nothing else is touched. No GPIO pins are driven. No boards are involved.

from machine import Pin
from time import sleep

# The onboard LED lives in a different place on different Picos.
# This finds it either way.
try:
    led = Pin("LED", Pin.OUT)   # Pico W / Pico 2 W (LED is on the wireless chip)
except Exception:
    led = Pin(25, Pin.OUT)      # plain Pico / Pico 2 (LED is on GP25)

while True:
    led.on()
    sleep(0.5)
    led.off()
    sleep(0.5)
