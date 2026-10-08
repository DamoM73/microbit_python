# Distance Sensor

!!! learn "On this page we will learn"
    - how to connect the Distance Sensor
    - how to measure the distance to an object

!!! terms "Terminology"
    - **distance sensor** – a sensor that measures how far away an object is.
    - **laser** – a narrow, focused beam of light; the Distance Sensor uses an invisible one to measure distance.

!!! tip "Files we need"
    Every program that uses the Distance Sensor needs these files in its folder, next to `main.py`. Click a file name to download it.

    - [PiicoDev_Unified.py](../drivers/PiicoDev_Unified.py){ download="PiicoDev_Unified.py" } → handles communication with all PiicoDev modules
    - [PiicoDev_VL53L1X.py](../drivers/PiicoDev_VL53L1X.py){ download="PiicoDev_VL53L1X.py" } → the Distance Sensor driver

    The example folders in your tutorial files already have these files. See [Upload the files](../micropython/piicodev.md#upload-the-files) for how to put them on the micro:bit.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/CjbOWeBz35s" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

The PiicoDev Distance Sensor (VL53L1X) uses a laser to measure the distance to an object, up to 4 metres away.

Possible uses:

- object detection for robots
- parking sensors
- measuring tapes
- gesture and proximity controls

## Connect it

1. Connect the sensor to the PiicoDev adapter with a PiicoDev cable. See [Using PiicoDev](../micropython/piicodev.md).
2. Upload these files to the micro:bit with `main.py`:
    - `PiicoDev_Unified.py`
    - `PiicoDev_VL53L1X.py`

!!! warning
    The sensor uses an invisible laser. Don't look into the sensor window.

## Set it up

```python linenums="1"
from microbit import *
from PiicoDev_VL53L1X import PiicoDev_VL53L1X

sensor = PiicoDev_VL53L1X()
```

## Methods

| Method | Parameters | Returns | Description |
| --- | --- | --- | --- |
| `sensor.read()` | none | int (mm) | Distance to the nearest object, up to 4000 mm |

### `read()`

Returns the distance to the nearest object in millimetres.

```python linenums="1"
--8<-- "examples/piicodev/distance/read/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → imports all the commands from the `microbit` library.
    - **line 2** → imports the Distance Sensor driver.
    - **line 5** → creates the sensor and calls it `sensor`.
    - **line 8** → starts an endless loop.
    - **line 9** → measures the distance in millimetres and prints it in the Shell.
    - **line 10** → waits 100 milliseconds before the loop repeats.

## Documentation

Documentation is the official guide written by the people who made the code library, and we can use it to look up every method and its parameters, including ones that aren't covered on this page.

- [Core Electronics — Distance Sensor micro:bit guide](https://core-electronics.com.au/guides/piicodev-distance-sensor-vl53l1x-micro-bit-guide/)
- [PiicoDev VL53L1X driver](https://github.com/CoreElectronics/CE-PiicoDev-VL53L1X-MicroPython-Module)

## Exercises

!!! primm "PRIMM"
    Time to **modify** the code and see what happens.

Starter files are in the `distance` folder of your tutorial files. Solutions are on the [Exercise Solutions](../reference/solutions.md#distance-sensor) page.

### Exercise 1

Starter: `distance/ex1_button_reading`

Can you make the micro:bit show the distance when button **A** is pressed?
