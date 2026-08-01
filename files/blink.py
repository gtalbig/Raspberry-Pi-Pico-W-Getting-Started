# blink.py — Onboard LED blink for the Raspberry Pi Pico W
# Sample file from the "Getting Started with the Raspberry Pi Pico W" guide by Guy Tal.
#
# On the Pico W the onboard LED is NOT on a fixed GPIO number.
# It is wired to the wireless chip, so you address it by the name "LED".

   from machine import Pin
   import time

   led = Pin("LED", Pin.OUT)   # onboard LED

   while True:
       led.value(1)
       time.sleep(1)
       led.value(0)
       time.sleep(1)
