# Read ESP32 temperature and output to built-in display.

from machine import Pin, SoftI2C
from ssd1306 import SSD1306_I2C
from esp32 import raw_temperature

# The built-in display uses an SSD1306 controller with I2C pin 4 and 5 for clock and data, respectively.
i2c = SoftI2C(scl=Pin(4), sda=Pin(5))
oled = SSD1306_I2C(128, 64, i2c)

esp32_temp = raw_temperature()
message = "CPU temp: {:d} F".format(esp32_temp)
oled.text(message, 0, 0)
oled.show()
