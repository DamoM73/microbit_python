# PiicoDev OLED Module

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/xEcLUxhMMDY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

The PiicoDev OLED Display Module is perfect for adding a graphical display to your project. The monochrome white-on-black display provides a sharp image and fits a surprising amount of detail. Use this module to display text, draw shapes, animations, and even create plots.

The PiicoDev OLED Module screen has 128 pixels x 64 pixels, with the `(0,0)` coordinate in the top lefthand corner.

## Getting set up

### Connect the PiicoDev module to your Micro:bit

Plug your Micro:bit into the PiicoDev adapter (buttons LED matrix facing up), connect your module to the adapter via the PiicoDev cable and connect your Micro:bit to your computer with a USB lead.

Make sure that the ASW switch is in the off position (see below)

![OLED AWS Switch](assets/oled_asw_switch.jpg)

The PiicoDev OLED Module screen has 128 pixels x 64 pixels, with the `(0,0)` coordinate in the top lefthand corner.

## Line Example

There are several options for drawing simple lines.

- `line(x1, y1, x2, y2, c)` will draw a two-point line from `(x1,y1)` to `(x2,y2)` of colour `c`.
- `hline(x, y, l, c)` will draw a horizontal line from `(x, y)` of length `l`, colour `c`. Always draws left-to-right.
- `vline(x, y, l, c)` will draw a verticle line from `(x, y)` of length `l`, colour `c`. Always draws left-to-right.

The following example draws horizontal and vertical lines from the same point and joins their ends with a two-point line. There is a small delay between the drawing of each line.

1. Stop the program running on your micro:bit by clicking the **Stop** button in Thonny.
2. Open the **24_oled_example_1** folder in Thonny.
3. Check that the following files are in the folder:
   - `main.py`
   - `PiicoDev_Unified.py` - Drives I2C communications for PiicoDev modules
   - `PiicoDev_SSD1306.py` - The device driver for the PiicoDev OLED Module
4. To run the program you will need to upload these three files to the micro:bit. To do this, select all three files in the file browser, right-click and select **Upload to micro:bit**.
5. Open `main.py` and your should see the code below

```{literalinclude} ./python_files/24_oled_example_1/main.py
:linenos:
```

## Rectangle Example

Draw an unfilled rectangle with `rect(x,y,width,height,colour)`

The top-left corner is specified by `x` and `y`. `width` and `height` set the width and height in pixels. `colour` sets the line colour as `1` (white) or `0` (black)

The following example draws an unfilled rectangle to the left of the display, and a filled white rectangle to the right. A filled black rectangle is then drawn over the top.

1. Stop the program running on your micro:bit by clicking the **Stop** button in Thonny.
2. Open the **24_oled_example_2** folder in Thonny.
3. Check that the following files are in the folder:
   - `main.py`
   - `PiicoDev_Unified.py` - Drives I2C communications for PiicoDev modules
   - `PiicoDev_SSD1306.py` - The device driver for the PiicoDev OLED Module
4. To run the program you will need to upload these three files to the micro:bit. To do this, select all three files in the file browser, right-click and select **Upload to micro:bit**.
5. Open `main.py` and your should see the code below

```{literalinclude} ./python_files/24_oled_example_2/main.py
:linenos:
```

## Text Example

Display alphanumeric text with `text(string, x, y, colour)`, where;

- `string` is a python string
- `x`, `y` are the top-left co-ordinates
- `colour` is `1` (white) or `0` (black)

The following example prints four lines. The first is a literal string, where the text to be printed is inserted into the function call. The second prints a string variable myString. The third and fourth print the value stored in a variable.

1. Stop the program running on your micro:bit by clicking the **Stop** button in Thonny.
2. Open the **24_oled_example_3** folder in Thonny.
3. Check that the following files are in the folder:
   - `main.py`
   - `PiicoDev_Unified.py` - Drives I2C communications for PiicoDev modules
   - `PiicoDev_SSD1306.py` - The device driver for the PiicoDev OLED Module
   - `font-pet-me-128.dat` - The font file used to display text 
4. To run the program you will need to upload these four files to the micro:bit. To do this, select all four files in the file browser, right-click and select **Upload to micro:bit**.
5. Open `main.py` and your should see the code below

```{literalinclude} ./python_files/24_oled_example_3/main.py
:linenos:
```
## Graph

Graphs are created with the `graph2D()` function allows plotting a single variable as it changes over time. The plot starts at the right-hand side of the display and shifts to the left every time it is updated.

`updateGraph2D(graph, value)` pushes the latest value onto a graph object. Multiple graphs can be shown at the same time and must be updated by making separate calls to updateGraph2D().

The following example graphs two functions independently.

1. Stop the program running on your micro:bit by clicking the **Stop** button in Thonny.
2. Open the **24_oled_example_4** folder in Thonny.
3. Check that the following files are in the folder:
   - `main.py`
   - `PiicoDev_Unified.py` - Drives I2C communications for PiicoDev modules
   - `PiicoDev_SSD1306.py` - The device driver for the PiicoDev OLED Module
   - `font-pet-me-128.dat` - The font file used to display text 
4. To run the program you will need to upload these four files to the micro:bit. To do this, select all four files in the file browser, right-click and select **Upload to micro:bit**.
5. Open `main.py` and your should see the code below


```{literalinclude} ./python_files/24_oled_example_4/main.py
:linenos:
```

### Animation

In general, the steps to create an animation are:

- Clear the display (we generally don't want to draw over old frames)
- Draw a frame - this is usually generated by some variable that changes with time.
- Update the display

The following example animates a rectangle bouncing around the screen.

1. Stop the program running on your micro:bit by clicking the **Stop** button in Thonny.
2. Open the **24_oled_example_5** folder in Thonny.
3. Check that the following files are in the folder:
   - `main.py`
   - `PiicoDev_Unified.py` - Drives I2C communications for PiicoDev modules
   - `PiicoDev_SSD1306.py` - The device driver for the PiicoDev OLED Module
   - `font-pet-me-128.dat` - The font file used to display text 
4. To run the program you will need to upload these four files to the micro:bit. To do this, select all four files in the file browser, right-click and select **Upload to micro:bit**.
5. Open `main.py` and your should see the code below

```{literalinclude} ./python_files/24_oled_example_5/main.py
:linenos:
```

### Bitmap Images

It is possible to display Portable Bitmap Images (.pbm) files on our OLED module. The source image needs to be uploaded to our micro:bit just like any other source file. 

```{admonition} Memory limitations
:class: error
Beware: the memory on a micro:bit is very limited and bitmap images will take a while to display.
```

The following example displays the PiicoDev logo on the screen.

1. Stop the program running on your micro:bit by clicking the **Stop** button in Thonny.
2. Open the **24_oled_example_6** folder in Thonny.
3. Check that the following files are in the folder:
   - `main.py`
   - `PiicoDev_Unified.py` - Drives I2C communications for PiicoDev modules
   - `PiicoDev_SSD1306.py` - The device driver for the PiicoDev OLED Module
   - `PiicoDev_logo.pbm` - The bitmap image file to be displayed
4. To run the program you will need to upload these four files to the micro:bit. To do this, select all four files in the file browser, right-click and select **Upload to micro:bit**.
5. Open `main.py` and your should see the code below

```{literalinclude} ./python_files/24_oled_example_6/main.py
:linenos:
```

