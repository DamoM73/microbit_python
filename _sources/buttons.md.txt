# Micro:bit Buttons

The Micro:bit has two input buttons **A** and **B** on the front. These buttons are an easy way to get user input. In Python these two buttons are called `button_a` and `button_b`.

```{admonition} Documentation
:class: important
All the button functions can be found at the **[BBC micro:bit MicroPython display documentation](https://microbit-micropython.readthedocs.io/en/latest/button.html)**.
```

There are three ways you can work with the buttons.

## Get presses

```{admonition} get_presses function
:class: important
Full details can be found at the **[BBC micro:bit MicroPython display.scroll documentation](https://microbit-micropython.readthedocs.io/en/latest/button.html#Button.get_presses)**.
```

`get_presses` counts the number of times that a button has been pressed. Restarting the Micro:bit or calling this function will return the count to `0`.

**main.py** file. Add the code below.

```{literalinclude} ./python_files/button_get_press/main.py
:linenos:
```

**Predict** in detail what you think will happen, and then **run** the program.

## Is pressed

```{admonition} is_pressed function
:class: important
Full details can be found at the **[BBC micro:bit MicroPython display.scroll documentation](https://microbit-micropython.readthedocs.io/en/latest/button.html#Button.is_pressed)**.
```

`is_pressed` returns the value of `True` if the button is currently pressed, otherwise it returns `False`.

Create a new file, call it **main.py** and then add the following code:

```{literalinclude} ./python_files/button_is_pressed/main.py
:linenos:
```

**Predict** in detail what you think will happen, and then **run** the program.

Let's break that code down:

- line 3 &rarr; creates an infinite loop, since the condition (`True`) will never be `False`
- line 4 &rarr; tests if `button_a` is currently being pressed.
- line 5 &rarr; if line 4 is `True` then the display will show a smiley face
- line 6 &rarr; tests if `button_b` is currently being pressed.
- line 7 &rarr; if line 6 is `True` then `break` will be called, and exit the `while` loop
- line 8 &rarr; if neither `button_a` or `button_b` is being pressed
- line 9 &rarr; displays a sad face

## Was pressed

```{admonition} was_pressed function
:class: important
Full details can be found at the **[BBC micro:bit MicroPython display.scroll documentation](https://microbit-micropython.readthedocs.io/en/latest/button.html#Button.is_pressed)**.
```

