# Buttons

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/hnT0qHM3_hQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

The micro:bit has two push buttons, **A** and **B**, that detect when they are pressed.

Possible uses:

- controlling games
- starting and stopping timers
- answering questions
- moving through menus

## Connect it

The buttons are built into the micro:bit, so we don't need to connect anything.

- Each example is a `main.py` file. See [Your First Program](../micropython/first-program.md) for how to create, upload and run it.
- In code, the buttons are called `button_a` and `button_b`. Every method below works with either button.

## Set it up

The buttons are part of the `microbit` library. We import it at the top of every program:

```python linenums="1"
from microbit import *
```

## Methods

| Method | Parameters | Returns | Description |
| --- | --- | --- | --- |
| `button_a.get_presses()` | none | int | Number of presses since the last call, then resets the count to `0` |
| `button_a.is_pressed()` | none | Boolean | `True` if the button is being held down right now |
| `button_a.was_pressed()` | none | Boolean | `True` if the button has been pressed since the last call |

### `get_presses()`

Counts how many times the button has been pressed. Each call resets the count to `0`.

```python linenums="1"
--8<-- "examples/microbit/buttons/get_presses/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → imports all the commands from the `microbit` library.
    - **line 4** → starts an endless loop.
    - **line 5** → gets the number of times button **A** was pressed since the last check and stores it in `presses`.
    - **line 6** → shows the number of presses.
    - **line 7** → waits 1 second, giving you time to press the button again.

### `is_pressed()`

Checks whether the button is being held down **right now**.

```python linenums="1"
--8<-- "examples/microbit/buttons/is_pressed/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → imports all the commands from the `microbit` library.
    - **line 4** → starts an endless loop.
    - **line 5** → checks if button **A** is being held down.
    - **line 6** → if it is, shows a happy face.
    - **line 7** → if it isn't…
    - **line 8** → …shows a sad face.

### `was_pressed()`

Checks whether the button has been pressed **since the last check**, even if it has been let go. Each call clears the press, so the button must be pressed again before it returns `True` again.

```python linenums="1"
--8<-- "examples/microbit/buttons/was_pressed/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → imports all the commands from the `microbit` library.
    - **line 4** → starts an endless loop.
    - **line 5** → checks if button **A** was pressed since the last check.
    - **line 6** → if it was, shows a happy face.
    - **line 7** → if it wasn't…
    - **line 8** → …shows a sad face.
    - **line 9** → waits 2 seconds. A press during this wait is still detected on the next loop.

!!! tip "`is_pressed()` or `was_pressed()`?"
    `is_pressed()` only sees the button while it is held down. `was_pressed()` remembers a press, so a quick press during the 2-second wait in the `was_pressed()` example is still detected.

## Documentation

- [BBC micro:bit MicroPython — buttons](https://microbit-micropython.readthedocs.io/en/v2-docs/button.html)

## Exercises

!!! primm "PRIMM"
    Time to **modify** the code and see what happens.

Starter files are in the `buttons` folder of your tutorial files. Solutions are on the [Exercise Solutions](../reference/solutions.md#buttons) page.

### Exercise 1

Starter: `buttons/ex1_press_challenge`

Can you create a program that challenges the player to press button **A** a certain number of times before time runs out?

### Exercise 2

Starter: `buttons/ex2_counter`

Can you create a program that counts how many times button **A** is pressed? The count starts at `0` and goes up by `1` with each press. Pressing button **B** resets the count to `0`.

### Exercise 3

Starter: `buttons/ex3_reaction_timer`

Can you create a program that tests the player's reaction time? It should:

- randomly choose which button to press: **A** or **B**
- count down 3-2-1, then show the button to press
- time how long it takes to press the correct button. [`running_time()`](module.md#running_time) may help.
- show the reaction time on the display

### Exercise 4

Starter: `buttons/ex4_memory_game`

Can you create a memory game that:

- randomly generates a 6-letter pattern using **A** and **B**
- shows the pattern to the player
- asks the player to repeat the pattern using the buttons
- shows a happy face if the pattern matches, or a sad face if it doesn't?
