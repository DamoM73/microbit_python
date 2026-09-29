# 3x RGB LED

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/7NIzQpjTXWg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

The PiicoDev 3x RGB LED Module has three full-colour LEDs that can each be set to any colour and brightness.

Possible uses:

- traffic lights
- status indicators for sensor readings
- colour-mixing projects
- notification lights

## Connect it

1. Connect the module to the PiicoDev adapter with a PiicoDev cable. See [Using PiicoDev](../micropython/piicodev.md).
2. Upload these files to the micro:bit with `main.py`:
    - `PiicoDev_Unified.py`
    - `PiicoDev_RGB.py`
3. The LEDs are numbered `0`, `1` and `2`.
4. Colours are lists of three numbers, `[red, green, blue]`, each from `0` to `255`. For example, `[255, 0, 255]` is magenta.

## Set it up

```python linenums="1"
from microbit import *
from PiicoDev_RGB import PiicoDev_RGB

leds = PiicoDev_RGB()
```

## Methods

| Method | Parameters | Returns | Description |
| --- | --- | --- | --- |
| `leds.setPixel(n, colour)` | `n`: LED 0–2<br>`colour`: `[r, g, b]` | none | Sets one LED's colour. Nothing changes until `show()`. |
| `leds.show()` | none | none | Sends the colours set with `setPixel()` to the LEDs |
| `leds.fill(colour)` | `colour`: `[r, g, b]` | none | Sets all three LEDs to one colour straight away |
| `leds.clear()` | none | none | Turns all the LEDs off |
| `leds.setBrightness(level)` | `level`: 0–255 | none | Sets the brightness of all the LEDs (default `50`) |
| `leds.pwrLED(state)` | `state`: `True` or `False` | none | Turns the small power LED on or off |
| `wheel(h)` | `h`: position on the colour wheel, 0–1 | list `[r, g, b]` | Converts a colour-wheel position into a colour |

### `setPixel()` and `show()`

`setPixel()` sets the colour of one LED in memory. `show()` sends the colours to the LEDs so they light up.

```python linenums="1"
--8<-- "examples/piicodev/rgb_led/setPixel/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → imports all the commands from the `microbit` library.
    - **line 2** → imports the RGB LED driver.
    - **line 5** → creates the module and calls it `leds`.
    - **line 8** → starts an endless loop.
    - **line 9** → sets LED `0` to red, in memory.
    - **line 10** → sends the colour to the LEDs so it lights up.

### `fill()`

Sets all three LEDs to the same colour straight away.

```python linenums="1"
--8<-- "examples/piicodev/rgb_led/fill/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → imports all the commands from the `microbit` library.
    - **line 2** → imports the RGB LED driver.
    - **line 5** → creates the module and calls it `leds`.
    - **line 8** → starts an endless loop.
    - **line 9** → sets all the LEDs to magenta.

### `clear()`

Turns all the LEDs off.

```python linenums="1"
--8<-- "examples/piicodev/rgb_led/clear/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → imports all the commands from the `microbit` library.
    - **line 2** → imports the RGB LED driver.
    - **line 5** → creates the module and calls it `leds`.
    - **line 8** → starts an endless loop.
    - **line 9** → sets all the LEDs to white.
    - **line 10** → waits 1 second.
    - **line 11** → turns all the LEDs off.
    - **line 12** → waits 1 second before the loop repeats.

### `setBrightness()`

Sets the brightness of all the LEDs, from `0` (off) to `255` (brightest).

```python linenums="1"
--8<-- "examples/piicodev/rgb_led/setBrightness/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → imports all the commands from the `microbit` library.
    - **line 2** → imports the RGB LED driver.
    - **line 5** → creates the module and calls it `leds`.
    - **line 6** → sets all the LEDs to blue at the default brightness.
    - **line 9** → starts an endless loop.
    - **line 10** → sets the brightness to `10`, much dimmer than the default `50`.
    - **line 11** → sends the new brightness to the LEDs.

### `pwrLED()`

Turns the small green power LED on the module on (`True`) or off (`False`).

```python linenums="1"
--8<-- "examples/piicodev/rgb_led/pwrLED/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → imports all the commands from the `microbit` library.
    - **line 2** → imports the RGB LED driver.
    - **line 5** → creates the module and calls it `leds`.
    - **line 8** → starts an endless loop.
    - **line 9** → turns the power LED off.

### `wheel()`

Converts a position on the colour wheel, from `0` to `1`, into an `[r, g, b]` colour.

`wheel()` is imported separately from the driver. It makes rainbow effects easy: `0` is red, and moving towards `1` goes through yellow, green, cyan, blue and magenta back to red.

```python linenums="1"
--8<-- "examples/piicodev/rgb_led/wheel/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → imports all the commands from the `microbit` library.
    - **line 2** → imports the RGB LED driver and the `wheel` function.
    - **line 5** → creates the module and calls it `leds`.
    - **line 8** → starts an endless loop.
    - **line 9** → gets the colour halfway around the wheel (cyan) and fills the LEDs with it.

## Documentation

Documentation is the official guide written by the people who made the code library, and we can use it to look up every method and its parameters, including ones that aren't covered on this page.

- [PiicoDev RGB LED driver](https://github.com/CoreElectronics/CE-PiicoDev-RGB-LED-MicroPython-Module)

## Exercises

!!! primm "PRIMM"
    Time to **modify** the code and see what happens.

Starter files are in the `rgb_led` folder of your tutorial files. Solutions are on the [Exercise Solutions](../reference/solutions.md#3x-rgb-led) page.

### Exercise 1

Starter: `rgb_led/ex1_traffic_light`

Can you make a traffic light, with LED `0` red, LED `1` amber and LED `2` green, lit one at a time in the right order?

### Exercise 2

Starter: `rgb_led/ex2_temperature_light`

Can you show the temperature as a colour: blue if it is below 20 °C, green from 20 to 25 °C, and red above 25 °C?
