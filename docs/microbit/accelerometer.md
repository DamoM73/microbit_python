# Accelerometer

!!! learn "On this page we will learn"
    - how to measure movement and tilt in three directions
    - how to read all three values at once
    - how to recognise gestures such as shaking or turning face up

!!! terms "Terminology"
    - **accelerometer** – a sensor that measures movement and tilt in three directions and can recognise gestures such as shaking.
    - **axis** – an imaginary line, called x, y or z, along which movement is measured.
    - **milli-g** – the unit for accelerometer readings, where about 1024 milli-g equals the pull of gravity.
    - **gesture** – a movement the accelerometer can recognise, such as shaking, tilting or turning face up.
    - **tuple** – a collection of values written in round brackets, like a list, but whose values can't be changed after it is created.
    - **unpacking** – storing each value from a tuple or list into its own variable in one line, such as `x, y, z = accelerometer.get_values()`.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/UT35ODxvmS0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

The accelerometer measures movement and tilt in three directions and recognises gestures such as shaking or turning face up.

Possible uses:

- step counters
- shake-to-roll dice
- tilt-controlled games
- motion alarms

## Connect it

The accelerometer is built into the micro:bit, so we don't need to connect anything.

- Each example is a `main.py` file. See [Your First Program](../micropython/first-program.md) for how to create, upload and run it.
- Most examples print readings. Watch them in Thonny's **Shell**.
- Movement is measured along three **axes** (imaginary lines):
    - **x** → tilting left and right
    - **y** → tilting forwards and backwards
    - **z** → moving up and down
- Readings are in **milli-g**. `0` means level on that axis; about `1024` or `-1024` is the pull of gravity.
- Gestures are strings: `"up"`, `"down"`, `"left"`, `"right"`, `"face up"`, `"face down"`, `"freefall"`, `"3g"`, `"6g"`, `"8g"` and `"shake"`.

## Set it up

The accelerometer is part of the `microbit` library. We import it at the top of every program:

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

Reads how much the micro:bit is tilted or moving left and right.

```python linenums="1"
--8<-- "examples/microbit/accelerometer/get_x/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → imports all the commands from the `microbit` library.
    - **line 4** → starts an endless loop.
    - **line 5** → gets the x-axis reading and stores it in `x`.
    - **line 6** → prints the reading in the Shell.
    - **line 7** → waits 100 milliseconds before the loop repeats.

### `get_y()`

Reads how much the micro:bit is tilted or moving forwards and backwards.

```python linenums="1"
--8<-- "examples/microbit/accelerometer/get_y/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → imports all the commands from the `microbit` library.
    - **line 4** → starts an endless loop.
    - **line 5** → gets the y-axis reading and stores it in `y`.
    - **line 6** → prints the reading in the Shell.
    - **line 7** → waits 100 milliseconds before the loop repeats.

### `get_z()`

Reads how much the micro:bit is moving up and down.

```python linenums="1"
--8<-- "examples/microbit/accelerometer/get_z/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → imports all the commands from the `microbit` library.
    - **line 4** → starts an endless loop.
    - **line 5** → gets the z-axis reading and stores it in `z`.
    - **line 6** → prints the reading in the Shell.
    - **line 7** → waits 100 milliseconds before the loop repeats.

### `get_values()`

Gets all three readings at once as a **tuple**.

```python linenums="1"
--8<-- "examples/microbit/accelerometer/get_values/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → imports all the commands from the `microbit` library.
    - **line 4** → starts an endless loop.
    - **line 5** → gets all three readings and **unpacks** them: the first value goes into `x`, the second into `y`, the third into `z`.
    - **line 6** → prints the three readings in the Shell.
    - **line 7** → waits 100 milliseconds before the loop repeats.

!!! tip "Tuples"
    A tuple is like a list, but its values can't be changed after it is created. It is written with round brackets, for example `(1, 2, 3)`.

### `current_gesture()`

Returns the name of the gesture happening right now, such as `"face up"` or `"shake"`.

```python linenums="1"
--8<-- "examples/microbit/accelerometer/current_gesture/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → imports all the commands from the `microbit` library.
    - **line 4** → starts an endless loop.
    - **line 5** → gets the current gesture as a string and stores it in `gesture`.
    - **line 6** → prints the gesture in the Shell.
    - **line 7** → waits 500 milliseconds before the loop repeats.

### `is_gesture()`

Checks whether a particular gesture is happening **right now**.

```python linenums="1"
--8<-- "examples/microbit/accelerometer/is_gesture/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → imports all the commands from the `microbit` library.
    - **line 4** → starts an endless loop.
    - **line 5** → checks if the micro:bit is face up right now.
    - **line 6** → if it is, shows a happy face.
    - **line 7** → if it isn't…
    - **line 8** → …shows a sleeping face.

### `was_gesture()`

Checks whether a particular gesture has happened **since the last check**, even if it has finished.

```python linenums="1"
--8<-- "examples/microbit/accelerometer/was_gesture/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → imports all the commands from the `microbit` library.
    - **line 4** → starts an endless loop.
    - **line 5** → waits 3 seconds. Shake the micro:bit now.
    - **line 6** → checks if a shake happened since the last check.
    - **line 7** → if it did, shows a happy face.
    - **line 8** → if it didn't…
    - **line 9** → …shows a sad face.

### `get_gestures()`

Returns every gesture that has happened since the last check, oldest first.

```python linenums="1"
--8<-- "examples/microbit/accelerometer/get_gestures/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → imports all the commands from the `microbit` library.
    - **line 4** → starts an endless loop.
    - **line 5** → waits 3 seconds. Move the micro:bit around now.
    - **line 6** → gets every gesture since the last check and prints them in the Shell.

## Documentation

Documentation is the official guide written by the people who made the code library, and we can use it to look up every method and its parameters, including ones that aren't covered on this page.

- [BBC micro:bit MicroPython — accelerometer](https://microbit-micropython.readthedocs.io/en/v2-docs/accelerometer.html)

## Exercises

!!! primm "PRIMM"
    Time to **modify** the code and see what happens.

Starter files are in the `accelerometer` folder of your tutorial files. Solutions are on the [Exercise Solutions](../reference/solutions.md#accelerometer) page.

### Exercise 1

Starter: `accelerometer/ex1_spirit_level`

Can you make a spirit level that shows `-` if the micro:bit is level left to right, `L` if the left side is too high, or `R` if the right side is too high?

### Exercise 2

Starter: `accelerometer/ex2_face_up`

Can you make the micro:bit show a happy face if it is face up, or an angry face if it isn't?

### Exercise 3

Starter: `accelerometer/ex3_shake_count`

Can you count how many times the micro:bit is shaken in 5 seconds, then show the count?

### Exercise 4

Starter: `accelerometer/ex4_3g`

Can you make a program that waits until button **A** is pressed, then shows whether the micro:bit has experienced `3g` since the program started?
