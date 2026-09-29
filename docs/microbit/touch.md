# Touch

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/spFD3SxxxHQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

The gold logo and pins 0, 1 and 2 can sense touch using **capacitive touch**, the same idea used by phone screens.

Possible uses:

- extra buttons
- touch-controlled games
- musical instruments
- interactive art

## Connect it

The touch logo and pins are built into the micro:bit, so we don't need to connect anything.

- Each example is a `main.py` file. See [Your First Program](../micropython/first-program.md) for how to create, upload and run it.
- The logo is ready to use. Pins 0, 1 and 2 must be set to capacitive touch mode first.

## Set it up

The touch logo and pins are part of the `microbit` library. We import it at the top of every program:

```python linenums="1"
from microbit import *
```

## Methods

| Method | Parameters | Returns | Description |
| --- | --- | --- | --- |
| `pin_logo.is_touched()` | none | Boolean | `True` if the logo is being touched |
| `pin0.set_touch_mode(pin0.CAPACITIVE)` | touch mode | none | Makes pin 0 sense touch like the logo (also `pin1`, `pin2`) |
| `pin0.is_touched()` | none | Boolean | `True` if pin 0 is being touched (also `pin1`, `pin2`) |

### `pin_logo.is_touched()`

Checks whether the gold logo is being touched right now.

```python linenums="1"
--8<-- "examples/microbit/touch/pin_logo/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → imports all the commands from the `microbit` library.
    - **line 4** → starts an endless loop.
    - **line 5** → checks if the logo is being touched.
    - **line 6** → if it is, shows a happy face.
    - **line 7** → if it isn't…
    - **line 8** → …shows a sad face.

### `set_touch_mode()` and `is_touched()` on pins

`set_touch_mode()` makes a pin sense touch the same way as the logo. `is_touched()` then checks whether that pin is being touched.

```python linenums="1"
--8<-- "examples/microbit/touch/pins/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → imports all the commands from the `microbit` library.
    - **line 4** → sets pin 0 to capacitive touch mode.
    - **line 7** → starts an endless loop.
    - **line 8** → checks if pin 0 is being touched.
    - **line 9** → if it is, shows a happy face.
    - **line 10** → if it isn't…
    - **line 11** → …shows a sad face.

## Documentation

Documentation is the official guide written by the people who made the code library, and we can use it to look up every method and its parameters, including ones that aren't covered on this page.

- [BBC micro:bit MicroPython — pins and touch](https://microbit-micropython.readthedocs.io/en/v2-docs/pin.html)

## Exercises

!!! primm "PRIMM"
    Time to **modify** the code and see what happens.

Starter files are in the `touch` folder of your tutorial files. Solutions are on the [Exercise Solutions](../reference/solutions.md#touch) page.

### Exercise 1

Starter: `touch/ex1_move_pixel`

Can you light the pixel at `(2, 2)`, then move it right when pin 2 is touched and left when pin 0 is touched?
