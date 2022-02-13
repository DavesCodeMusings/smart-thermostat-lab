from machine import Pin, SoftI2C
from ssd1306 import SSD1306_I2C

# These values work with WeMos LOLIN32 OLED
i2c_clock = 4
i2c_data = 5
oled_height = 64
oled_width = 128

# Initialize I2C and OLED
i2c = SoftI2C(scl=Pin(i2c_clock), sda=Pin(i2c_data))
oled = SSD1306_I2C(oled_width, oled_height, i2c)

# Experiment with different values for temperature and thermostat setting
temperature = 65
thermostat_set = 68

# Write information
oled.text('Temperature: ' + str(temperature), 0, 0)
oled.text('Thermostat:  ' + str(thermostat_set), 0, 12)

if (temperature < thermostat_set):
    oled.text('Heat is running.', 0, 56)
else:
    oled.text('Heat is off.', 0, 56)

# Update display
oled.show()
