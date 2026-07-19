# Micro:bit Buttons

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/hnT0qHM3_hQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

The micro:bit has two input buttons, **A** and **B**, on the front. These buttons are an easy way to get input from the user. In Python, these two buttons are called `button_a` and `button_b`.

```{admonition} Documentation
:class: important
All the button functions can be found at the **[BBC micro:bit MicroPython button documentation](https://microbit-micropython.readthedocs.io/en/latest/button.html)**.
```

There are three ways you can work with the buttons.

## Get Presses

```{admonition} get_presses function
:class: important
**`get_presses()`**

Full details can be found at the **[BBC micro:bit MicroPython button.get_presses documentation](https://microbit-micropython.readthedocs.io/en/latest/button.html#Button.get_presses)**.
```

`get_presses()` counts how many times the button has been pressed. Restarting the micro:bit or calling this function will reset the count to `0`.

Create a **main.py** file. Add the code below.

```{literalinclude} ./python_files/button_get_press/main.py
:linenos:
```

**Predict** what you think will happen. Be specific. Then **run** the program.

```{admonition} Code explanation
:class: notice
- **line 9** &rarr; creates an endless loop.
- **line 11** &rarr; counts how many times button **A** has been pressed since the last count.
- **line 16** &rarr; displays the number of button presses.
- **line 17** &rarr; waits 1000 milliseconds before going back to the top of the loop.
- **line 18** &rarr; clears the display.
```

### Get Presses Exercises

1. Create a program that challenges the player to press a button a certain number of times before time runs out.

## Is Pressed

```{admonition} is_pressed function
:class: important
**`is_pressed()`**

Full details can be found at the **[BBC micro:bit MicroPython button.is_pressed documentation](https://microbit-micropython.readthedocs.io/en/latest/button.html#Button.is_pressed)**.
```

`is_pressed()` returns `True` if the button is being pressed right now. Otherwise, it returns `False`.

Create a new file called **main.py**, and then add the following code:

```{literalinclude} ./python_files/button_is_pressed/main.py
:linenos:
```

**Predict** what you think will happen. Be specific. Then **run** the program.

```{admonition} Code explanation
:class: notice
- **line 9** &rarr; creates an endless loop.
- **line 11** &rarr; checks if button **A** is being pressed right now.
- **line 12** &rarr; checks if button **B** is being pressed right now.
- **line 17** &rarr; if button **A** is pressed, the next line will run.
- **line 18** &rarr; shows a happy face.
- **line 19** &rarr; if button **A** is not pressed, this checks if button **B** is pressed.
- **line 20** &rarr; exits the `while` loop.
- **line 21** &rarr; if neither button is pressed, the next line will run.
- **line 22** &rarr; shows a sad face.
- **line 24** &rarr; clears the display after the loop ends.
```

### Is Pressed Exercise

1. Create a program that tests the user's reaction time. It should:
   - randomly choose which button to press: **A** or **B**
   - do a 3-2-1 countdown, then display the button to press
   - time how long it takes the user to press the correct button. **[ticks_ms()](https://microbit-micropython.readthedocs.io/en/latest/utime.html#utime.utime.ticks_ms)** may be helpful.
   - show the reaction time on the display

## Was Pressed

```{admonition} was_pressed function
:class: important
**`was_pressed()`**

Full details can be found at the **[BBC micro:bit MicroPython button.was_pressed documentation](https://microbit-micropython.readthedocs.io/en/latest/button.html#Button.was_pressed)**.
```

`was_pressed()` returns `True` if the button has been pressed since the micro:bit started, or since the last time this function was called. Otherwise, it returns `False`.

Calling this function clears the press state. This means the button must be pressed again before `was_pressed()` can return `True` again.

```{literalinclude} ./python_files/button_was_pressed/main.py
:linenos:
```

```{admonition} Code explanation
:class: notice
- **line 9** &rarr; clears the display of any previous image.
- **line 11** &rarr; creates an endless loop.
- **line 13** &rarr; checks if button **A** has been pressed since the last check.
- **line 14** &rarr; checks if button **B** has been pressed since the last check.
- **line 19** &rarr; if button **A** was pressed, the next line will run.
- **line 20** &rarr; shows a happy face.
- **line 21** &rarr; if button **A** was not pressed, this checks if button **B** was pressed.
- **line 22** &rarr; shows a sad face.
```

### Was Pressed Exercise

1. Create a program that counts how many times button **A** is pressed. The count should start at `0`. Each time button **A** is pressed, the count should increase by `1`. Pressing button **B** should reset the count to `0`.
2. Create a memory game that:
   - randomly generates a 6-letter pattern using **A** and **B**
   - displays the pattern to the user
   - asks the user to repeat the pattern
   - displays a smiley face if the repeated pattern matches the generated pattern
   - displays a sad face if the patterns do not match
