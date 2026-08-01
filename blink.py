# blink.py — Onboard LED blink for the Raspberry Pi Pico W
# Sample file from the "Getting Started with the Raspberry Pi Pico W" guide by Guy Tal.
#
# On the Pico W the onboard LED is NOT on a fixed GPIO number.
# It is wired to the wireless chip, so you address it by the name "LED".

from machine import Pin
from time import sleep

led = Pin("LED", Pin.OUT)   # "LED" = onboard LED on the Pico W

while True:
    led.on()          # LED on
    sleep(0.5)        # wait half a second
    led.off()         # LED off
    sleep(0.5)        # wait half a second
