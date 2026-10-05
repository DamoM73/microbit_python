# Light Sensor

!!! learn "On this page we will learn"
    - how the micro:bit measures light with its display
    - how to read the light level

!!! terms "Terminology"
    - **light sensor** – a sensor that measures how much light is shining on it; on the micro:bit, the display LEDs do this job.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/ii0U_FMr-Z4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

The micro:bit uses the LEDs on its display to measure how much light is shining on it.

Possible uses:

- night lights
- day and night detectors
- light-activated alarms
- automatic brightness

## Connect it

The light sensor is the display itself, so we don't need to connect anything.

- Each example is a `main.py` file. See [Your First Program](../micropython/first-program.md) for how to create, upload and run it.
- Readings go from `0` (dark) to `255` (bright).

## Set it up

The light sensor is part of the `microbit` library. We import it at the top of every program:

```python linenums="1"
from microbit import *
```

## Methods

| Method | Parameters | Returns | Description |
| --- | --- | --- | --- |
| `display.read_light_level()` | none | int (0–255) | The light level on the display |

### `display.read_light_level()`

Returns how much light is shining on the display, from `0` (dark) to `255` (bright).

```python linenums="1"
--8<-- "examples/microbit/light/read_light_level/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → imports all the commands from the `microbit` library.
    - **line 4** → starts an endless loop.
    - **line 5** → reads the light level and scrolls it across the display.

## Documentation

Documentation is the official guide written by the people who made the code library, and we can use it to look up every method and its parameters, including ones that aren't covered on this page.

- [BBC micro:bit MicroPython — display.read_light_level](https://microbit-micropython.readthedocs.io/en/v2-docs/display.html#microbit.display.read_light_level)

## Exercises

!!! primm "PRIMM"
    Time to **modify** the code and see what happens.

Starter files are in the `light` folder of your tutorial files. Solutions are on the [Exercise Solutions](../reference/solutions.md#light-sensor) page.

### Exercise 1

Starter: `light/ex1_up_down`

Can you create a program that checks the light level every 2 seconds, and shows an up arrow if it has increased since the last check, or a down arrow if it has decreased?

### Exercise 2

Starter: `light/ex2_night_light`

Can you create a program that turns on all the LEDs when the light level falls below `100`?
