# Micro:bit Light Sensor

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/ii0U_FMr-Z4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

A light sensor is an input device that measures light levels. Your BBC micro:bit can use its LEDs to sense the amount of light around it.

```{admonition} Light functions
:class: important
Full details can be found at the **[BBC micro:bit MicroPython light documentation](https://microbit-micropython.readthedocs.io/en/latest/display.html?highlight=light#microbit.display.read_light_level)**.
```

## Get Light Level

The micro:bit uses the LEDs in its display to sense how much light is shining on it.

`read_light_level()` returns an integer between `0` and `255`. A larger number means more light.

For example:

```{literalinclude} ./python_files/11_light/main.py
:linenos:
```

```{admonition} Code explanation
:class: notice
- **line 9** &rarr; creates an endless loop.
- **line 11** &rarr; takes the current light reading and stores it in the `light_level` variable.
- **line 16** &rarr; scrolls the light level across the display.
- **line 18** &rarr; waits 500 milliseconds before going back to the top of the loop.
```

### Light Exercises

1. Create a program that checks the light level every 2 seconds. It should display a message showing whether the light level has increased (&uarr;) or decreased (&darr;).
2. Create a program that measures the light level and turns on all the LEDs when the light level falls below `100`.
