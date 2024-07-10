# Micro:bit Touch Sensor

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/spFD3SxxxHQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

We can use the gold logo as another input in your projects. It's like having an extra button. The touch logo uses capacitive touch, sensing tiny changes in electrical fields to know when your finger is pressing it - just like your phone or tablet screen.

```{admonition} Pins
:class: important
Full details can be found at the **[BBC micro:bit MicroPython pins documentation](https://microbit-micropython.readthedocs.io/en/v2-docs/microbit_micropython_api.html?highlight=touch#pins)**.
```

## Pin logo

The logo at the top of the micro:bit is a capacitive touch button.

Calling `pin_logo.is_touched()` will return `True` if the logo is being touched.

For example:

```{literalinclude} ./python_files/touch/main.py
:linenos:
```

```{admonition} Code explaination
:class: notice
- **line 5** &rarr; creates an infinite loop, since the condition (`True`) will never be `False`
- **line 6** &rarr; make the display blank
- **line 7** &rarr; checks if the pin logo is being touched
- **line 8** &rarr; shows a smiley face on display
- **line 9** &rarr; waits for 10 milliseconds
```

## Other Pins

Pins 0, 1 and 2 can also do capacitive touch, but they need to be configured first.

For example:

```{literalinclude} ./python_files/touch_pins/main.py
:linenos:
```

```{admonition} Code explaination
:class: notice
- **line 5** &rarr; configure the pin0 to sense capacitve touch
- **line 7** &rarr; creates an infinite loop, since the condition (`True`) will never be `False`
- **line 8** &rarr; make the display blank
- **line 9** &rarr; checks if the pin logo is being touched
- **line 10** &rarr; shows a smiley face on display
- **line 11** &rarr; waits for 10 milliseconds 
```

## Touch exercises

1. Draw one pixel on the screen at position (2,2), then have the pixel move right if Pin2 is touched, or move left if Pin0 is touched.
2. Improve the last program so the pixel wraps around the screen.