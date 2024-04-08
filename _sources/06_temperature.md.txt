# Micro:bit Temperature Sensor

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/mrHn8eZ9eqg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

A temperature sensor is an input device that measures temperature. Your BBC micro:bit has a temperature sensor inside the processor which can give you an approximation of the air temperature.

```{admonition} Tempterature functions
:class: important
Full details can be found at the **[BBC micro:bit MicroPython temperature documentation](https://microbit-micropython.readthedocs.io/en/latest/microbit.html?highlight=Temperature%20#microbit.temperature)**.
```

## Temperature

To get a temperature reading, call the `temperature()` function.

For example:

```{literalinclude} ./python_files/temp/main.py
:linenos:
```

### Temperature Exercises

1. Create a program that samples the air temperature every two seconds and keeps a record of the minimum and maximum temperatures. When button **A** is pressed the minimum temperature is displayed, and when button **B** is pressed the maximum temperature is displayed.
2. For humans comfortable room temperature typically ranges between 20 to 22 degrees Celsius. Make your micro:bit monitor the room temperature and show a happy face if it is in the correct range. If the temperature is too high, show and up arrow, if it is too low shows a down arrow.
