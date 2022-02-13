# Example of reading touch inputs on the LOLIN32 OLED

from machine import Pin, SoftI2C, TouchPad
from time import sleep
from ssd1306 import SSD1306_I2C

# These values work with WeMos LOLIN32 OLED
i2c_clock = 4
i2c_data = 5
oled_height = 64
oled_width = 128

# Initialize I2C and OLED
i2c = SoftI2C(scl=Pin(i2c_clock), sda=Pin(i2c_data))
oled = SSD1306_I2C(oled_width, oled_height, i2c)

# These GPIO pins will be used as touch pad inputs
input_up = 15
input_down = 2

# Initialize touch input
up = TouchPad(Pin(input_up))
down = TouchPad(Pin(input_down))

# Repeat forever...
while 1:

  # Read from inputs
  up_value = up.read()
  down_value = down.read()

  # Clear display by filling with black
  oled.fill(0)
  
  # Write to display
  oled.text('Up:  ' + str(up_value), 0, 0)
  oled.text('Down: ' + str(down_value), 0, 12)

  # Determine what input was touched (values go down when fingers are near)
  if (up_value < 500):
      oled.text('^', 0, 48)
  if (down_value < 500):
      oled.text('v', 0, 56)

  # Update display
  oled.show()
  
  # Wait 1 second
  sleep(1)
