# Lab 2: Monitoring CPU Temperature
This lab builds on Lab 1, displaying the temperature of the ESP32 CPU on the display rather than a Hello World message. It introduces the idea of periodically reading from sensors and updating the display. This lays the foundation needed for later labs that will read room temperature.

## Using ESP32 Package Functions
MicroPython has a package of functions to use with the ESP32 microcontroller. One of those functions is `raw_temperature()` and it reads the CPU core temperature in degrees Fahrenheit. We'll use this new function, together with the code from Lab 1 to read the CPU temperature and show it on the built-in display.

But first, here's a simple example to read CPU temperature and print it in the Thonny editor.

```
from esp32 import raw_temperature
cpu_temp = raw_temperature()
print("CPU temperature: " + str(cpu_temp) + "°F")
```

When you run the code above, the temperature does not print to the built-in display. In fact, the display will show whatever you last wrote to it, so it may be displaying Hello World at the moment. To find the temperature output, look in Thonny toward the bottom. There's a window called _Shell_ that shows the output from print statements. You should see a CPU temperature reading of around 125°F.

## Sending CPU Temperature to the Display
To write CPU temperature on the display, you'll need to adapt the Hello World example from Lab 1.

### Hello World
```
from machine import Pin, SoftI2C
import ssd1306
i2c = SoftI2C(scl=Pin(4), sda=Pin(5))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
oled.text('Hello World!', 0, 0)
oled.show()
```

Obviously, the trick here is to replace `oled.text('Hello World!', 0, 0)` with something that displays the CPU temperature. But, there's the additional steps of importing the esp32 package and calling the `raw_temperature()` function to read the CPU temperature. Think about how you might do this before moving on.

### Hello CPU Temperature
The first step is to import the esp32 package. This is done by addin another from/import statement for the esp32 package and the raw_temperature function.

```
from machine import Pin, SoftI2C
import ssd1306
from esp32 import raw_temperature
```

Next, we need to read the CPU temperature. We've already figured out how to read it in the example that prints CPU temperature in the Thonny editor window. All we need to do is copy `cpu_temp = raw_temperature()` and put it in the right place. That could be anywhere between the `from esp32 import raw_temperature` statement that makes the function available and the `oled.text` statement that shows the temperature value.

Having it closer to `oled.text` will be useful later on, so we'll put it there.

```
from machine import Pin, SoftI2C
import ssd1306
from esp32 import raw_temperature
i2c = SoftI2C(scl=Pin(4), sda=Pin(5))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
cpu_temp = raw_temperature()
```

Finally, we'll include the lines that display the value. Here's the completed example:

```
from machine import Pin, SoftI2C
import ssd1306
from esp32 import raw_temperature
i2c = SoftI2C(scl=Pin(4), sda=Pin(5))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
cpu_temp = raw_temperature()
oled.text("CPU temperature: " + str(cpu_temp) + "°F", 0, 0)
oled.show()
```

Copy this to Thonny and run it, and you'll see it's probably not exactly what you expected.

## Debugging
There's a big problem with the code. Because the display width is not very big, the actual temperature reading gets cut off. One solution is to abbreviate Temperature to Temp.

```
from machine import Pin, SoftI2C
import ssd1306
from esp32 import raw_temperature
i2c = SoftI2C(scl=Pin(4), sda=Pin(5))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
cpu_temp = raw_temperature()
oled.text("CPU temp: " + str(cpu_temp) + "°F", 0, 0)
oled.show()
```

Now it fits the display, but we've got a new problem. The degree symbol shows up as three blocks instead of what we got when running the first example that prints in Thonny. That's because the SSD1306 only has a limited number of characters it can display and the degree symbol is not one of them. So, we'll take it out and assume anyone looking at the display will know that some number followed by F is a temperature in Fahrenheit.

```
from machine import Pin, SoftI2C
import ssd1306
from esp32 import raw_temperature
i2c = SoftI2C(scl=Pin(4), sda=Pin(5))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
cpu_temp = raw_temperature()
oled.text("CPU temp: " + str(cpu_temp) + "F", 0, 0)
oled.show()
```

## Enhancing
So far, the program reads the CPU temperature, displays it, and then... what? Nothing. It just stops. If the CPU temperature changes, we won't know unless we rerun the program. That's not very useful, so we'll add a feature to check the temperature periodically and update the display with a new value.

To do this, we'll need to learn about two things: while loops, and the sleep function. We'll also edit the code to make it easier to read and understand.

Let's start with making it easier to read.

```
# Read CPU core temperature and output to built-in display.

from machine import Pin, SoftI2C
import ssd1306
from esp32 import raw_temperature

# The built-in display uses an SSD1306 controller with I2C pin 4 and 5 for clock and data, respectively.
i2c = SoftI2C(scl=Pin(4), sda=Pin(5))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

cpu_temp = raw_temperature()
oled.text("CPU temp: " + str(cpu_temp) + "F", 0, 0)
oled.show()
```

The example above is the same code, but it adds two comments (the lines preceded by #) and a few blank lines.

This can make reading the code easier on your eyes, just like this document uses headings to divide sections and blank lines to separate paragraphs. And just like a document, we start with a title of sorts, describing what the code does. The next comment is like a section heading, describing the code that follows. These simple changes help make the code easier to understand and maintain.

> ### Comment the Why, Not the How
> Look at the comment about the built-in display. It describes the purpose of the next two lines, but it explains why they are included, not what they do. Once you get past your first few programs, you'll know how to use the functions that initialize the I2C bus and the SSD1306 OLED display chip. What you might not know is why pins 4 and 5 were selected. By including the why and not the how, you can help anyone who comes along later understand the decisions that went into writing your code.

## Periodic Updates
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
