# Micro:bit Module

The micro:bit has built-in functions for useful tasks we have not used yet. These functions are grouped in the `microbit` module. A module is a collection of code that you can import and use in your own program.

```{admonition} Documentation
:class: important
All the `microbit` module functions can be found in the **[BBC micro:bit MicroPython micro:bit documentation](https://microbit-micropython.readthedocs.io/en/v2-docs/microbit.html#microbit.running_time)**.
```

## Running Time

The `running_time()` function measures how long the micro:bit has been running since it was turned on or reset. It gives the time in milliseconds. There are `1000` milliseconds in one second.

### Running Time Demonstration

1. Stop and close the current **main.py** file.
2. Navigate to the **17_running_time_1** folder in Thonny and open the **main.py** file. 

You should see the code that shows how to use `running_time()` to print the current time count in the terminal.

```{literalinclude} ./python_files/17_running_time_1/main.py
:linenos:
```

### Running Time Example

1. Stop and close the current **main.py** file.
2. Navigate to the **17_running_time_2** folder in Thonny and open the **main.py** file.

The code below uses `running_time()` to create a 5-second countdown timer. The timer starts when button **A** is pressed.

```{literalinclude} ./python_files/17_running_time_2/main.py
:linenos:
```

## Set Volume

The `set_volume()` function changes the volume of the micro:bit's speaker. Use a number from `0` to `255`, where `0` is silent and `255` is the loudest.

### Set Volume Demonstration

1. Stop and close the current **main.py** file.
2. Navigate to the **17_set_volume_1** folder in Thonny and open the **main.py** file.

```{literalinclude} ./python_files/17_set_volume_1/main.py
:linenos:
```

## Sleep

The `sleep()` function pauses the program for a chosen number of milliseconds. Use it when you want the micro:bit to wait before doing the next instruction.

### Sleep Demonstration

1. Stop and close the current **main.py** file.
2. Navigate to the **17_sleep_1** folder in Thonny and open the **main.py** file.

```{literalinclude} ./python_files/17_sleep_1/main.py
:linenos:
```

## Run Every

The `run_every()` function runs another function at regular time intervals. This lets your program repeat a task, such as updating a timer, while the rest of the program keeps running.

### Run Every Demonstration

1. Stop and close the current **main.py** file.
2. Navigate to the **17_run_every_1** folder in Thonny and open the **main.py** file.

You should see the code below

```{literalinclude} ./python_files/17_run_every_1/main.py
:linenos:
```

### Run Every Example

1. Stop and close the current **main.py** file.
2. Navigate to the **17_run_every_2** folder in Thonny and open the **main.py** file.

The code below uses `run_every()` to create a countdown timer. The timer only counts down while a button is being pressed.

```{literalinclude} ./python_files/17_run_every_2/main.py
:linenos:
```
