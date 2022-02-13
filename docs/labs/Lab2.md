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
Since the DHT11 is not built onto the microcontroller board like the OLED display, it has to be wired in separately. For the DHT11, we'll need 3.3V power, ground, and a GPIO pin for data. The diagram below shows the pin connections for the microcontroller.

![HiLetGo ESP32 OLED](https://github.com/DavesCodeMusings/smart-thermostat-lab/blob/main/docs/images/HiLetGo_ESP32_OLED_Pins.png)

_Pin Diagram for a WeMOS LOLIN32 OLED clone from manufacturer HiLetGo_

Notice that most pins have more than one label assigned to them. Depending on how they are configured in software, these pins can perform multiple functions. Choosing a pin labeled only as GPIO can help avoid contention with these functions later on.

The only two GPIO only pins are GPIO_5 and GPIO_16. You might recall GPIO_5 is being used for I2C, so that leaves GPIO_16 as the one pin that's least likely to be used for something else. We'll use GPIO_16 for the DHT11's data connection.

The power and ground connections are easier. Just choose a red 3.3 volt (3V3) connection and a black ground (GND) connection. Either one of the two 3V3 connections and any of the three available GND connections will work. Just be sure to use 3V3 and not 5V.

> 3V3 is just a shorthand way of saying 3.3V

## Reading from the DHT11
This bit of code will read the temperature value from the DHT11 and display it in the Thonny shell window. Open a new editor window and copy the program below. Run it to show the temperature from the DHT11. Verify that it's a reasonable value (close to actual room temperature.) If not, verify your wiring.

```
# Read temperature and humidity from DHT11.

from dht import DHT11
DHT11_DATA = 16  # Set pin number to whatever GPIO the DHT11 data line is attached to.
dht11 = DHT11(Pin(DHT11_DATA))

# DHT11 reads temperature in Celsius.
dht11.measure()  # If DHT11 is not attached, program will abort or hang at this line!
temp_celsius = dht11.temperature()
temp_fahrenheit = 1.8 * temp_celsius + 32  # F = 9/5 C + 32

print("Temp: {:2.0f}".format(temp_fahrenheit))
```

Use what you've learned in the previous lab to take bits of this code and incorporate them into your previous work. The resulting code should read temperature from the DHT11 sensor and display it on the OLED. Key pieces are: the import statement, the measurement, and the Celsius to Fahrenheit conversion.

If you get stuck, see the program [dht11-temperature-oneshot.py](https://github.com/DavesCodeMusings/smart-thermostat-lab/blob/main/solutions/dht11-temperature-oneshot.py)

## Updating the Display
So far, the program reads the temperature, displays it, and then... what? Nothing. It just stops. If the temperature changes, we won't know unless we rerun the program. That's not very useful, so we'll add a feature to check the temperature periodically and update the display with a new value.

To do this, we'll need to learn about two things: while loops, and the sleep function. We'll also edit the code to make it easier to read and understand.
The example above is the same code, but it adds two comments (the lines preceded by #) and a few blank lines.

To get the code to update periodically, we'll need to add a loop. And to control how fast the updates come, we'll use a delay.

The while loop allows repeating a section of code. Here's an example:

```
x = 5
while (x > 0):
    print("Hello World!")
    x = x - 1
```

The code above will repeat `print("Hello World!")` exacly five times. It uses the variable _x_ to keep track of how many times the loop has been repeated. It keeps going as long as x is greater than zero.

We can also make a while loop that repeats forever by removing all the lines dealing with the counter variable _x_ and writing the while loop like the example below.

```
while (1)
    print("Hello World!")
```

Copy this to Thonny and you'll quickly flood the shell window with lines of Hello World. When you've seen enough, click on Thonny's red stop button.

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

1. Start with the existing code that reads DHT11 temperature and writes it to the OLED display.
2. Determine where the while loop should start and what code it should include.
3. Add a delay in the while loop to pause for some number of seconds.
4. Clear the screen between updates.

> Clearing the screen can be done using the statement `oled.fill(0)` to fill the OLED with the background color.

You can test your program by wrapping your hands around the DHT11 to warm it up. Verify the temperature on the display rises as you do this.

If you get stuck, look at [dht11-temperature-humidity.py](https://github.com/DavesCodeMusings/smart-thermostat-lab/blob/main/solutions/dht11-temperature-humidity.py)

## Next Steps
Now that we can measure the room's temperature, we can compare it to the temperature we're trying to maintain to decide if the heat needs to run or not. We should also have a way to adjust that temperature setting. Both of those things will be covered in the next lab where we'll use the ESP32's touch inputs to move the set temperature up or down.
