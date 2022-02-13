# Connect to Wireless Access Point

SSID = "MyAccessPoint"
PASSWORD = "P@ssw0rd"

import network
from time import sleep

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

if not wlan.isconnected():
    print("Connecting to network.", end="")
    wlan.connect(SSID, PASSWORD)
    while not wlan.isconnected():
        sleep(1)
        print(".", end="")  # Suppress the newline to add dots in a row.

    print("OK")  # Connected.

# See http://docs.micropython.org/en/latest/library/network.WLAN.html#network.WLAN.ifconfig
dhcp_info = wlan.ifconfig()
ip_addr = dhcp_info[0]
netmask = dhcp_info[1]
gateway = dhcp_info[2]
dns = dhcp_info[3]

print("IP Addr:", ip_addr)
print("Netmask:", netmask)
print("Gateway:", gateway)
print("DNS:    ", dns)
print('network config:', wlan.ifconfig())
