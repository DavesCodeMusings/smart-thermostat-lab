# Read touch inputs to change thermostat setting.

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

# Initialize simulated values for temperature and set point
temperature = 65
thermostat_set = 68

# Repeat forever...
while 1:

  # Read from inputs
  up_value = up.read()
  down_value = down.read()

  # Clear display by filling with black
  oled.fill(0)

  # Write (simulated) temperature reading
  oled.text('Temperature: ' + str(temperature), 0, 0)

  # Determine what input was touched (values go down when fingers are near)
  # Adjust thermostat up/down accordingly
  if (up_value < 500):
    oled.text('^', 120, 0)
    thermostat_set += 1
      
  if (down_value < 500):
    oled.text('v', 120, 12)
    thermostat_set -= 1
      
  # Write thermostat setting
  oled.text('Thermostat:  ' + str(thermostat_set), 0, 12)
  
  # Determine if heat should be running
  if (temperature < thermostat_set):
    oled.text('Heat is running.', 0, 56)
  else:
    oled.text('Heat is off.', 0, 56)

  # Update display
  oled.show()
  
  # Wait 1 second
  sleep(1)
