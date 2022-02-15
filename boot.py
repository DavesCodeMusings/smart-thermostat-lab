# Show ESP32 hardware capabilities

from machine import freq, Pin, SoftI2C
from gc import collect, mem_free
from esp import flash_size
from os import uname
from ssd1306 import SSD1306_I2C

# Board with built-in OLED uses pins 4 (clock) & 5 (data)
i2c = SoftI2C(scl=Pin(4), sda=Pin(5))
oled = SSD1306_I2C(128, 64, i2c)

collect()  # Run garbage collection to free as much RAM as possible.
arch = "CPU: {:>11s}".format(uname()[0])
speed = "Speed:   {:4.0f}MHz".format(freq() / 1000 / 1000)
ram_free = "RAM:      {:4.0f}KB".format(mem_free() / 1024)
flash_total = "Flash:    {:4.0f}MB".format(flash_size() / 1024 / 1024)
version = "MicroPy:{:>8s}".format(uname()[2])

oled.text(arch, 0, 0)
oled.text(speed, 0, 12)
oled.text(ram_free, 0, 24)
oled.text(flash_total, 0, 36)
oled.text(version, 0, 48)
oled.show()

print(arch)
print(speed)
print(ram_free)
print(flash_total)
print(version)
