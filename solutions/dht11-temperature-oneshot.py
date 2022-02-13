# Read DHT11 temperature and output to built-in display.

from machine import Pin, SoftI2C
from ssd1306 import SSD1306_I2C
from dht import DHT11

# The built-in display uses an SSD1306 controller with I2C pin 4 and 5 for clock and data, respectively.
i2c = SoftI2C(scl=Pin(4), sda=Pin(5))
oled = SSD1306_I2C(128, 64, i2c)

# The DHT11 should be attached to GPIO pin 6 or adjust accordingly.
DHT11_DATA = 6
dht11 = DHT11(Pin(DHT11_DATA))

oled.text("Hello DHT11!", 0, 0)

dht11.measure()  # If DHT11 is not attached, program will abort or hang at this line!
temp_celsius = dht11.temperature()
temp_fahrenheit = 1.8 * temp_celsius + 32  # F = 9/5 C + 32

message = "Temp: {:2.0f}F".format(temp_fahrenheit)
oled.text(message, 0, 10)  # Start on pixel row 10 to leave some space between text above.
oled.show()
