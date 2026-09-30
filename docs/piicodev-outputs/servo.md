# Servo Driver

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/7D_5JzoxYyo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

The PiicoDev Servo Driver controls up to four servo motors, turning them to an angle or spinning them at a speed.

Possible uses:

- opening and closing gates and doors
- robot arms and grabbers
- wheels for small robots
- moving parts in models and animatronics

## Connect it

1. Connect the Servo Driver to the PiicoDev adapter with a PiicoDev cable. See [Using PiicoDev](../micropython/piicodev.md).
2. Put a horn (the plastic arm) on each servo's hub.
3. Plug the **continuous rotation servo** into **channel 1** (far left), with the orange wire lined up with **sig**.
4. Plug the **micro servo** into **channel 4** (far right), the same way.
5. Plug the power supply into the driver's USB-C socket and turn it on. Servos need more power than the micro:bit can provide.
6. Make sure the **ASW** switches are **off**.
7. Upload these files to the micro:bit with `main.py`:
    - `PiicoDev_Unified.py`
    - `PiicoDev_Servo.py`

!!! tip "Two kinds of servo"
    - A **micro servo** turns to an **angle**, from 0° to 180°, and holds it.
    - A **continuous rotation servo** spins like a wheel at a **speed**, from `-1` (full speed backwards) to `1` (full speed forwards).

## Set it up

Create the driver, then create a servo for each channel you use:

```python linenums="1"
from microbit import *
from PiicoDev_Servo import PiicoDev_Servo, PiicoDev_Servo_Driver

controller = PiicoDev_Servo_Driver()
servo = PiicoDev_Servo(controller, 4, min_us=625, max_us=2750, degrees=180)
motor = PiicoDev_Servo(controller, 1, midpoint_us=1500, range_us=1800)
```

The extra settings (`min_us`, `max_us`, `midpoint_us`, `range_us`) match the servos in our kits.

## Methods

| Method | Parameters | Returns | Description |
| --- | --- | --- | --- |
| `PiicoDev_Servo(controller, channel, ...)` | `controller`: the driver<br>`channel`: 1–4 | servo | Creates a servo on a channel |
| `servo.angle` | set to 0–180 | float | Turns a micro servo to an angle |
| `motor.speed` | set to -1 to 1 | float | Spins a continuous servo at a speed. `0` is stopped. |
| `servo.release()` | none | none | Stops sending signals, so the servo goes limp |

`angle` and `speed` are **properties**, so you set them with `=` instead of brackets.

### `angle`

Turns a micro servo to an angle from `0` to `180` degrees and holds it there.

```python linenums="1"
--8<-- "examples/piicodev/servo/angle/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → imports all the commands from the `microbit` library.
    - **line 2** → imports the Servo Driver classes.
    - **line 5** → creates the Servo Driver and calls it `controller`.
    - **line 6** → creates the micro servo on channel 4 and calls it `servo`.
    - **line 9** → starts an endless loop.
    - **line 10** → turns the servo to 90°.

### `speed`

Spins a continuous servo at a speed from `-1` (full speed backwards) to `1` (full speed forwards). `0` stops it.

```python linenums="1"
--8<-- "examples/piicodev/servo/speed/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → imports all the commands from the `microbit` library.
    - **line 2** → imports the Servo Driver classes.
    - **line 5** → creates the Servo Driver and calls it `controller`.
    - **line 6** → creates the continuous servo on channel 1 and calls it `motor`.
    - **line 9** → starts an endless loop.
    - **line 10** → spins forwards at half speed. Stop the program to stop the servo, or set `speed` to `0`.

### `release()`

Stops sending signals to the servo, so it goes limp and can be turned by hand.

```python linenums="1"
--8<-- "examples/piicodev/servo/release/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → imports all the commands from the `microbit` library.
    - **line 2** → imports the Servo Driver classes.
    - **line 5** → creates the Servo Driver and calls it `controller`.
    - **line 6** → creates the micro servo on channel 4 and calls it `servo`.
    - **line 9** → starts an endless loop.
    - **line 10** → turns the servo to 90°.
    - **line 11** → waits 1 second.
    - **line 12** → releases the servo. Try turning the horn by hand now.
    - **line 13** → waits 3 seconds before the loop repeats.

### Calibrating a continuous servo

If a continuous servo creeps when `speed` is `0`, its midpoint needs adjusting.

```python linenums="1"
--8<-- "examples/piicodev/servo/calibrate/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → imports all the commands from the `microbit` library.
    - **line 2** → imports the Servo Driver classes.
    - **line 5** → creates the Servo Driver and calls it `controller`.
    - **line 6** → creates the continuous servo with a midpoint of `1500`.
    - **line 7** → sets the speed to `0`. If the servo still turns, change `midpoint_us` on line 6 by about 25 at a time and run again until it stops. Use the same value in your other programs.

## Documentation

Documentation is the official guide written by the people who made the code library, and we can use it to look up every method and its parameters, including ones that aren't covered on this page.

- [PiicoDev Servo Driver](https://github.com/CoreElectronics/CE-PiicoDev-Servo-Driver-MicroPython-Module)
