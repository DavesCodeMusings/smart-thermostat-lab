# Detecting Presence
Presence detection is just a fancy way of saying figuring out if people are home or not. If no one is home, the thermostat can be lowered to save energy. In this lab, we'll use the ESP32's Bluetooth capabilities to scan for cell phones in the area. If the phone's Bluetooth is no longer in range, we can assume the person has left the house and adjust the thermostat down.

## Scanning for Bluetooth Devices
