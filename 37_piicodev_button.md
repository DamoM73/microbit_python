# PiicoDev Button

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/oNsP-YnHCho?si=uQfdLjlPCQs57Zy8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Buttons are a ubiquitous user interface - of course, you've seen them everywhere! The humble button is often the fastest way to create a control interface for your project too. This guide will help you get started with a PiicoDev® Button - an intuitive input device that allows you to easily interact with your project. We'll walk through some examples to read from the Button and remix the example code to do something cool with our development board.

## Getting set up

### Connect the PiicoDev Button module to your Micro:bit

Plug your Micro:bit into the PiicoDev adapter (buttons LED matrix facing up), connect your Button module to the adapter via the PiicoDev cable and connect your Micro:bit to your computer with a USB lead.

### Download the PiicoDev Modules

Create a new folder for this example. Then download the following files and save them to your new folder (Right Click > "Save Link As").

- **[`PiicoDev_Unified.py`](https://raw.githubusercontent.com/CoreElectronics/CE-PiicoDev-Unified/main/min/PiicoDev_Unified.py)** - The device driver.
- **[`PiicoDev_Switch.py`](https://raw.githubusercontent.com/CoreElectronics/CE-PiicoDev-Switch-MicroPython-Module/main/min/PiicoDev_Switch.py)** - The PiicoDev Unified Libraries: Drives I2C communications for PiicoDev modules

## Is Pressed

`button.is_pressed` continually returns a `1` as long as the button is pressed.

Create a new directory called `is_pressed` then create a new file inside it called `main.py` and add the code below.

Upload `main.py` along with `PiicoDev_Unified.py` and `PiicoDev_Switch.py` to the micro:bit and then **run** it. Notice what happens when you hold the button down.

```{literalinclude} ./python_files/piico_button_ispressed/main.py
:linenos:
```

Lets look at the important parts of that code:

- **line 1**: imports all the microbit commands
- **line 2**: imports all the button commands
- **line 6**: labels the button as `button`
- **line 14**: reads the current state of the button and stores it in `button_pressed`
- **lines 19 & 20**: displays a happy face if the button is currently pressed
- **lines 21 & 22**: displays a sad face if the button is not pressed

## Was Pressed

`button.was_pressed` returns one `1` when the button is pressed, then won't return another `1` before the button is released.

Create a new directory called `double_pressed` then create a new file inside it called `main.py` and add the code below.

Upload `main.py` along with `PiicoDev_Unified.py` and `PiicoDev_Switch.py` to the micro:bit and then run it. Notice what happens when you hold the button down.

```{literalinclude} ./python_files/piico_button_waspressed/main.py
:linenos:
```

Lets look at the important parts of that code:

- **line 1**: imports all the microbit commands
- **line 2**: imports all the button commands
- **line 6**: labels the button as `button`
- **line 14**: reads the button has been presses since it's last release and stores it in `button_pressed`
- **lines 19 & 20**: displays a happy face if the button was pressed
- **lines 21 & 22**: displays a sad face if the button was not pressed

## Was Double Pressed

`button.was_pressed` returns one `1` if the button has been double pressed since the last time it has been released.

Create a new directory called `was_double_pressed` then create a new file inside it called `main.py` and add the code below.

Upload `main.py` along with `PiicoDev_Unified.py` and `PiicoDev_Switch.py` to the micro:bit and then run it. Notice what happens when you hold the button down.

```{literalinclude} ./python_files/piico_button_doublepressed/main.py
:linenos:
```

Lets look at the important parts of that code:

- **line 1**: imports all the microbit commands
- **line 2**: imports all the button commands
- **line 6**: labels the button as `button`
- **line 14**: reads the button has been presses since it's last release and stores it in `button_pressed`
- **lines 19 & 20**: displays a happy face if the button was pressed
- **lines 21 & 22**: displays a sad face if the button was not pressed
