# PiicoDev Distance Sensor

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/CjbOWeBz35s" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

The PiicoDev Distance Sensor is a long-distance laser-ranging sensor that uses Time-of-Flight (ToF) to accurately measure distances up to 4m.

## Getting set up

### Connect the PiicoDev module to your Micro:bit

Plug your Micro:bit into the PiicoDev adapter (buttons LED matrix facing up), connect your sensor to the adapter via the PiicoDev cable and connect your Micro:bit to your computer with a USB lead.

## Example code

1. Stop the program running on your micro:bit by clicking the **Stop** button in Thonny.
2. Open the **22_piico_distance_example** folder in Thonny.
3. Check that the following files are in the folder:
   - `main.py`
   - `PiicoDev_Unified.py` - Drives I2C communications for PiicoDev modules
   - `PiicoDev_VL53L1X.py` - The device driver for the PiicoDev Distance Sensor
4. To run the program you will need to upload all three files to the micro:bit. To do this, select all three files in the file browser, right-click and select **Upload to micro:bit**.
5. Open `main.py` and your should see the code below

```{literalinclude} ./python_files/22_piico_distance_example/main.py
:linenos:
```
1. **Predict** what you think will happen. Be specific.
2. **Run** the program.
3. Time to **investigate** the code. What does each line do?

Lets look at the important parts of that code:

- **line 1**: imports all the microbit commands
- **line 2** imports all the commands for the atmospheric sensor from the PiicoDev_BME280 library
- **line 6**: labels the distance Sensor as `distSensor`
- **line 13**: takes a reading from the sensor
- **line 16**: converts the reaidn into a string then append mm to it
- **line 19**: prints the reading value
- **line 20**: sleeps  100ms

## Commands

### `read()`

Return the distance to object in front of sensor in mm up to 4000

| Parameter | Type | Unit | Description |
| --- | --- | --- | --- |
| returned | int | mm | Range |

## Piicodev Distance Exercise 1

1. Stop the program running on your micro:bit by clicking the **Stop** button in Thonny.
2. Open the **22_piico_distance_ex1** folder in Thonny.
3. In **main.py**, write a program that displays a distance reading on the micro:bit when button **A** is pressed.