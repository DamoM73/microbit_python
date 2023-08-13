# Micro:bit Touch Sensor

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

## Other Pins

Pins 0, 1 and 2 can also do capacitive touch, but they need to be configured first.

For example:

```{literalinclude} ./python_files/touch_pins/main.py
:linenos:
```

## Touch exercises

1. Draw one pixel on the screen at position (2,2), then have the pixel move right if Pin2 is touched, or move left if Pin0 is touched.
2. Improve the last program so the pixel wraps around the screen.