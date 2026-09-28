# Compass

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/a3P6LWwPBqM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

The compass (a **magnetometer**) measures magnetic fields, so it can find which direction the micro:bit is pointing and detect nearby magnets.

Possible uses:

- navigation tools
- treasure hunts
- magnet-triggered switches

## Connect it

The compass is built into the micro:bit, so there is nothing to connect.

- Each example is a `main.py` file. See [Your First Program](../micropython/first-program.md) for how to create, upload and run it.
- The compass must be **calibrated** before it gives headings. Calibration starts automatically the first time a heading is needed: tilt the micro:bit in every direction until all the LEDs are lit.
- Headings are measured from the top of the micro:bit (the USB socket end), from `0` to `359` degrees. For example, pointing South-East gives `135`.

![compass headings](../assets/compass_headings.png)

## Set it up

The compass is part of the `microbit` library. Import it at the top of every program:

```python linenums="1"
from microbit import *
```

## Methods

| Method | Parameters | Returns | Description |
| --- | --- | --- | --- |
| `compass.calibrate()` | none | none | Starts the calibration game |
| `compass.is_calibrated()` | none | Boolean | `True` if the compass has been calibrated |
| `compass.heading()` | none | int (0–359) | The direction the micro:bit is pointing, in degrees |
| `compass.get_field_strength()` | none | int (nanotesla) | The strength of the magnetic field around the micro:bit |

### `compass.calibrate()`

```python linenums="1"
--8<-- "examples/microbit/compass/calibrate/main.py"
```

??? note "Code explanation"
    - line 1 → imports all the commands from the `microbit` library
    - line 4 → starts calibration. Tilt the micro:bit until every LED is lit.
    - line 7 → starts an endless loop
    - line 8 → shows a tick once calibration is finished

### `compass.is_calibrated()`

```python linenums="1"
--8<-- "examples/microbit/compass/is_calibrated/main.py"
```

??? note "Code explanation"
    - line 1 → imports all the commands from the `microbit` library
    - line 4 → starts an endless loop
    - line 5 → checks if the compass has been calibrated
    - line 6 → if it has, shows a tick
    - line 7 → if it hasn't…
    - line 8 → …shows a cross
    - line 9 → waits 1 second before the loop repeats

### `compass.heading()`

```python linenums="1"
--8<-- "examples/microbit/compass/heading/main.py"
```

??? note "Code explanation"
    - line 1 → imports all the commands from the `microbit` library
    - line 4 → starts an endless loop
    - line 5 → gets the compass heading and stores it in `heading`
    - line 6 → scrolls the heading across the display
    - line 7 → waits 500 milliseconds before the loop repeats

### `compass.get_field_strength()`

```python linenums="1"
--8<-- "examples/microbit/compass/get_field_strength/main.py"
```

??? note "Code explanation"
    - line 1 → imports all the commands from the `microbit` library
    - line 4 → starts an endless loop
    - line 5 → gets the magnetic field strength and stores it in `field`
    - line 6 → scrolls the field strength across the display
    - line 7 → waits 500 milliseconds before the loop repeats

## Documentation

- [BBC micro:bit MicroPython — compass](https://microbit-micropython.readthedocs.io/en/v2-docs/compass.html)

## Exercises

Starter files are in the `compass` folder of your tutorial files. Solutions are on the [Exercise Solutions](../reference/solutions.md#compass) page.

### Exercise 1

Starter: `compass/ex1_north`

Show `N` when the micro:bit is pointing North.

### Exercise 2

Starter: `compass/ex2_eight_points`

When button **A** is pressed, show which of the 8 compass directions in the image above the micro:bit is pointing (N, NE, E, SE, S, SW, W, NW).

### Exercise 3

Starter: `compass/ex3_microtesla`

Change the `get_field_strength()` example to show the reading in microtesla with no decimal places (1 microtesla = 1000 nanotesla).

### Exercise 4

Starter: `compass/ex4_magnet`

Show a happy face when a magnet is touching the right side of the micro:bit. Otherwise show an angry face.
