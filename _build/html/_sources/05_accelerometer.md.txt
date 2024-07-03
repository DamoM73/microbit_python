# Micro:bit Accelerometer

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/UT35ODxvmS0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

The BBC micro:bit comes with an **accelerometer**. An accelerometer can detect and measure how fast something is moving or how it's being tilted. It can sense motion in different directions like up, down, left, and right. 

```{admonition} Accelerometer functions
:class: important
Full details can be found at the **[BBC micro:bit MicroPython accelerometer documentation](https://microbit-micropython.readthedocs.io/en/latest/accelerometer.html#module-microbit.accelerometer)**.
```

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

```{admonition} Code explaination
:class: notice
- **line 5** &rarr; creates an infinite loop, since the condition (`True`) will never be `False`.
- **line 6** &rarr; gets the x-axis reading from the accelerometer and store it in the x_reading variable.
- **line 7** &rarr; displays the x_reading on matrix
```

### Get values

You can also get a tuple containing the x, y and z values the micro:bit is experiencing:

Below is an example:

```{literalinclude} ./python_files/movement_values/main.py
:linenos:
```

```{admonition} Code explaination
:class: notice
- **line 5** &rarr; creates an infinite loop, since the condition (`True`) will never be `False`.
- **line 6** &rarr; gets the tuple of the accelerometer reading and stores it in the values variable.
- **line 7** &rarr; displays accelerometer readings to the matrix
- **line 8** &rarr; waits 1 second
```

```{admonition} Tuples
:class: notice
Tuples in Python are like lists, but you can't change their values once they're created. They are useful for storing a collection of items that should not be modified. You create a tuple by placing the items inside parentheses, separated by commas, like this: my_tuple = (1, 2, 3).
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

```{admonition} Code explaination
:class: notice
- **line 5** &rarr; creates an infinite loop, since the condition (`True`) will never be `False`.
- **line 6** &rarr; stores the current gesture in the variable called gesture
- **line 7** &rarr; scrolls the gesture across the display
- **line 8** &rarr; waits 1 second
```

### Get gestures

The micro:bit can also provide you with a list of historical gestures. It returns a tuple with the latest gesture first.

Below is an example of `get_gestures`:

```{literalinclude} ./python_files/gestures_get_gestures/main.py
:linenos:
```

```{admonition} Code explaination
:class: notice
- **line 5** &rarr; waits 5 seconds
- **line 7** &rarr; gets a list of all the guestures that have occured since the micro:bit was turned on and stores it in the variable called gestures
- **line 9** &rarr; iterates over the list of gestures
- **line 10** &rarr; scroll the current guesture across the display
```

### Was gesture TODO

The `was_gesture` method check to see if the micro:bit recorded a gesture since the last call.

Below is an example to see if the micro:bit was shaken during the 5 second sleep.

```{literalinclude} ./python_files/gestures_get_gestures/main.py
:linenos:
```

### Gesture exercises

1. Make the micro:bit display a happy face if it is face up, or display an angry face if it is not.
2. Make a program that counts the number of times it has been shaken over a five second period
3. Make a program that waits button **A** is pressed, and then reports if it has experienced 3gs
