# Micro:bit Sensors

For a little board the Micro:bit comes packed with a heap of sensors. This lesson will explore them.

## Movement

```{admonition} Movement functions
:class: important
Full details can be found at the **[BBC micro:bit MicroPython movement documentation](https://microbit-micropython.readthedocs.io/en/latest/tutorials/movement.html#movement)**.
```

Your BBC micro:bit comes with an accelerometer. An accelerometer can detect and measure how fast something is moving or how it's being tilted. It can sense motion in different directions like up, down, left, and right. 

The micro:bit accelerometer measures movement along three axes:

- X - tilting from left to right.
- Y - tilting forwards and backwards.
- Z - moving up and down.

There is a method for each axis that returns a positive or negative number indicating a measurement in milli-g’s. When the reading is 0 you are “level” along that particular axis.

Below is an example for the x-axis:

```{literalinclude} ./python_files/movement/main.py
:linenos:
```

### Movement exercises

1. Change the example above to show the value for the y-axis
2. Change the example above to show the value for the z-axis
3. Make a leveling device that shows a `-` if the x-axis is level, `L` if the left side is too high or `R` if the right side is too high.

## Temperature

## Light

## Compass

## Touch