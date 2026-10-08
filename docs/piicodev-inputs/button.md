# Button

!!! learn "On this page we will learn"
    - how to connect the PiicoDev Button
    - how to check whether it is pressed or was pressed
    - how to detect double presses and count presses

!!! tip "Files we need"
    Every program that uses the Button needs these files in its folder, next to `main.py`. Click a file name to download it.

    - [PiicoDev_Unified.py](../drivers/PiicoDev_Unified.py){ download="PiicoDev_Unified.py" } → handles communication with all PiicoDev modules
    - [PiicoDev_Switch.py](../drivers/PiicoDev_Switch.py){ download="PiicoDev_Switch.py" } → the Button driver

    The example folders in your tutorial files already have these files. See [Upload the files](../micropython/piicodev.md#upload-the-files) for how to put them on the micro:bit.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/oNsP-YnHCho" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

The PiicoDev Button is a large push button that detects presses, double presses and counts how many times it has been pressed.

Possible uses:

- extra game controls
- start and stop buttons
- emergency stop buttons
- counters

## Connect it

1. Connect the button to the PiicoDev adapter with a PiicoDev cable. See [Using PiicoDev](../micropython/piicodev.md).
2. Upload these files to the micro:bit with `main.py`:
    - `PiicoDev_Unified.py`
    - `PiicoDev_Switch.py`
3. To use more than one button, give each one a different setting on its **ID switches**, then create each one with `PiicoDev_Switch(id=[1, 0, 0, 0])` and so on.

## Set it up

```python linenums="1"
from microbit import *
from PiicoDev_Switch import PiicoDev_Switch

button = PiicoDev_Switch()
```

## Methods

| Method | Parameters | Returns | Description |
| --- | --- | --- | --- |
| `button.is_pressed` | none | Boolean | `True` while the button is held down |
| `button.was_pressed` | none | Boolean | `True` if the button was pressed since the last check |
| `button.was_double_pressed` | none | Boolean | `True` if the button was double pressed since the last check |
| `button.press_count` | none | int | Number of presses since the last check |

These are **properties**, so they have no brackets.

### `is_pressed`

Is `True` while the button is being held down.

```python linenums="1"
--8<-- "examples/piicodev/button/is_pressed/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → imports all the commands from the `microbit` library.
    - **line 2** → imports the Button driver.
    - **line 5** → creates the button and calls it `button`.
    - **line 8** → starts an endless loop.
    - **line 9** → checks if the button is being held down.
    - **line 10** → if it is, shows a happy face.
    - **line 11** → if it isn't…
    - **line 12** → …shows a sad face.
    - **line 13** → waits 100 milliseconds before the loop repeats.

### `was_pressed`

Is `True` if the button has been pressed since the last check, even if it has been let go.

```python linenums="1"
--8<-- "examples/piicodev/button/was_pressed/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → imports all the commands from the `microbit` library.
    - **line 2** → imports the Button driver.
    - **line 5** → creates the button and calls it `button`.
    - **line 8** → starts an endless loop.
    - **line 9** → checks if the button was pressed since the last check.
    - **line 10** → if it was, shows a happy face.
    - **line 11** → if it wasn't…
    - **line 12** → …shows a sad face.
    - **line 13** → waits 1 second. A quick press during this wait is still detected on the next loop.

### `was_double_pressed`

Is `True` if the button has been pressed twice quickly since the last check.

```python linenums="1"
--8<-- "examples/piicodev/button/was_double_pressed/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → imports all the commands from the `microbit` library.
    - **line 2** → imports the Button driver.
    - **line 5** → creates the button and calls it `button`.
    - **line 8** → starts an endless loop.
    - **line 9** → checks if the button was double pressed since the last check.
    - **line 10** → if it was, shows a happy face.
    - **line 11** → if it wasn't…
    - **line 12** → …shows a sad face.
    - **line 13** → waits 1 second before the loop repeats.

### `press_count`

Gives the number of presses since the last check, then resets the count to `0`.

```python linenums="1"
--8<-- "examples/piicodev/button/press_count/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → imports all the commands from the `microbit` library.
    - **line 2** → imports the Button driver.
    - **line 5** → creates the button and calls it `button`.
    - **line 8** → starts an endless loop.
    - **line 9** → prints the number of presses since the last check, then the count resets.
    - **line 10** → waits 2 seconds, giving you time to press the button.

## Documentation

Documentation is the official guide written by the people who made the code library, and we can use it to look up every method and its parameters, including ones that aren't covered on this page.

- [PiicoDev Switch driver](https://github.com/CoreElectronics/CE-PiicoDev-Switch-MicroPython-Module)
