# Scan for available WiFi access points.

from machine import Pin, SoftI2C
from ssd1306 import SSD1306_I2C
import network

i2c = SoftI2C(scl=Pin(4), sda=Pin(5))
oled = SSD1306_I2C(128, 64, i2c)

station = network.WLAN(network.STA_IF)
station.active(True)

# For more info, see https://docs.micropython.org/en/latest/library/network.WLAN.html
ap_list = station.scan()
row = 0
for ap in ap_list:
    ssid = str(ap[0], 'utf-8')       # Wireless access point name.
    signal_strength = str(ap[3])     # Wireless signal strength meausred in dBm.
    hidden = ap[5]
    if (not hidden and ssid != ''):  # Don't show any hidden or blank SSIDs.
        oled.text(str(signal_strength) + " " + ssid, 0, row * 10)
        row += 1
        if (row >= 6):               # Stop printing to avoid filling up the display.
            break

oled.show()
