# Micro:bit Accelerometer

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/UT35ODxvmS0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

The BBC micro:bit has an **accelerometer**. An accelerometer can detect movement and tilt. It can sense motion in different directions, such as up, down, left, and right.

```{admonition} Accelerometer functions
:class: important
Full details can be found at the **[BBC micro:bit MicroPython accelerometer documentation](https://microbit-micropython.readthedocs.io/en/latest/accelerometer.html#module-microbit.accelerometer)**.
```

## Movement

The micro:bit accelerometer measures movement along three axes. An axis is an imaginary line used to measure direction.

- X - tilting left and right.
- Y - tilting forward and backward.
- Z - moving up and down.

### Get x

There is a method for each axis. Each method returns a positive or negative number measured in milli-gs. When the reading is `0`, the micro:bit is level on that axis.

1. Stop and close the current **main.py** file.
2. Navigate to the **08_movement_get_axis** folder in Thonny and open the **main.py** file.

You should see the code below, it is an example for the x-axis:

```{literalinclude} ./python_files/08_movement_get_axis/main.py
:linenos:
```

1. **Predict** what you think will happen. Be specific.
2. **Run** the program.
3. Time to **investigate** the code. What does each line do?

```{admonition} Code explanation
:class: notice
- **line 9** &rarr; creates an endless loop.
- **line 11** &rarr; gets the x-axis reading and stores it in the `x_reading` variable.
- **line 12** &rarr; gets the y-axis reading and stores it in the `y_reading` variable.
- **line 13** &rarr; gets the z-axis reading and stores it in the `z_reading` variable.
- **line 18** &rarr; prints the three readings in the shell.
- **line 20** &rarr; waits 100 milliseconds before going back to the top of the loop.
```

### Get values

You can also get a tuple containing the x, y, and z values from the micro:bit.

1. Stop and close the current **main.py** file.
2. Navigate to the **08_movement_get_values** folder in Thonny and open the **main.py** file.

You should see the code below:

```{literalinclude} ./python_files/08_movement_get_values/main.py
:linenos:
```

1. **Predict** what you think will happen. Be specific.
2. **Run** the program.
3. Time to **investigate** the code. What does each line do?

```{admonition} Code explanation
:class: notice
- **line 9** &rarr; creates an endless loop.
- **line 11** &rarr; gets the accelerometer readings and stores them in the `values` variable.
- **line 14** &rarr; gets the x-axis reading from the tuple.
- **line 15** &rarr; gets the y-axis reading from the tuple.
- **line 16** &rarr; gets the z-axis reading from the tuple.
- **line 19** &rarr; prints the three readings in the shell.
- **line 21** &rarr; waits 100 milliseconds before going back to the top of the loop.
```

```{admonition} Tuples
:class: note
Tuples in Python are like lists, but you cannot change their values after they are created. They are useful for storing a group of items that should stay the same. You create a tuple by putting the items inside parentheses, separated by commas, like this: `my_tuple = (1, 2, 3)`.
```

### Movement Exercise 1

1. Stop and close the current **main.py** file.
2. Open the **main.py** file in the **08_movement_get_values_ex1** folder in Thonny.
3. Change the code to show the value for the y-axis.

### Movement Exercise 2

1. Stop and close the current **main.py** file.
2. Open the **main.py** file in the **08_movement_get_values_ex2** folder in Thonny.
3. Change the code to show the value for the z-axis.

### Movement Exercise 3
1. Stop and close the current **main.py** file.
2. Open the **main.py** file in the **08_movement_get_values_ex3** folder in Thonny.
3. Make a levelling device that shows `-` if the x-axis is level, `L` if the left side is too high, or `R` if the right side is too high.

## Gestures

One useful feature of the accelerometer is gesture detection. If you move your BBC micro:bit in a certain way, MicroPython can detect that movement as a gesture.

MicroPython can recognise these gestures: `up`, `down`, `left`, `right`, `face up`, `face down`, `freefall`, `3g`, `6g`, `8g`, and `shake`. Gestures are written as strings. Most names are easy to understand. The `3g`, `6g`, and `8g` gestures happen when the micro:bit experiences those levels of g-force.

### Current Gesture

You can get the current gesture by using the `current_gesture()` method, which returns a string.

1. Stop and close the current **main.py** file.
2. Navigate to the **09_gestures_current** folder in Thonny and open the **main.py** file.

You should see the code below:

```{literalinclude} ./python_files/09_gestures_current/main.py
:linenos:
```

1. **Predict** what you think will happen. Be specific.
2. **Run** the program.
3. Time to **investigate** the code. What does each line do?

```{admonition} Code explanation
:class: notice
- **line 9** &rarr; creates an endless loop.
- **line 11** &rarr; stores the current gesture in the `gesture` variable.
- **line 16** &rarr; prints the gesture in the shell.
- **line 17** &rarr; waits 1 second before going back to the top of the loop.
```

### Get gestures

The micro:bit can also give you a list of past gestures. It returns a tuple with the newest gesture first.

1. Stop and close the current **main.py** file.
2. Navigate to the **09_gestures_get** folder in Thonny and open the **main.py** file.  

You should see the code below:

```{literalinclude} ./python_files/09_gestures_get/main.py
:linenos:
```

1. **Predict** what you think will happen. Be specific.
2. **Run** the program.
3. Time to **investigate** the code. What does each line do?

```{admonition} Code explanation
:class: notice
- **lines 10-16** &rarr; shows a countdown from `3` to `0`.
- **line 18** &rarr; gets all the gestures that have happened since the last check and stores them in the `gestures` variable.
- **line 23** &rarr; loops through the gestures.
- **line 24** &rarr; prints each gesture in the shell.
- **line 25** &rarr; shows the **NO** image to mark the end of the round.
- **line 26** &rarr; waits 5 seconds before going back to the top of the loop.
```

### Was Gesture

The `was_gesture()` method checks whether the micro:bit has recorded a specific gesture since the last check.

1. Stop and close the current **main.py** file.
2. Navigate to the **09_gestures_was** folder in Thonny and open the **main.py** file.

You should see the code below that checks if the micro:bit was shaken during the 3-second wait.

```{literalinclude} ./python_files/09_gestures_was/main.py
:linenos:
```

1. **Predict** what you think will happen. Be specific.
2. **Run** the program.
3. Time to **investigate** the code. What does each line do?

```{admonition} Code explanation
:class: notice
- **line 10** &rarr; displays the **YES** image to show the round has started.
- **line 11** &rarr; waits 3 seconds.
- **line 14** &rarr; checks if the micro:bit was shaken during the wait.
- **line 19** &rarr; if the micro:bit was shaken, the next line will run.
- **line 20** &rarr; displays a happy face.
- **line 21** &rarr; if the micro:bit was not shaken, the next line will run.
- **line 22** &rarr; displays a sad face.
- **line 24** &rarr; waits 500 milliseconds before going back to the top of the loop.
```

### Gesture Exercise 1

1. Stop and close the current **main.py** file.
2. Open the **main.py** file in the **09_gestures_was_ex1** folder in Thonny.
3. Make the micro:bit display a happy face if it is face up, or display an angry face if it is not.

### Gesture Exercise 2

1. Stop and close the current **main.py** file.
2. Open the **main.py** file in the **09_gestures_was_ex2** folder in Thonny.
3. Make a program that counts how many times the micro:bit has been shaken over a 5-second period.

### Gesture Exercise 3
1. Stop and close the current **main.py** file.
2. Open the **main.py** file in the **09_gestures_was_ex3** folder in Thonny.
3. Make a program that waits until button **A** is pressed, and then reports if the micro:bit has experienced `3g`.
