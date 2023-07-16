# Micro:bit Buttons

The Micro:bit has two input buttons **A** and **B** on the front. These buttons are an easy way to get user input. In Python these two buttons are called `button_a` and `button_b`.

```{admonition} Documentation
:class: important
All the button functions can be found at the **[BBC micro:bit MicroPython button documentation](https://microbit-micropython.readthedocs.io/en/latest/button.html)**.
```

There are three ways you can work with the buttons.

## Get Presses

```{admonition} get_presses function
:class: important
Full details can be found at the **[BBC micro:bit MicroPython button.get_presses documentation](https://microbit-micropython.readthedocs.io/en/latest/button.html#Button.get_presses)**.
```

`get_presses` counts the number of times that the button has been pressed. Restarting the Micro:bit or calling this function will return the count to `0`.

**main.py** file. Add the code below.

```{literalinclude} ./python_files/button_get_press/main.py
:linenos:
```

**Predict** in detail what you think will happen, and then **run** the program.

### Get Presses Exercises

1. Create a program that challenges the player to press a button a certain number of times within a time limit.

## Is Pressed

```{admonition} is_pressed function
:class: important
Full details can be found at the **[BBC micro:bit MicroPython button.is_pressed documentation](https://microbit-micropython.readthedocs.io/en/latest/button.html#Button.is_pressed)**.
```

`is_pressed` returns the value of `True` if the button is currently pressed, otherwise it returns `False`.

Create a new file, call it **main.py** and then add the following code:

```{literalinclude} ./python_files/button_is_pressed/main.py
:linenos:
```

**Predict** in detail what you think will happen, and then **run** the program.

Let's break that code down:

- line 3 &rarr; creates an infinite loop, since the condition (`True`) will never be `False`
- line 4 &rarr; tests if button **A** is currently being pressed.
- line 5 &rarr; if line 4 is `True` then the display will show a smiley face
- line 6 &rarr; tests if button **B** is currently being pressed.
- line 7 &rarr; if line 6 is `True` then `break` will be called, and exit the `while` loop
- line 8 &rarr; if neither button **A** or button **B** is being pressed
- line 9 &rarr; displays a sad face

### Is pressed exercise

1. Create a program that tests a user reaction time. It should:
   - Randomly choose which button to press **A** or **B**
   - Do a 3-2-1 countdown then display the button to press
   - Time how long it takes for the user to press the correct button (**[ticks_us()](https://microbit-micropython.readthedocs.io/en/latest/utime.html#utime.utime.ticks_ms)** may be helpful)
   - Show the reaction time on the display

## Was Pressed

```{admonition} was_pressed function
:class: important
Full details can be found at the **[BBC micro:bit MicroPython button.was_pressed documentation](https://microbit-micropython.readthedocs.io/en/latest/button.html#Button.was_pressed)**.
```

`was_pressed` will returns `True` or `False` to indicate if the button was pressed (went from up to down) since the device started, or the last time this method was called. Calling this method will clear the press state so that the button must be pressed again before this method will return `True` again.

```{literalinclude} ./python_files/button_was_pressed/main.py
:linenos:
```

Breaking that code down:

- line 3 &rarr; clears the display of any previous image
- line 5 &rarr; creates an infinite loop, since the condition (`True`) will never be `False`
- line 6 &rarr; does two things:
  - tests if button **A** has been pressed (moved from the up position to the down position)
  - if `button_a.was_pressed()` is `True` resets it to `False`
- line 7 &rarr; changes display to smiley face
- line 8 &rarr; does two things:
  - tests if button **B** has been pressed (moved from the up position to the down position)
  - if `button_b.was_pressed()` is `True` resets it to `False`
- line 7 &rarr; changes display to sad face

### Was Pressed Exercise

1. Create program that counts the number of times button **A** is pressed. The count should start at 0, and for each press of button A, the count should increment by 1. Pressing button **B** should reset the count to 0.
2. Create a memory game that:
   - randomly generates a 6 letter A or B pattern
   - displays the pattern to the user
   - gets the user to repeat the pattern
   - displays a smiley face if the repeated pattern is the same as the generated pattern or a sad face if they don't match