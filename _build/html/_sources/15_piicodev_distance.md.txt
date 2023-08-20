# PiicoDev Distance Sensor

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/CjbOWeBz35s" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

The PiicoDev Distance Sensor is a long-distance laser-ranging sensor that uses Time-of-Flight (ToF) to accurately measure distances up to 4m.

## Getting set up

### Connect the PiicoDev module to your Micro:bit

Plug your Micro:bit into the PiicoDev adapter (buttons LED matrix facing up), connect your sensor to the adapter via the PiicoDev cable and connect your Micro:bit to your computer with a USB lead.

### Download the PiicoDev Modules and Example Code

Create a new folder for this example. Then download the following files and save them to your new folder (Right Click > "Save Link As").

- **[`PiicoDev_Unified.py`](https://raw.githubusercontent.com/CoreElectronics/CE-PiicoDev-Unified/main/min/PiicoDev_Unified.py)** - The PiicoDev Unified Libraries: Drives I2C communications for PiicoDev modules
- **[`PiicoDev_VL53L1X.py`](https://raw.githubusercontent.com/CoreElectronics/CE-PiicoDev-VL53L1X-MicroPython-Module/main/min/PiicoDev_VL53L1X.py)** - The device driver.
- **[`main.py`](https://raw.githubusercontent.com/CoreElectronics/CE-PiicoDev-VL53L1X-MicroPython-Module/main/main.py)** - an example script for this PiicoDev Sensor

## Example code

Below is the example code provided my Core Electronics in the `main.py`:

```{literalinclude} ./python_files/piico_distance_example/main.py
:linenos:
```

Lets look at the important parts of that code:

- **line 1**: imports all the commands for the atmospheric sensor from the PiicoDev_BME280 library
- **line 4**: labels the distance Sensor as `distSensor`
- **line 7**: takes a reading from the sensor
- **line 8**: prints the reading value

## Commands

### `read()`

Return the distance to object in front of sensor in mm up to 4000

| Parameter | Type | Unit | Description |
| --- | --- | --- | --- |
| returned | int | mm | Range |

## Exercise

1. Make a program that displays a distance reading on the micro:bit when button **A** is pressed