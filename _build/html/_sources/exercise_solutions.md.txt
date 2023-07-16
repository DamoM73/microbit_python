# Exercise Solutions

Below you will find **a** solution to all the exercises from this course. Like all programming, there are countless ways to solve a problem, the solutions presented here are just one way. If you get the outcomes you required, then your code solves the problem.

## First Program Exercises

### First Program Exercise 1

```{literalinclude} ./python_files/first_program_ex1/main.py
:linenos:
```

### First Program Exercise 2

```{literalinclude} ./python_files/first_program_ex2/main.py
:linenos:
```

### First Program Exercise 3

Without the `while` statement the micro:bit will display the message and then stop on the Heart. This happens because the code is just sequential. It reaches the end and stops. The `while` statement is needed to make the micro:bit loop back to the start of the message.

### First Program Exercise 4

When the micro:bit is unplugged it turns off because it is using the power from the computer. When it is plugged back in, it does nothing, because the code hasn't been sent from the computer.

## Display Exercises

### Text Exercise 1

```{literalinclude} ./python_files/display_show_ex1/main.py
:linenos:
```

### Text Exercise 2

```{literalinclude} ./python_files/display_show_ex2/main.py
:linenos:
```

### Text Exercise 3

```{literalinclude} ./python_files/display_show_ex3/main.py
:linenos:
```

### Image Exercise 1

```{literalinclude} ./python_files/display_images_ex1/main.py
:linenos:
```

### Image Exercise 2

```{literalinclude} ./python_files/display_images_ex2/main.py
:linenos:
```

### Image Exercise 3

```{literalinclude} ./python_files/display_images_ex3/main.py
:linenos:
```

### Custom Exercise 1

The LEDs flash all over the place.

This is caused by the micro:bit processor working faster than the LEDs. By the time an LED has been light up to the correct level, the processor has moved both the `x` value and the `y` value far beyond where they need to be. The `sleep(10)` makes the processor wait until the LED is lit up before continuing in the loop.

### Custom Exercise 2

```{literalinclude} ./python_files/display_custom_ex2/main.py
:linenos:
```

### Custom Exercise 3

```{literalinclude} ./python_files/display_custom_ex3/main.py
:linenos:
```

## Buttons Exercises

### Get Presses Exercises 1

```{literalinclude} ./python_files/button_was_pressed_ex1/main.py
:linenos:
```

### Is Pressed Exercise 1

```{literalinclude} ./python_files/button_is_pressed_ex1/main.py
:linenos:
```

### Was Pressed Exercise 1

```{literalinclude} ./python_files/button_was_pressed_ex1/main.py
:linenos:
```

### Was Pressed Exercise 2

```{literalinclude} ./python_files/button_was_pressed_ex2/main.py
:linenos:
```