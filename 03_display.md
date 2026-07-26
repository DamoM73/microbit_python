# Micro:bit Display

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/eRhlaXqT-0w" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

We have already used the micro:bit display in our first program. In this section, we will learn more about its features.

```{admonition} Documentation
:class: important
Throughout this tutorial, links to the official documentation will be provided in green callout boxes like this one.

All the display functions can be found at the **[BBC micro:bit MicroPython display documentation](https://microbit-micropython.readthedocs.io/en/latest/display.html#module-microbit.display)**.
```

## Text

### Scroll

```{admonition} scroll function
:class: important
**`microbit.display.scroll(text, delay=150, \*, wait=True, loop=False, monospace=False)`**

Full details can be found at the **[BBC micro:bit MicroPython display.scroll documentation](https://microbit-micropython.readthedocs.io/en/latest/display.html#microbit.display.scroll)**.
```

Our first program used the `scroll()` function to make a string scroll across the display.

```{literalinclude} ./python_files/01_first_program/main.py
:linenos:
```

![first_program displayed](./assets/first_program.gif)

Although our example uses strings, the `scroll()` function can also display **floats**, **integers**, and **Boolean** values.

### Show

```{admonition} show function
:class: important
**`microbit.display.show(image)`**

Full details can be found at the **[BBC micro:bit MicroPython display.show documentation](https://microbit-micropython.readthedocs.io/en/latest/display.html#microbit.display.show)**.
```

Another way to display characters is to use the `show()` function.

Before we can run the code below, we need to:

- stop the micro:bit by clicking Thonny's **stop** button
- navigate back to the **micro:bit** directory and create a new directory called **display_show**.
- navigate to the **display_show** directory.

Create a new file called **main.py** and add the code below.

```{literalinclude} ./python_files/02_display_show/main.py
:linenos:
```

**Predict** what you think the program will do. Be specific. For example, "pause for 2 seconds" is better than just "pause". Then **run** the program.

![display show](./assets/display_show.gif)

```{admonition} Code explanation
:class: notice
- **line 1** &rarr; imports all the commands from the `microbit` library.
- **line 9** &rarr; sets up the endless loop.
- **line 15** &rarr; `display.show()` displays one character at a time.
  - `3.14159` &rarr; message to be displayed. This can be a string, integer, float or Boolean.
  - `delay=500` &rarr; puts a 500 millisecond pause after each character
- **line 16** &rarr; `display.clear()` changes the value of each pixel to `0`, which clears the screen.
- **line 17** &rarr; waits 1000 milliseconds before going back to the top of the loop.
```

Time to **modify** the code and see what happens:

### Text Exercises

1. Can you make it display a different message? For example:

![Display Text Exercise 1](./assets/display_text_ex1.gif)

2. Can you change the time between each character? For example:

![Display Text Exercise 2](./assets/display_text_ex2.gif)

3. Using the details in the **display.show docs**, can you display the same message without the `while True` loop?

![Display Text Exercise 3](./assets/display_text_ex3.gif)

## Images

```{admonition} micro:bit Images
:class: important
The micro:bit has a wide range of **[pre-set images](https://microbit-micropython.readthedocs.io/en/latest/image.html#attributes)** that can be used with the `show()` function.
```

You can also use the `display.show()` function to display pre-set images.

Again, since we are making a new program, create a new folder called **display_images** in the **micro:bit** folder. Then create a new **main.py** file.

Add the following code to the file.

```{literalinclude} ./python_files/03_display_images/main.py
:linenos:
```

**Predict** what you think the program will do. Remember to be specific. Then **run** the program.

![display image](./assets/display_image.gif)

```{admonition} Code explanation
:class: notice
- **line 15** &rarr; `display.show(Image.HEART)` shows a heart on the display.
- **line 17** &rarr; `display.show(Image.HEART_SMALL)` shows a small heart on the display.
```

Time to **modify** the code:

### Image Exercises

1. Can you change the heartbeat animation so it looks more like an **[actual heartbeat](https://www.youtube.com/watch?v=gJpT_wHZeF8)**? Like this:

![display image ex1](./assets/display_image_ex1.gif)

2. Can you make the display show a clock face progressing from 1 to 12? Like this:

![display image ex2](./assets/display_image_ex2.gif)

3. Can you make the display show a square spinning? Like this:

![display image ex3](./assets/display_image_ex3.gif)

## Custom

```{admonition} set_pixel function
:class: important

**`microbit.display.set_pixel(x, y, value)`**

Full details can be found at the **[BBC micro:bit MicroPython display.set_pixel documentation](https://microbit-micropython.readthedocs.io/en/latest/display.html#microbit.display.set_pixel)**.
```

You can also directly control the individual LEDs on the display. The image below shows the coordinate numbers for each LED:

- top left &rarr; `(0,0)`
- bottom right &rarr; `(4,4)`

![display coordinates](./assets/display_coords.jpg)

Each pixel can be set to a value from `0` (off) to `9` (brightest).

To explore this, we will make a new program. Create a new folder called **display_custom** in the **micro:bit** folder. Then create a new **main.py** file.

Add the code below, save it, and then run it on the micro:bit.

```{literalinclude} ./python_files/04_display_custom/main.py
:linenos:
```

**Predict** what you think the program will do. Remember to be specific. Then **run** the program.

![display custom](./assets/display_custom.gif)

```{admonition} Code explanation
:class: notice 
This code uses nested loops. A nested loop is a loop inside another loop.

- **line 7** &rarr; stores the number of rows on the display.
- **line 8** &rarr; stores the number of columns on the display.
- **line 10** &rarr; clears the display before the loop starts.
- **line 11** &rarr; creates an endless loop.
- **line 17** &rarr; changes the column number from `0` to `4`.
- **line 18** &rarr; changes the row number from `0` to `4` for each column.
- **line 19** &rarr; turns the selected LED on at full brightness.
- **line 20** &rarr; waits 50 milliseconds so the LED can be seen.
- **line 21** &rarr; clears the display before moving to the next LED.
```

Time to **modify** the code:

### Custom Exercises

1. What happens if you remove the `sleep(50)` statement? Why do you think this happens?

2. Can you change the code so it moves across the rows instead of down the columns? 

![display custom ex2](./assets/display_custom_ex2.gif)

3. Can you create this smiley face with glasses? The **[Image class](https://microbit-micropython.readthedocs.io/en/latest/image.html#microbit.Image)** might help.

![display custom ex3](./assets/display_custom_ex3.png)

## Other Functions

There are other display-related functions, such as:

- **[get_pixel](https://microbit-micropython.readthedocs.io/en/latest/display.html#microbit.display.get_pixel)** &rarr; returns the brightness of a given pixel
- **[on](https://microbit-micropython.readthedocs.io/en/latest/display.html#microbit.display.on)** &rarr; turns the display on
- **[off](https://microbit-micropython.readthedocs.io/en/latest/display.html#microbit.display.off)** &rarr; turns the display off
- **[is_on](https://microbit-micropython.readthedocs.io/en/latest/display.html#microbit.display.is_on)** &rarr; indicates if the display is on
- **[read_light_level](https://microbit-micropython.readthedocs.io/en/latest/display.html#microbit.display.read_light_level)** &rarr; gives a reading of the light level around the micro:bit.

