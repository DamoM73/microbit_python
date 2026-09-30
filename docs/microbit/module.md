# microbit Module

!!! learn "On this page we will learn"
    - how to pause a program with `sleep()`
    - how to measure how long a program has been running
    - how to run code on a schedule with `run_every()`

The `microbit` module contains general functions for pausing a program, measuring time and running code on a schedule.

Possible uses:

- timers and stopwatches
- games with time limits
- tasks that repeat in the background

## Connect it

These functions are built into MicroPython on the micro:bit, so we don't need to connect anything.

- Each example is a `main.py` file. See [Your First Program](../micropython/first-program.md) for how to create, upload and run it.
- Times are in **milliseconds** (ms). There are `1000` milliseconds in one second.
- A **module** is a collection of code you can import into your program. `from microbit import *` imports everything in the `microbit` module, including the display, buttons and the functions on this page.

## Set it up

We import the `microbit` module at the top of every program:

```python linenums="1"
from microbit import *
```

## Methods

| Method | Parameters | Returns | Description |
| --- | --- | --- | --- |
| `sleep(ms)` | `ms`: milliseconds | none | Pauses the program |
| `running_time()` | none | int (ms) | Time since the micro:bit was turned on or reset |
| `run_every(function, s=1)` | `function`: function to run<br>`h`, `min`, `s` or `ms`: how often | none | Runs a function repeatedly in the background |

### `sleep()`

Pauses the program for a number of milliseconds before running the next line.

```python linenums="1"
--8<-- "examples/microbit/module/sleep/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → imports all the commands from the `microbit` library.
    - **line 4** → prints a line in the Shell.
    - **line 5** → prints the next line straight away.
    - **line 6** → pauses the program for 2000 milliseconds (2 seconds).
    - **line 7** → prints the last line after the pause.

### `running_time()`

Returns how many milliseconds have passed since the micro:bit was turned on or reset.

```python linenums="1"
--8<-- "examples/microbit/module/running_time/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → imports all the commands from the `microbit` library.
    - **line 4** → starts an endless loop.
    - **line 5** → prints the number of milliseconds since the micro:bit started.
    - **line 6** → waits 1 second before the loop repeats.

### `run_every()`

Runs a function over and over at a set time interval.

The function keeps running on schedule while the main loop does something else.

```python linenums="1"
--8<-- "examples/microbit/module/run_every/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → imports all the commands from the `microbit` library.
    - **line 2** → imports the `music` module.
    - **line 5** → defines a function called `beep`.
    - **line 6** → the function plays an 880 Hz tone for 100 milliseconds.
    - **line 8** → runs `beep` every 1 second in the background.
    - **line 11** → starts an endless loop.
    - **line 12** → scrolls `Hello`, while the beep keeps running every second.

## Documentation

Documentation is the official guide written by the people who made the code library, and we can use it to look up every method and its parameters, including ones that aren't covered on this page.

- [BBC micro:bit MicroPython — microbit module](https://microbit-micropython.readthedocs.io/en/v2-docs/microbit.html)
