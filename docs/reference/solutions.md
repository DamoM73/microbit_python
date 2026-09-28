# Exercise Solutions

These are **a** solution to each exercise. There are many ways to solve a programming problem. If your program produces the required result, it solves the problem.

## Your First Program

### Exercise 1

```python linenums="1"
--8<-- "solutions/micropython/ex1_message.py"
```

### Exercise 2

```python linenums="1"
--8<-- "solutions/micropython/ex2_shapes.py"
```

### Exercise 3

The micro:bit shows the message and the heart once, then stops. Without the `while True:` loop the code runs in sequence from top to bottom, reaches the end and finishes. The loop sends the program back to the top so it repeats.

### Exercise 4

The micro:bit turns off when unplugged because it gets its power from the computer. When it is plugged back in, nothing happens because the program is still only on the computer. It hasn't been uploaded to the micro:bit.

## Display

### Exercise 1

```python linenums="1"
--8<-- "solutions/microbit/display/ex1_show_message.py"
```

### Exercise 2

```python linenums="1"
--8<-- "solutions/microbit/display/ex2_show_delay.py"
```

### Exercise 3

```python linenums="1"
--8<-- "solutions/microbit/display/ex3_show_no_loop.py"
```

### Exercise 4

```python linenums="1"
--8<-- "solutions/microbit/display/ex4_heartbeat.py"
```

### Exercise 5

```python linenums="1"
--8<-- "solutions/microbit/display/ex5_clock.py"
```

### Exercise 6

```python linenums="1"
--8<-- "solutions/microbit/display/ex6_spinning_square.py"
```

### Exercise 7

The pixels flash on and off too quickly to see. The micro:bit runs much faster than our eyes can follow, so each pixel is cleared almost as soon as it is turned on. `sleep(50)` keeps each pixel lit long enough to be seen.

### Exercise 8

```python linenums="1"
--8<-- "solutions/microbit/display/ex8_rows.py"
```

### Exercise 9

```python linenums="1"
--8<-- "solutions/microbit/display/ex9_glasses.py"
```

## Buttons

### Exercise 1

```python linenums="1"
--8<-- "solutions/microbit/buttons/ex1_press_challenge.py"
```

### Exercise 2

```python linenums="1"
--8<-- "solutions/microbit/buttons/ex2_counter.py"
```

### Exercise 3

```python linenums="1"
--8<-- "solutions/microbit/buttons/ex3_reaction_timer.py"
```

### Exercise 4

```python linenums="1"
--8<-- "solutions/microbit/buttons/ex4_memory_game.py"
```

## Accelerometer

### Exercise 1

Readings between `-100` and `100` count as level. Change this range to make the level more or less sensitive.

```python linenums="1"
--8<-- "solutions/microbit/accelerometer/ex1_spirit_level.py"
```

### Exercise 2

```python linenums="1"
--8<-- "solutions/microbit/accelerometer/ex2_face_up.py"
```

### Exercise 3

```python linenums="1"
--8<-- "solutions/microbit/accelerometer/ex3_shake_count.py"
```

### Exercise 4

```python linenums="1"
--8<-- "solutions/microbit/accelerometer/ex4_3g.py"
```

## Temperature

### Exercise 1

```python linenums="1"
--8<-- "solutions/microbit/temperature/ex1_min_max.py"
```

### Exercise 2

```python linenums="1"
--8<-- "solutions/microbit/temperature/ex2_comfort.py"
```

## Light Sensor

### Exercise 1

```python linenums="1"
--8<-- "solutions/microbit/light/ex1_up_down.py"
```

### Exercise 2

The display is cleared before each reading, because lit LEDs affect the light reading.

```python linenums="1"
--8<-- "solutions/microbit/light/ex2_night_light.py"
```

## Compass

### Exercise 1

Headings from 338° to 22° count as North.

```python linenums="1"
--8<-- "solutions/microbit/compass/ex1_north.py"
```

### Exercise 2

Adding 22 then dividing by 45 splits the 360° circle into eight 45° slices centred on each direction.

```python linenums="1"
--8<-- "solutions/microbit/compass/ex2_eight_points.py"
```

### Exercise 3

```python linenums="1"
--8<-- "solutions/microbit/compass/ex3_microtesla.py"
```

### Exercise 4

Test your magnet first with the `get_field_strength()` example, then change `500000` to suit it.

```python linenums="1"
--8<-- "solutions/microbit/compass/ex4_magnet.py"
```

## Touch

### Exercise 1

```python linenums="1"
--8<-- "solutions/microbit/touch/ex1_move_pixel.py"
```

## Sound

### Exercise 1

This plays the opening of "Mary Had a Little Lamb".

```python linenums="1"
--8<-- "solutions/microbit/sound/ex1_my_tune.py"
```

### Exercise 2

This depends on your College Song. Use `speech.sing()` with a pitch number before each sound, as in the `sing()` example.

### Exercise 3

`sound_level()` goes from `0` to `255`. Dividing by `51` gives a number of rows from `0` to `5`.

```python linenums="1"
--8<-- "solutions/microbit/sound/ex3_sound_meter.py"
```

## Radio

### Exercise 1

Press **A** on one micro:bit to give it the image to start.

```python linenums="1"
--8<-- "solutions/microbit/radio/ex1_pass_image.py"
```

### Exercise 2

```python linenums="1"
--8<-- "solutions/microbit/radio/ex2_yes_no.py"
```

### Exercise 3

#### Outside micro:bit

```python linenums="1"
--8<-- "solutions/microbit/radio/ex3_outside.py"
```

#### Inside micro:bit

```python linenums="1"
--8<-- "solutions/microbit/radio/ex3_inside.py"
```

## Atmospheric Sensor

### Exercise 1

```python linenums="1"
--8<-- "solutions/piicodev/atmospheric/ex1_buttons.py"
```

### Exercise 2

```python linenums="1"
--8<-- "solutions/piicodev/atmospheric/ex2_height_change.py"
```

## Colour Sensor

### Exercise 1

`white` is the amount of ambient light in lux. `cct` is the colour temperature in kelvin: lower numbers are warmer (more orange) light, higher numbers are cooler (more blue) light.

```python linenums="1"
--8<-- "solutions/piicodev/colour/ex1_rgb_dictionary.py"
```

### Exercise 2

`classifyHue()` returns `None` when it can't decide, so the `if colour:` check skips those readings.

```python linenums="1"
--8<-- "solutions/piicodev/colour/ex2_show_colour.py"
```

## Distance Sensor

### Exercise 1

```python linenums="1"
--8<-- "solutions/piicodev/distance/ex1_button_reading.py"
```

## Real Time Clock

### Exercise 1

`"{:02}".format()` adds a leading zero, so 9 minutes shows as `09`.

```python linenums="1"
--8<-- "solutions/piicodev/rtc/ex1_clock.py"
```

### Exercise 2

```python linenums="1"
--8<-- "solutions/piicodev/rtc/ex2_stopwatch.py"
```

## 3x RGB LED

### Exercise 1

```python linenums="1"
--8<-- "solutions/piicodev/rgb_led/ex1_traffic_light.py"
```

### Exercise 2

```python linenums="1"
--8<-- "solutions/piicodev/rgb_led/ex2_temperature_light.py"
```
