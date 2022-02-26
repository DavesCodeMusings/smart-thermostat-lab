# smart-thermostat
A series of labs to build a smart thermostat using MicroPython. Get started by viewing [the labs](docs/index.md).

## Learning objectives
* Introduction to microcontrollers and MicroPython programming language
* Writing code to read values from internal and external sensors
* Building a user interface with the built-in display and touch inputs
* Communicating with other devices as part of an internet of things (IoT)

## Hardware requirements
* WeMos Lolin32 OLED ESP32 microcontroller ([or similar clone](http://www.hiletgo.com/ProductDetail/1997554.html)).
* Micro-B USB cable for attaching microcontroller board to host computer.
* DHT11 temperature / humidity sensor.
* Host computer with USB port capable of downloading and installing software below.

> Chromebooks used in schools often have policies that prevent installation of software making them unsuitable.
> A [Raspberry Pi 400](https://www.raspberrypi.com/products/raspberry-pi-400/?variant=raspberry-pi-400-us-kit)
> kit has everything needed except the HDMI monitor.
> [Other items](https://www.amazon.com/hz/wishlist/ls/3DOVN9NREQHIB?ref_=wl_share) can be found online as well.

## Software requirements
* [Thony Editor](https://thonny.org/) installed on host computer.
* [MicroPython firmware for ESP32](https://micropython.org/download/esp32/)

## Network access requirements
* The host computer will need access to the internet for downloading host software, MicroPython firmware and modules.
* The microcontroller will need WiFi access for the internet of things (IoT) labs.

> School networks may not be set up to allow access from the microcontroller. It may be possible to use an
> inexpensive home internet router for the purpose of connecting the microcontrollers to an isolated network.
