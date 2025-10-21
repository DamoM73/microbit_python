# Micro:bit Module

The micro:bit has built-in funtions that provide features beyond the input and output  compenents we have already explored. These functions are grouped together in the `microbit` module.

```{admonition} Documentation
:class: important
All the microbit module functions can be at **[BBC micro:bit MicroPython Microbit documentation](https://microbit-micropython.readthedocs.io/en/v2-docs/microbit.html#microbit.running_time)**.
```

## Running Time

The `running_time()` function measures how long the device has been running since the last power-on or reset. It returns the elapsed time in milliseconds.

### Running Time Demonstration

The code below shows how to use the `running_time()` function to show it's current count in the terminal.

```{literalinclude} ./python_files/running_time_1/main.py
:linenos:
```

### Running Time Example

The code belw shows how to use `running_time()` to create a 5 second countdown timer, that starts when button a is pressed.

```{literalinclude} ./python_files/running_time_2/main.py
:linenos:
```

## Set Volume

The `set_volume()` function adjusts the volume of the micro:bit's speaker. It takes a single argument, which is the volume level (0-255).

### Set Volume Demonstration

```{literalinclude} ./python_files/set_volume_1/main.py
:linenos:
```

## Sleep

The `sleep()` function pauses the execution of the program for a specified number of milliseconds. This is useful for creating delays in your code.

### Sleep Demonstration

```{literalinclude} ./python_files/sleep_1/main.py
:linenos:
```

## Run Every

The `run_every()` function allows you to schedule a function to be called at regular intervals. This lets your program perform a task again and again without stopping the rest of it from running.

### Run Every Demonstration

```{literalinclude} ./python_files/run_every_1/main.py
:linenos:
```

### Run Every Example

The code below shows how to use `run_every()` to create a countdown timer that reduces the time every second only when a button is pressed.

```{literalinclude} ./python_files/run_every_2/main.py
:linenos:
```