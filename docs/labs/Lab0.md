# Installing Thonny and Flashing MicroPython Firmware
This can be done ahead of time to allow students more time to concentrate on coding, or it can be used as a way to introduce students to the Thonny editor and its tools for flashing firmware on newly purchased devices.

## Installing the USB Device Driver
As a prerequisite, you'll need a device driver for your operating system (on Windows, at least.) The WeMos LOLIN32 and clones use the Silicon Labs CP210x chip for USB communication. The steps below detail how to get the CP210x driver installed.

> The web site where you get the drivers uses a pop-up window for the download. Your browser may ask for confirmation or may block it outright unless you add an exception.

1. Navigate to https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers
2. Click the _Downloads_ tab.
3. Download the driver for your OS and open the ZIP file.
4. Follow the instructions in the Release Notes text file to install the driver.
5. Run Device Manager (if using Windows) and look under Ports (COM & LPT) to verify the Silicon Labs CP210x is found.

## Installing Thonny
Visit [thonny.org](https://thonny.org/) to download the installer program for the Thonny editor. Installation is like any other program. For more detailed instructions, see the [Thonny Wiki](https://github.com/thonny/thonny/wiki/) where you will find articles for installing on Windows, macOS, and Linux operating systems.

> If you are using a Raspberry Pi 400 as the host computer, the Raspberry Pi OS already has Thonny installed, so you can skip Thonny installation, but you still need to configure the ESP32 and install firmware as shown in the following steps.

## Downloading MicroPython Firmware
You'll need to install MicroPython on the microcontroller. This is a one-time task.

1. Plug the ESP32 into the host computer.
2. Go to the MicroPython web site's [ESP32 firmware download](https://micropython.org/download/esp32/).
3. Skip over the installation instructions (Thonny makes it easier) and scroll down to Firmware Releases.
4. Find the latest .bin file (v1.18 at the time this document was written.)
5. Download the file, making a note of where it's saved.

## Configuring for the ESP32 Microcontroller
Once Thonny is installed, we need to tell it about the microcontroller we're using.

1. Attach the ESP32 microcotroller to the host computer (where Thonny is installed) via the USB cable.
2. Start Thonny.
3. Navigate to Tools > Options, and select the Interpreter tab.
4. Choose MicroPython (ESP32) from the interpreter drop-down selector.
5. Choose SiliconLabs from the port drop-down. [Figure 1]
6. Leave the dialog box open for the next steps.

## Flashing Firmware
After Thonny is configured for the ESP32, you can use it to write the MicroPython firmware to the microcontroller. In the same area where you configured the interpreter and port selections, you'll see a link that reads Install or Update Firmware. It's just above the OK button.

1. Click the Install or Update Firmware link.
2. Select the Silicon Labs USB to UART Bridge for the port.
3. Browse to where you downloaded the MicroPython firmware file (e.g. esp32-20220117-v1.18.bin).
4. Leave the Flash Mode options as-is.
5. Click Install. [Figure 2]

Progress messages will scroll by, including the percent complete. Click close when it's finished. [Figure 3]

## Screenshots

![Interpreter Options](https://github.com/DavesCodeMusings/smart-thermostat-lab/blob/main/docs/labs/screenshots/options-interpreter.png)

_Figure 1: Interpreter options_

![Firmware Installer](https://github.com/DavesCodeMusings/smart-thermostat-lab/blob/main/docs/labs/screenshots/firmware.png)

_Figure 2: Selections for firmware installation_

![Firmware Flash Complete](https://github.com/DavesCodeMusings/smart-thermostat-lab/blob/main/docs/labs/screenshots/firmware-done.png)

_Figure 3: Firmware installation complete_
