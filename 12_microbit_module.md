# Micro:bit Module

The micro:bit has built-in funtions that provide features beyond the input and output  compenents we have already explored. These functions are grouped together in the `microbit` module.

```{admonition} Documentation
:class: important
All the microbit module functions can be at **[BBC micro:bit MicroPython Microbit documentation](https://microbit-micropython.readthedocs.io/en/v2-docs/microbit.html#microbit.running_time)**.
```

## Running Time

The `running_time()` function measures how long the device has been running since the last power-on or reset. It returns the elapsed time in milliseconds.

## Reset

The `reset()` function restarts the micro:bit, stopping any running code and resetting all variables and states to their initial values.

## Set Volume

The `set_volume()` function adjusts the volume of the micro:bit's speaker. It takes a single argument, which is the volume level (0-255).

## Sleep

The `sleep()` function pauses the execution of the program for a specified number of milliseconds. This is useful for creating delays in your code.

## Run Every

The `run_every()` function allows you to schedule a function to be called at regular intervals. It takes two arguments: the function to be called and the interval in milliseconds.