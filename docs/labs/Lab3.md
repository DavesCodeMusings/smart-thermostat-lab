# Lab 3: Using Touch Inputs
The thermostat with no way to adjust it up or down is not going to win many friends. In this lab, we'll enhance the code to have an adjustable set point at which the heat turns on or off. We'll also use the ESP32's touch sensitive pins as a way to detect when someone wants to adjust the temperature up or down.

## Reading Touch Inputs

```
# Read ESP32 touch inputs and display values

from machine import Pin, TouchPad
from time import sleep

gpio_up = 15
gpio_down = 2
up = TouchPad(Pin(gpio_up))
down = TouchPad(Pin(gpio_down))

while 1:
    up_value = up.read()
    down_value = down.read()
    print("Up = {:03d}  Down = {:03d}".format(up_value, down_value))
    sleep(1)
```

Run the program and watch the numbers scrolling by. Find pin 2 on the microcotroller and press your finger against it. Watch what happens to the numbers on the display. Touch pin 15 and see what happens.

Make a few notes on your observations.

* How do the readings change when you touch an input?
* What's the lowest reading you observed?
* What's the highest reading?

Using your notes, choose a number in between the highest number and the lowest number. Write a comparison that will determine if an input is being touched or not.

Here's some sample code to show how Python does comparisons:

```
if (touch_input < touch_threshold):
    print("Touching input.")
```

Incorporate a comparrison like this into your code to determine if the _Up_ input is being pressed. Do the same for the _Down_ input. Once it's working like you expect, remove the line that prints the input values and only print a message when Up or Down is pressed.

If you get stuck, look at [touch-input-up-down.py](https://github.com/DavesCodeMusings/smart-thermostat-lab/blob/main/solutions/touch-input-up-down.py)

## Adjusting the Thermostat Up or Down

