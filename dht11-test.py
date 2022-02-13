# Read temperature and humidity from DHT11 and display.

from machine import Pin, SoftI2C
from ssd1306 import SSD1306_I2C
from dht import DHT11

# LOLIN32 built-in display uses I2C pins 4 and 5. DHT data is attached to pin 6.
i2c = SoftI2C(scl=Pin(4), sda=Pin(5))
oled = SSD1306_I2C(128, 64, i2c)
dht11 = DHT11(Pin(6))

# DHT11 gives temperature in Celsius and relative humidity in percent.
dht11.measure()  # If DHT11 is not attached, program will hang at this line!
humidity = dht11.humidity()
temp_celsius = dht11.temperature()
temp_fahrenheit = temp_celsius * 9 / 5 + 32

# Display at the top with temperature on the left and humidity on the right.
oled.text("Temp.", 0, 0)
oled.text("Hum.", 64, 0)
oled.text(str(round(temp_fahrenheit)) + "F", 0, 12)
oled.text(str(round(humidity)) + "%", 64, 12)
oled.show()
