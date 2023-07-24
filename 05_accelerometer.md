# Micro:bit Accelerometer

```{admonition} Accelerometer functions
:class: important
Full details can be found at the **[BBC micro:bit MicroPython accelerometer documentation](https://microbit-micropython.readthedocs.io/en/latest/accelerometer.html#module-microbit.accelerometer)**.
```

The BBC micro:bit comes with an **accelerometer**. An accelerometer can detect and measure how fast something is moving or how it's being tilted. It can sense motion in different directions like up, down, left, and right. 

## Movement

The micro:bit accelerometer measures movement along three axes:

- X - tilting from left to right.
- Y - tilting forwards and backwards.
- Z - moving up and down.

### Get x

There is a method for each axis that returns a positive or negative number indicating a measurement in milli-g’s. When the reading is 0 you are “level” along that particular axis.

Below is an example for the x-axis:

```{literalinclude} ./python_files/movement/main.py
:linenos:
```

### Get values

You can also get a tuple containing the x, y and z values the micro:bit is experiencing:

Below is an example:

```{literalinclude} ./python_files/movement_values/main.py
:linenos:
```


### Movement exercises

1. Change the x-axis example above to show the value for the y-axis
2. Change the x-axis example above to show the value for the z-axis
3. Make a levelling device that shows a `-` if the x-axis is level, `L` if the left side is too high or `R` if the right side is too high.

## Gestures

The really interesting side-effect of having an accelerometer is gesture detection. If you move your BBC micro:bit in a certain way (as a gesture) then MicroPython is able to detect this.

MicroPython is able to recognise the following gestures: `up`, `down`, `left`, `right`, `face up`, `face down`, `freefall`, `3g`, `6g`, `8g`, `shake`. Gestures are always represented as strings. While most of the names should be obvious, the `3g`, `6g` and `8g` gestures apply when the device encounters these levels of g-force (like when an astronaut is launched into space).

### Current gestures

You can get the current gesture by using the `current_gesture` method which return a string.

Below is an example for displaying the current gesture:

```{literalinclude} ./python_files/gestures/main.py
:linenos:
```

### Get gestures

The micro:bit can also provide you with a list of historical gestures. It returns a tuple with the latest gesture first.

Below is an example of `get_gestures`:

```{literalinclude} ./python_files/gestures_get_gestures/main.py
:linenos:
```

### Was gesture

The `was_gesture` method check to see if the micro:bit recorded a gesture since the last call.

Below is an example to see if the micro:bit was shaken during the 5 second sleep.

```{literalinclude} ./python_files/gestures_get_gestures/main.py
:linenos:
```

### Gesture exercises

1. Make the micro:bit display a happy face if it is face up, or display an angry face if it is not.
2. Make a program that counts the number of times it has been shaken over a five second period
3. Make a program that waits button **A** is pressed, and then reports if it has experienced 3gs