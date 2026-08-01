# wifi_connect.py — Connect the Raspberry Pi Pico W to a Wi-Fi network
# Sample file from the "Getting Started with the Raspberry Pi Pico W" guide by Guy Tal.
#
# The Pico W supports 2.4 GHz networks only.

import network
from time import sleep

SSID = "YOUR_NETWORK_NAME"
PASSWORD = "YOUR_PASSWORD"

wlan = network.WLAN(network.STA_IF)   # station (client) mode
wlan.active(True)
wlan.connect(SSID, PASSWORD)

# Wait up to 10 seconds for a connection
for _ in range(20):
    if wlan.isconnected():
        break
    print("Connecting...")
    sleep(0.5)

if wlan.isconnected():
    print("Connected. IP address:", wlan.ifconfig()[0])
else:
    print("Connection failed — check the SSID and password.")
