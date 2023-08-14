# Micro:bit Compass Sensor

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/a3P6LWwPBqM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Your micro:bit has an input sensor for measuring magnetic fields (magnetometer), which you can use as a compass. 

```{admonition} Compass functions
:class: important
Full details can be found at the **[BBC micro:bit MicroPython compass documentation](https://microbit-micropython.readthedocs.io/en/latest/compass.html#module-microbit.compass)**.
```

## `Calibrate`

Before the compass can be used it needs to be calibrated. This process helps the magnetometer sensor accurately determine the orientation and direction of the Earth's magnetic field relative to the micro:bit's axes. The calibration process involves tilting the micro:bit in different directions until all the LEDs are lit up.

The calibration process will automatically run if the compass is called and not calibration data is stored. You can manually initiate the calibration process by calling `compass.calibrate()`.

## Heading

The micro:bit uses `heading()` to return its current bearing ranging from `0` to `359`. The image below shows how these align to the cardinal and intercardinal directions (North, South, East, West, North-East, South-East, North-West and South-West) and the reading is taken from the top of he micro:bit (where the USB socket is). For example, if the top of the micro:bit is pointed towards the South-East (SE) the micro:bit will give a reading of 135&deg;

![compass headings](assets/compass_headings.png)

The code below shows `heading()` in action:

```{literalinclude} ./python_files/heading/main.py
:linenos:
```

### Heading Exercises

1. Make a program that displays `N` when the micro:bit is pointing North.
2. Improve the last program so it shows the 8 cardinal, and intercardinal directions (the ones on the image above) when button **A** is pressed

## Magnetic strength

The magnetometer actually measures magnetic fields. When it is used to measure the Earth's magnetic field turns it into a compass, but we can also use it to measure local magnetic fields.

The `get_field` method returns the strength of the magnetic field around the micro:bit in nano teslas.

Run the program below and use the magnet in your kit to change the value.

```{literalinclude} ./python_files/mag_strength/main.py
:linenos:
```

### Magnetic strength exercises

1. Change the magnetic strength example above so it displays microteslas with no decimals
2. Make a program that shows a smiley face if the magnet is touching the right side of the micro:bit, otherwise is shows and angry face.