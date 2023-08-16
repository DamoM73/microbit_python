# PiicoDev Intro

PiicoDev hardware has been designed from the ground-up with rapid prototyping and maker education in mind. This product range is produced by an Australian business [Core Electronics](https://core-electronics.com.au/). In addition to selling electronic products, Core Electronics also provide tutorials across a wide range of tutorials.

## Using the PiicoDev modules

Unlike the micro:bit modules, the code that runs the PiicoDev modules is not installed on the micro:bit. This means that you will need to download files and save them to the folder containing your `main.py` file. These files are:

- **PiicoDev Unified Libraries**: &rarr; `PiicoDev_Unified.py`
  - provides the commands for all the PiicoDev modules
  - you will only need one of these in the each folder
- **The device drive**
  - this is different for each PiicoDev module
  - you will need a device driver for each different PiicoDev module you are using. For example, if you are using the Distance Sensor and the OLED Module, you will need a device driver for both of these.

These files can be found on the micro:bit guides for the PiicoDev modules:

### Input Devices

- [PiicoDev Atmospheric Sensor](https://core-electronics.com.au/guides/piicodev-atmospheric-sensor-bme280-quickstart-guide-for-microbit/)
- [PiicoDev Distance Sensor](https://core-electronics.com.au/guides/piicodev-distance-sensor-vl53l1x-micro-bit-guide/)
- [PiicoDev Colour Sensor](https://core-electronics.com.au/guides/micro-bit/piicodev-colour-sensor-veml6040-micro-bit-guide/)
- [PiicoDev Rotary Potentiometer](https://core-electronics.com.au/guides/piicodev-potentiometer-getting-started-guide/#ONVMI66)
- [PiicoDev Slide Potentiometer](https://core-electronics.com.au/guides/piicodev/piicodev-potentiometer-getting-started-guide/#ONVMI66)

### Output Devices

- [PiicoDev OLED Module](https://core-electronics.com.au/guides/micro-bit/piicodev-oled-ssd1306-microbit-guide/)

## Uploading to the micro:bit

If you want to use the micro:bit untethered (not connected to the computer), then you need to upload the **PiicoDev Unified Libraries** and the **device drivers** to the micro:bit along with `main.py`.