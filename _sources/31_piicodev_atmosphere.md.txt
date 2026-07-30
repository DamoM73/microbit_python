# PiicoDev Atmospheric Sensor

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/gOmtS4pFegE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

The PiicoDev Atmospheric Sensor allows you to easily measure barometric pressure, humidity, and temperature. Use it to build your own weather station or perform experiments.

## Getting set up

### Connect the PiicoDev module to your Micro:bit

Plug your Micro:bit into the PiicoDev adapter (buttons LED matrix facing up), connect your module to the adapter via the PiicoDev cable and connect your Micro:bit to your computer with a USB lead.

## Checking the files

1. Stop the program running on your micro:bit by clicking the **Stop** button in Thonny.
2. Open the **20_piico_atmosphere** folder in Thonny.
3. Check that the following files are in the folder:
   - `main.py`
   - `PiicoDev_Unified.py` - Drives I2C communications for PiicoDev modules
   - `PiicoDev_BME280.py` - The device driver for the PiicoDev Atmospheric Sensor
4. To run the program you will need to upload all three files to the micro:bit. To do this, select all three files in the file browser, right-click and select **Upload to micro:bit**.
5. Open `main.py` and your should see the code below

```{literalinclude} ./python_files/20_piico_atmosphere/main.py
:linenos:
```

1. **Predict** what you think will happen. Be specific.
2. **Run** the program.
3. Time to **investigate** the code. What does each line do?

Lets look at the important parts of that code:

- **line 6**: imports all the commands for the atmospheric sensor from the PiicoDev_BME280 library
- **line 7**: import the `sleep_ms` command from the PiicoDev_Unified library and is used the same as `sleep`
- **line 9**: labels the Atmospheric Sensor as `sensor`
- **line 10**: sets the current air pressure as the starting altitude
  - since air pressure changes according to your altitude, if can be used to calculate changes in height
- **line 14**: this uses a Python technique called **unpacking**
  - the `sensor.values()` call returns three values in a tuple
  - each value is assigned to variables in order
    - first value &rarr; tempC
    - second value &rarr; presPa
    - third value &rarr; humRH
- **line 15**: converts the air pressure reading into a more common unit
- **line 16**: if you uncomment this, it will calculating and displaying changes in altitude

## Commands

Below are the different commands available for the Atmospheric Sensor

### `altitude(pressure_sea_level=1013.25)`

| Parameter | Type | Range | Default | Description |
| --- | --- | --- | --- | --- |
| pressure_sea_level | float | any |1013.25 | Enter the current sea level pressure. This value is available from your favourite weather service (hPa)|
| returned | float | | | Altitude (m) |

### `values()`

<div style="width:100%">

| Parameter | Type | Range | Default | Description |
| --- | --- | --- | --- | --- |
| returned 1st | float | any | Temperature (degC) |
| returned 2nd | float | any | Pressure (Pa) |
| returned 3rd | float | Relative humidity (%) |
</div>

## Piico Atmospheric Sensor Exercise 1
1. Stop the program running on your micro:bit by clicking the **Stop** button in Thonny.
2. Open the **20_piico_atmosphere_ex1** folder in Thonny.
3. Edit the `main.py` file so that the micro:bit display to the nearest whole number:
   - temperature when button **A** is pressed
   - humidity when button **B** is pressed

## Piico Atmospheric Sensor Exercise 2
1. Stop the program running on your micro:bit by clicking the **Stop** button in Thonny.
2. Open the **20_piico_atmosphere_ex2** folder in Thonny  
3. Edit the `main.py` file so that the micro:bit upon pressing button **A** it will display the change in altitude from the last time button **A** was pressed.