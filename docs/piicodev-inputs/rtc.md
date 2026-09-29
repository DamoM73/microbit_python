# Real Time Clock

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/ewzzmh7HUJE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

The PiicoDev Real Time Clock (RV-3028) keeps track of the date and time, even while the micro:bit is turned off.

Possible uses:

- clocks and alarm clocks
- timetable and bell reminders
- data loggers that record when each reading was taken
- countdowns to a date

## Connect it

1. Connect the clock to the PiicoDev adapter with a PiicoDev cable. See [Using PiicoDev](../micropython/piicodev.md).
2. Upload these files to the micro:bit with `main.py`:
    - `PiicoDev_Unified.py`
    - `PiicoDev_RV3028.py`
3. The clock keeps time using a small built-in backup power store, so set the time once and it keeps counting.

## Set it up

```python linenums="1"
from microbit import *
from PiicoDev_RV3028 import PiicoDev_RV3028

rtc = PiicoDev_RV3028()
```

## Methods

The date and time are stored in **properties**. Set them, then call `setDateTime()`; or call `getDateTime()`, then read them.

| Property | Values |
| --- | --- |
| `rtc.year` | 2000–2099 when setting; `getDateTime()` gives the last two digits, such as `26` |
| `rtc.month` | 1–12 |
| `rtc.day` | 1–31 |
| `rtc.hour` | 0–23 in 24-hour mode |
| `rtc.minute` | 0–59 |
| `rtc.second` | 0–59 |
| `rtc.ampm` | `"24"`, `"AM"` or `"PM"` |
| `rtc.weekday` | 0–6, where `0` is Monday |
| `rtc.weekdayName` | the name of the day, such as `"Monday"` |

| Method | Parameters | Returns | Description |
| --- | --- | --- | --- |
| `rtc.setDateTime()` | none | none | Writes the date and time properties to the clock |
| `rtc.getDateTime()` | none | none | Reads the clock into the date and time properties |
| `rtc.timestamp()` | none | string | Date and time as `YYYY-MM-DD HH:MM:SS` |
| `rtc.getUnixTime()` | none | int | Reads the clock's **Unix time** counter |
| `rtc.setUnixTime(time)` | `time`: Unix time | none | Sets the Unix time counter. It doesn't change the date and time. |

### `setDateTime()`

Writes the date and time properties to the clock.

Run this once to set the clock. Change the values to the current date and time first.

```python linenums="1"
--8<-- "examples/piicodev/rtc/setDateTime/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → imports all the commands from the `microbit` library.
    - **line 2** → imports the Real Time Clock driver.
    - **line 5** → creates the clock and calls it `rtc`.
    - **lines 6–11** → sets the year, month, day, hour, minute and second properties.
    - **line 12** → sets the day of the week. The clock doesn't work this out from the date, so we need to set it ourselves.
    - **line 13** → uses 24-hour time.
    - **line 14** → writes the date and time to the clock.

### `timestamp()`

Returns the date and time as one string, in the format `YYYY-MM-DD HH:MM:SS`.

```python linenums="1"
--8<-- "examples/piicodev/rtc/timestamp/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → imports all the commands from the `microbit` library.
    - **line 2** → imports the Real Time Clock driver.
    - **line 5** → creates the clock and calls it `rtc`.
    - **line 8** → starts an endless loop.
    - **line 9** → prints the date and time in the Shell.
    - **line 10** → waits 1 second before the loop repeats.

### `getDateTime()`

Reads the date and time from the clock into the `year`, `month`, `day`, `hour`, `minute`, `second` and `weekday` properties. `weekday` holds the day as a number from `0` (Monday) to `6` (Sunday), and `weekdayName` gives its name, such as `"Monday"`.

```python linenums="1"
--8<-- "examples/piicodev/rtc/getDateTime/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → imports all the commands from the `microbit` library.
    - **line 2** → imports the Real Time Clock driver.
    - **line 5** → creates the clock and calls it `rtc`.
    - **line 8** → starts an endless loop.
    - **line 9** → reads the clock into the date and time properties.
    - **line 10** → prints the hour and minute in the Shell.
    - **line 11** → waits 1 second before the loop repeats.

### `getUnixTime()`

Returns the clock's **Unix time**: the number of seconds since 1 January 1970.

Unix time is one number that counts seconds. It makes working out the time between two events easy: subtract one from the other. The clock keeps Unix time on a separate counter from the date and time, so it only matches the date and time once we set it with `setUnixTime()`.

```python linenums="1"
--8<-- "examples/piicodev/rtc/getUnixTime/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → imports all the commands from the `microbit` library.
    - **line 2** → imports the Real Time Clock driver.
    - **line 5** → creates the clock and calls it `rtc`.
    - **line 8** → starts an endless loop.
    - **line 9** → prints the Unix time in the Shell. It goes up by 1 every second.
    - **line 10** → waits 1 second before the loop repeats.

### `setUnixTime()`

Sets the clock's Unix time counter. It doesn't change the date and time that `timestamp()` and `getDateTime()` read.

```python linenums="1"
--8<-- "examples/piicodev/rtc/setUnixTime/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → imports all the commands from the `microbit` library.
    - **line 2** → imports the Real Time Clock driver.
    - **line 5** → creates the clock and calls it `rtc`.
    - **line 6** → sets the clock to Unix time `1790000000`.
    - **line 9** → starts an endless loop.
    - **line 10** → prints the Unix time in the Shell. It starts at `1790000000` and goes up by 1 every second.
    - **line 11** → waits 1 second before the loop repeats.

## Documentation

Documentation is the official guide written by the people who made the code library, and we can use it to look up every method and its parameters, including ones that aren't covered on this page.

- [PiicoDev RV-3028 driver](https://github.com/CoreElectronics/CE-PiicoDev-RV3028-MicroPython-Module)

## Exercises

!!! primm "PRIMM"
    Time to **modify** the code and see what happens.

Starter files are in the `rtc` folder of your tutorial files. Solutions are on the [Exercise Solutions](../reference/solutions.md#real-time-clock) page.

### Exercise 1

Starter: `rtc/ex1_clock`

Can you make a clock that shows the time when button **A** is pressed and the date when button **B** is pressed?

### Exercise 2

Starter: `rtc/ex2_greeting`

Can you make the micro:bit greet you when button **A** is pressed? It should show `Good morning` before 12 pm, `Good afternoon` from 12 pm until 6 pm, and `Good evening` after 6 pm.
