# Atmospheric Sensor

!!! learn "On this page we will learn"
    - how to connect the Atmospheric Sensor
    - how to read temperature, air pressure and humidity
    - how to estimate altitude from air pressure

!!! terms "Terminology"
    - **air pressure** – the weight of the air pushing down on us, which drops as we go higher.
    - **humidity** – the amount of water vapour in the air, measured as a percentage.
    - **altitude** – the height above sea level, which the Atmospheric Sensor works out from air pressure.
    - **pascal** – the unit for measuring pressure (Pa); 100 pascals make 1 hectopascal (hPa).

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/gOmtS4pFegE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

The PiicoDev Atmospheric Sensor (BME280) measures temperature, air pressure and humidity.

Possible uses:

- weather stations
- indoor climate monitors
- measuring changes in height (altitude)
- science experiments

## Connect it

1. Connect the sensor to the PiicoDev adapter with a PiicoDev cable. See [Using PiicoDev](../micropython/piicodev.md).
2. Upload these files to the micro:bit with `main.py`:
    - `PiicoDev_Unified.py`
    - `PiicoDev_BME280.py`

## Set it up

```python linenums="1"
from microbit import *
from PiicoDev_BME280 import PiicoDev_BME280

sensor = PiicoDev_BME280()
```

## Methods

| Method | Parameters | Returns | Description |
| --- | --- | --- | --- |
| `sensor.values()` | none | tuple `(temp, pressure, humidity)` | Temperature (°C), air pressure (Pa) and relative humidity (%) |
| `sensor.altitude(pressure_sea_level=1013.25)` | `pressure_sea_level`: today's sea-level pressure in hPa | float (m) | Height above sea level, calculated from air pressure |

### `values()`

Returns the temperature (°C), air pressure (Pa) and humidity (%) together as a tuple.

```python linenums="1"
--8<-- "examples/piicodev/atmospheric/values/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → imports all the commands from the `microbit` library.
    - **line 2** → imports the Atmospheric Sensor driver.
    - **line 5** → creates the sensor and calls it `sensor`.
    - **line 8** → starts an endless loop.
    - **line 9** → prints the temperature (°C), air pressure (Pa) and humidity (%) in the Shell.
    - **line 10** → waits 1 second before the loop repeats.

### `altitude()`

Returns the height above sea level in metres, calculated from the air pressure.

Air pressure drops as you go higher, so the sensor can work out changes in height. For an accurate height above sea level, enter today's sea-level pressure from the [Bureau of Meteorology](http://www.bom.gov.au/).

```python linenums="1"
--8<-- "examples/piicodev/atmospheric/altitude/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → imports all the commands from the `microbit` library.
    - **line 2** → imports the Atmospheric Sensor driver.
    - **line 5** → creates the sensor and calls it `sensor`.
    - **line 8** → starts an endless loop.
    - **line 9** → prints the altitude in metres in the Shell.
    - **line 10** → waits 1 second before the loop repeats.

## Documentation

Documentation is the official guide written by the people who made the code library, and we can use it to look up every method and its parameters, including ones that aren't covered on this page.

- [Core Electronics — Atmospheric Sensor micro:bit guide](https://core-electronics.com.au/guides/piicodev-atmospheric-sensor-bme280-quickstart-guide-for-microbit/)
- [PiicoDev BME280 driver](https://github.com/CoreElectronics/CE-PiicoDev-BME280-MicroPython-Module)

## Exercises

!!! primm "PRIMM"
    Time to **modify** the code and see what happens.

Starter files are in the `atmospheric` folder of your tutorial files. Solutions are on the [Exercise Solutions](../reference/solutions.md#atmospheric-sensor) page.

### Exercise 1

Starter: `atmospheric/ex1_buttons`

Can you make the micro:bit show the temperature, rounded to a whole number, when button **A** is pressed, and the humidity when button **B** is pressed?

### Exercise 2

Starter: `atmospheric/ex2_height_change`

Can you make the micro:bit show how much the altitude has changed since the last time button **A** was pressed?
