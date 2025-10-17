# Micro:bit Light Sensor

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/ii0U_FMr-Z4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

A light sensor is an input device that measures light levels. Your BBC micro:bit uses the LEDs to sense the levels of light and lets you program your micro:bit as a light sensor.

```{admonition} Light functions
:class: important
Full details can be found at the **[BBC micro:bit MicroPython light documentation](https://microbit-micropython.readthedocs.io/en/latest/display.html?highlight=light#microbit.display.read_light_level)**.
```

## Get light level

The micro:bit uses the display’s LEDs in reverse-bias mode to sense the amount of light falling on the display. 

Returns an integer between `0` and `255` representing the light level, with larger meaning more light.

For example:

```{literalinclude} ./python_files/light/main.py
:linenos:
```

```{admonition} Code explaination
:class: notice
- **line 5** &rarr; creates an infinite loop, since the condition (`True`) will never be `False`.
- **line 6** &rarr; checks whether button A has been pressed
- **line 7** &rarr; takes the current light reading and stores it in the light_level variable
- **line 8** &rarr; waits for 100 milliseconds
- **line 9** &rarr; scrolls the light level across the display
- **line 10** &rarr; makes the display blank
- **line 11** &rarr; waits half a second
- **line 12** &rarr; turns on the centre pixel in the display
- **line 13** &rarr; waits half a second
```

### Light Exercises

1. Create a program that samples light levels using the micro:bit's light sensor every two seconds. It should displays messages based on whether the light level has increased (&uarr;) or decreased (&darr;).
2. Create a program that measures the light level using the micro:bit's light sensor and activates all the LEDs on the micro:bit when the light level falls below a threshold of 100.
