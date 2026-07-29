# Micro:bit Touch Sensor

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/spFD3SxxxHQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

You can use the gold logo as another input in your projects. It works like an extra button. The logo uses **capacitive touch**, which means it senses tiny electrical changes when your finger touches it. Phone and tablet screens use a similar idea.

```{admonition} Pins
:class: important
Full details can be found at the **[BBC micro:bit MicroPython pins documentation](https://microbit-micropython.readthedocs.io/en/v2-docs/microbit_micropython_api.html?highlight=touch#pins)**.
```

## Pin logo

The logo at the top of the micro:bit is a capacitive touch button.

Calling `pin_logo.is_touched()` returns `True` if the logo is being touched.

1. Stop and close the current **main.py** file.
2. Navigate to the **14_touch** folder in Thonny and open the **main.py** file.

You should see the code below:

```{literalinclude} ./python_files/14_touch/main.py
:linenos:
```

1. **Predict** what you think will happen. Be specific.
2. **Run** the program.
3. Time to **investigate** the code. What does each line do?

```{admonition} Code explanation
:class: notice
- **line 5** &rarr; creates a loop that keeps running
- **line 6** &rarr; makes the display blank
- **line 7** &rarr; checks if the pin logo is being touched
- **line 8** &rarr; shows a smiley face on the display
- **line 9** &rarr; waits for 10 milliseconds
```

## Other Pins

Pins 0, 1, and 2 can also work as touch inputs, but they need to be set up first.

1. Stop and close the current **main.py** file.
2. Navigate to the **14_touch_pins** folder in Thonny and open the **main.py** file.

You should see the code below:

```{literalinclude} ./python_files/14_touch_pins/main.py
:linenos:
```

1. **Predict** what you think will happen. Be specific.
2. **Run** the program.
3. Time to **investigate** the code. What does each line do?

```{admonition} Code explanation
:class: notice
- **line 5** &rarr; sets up pin 0 to sense capacitive touch
- **line 7** &rarr; creates a loop that keeps running
- **line 8** &rarr; makes the display blank
- **line 9** &rarr; checks if pin 0 is being touched
- **line 10** &rarr; shows a smiley face on the display
- **line 11** &rarr; waits for 10 milliseconds 
```

## Touch exercise 1

1. Stop and close the current **main.py** file.
2. Navigate to the **14_touch_ex1** folder in Thonny and open the **main.py** file.
3. Draw one pixel on the screen at position `(2, 2)`. Make the pixel move right if pin 2 is touched, or left if pin 0 is touched.
