# Accelerometer

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/UT35ODxvmS0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

The accelerometer measures movement and tilt in three directions and recognises gestures such as shaking or turning face up.

Possible uses:

- step counters
- shake-to-roll dice
- tilt-controlled games
- motion alarms

## Connect it

The accelerometer is built into the micro:bit, so there is nothing to connect.

- Each example is a `main.py` file. See [Your First Program](../micropython/first-program.md) for how to create, upload and run it.
- Most examples print readings. Watch them in Thonny's **Shell**.
- Movement is measured along three **axes** (imaginary lines):
    - **x** → tilting left and right
    - **y** → tilting forwards and backwards
    - **z** → moving up and down
- Readings are in **milli-g**. `0` means level on that axis; about `1024` or `-1024` is the pull of gravity.
- Gestures are strings: `"up"`, `"down"`, `"left"`, `"right"`, `"face up"`, `"face down"`, `"freefall"`, `"3g"`, `"6g"`, `"8g"` and `"shake"`.

## Set it up

The accelerometer is part of the `microbit` library. Import it at the top of every program:

```python linenums="1"
from microbit import *
```

## Methods

| Method | Parameters | Returns | Description |
| --- | --- | --- | --- |
| `accelerometer.get_x()` | none | int (milli-g) | Movement along the x-axis |
| `accelerometer.get_y()` | none | int (milli-g) | Movement along the y-axis |
| `accelerometer.get_z()` | none | int (milli-g) | Movement along the z-axis |
| `accelerometer.get_values()` | none | tuple `(x, y, z)` | All three readings at once |
| `accelerometer.current_gesture()` | none | string | The gesture happening right now |
| `accelerometer.is_gesture(name)` | `name`: gesture string | Boolean | `True` if that gesture is happening right now |
| `accelerometer.was_gesture(name)` | `name`: gesture string | Boolean | `True` if that gesture happened since the last call |
| `accelerometer.get_gestures()` | none | tuple of strings | All gestures since the last call, oldest first |

### `get_x()`

```python linenums="1"
--8<-- "examples/microbit/accelerometer/get_x/main.py"
```

??? note "Code explanation"
    - line 1 → imports all the commands from the `microbit` library
    - line 4 → starts an endless loop
    - line 5 → gets the x-axis reading and stores it in `x`
    - line 6 → prints the reading in the Shell
    - line 7 → waits 100 milliseconds before the loop repeats

### `get_y()`

```python linenums="1"
--8<-- "examples/microbit/accelerometer/get_y/main.py"
```

??? note "Code explanation"
    - line 1 → imports all the commands from the `microbit` library
    - line 4 → starts an endless loop
    - line 5 → gets the y-axis reading and stores it in `y`
    - line 6 → prints the reading in the Shell
    - line 7 → waits 100 milliseconds before the loop repeats

### `get_z()`

```python linenums="1"
--8<-- "examples/microbit/accelerometer/get_z/main.py"
```

??? note "Code explanation"
    - line 1 → imports all the commands from the `microbit` library
    - line 4 → starts an endless loop
    - line 5 → gets the z-axis reading and stores it in `z`
    - line 6 → prints the reading in the Shell
    - line 7 → waits 100 milliseconds before the loop repeats

### `get_values()`

Gets all three readings at once as a **tuple**.

```python linenums="1"
--8<-- "examples/microbit/accelerometer/get_values/main.py"
```

??? note "Code explanation"
    - line 1 → imports all the commands from the `microbit` library
    - line 4 → starts an endless loop
    - line 5 → gets all three readings and **unpacks** them: the first value goes into `x`, the second into `y`, the third into `z`
    - line 6 → prints the three readings in the Shell
    - line 7 → waits 100 milliseconds before the loop repeats

!!! note "Tuples"
    A tuple is like a list, but its values can't be changed after it is created. It is written with round brackets, for example `(1, 2, 3)`.

### `current_gesture()`

```python linenums="1"
--8<-- "examples/microbit/accelerometer/current_gesture/main.py"
```

??? note "Code explanation"
    - line 1 → imports all the commands from the `microbit` library
    - line 4 → starts an endless loop
    - line 5 → gets the current gesture as a string and stores it in `gesture`
    - line 6 → prints the gesture in the Shell
    - line 7 → waits 500 milliseconds before the loop repeats

### `is_gesture()`

```python linenums="1"
--8<-- "examples/microbit/accelerometer/is_gesture/main.py"
```

??? note "Code explanation"
    - line 1 → imports all the commands from the `microbit` library
    - line 4 → starts an endless loop
    - line 5 → checks if the micro:bit is face up right now
    - line 6 → if it is, shows a happy face
    - line 7 → if it isn't…
    - line 8 → …shows a sleeping face

### `was_gesture()`

```python linenums="1"
--8<-- "examples/microbit/accelerometer/was_gesture/main.py"
```

??? note "Code explanation"
    - line 1 → imports all the commands from the `microbit` library
    - line 4 → starts an endless loop
    - line 5 → shows a tick to start the round
    - line 6 → waits 3 seconds. Shake the micro:bit now.
    - line 7 → checks if a shake happened since the last check
    - line 8 → if it did, shows a happy face
    - line 9 → if it didn't…
    - line 10 → …shows a sad face
    - line 11 → waits 1 second before the next round

### `get_gestures()`

```python linenums="1"
--8<-- "examples/microbit/accelerometer/get_gestures/main.py"
```

??? note "Code explanation"
    - line 1 → imports all the commands from the `microbit` library
    - line 4 → starts an endless loop
    - line 5 → shows a tick to start the round
    - line 6 → waits 3 seconds. Move the micro:bit around now.
    - line 7 → gets every gesture since the last check and stores them in `gestures`
    - line 8 → prints the gestures in the Shell
    - line 9 → shows a cross to end the round
    - line 10 → waits 2 seconds before the next round

## Documentation

- [BBC micro:bit MicroPython — accelerometer](https://microbit-micropython.readthedocs.io/en/v2-docs/accelerometer.html)

## Exercises

Starter files are in the `accelerometer` folder of your tutorial files. Solutions are on the [Exercise Solutions](../reference/solutions.md#accelerometer) page.

### Exercise 1

Starter: `accelerometer/ex1_spirit_level`

Make a spirit level that shows `-` if the micro:bit is level left to right, `L` if the left side is too high, or `R` if the right side is too high.

### Exercise 2

Starter: `accelerometer/ex2_face_up`

Show a happy face if the micro:bit is face up, or an angry face if it isn't.

### Exercise 3

Starter: `accelerometer/ex3_shake_count`

Count how many times the micro:bit is shaken in 5 seconds, then show the count.

### Exercise 4

Starter: `accelerometer/ex4_3g`

Wait until button **A** is pressed, then show whether the micro:bit has experienced `3g` since the program started.
