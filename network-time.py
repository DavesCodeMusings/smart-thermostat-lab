# Connect to WiFi and set clock to network time.

# Note: Reset your ESP32 after saving this file.
# Saving in Thonny sets the ESP32 clock to local time. Resetting will re-sync with network time.

SSID = "MyAccessPoint"
PASSWORD = "P@ssw0rd"
TZ_OFFSET = -6

import network
from ntptime import settime
from time import gmtime, localtime, sleep, time
from machine import RTC

# Monday is 0, not Sunday like other systems.
DAY_OF_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Need an internet connection to get network time.
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    print("Connecting to network.", end="")
    wlan.connect(SSID, PASSWORD)
    while not wlan.isconnected():
        sleep(1)
        print(".", end="")  # Suppress the newline to add dots in a row.
    print(" OK")  # Connected.

    # Sometimes a busy ntp server can time out, so try again if that happens.
    print("Syncing time...", end=" ")
    try:
        settime()
    except:
        settime()

    # Date-Time returned is: [year, month, mday, hour, minute, second, weekday, yearday]
    # See https://docs.micropython.org/en/latest/library/time.html
    # This example formats dates according to US convention: MM/DD/YYYY.
    utc = gmtime()
    utc_d = "{:s}, {:d}/{:d}/{:d}".format(DAY_OF_WEEK[utc[6]], utc[1], utc[2], utc[0])
    utc_t = "{:d}:{:02d}:{:02d}".format(utc[3], utc[4], utc[5])
    print(utc_d, utc_t, "UTC")

local = localtime(time() + TZ_OFFSET * 3600)
local_d = "{:s}, {:d}/{:d}/{:d}".format(DAY_OF_WEEK[local[6]], local[1], local[2], local[0])
local_t = "{:d}:{:02d}:{:02d}".format(local[3], local[4], local[5])
print(local_d, local_t)
