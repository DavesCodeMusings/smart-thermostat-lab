# Read CPU core temperature and output to built-in display.

from machine import Pin, SoftI2C
from ssd1306 import SSD1306_I2C
from esp32 import raw_temperature
from time import sleep

# The built-in display uses an SSD1306 controller with I2C pin 4 and 5 for clock and data, respectively.
i2c = SoftI2C(scl=Pin(4), sda=Pin(5))
oled = SSD1306_I2C(128, 64, i2c)

while (1):
    cpu_temp = raw_temperature()
    oled.fill(0)  # clear the display
    oled.text("CPU temp: " + str(cpu_temp) + "F", 0, 0)
    oled.show()
    sleep(1)
