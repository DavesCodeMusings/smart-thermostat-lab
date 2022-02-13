# Lab 2: Measuring Temperature and Humidity
To control the temperature of a room, we first need to measure the temperature of the room. In lab 1, we used the ESP32's built-in temperature sensor, but quickly discovered it's much better at measuring CPU temperature than room temperature. In this lab, we'll attach a sensor called the DHT11, to measure room temperature. The DHT11 can also measure relative humidity, so we can include that informataion on the thermostat display without much extra effort or expense.

## Using Lab 1 as a Starting Point
Since we already know how to measure ESP32 temperature and write it to the built-in OLED display, we'll use that code as a basis for this lab. Sample code is show below. Yours may look different and that's fine, as long as it can read the ESP32 temperature and display it, it'll work.

```
# Read ESP32 temperature and output to built-in display.

from machine import Pin, SoftI2C
from ssd1306 import SSD1306_I2C
from esp32 import raw_temperature

# The built-in display uses an SSD1306 controller with I2C pin 4 and 5 for clock and data, respectively.
i2c = SoftI2C(scl=Pin(4), sda=Pin(5))
oled = SSD1306_I2C(128, 64, i2c)

oled.text("Hello World!", 0, 0)

esp32_temp = raw_temperature()
message = "ESP32 temp: {:d}F".format(esp32_temp)
oled.text(message, 0, 10)  # Start on pixel row 10 to leave some space between text above.
oled.show()
```

> ### Code Comments and Blank Lines
> The lines starting with # are comment lines. They don't tell the microcotroller to do anything, they're simply there to help a human understand what the code is doing. The comment at the top gives an overview of what the program does. Other comments describe specific parts of the program.
> 
> When you write comments, try to focus on the why rather than the what. For example, `# Start on pixel row 10` would explain what you're doing, but `# Start on pixel row 10 to leave some space between text above.` explains why you are doing this. This can be very helpful for anyone else who looks at your code, or for yourself in six months when you forget why you chose row 10.

## Wiring the DHT11
Since the DHT11 is not built into the microcontroller board like the OLED display, it has to be wired in.



## Reading from the DHT11
This tiny bit of code will read the temperature value from the DHT11 and display it in the Thonny shell window.

```

```

Use what you've learned in the previous lab to take bits of this code and incorporate them into your previous work. The resulting code should read temperature from the DHT11 sensor and display it on the OLED.




## Enhancing
So far, the program reads the temperature, displays it, and then... what? Nothing. It just stops. If the temperature changes, we won't know unless we rerun the program. That's not very useful, so we'll add a feature to check the temperature periodically and update the display with a new value.

To do this, we'll need to learn about two things: while loops, and the sleep function. We'll also edit the code to make it easier to read and understand.
The example above is the same code, but it adds two comments (the lines preceded by #) and a few blank lines.

To get the code to update periodically, we'll need to add a loop. And to control how fast the updates come, we'll use a delay.

The while loop allows repeating a section of code. Here's an example:

```
while (1 == 1):
  print("Hello World!")
```

Copy this to Thonny and you'll quickly flood the shell window with lines of Hello World. When you've seen enough, click on Thonny's red stop button.

> ### Conditional Expression
> While loops run until the expression in parentheses is true. This is called a conditional expression. Normally, you'll see a while loop more like `while (x > 0):` or any comparison other than 1 == 1. One equals one is always true, so the while loop just keeps going until we stop the program or pull the plug. You can also simplfy the expression to just 1, as we'll see in the upcoming example.

A while loop like the one above will go as fast as the CPU can manage. We can add a delay using the `sleep()` function that will drastically slow the output to one line every few seconds. Here's an example:

```
from time import sleep

while (1):
  print("Hello World!")
  sleep(3)
```

The example above will also run forever, filling the Thonny shell window with Hello World, just not all at once. The `sleep()` function tells the CPU to wait a number of seconds before continuing. In this case, we're using `sleep(3)`, so there's a three second pause before the loop repeats.

## Putting It All Together
Now that you know how to use a loop and a delay in your MicroPython code, it's time to add these things into the CPU temperature monitor so that it can update the display periodically.

Here's what you'll need to do:

1. Determine where the while loop should start and what code it should include.
2. Add a delay in the while loop to pause for some number of seconds.
3. Clear the screen between updates.

> Clearing the screen was briefly mentioned at the end of Lab 1. You can do it with `oled.fill(0)` to fill the display with all black.

If you get stuck, there is an example called [cpu-temperature.py](https://github.com/DavesCodeMusings/smart-thermostat-lab/blob/main/cpu-temperature.py) in the repository.

## Next Steps
There are a number of functions in the MicroPython ESP32 package. You can find them in the [MicroPython documentation](https://docs.micropython.org/en/latest/library/esp32.html). Take a look at the available functions in ESP32 and also the [other built-in packages](https://docs.micropython.org/en/latest/library/) available for MicroPython. 
there's also a [quick reference](https://docs.micropython.org/en/latest/esp32/quickref.html) that gives a lot of good information for using MicroPython on the ESP32. Don't feel like you need to understand all of this, just know where to find it when you need it.
