# Micro:bit Temperature Sensor

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/mrHn8eZ9eqg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

A temperature sensor is an input device that measures temperature. Your BBC micro:bit has a temperature sensor inside the processor. It can give you an approximate reading of the air temperature.

```{admonition} Temperature functions
:class: important
Full details can be found at the **[BBC micro:bit MicroPython temperature documentation](https://microbit-micropython.readthedocs.io/en/latest/microbit.html?highlight=Temperature%20#microbit.temperature)**.
```

## Temperature

To get a temperature reading, call the `temperature()` function.

For example:

```{literalinclude} ./python_files/temp/main.py
:linenos:
```

```{admonition} Code explanation
:class: notice
- **line 9** &rarr; creates an endless loop.
- **line 11** &rarr; gets the current temperature and stores it in the `temp` variable.
- **line 14** &rarr; turns the temperature into text and adds `C` for Celsius.
- **line 17** &rarr; scrolls the current temperature across the display.
```

### Temperature Exercises

1. Create a program that checks the air temperature every 2 seconds and keeps track of the minimum and maximum temperatures. When button **A** is pressed, display the minimum temperature. When button **B** is pressed, display the maximum temperature.
2. A comfortable room temperature for humans is usually between 20 and 22 degrees Celsius. Make your micro:bit monitor the room temperature and show a happy face if it is in that range. If the temperature is too high, show an up arrow. If it is too low, show a down arrow.
