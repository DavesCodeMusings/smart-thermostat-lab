# Example of printing to the builtin display of the LOLIN32 OLED

from machine import Pin, SoftI2C
from ssd1306 import SSD1306_I2C

# These values work with WeMos LOLIN32 OLED
i2c_clock = 4
i2c_data = 5
oled_height = 64
oled_width = 128

# Initialize I2C
i2c = SoftI2C(scl=Pin(i2c_clock), sda=Pin(i2c_data))

# Initialize OLED
oled = SSD1306_I2C(oled_width, oled_height, i2c)

# Write messages
oled.text('Hello!', 0, 0)
oled.text('Hello World!', 0, 12)
oled.text('Hello Cleveland!', 0, 24)

# Display messages
oled.show()
