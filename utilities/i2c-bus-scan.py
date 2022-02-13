# Scan for I2C devices and print addresses found

from machine import Pin, SoftI2C

# These values work with WeMos LOLIN32 OLED
i2c_clock = 4
i2c_data = 5

i2c = SoftI2C(scl=Pin(i2c_clock), sda=Pin(i2c_data))

print('Scanning i2c bus...')
devices = i2c.scan()

if (len(devices) == 0):
    print("No i2c device !")
else:
    print('Devices found:', len(devices))
    for address in devices:  
        print("Address: ", hex(address))
