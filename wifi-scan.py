# Scan for available WiFi access points.

import network

station = network.WLAN(network.STA_IF)
station.active(True)

# For more info, see https://docs.micropython.org/en/latest/library/network.WLAN.html
ap_list = station.scan()
for ap in ap_list:
    ssid = str(ap[0], 'utf-8')       # Wireless access point name.
    signal_strength = str(ap[3])     # Wireless signal strength meausred in dBm.
    hidden = ap[5]
    if (not hidden and ssid != ''):  # Don't show any hidden or blank SSIDs.
        print(signal_strength, ssid)
