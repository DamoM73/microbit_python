# Temperature

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/mrHn8eZ9eqg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

The temperature sensor inside the micro:bit's processor gives an approximate reading of the air temperature in degrees Celsius.

Possible uses:

- weather stations
- overheating alerts
- room monitors

## Connect it

The temperature sensor is built into the micro:bit, so there is nothing to connect.

- Each example is a `main.py` file. See [Your First Program](../micropython/first-program.md) for how to create, upload and run it.
- The sensor is inside the processor, so the reading can be a little higher than the air temperature when the micro:bit has been working hard.

## Set it up

`temperature()` is part of the `microbit` library. Import it at the top of every program:

```python linenums="1"
from microbit import *
```

## Methods

| Method | Parameters | Returns | Description |
| --- | --- | --- | --- |
| `temperature()` | none | int (°C) | The current temperature |

### `temperature()`

```python linenums="1"
--8<-- "examples/microbit/temperature/temperature/main.py"
```

??? note "Code explanation"
    - line 1 → imports all the commands from the `microbit` library
    - line 4 → starts an endless loop
    - line 5 → gets the current temperature and stores it in `temp`
    - line 6 → turns `temp` into a string, adds `"C"` for Celsius and scrolls it across the display
    - line 7 → waits 1 second before the loop repeats

## Documentation

- [BBC micro:bit MicroPython — temperature](https://microbit-micropython.readthedocs.io/en/v2-docs/microbit.html#microbit.temperature)

## Exercises

Starter files are in the `temperature` folder of your tutorial files. Solutions are on the [Exercise Solutions](../reference/solutions.md#temperature) page.

### Exercise 1

Starter: `temperature/ex1_min_max`

Check the temperature every 2 seconds and keep track of the minimum and maximum. Show the minimum when button **A** is pressed and the maximum when button **B** is pressed.

### Exercise 2

Starter: `temperature/ex2_comfort`

A comfortable room temperature is between 20 and 22 °C. Show a happy face if the temperature is in that range, an up arrow if it is too high, and a down arrow if it is too low.
