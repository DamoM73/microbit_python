# Light Sensor

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/ii0U_FMr-Z4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

The micro:bit uses the LEDs on its display to measure how much light is shining on it.

Possible uses:

- night lights
- day and night detectors
- light-activated alarms
- automatic brightness

## Connect it

The light sensor is the display itself, so there is nothing to connect.

- Each example is a `main.py` file. See [Your First Program](../micropython/first-program.md) for how to create, upload and run it.
- Readings go from `0` (dark) to `255` (bright).

## Set it up

The light sensor is part of the `microbit` library. Import it at the top of every program:

```python linenums="1"
from microbit import *
```

## Methods

| Method | Parameters | Returns | Description |
| --- | --- | --- | --- |
| `display.read_light_level()` | none | int (0–255) | The light level on the display |

### `display.read_light_level()`

```python linenums="1"
--8<-- "examples/microbit/light/read_light_level/main.py"
```

??? note "Code explanation"
    - line 1 → imports all the commands from the `microbit` library
    - line 4 → starts an endless loop
    - line 5 → reads the light level and stores it in `light`
    - line 6 → scrolls the light level across the display
    - line 7 → waits 500 milliseconds before the loop repeats

## Documentation

- [BBC micro:bit MicroPython — display.read_light_level](https://microbit-micropython.readthedocs.io/en/v2-docs/display.html#microbit.display.read_light_level)

## Exercises

Starter files are in the `light` folder of your tutorial files. Solutions are on the [Exercise Solutions](../reference/solutions.md#light-sensor) page.

### Exercise 1

Starter: `light/ex1_up_down`

Check the light level every 2 seconds. Show an up arrow if it has increased since the last check, or a down arrow if it has decreased.

### Exercise 2

Starter: `light/ex2_night_light`

Turn on all the LEDs when the light level falls below `100`.
