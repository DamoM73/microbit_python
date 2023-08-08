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