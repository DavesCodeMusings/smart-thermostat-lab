# Connect to WiFi and set clock to network time.

SSID = "MyAccessPoint"
PASSWORD = "P@ssw0rd"

import network
from time import sleep, localtime, time
from ntptime import settime

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

if not wlan.isconnected():
    print("Connecting to network.", end="")
    wlan.connect(SSID, PASSWORD)
    while not wlan.isconnected():
        sleep(1)
        print(".", end="")  # Suppress the newline to add dots in a row.

    print("OK")  # Connected.
    
# See docs.micropython.org/en/latest/library/time.html
print("Syncing time.")
settime()
utc = localtime()
leading_zero = "0" if (utc[4] < 10) else ""
print("UTC time:", str(utc[1]) + "/" + str(utc[2]) + "/" +str(utc[0]), str(utc[3]) + ":" + leading_zero + str(utc[4]))
