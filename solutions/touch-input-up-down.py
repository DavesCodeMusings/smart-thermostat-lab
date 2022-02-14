# Read ESP32 touch inputs and indicate which was touched.

from machine import Pin, TouchPad
from time import sleep

gpio_up = 15
gpio_down = 2
up_input = TouchPad(Pin(gpio_up))
down_input = TouchPad(Pin(gpio_down))

while 1:
    up_value = up_input.read()
    down_value = down_input.read()

    if (up_value < 500):
        print("Pressing UP.")
    if (down_value < 500):
        print("Pressing DOWN.")
        
    sleep(1)
