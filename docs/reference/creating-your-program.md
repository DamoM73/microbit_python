# Creating Your Program

!!! learn "On this page we will learn"
    - how to choose the components our project needs
    - how to wire up the components and test each one
    - the structure every program in this course uses: imports, setup and main loop
    - how to plan, build and test a program step by step

When we make our own project, we work through three stages, in this order:

1. **Choose the components** → work out which inputs and outputs the project needs.
2. **Wire them up** → connect the components, upload their files and check that each one works.
3. **Create the program** → plan, build and test the code one step at a time.

Doing it in this order saves us time. If something doesn't work later, we already know each component works on its own, so the problem must be in our code.

At the end of this page, we follow all three stages to build a **Too Hot Alarm**. It shows green lights and a happy face when the room is comfortable, and red lights, a sad face and a beep when it gets too hot.

## 1. Choose the components

Every project takes information in, works out what to do with it, and does something with the result. So let's start with the project's inputs and outputs:

1. Write one sentence that says what the project does.
2. List the information it needs → these are the **inputs**.
3. List what it needs to do or show → these are the **outputs**.
4. For each input and output, find a component that can do the job on the [Components](components.md) page. When a built-in component can do the job well, we use it, because there is less to wire up.

Then put the components in a planning table. The last column tells us which page to read for the code we need.

| Component | Input or output | What it does in our project | Page |
| --- | --- | --- | --- |
| | | | |

## 2. Wire them up

Now that we know our components, let's connect them. Built-in components, like the display and speaker, don't need connecting.

### Wiring checklist

1. **Unplug the USB cable and battery pack.** Connecting components while the micro:bit has power can damage them. With no power connected, the micro:bit's lights should be off.
2. **Plug the micro:bit into the PiicoDev Adapter**, with the buttons and LED display facing up.
3. **Chain the PiicoDev modules with PiicoDev cables**: adapter → module → module. The order of the modules in the chain doesn't matter.
4. **Check the address switches (ASW).** Keep them all off, unless the project uses two of the same module. See [Using PiicoDev](../micropython/piicodev.md#connect-a-module).
5. **Connect any other components** following their page's Connect it section. For example, the [Glowbit Rainbow](../other/glowbit.md) uses alligator clips. Make sure the clips don't touch each other.
6. **Plug the USB cable back in.** The micro:bit's lights should come on, and so should the power LED on each PiicoDev module.

### Upload the driver files

Each PiicoDev module needs its device driver, as well as `PiicoDev_Unified.py`. We get these from the [device drivers table](../micropython/piicodev.md#device-drivers).

1. [Create a new program](../micropython/first-program.md#create-a-new-program) folder for the project, with a `main.py`.
2. Copy `PiicoDev_Unified.py` and the driver for each type of module into the folder. The example folders for each module in your tutorial files already have them.
3. [Upload the files](../micropython/piicodev.md#upload-the-files) to the micro:bit.

!!! warning "Remove drivers we aren't using"
    The micro:bit has very little space for files. Before uploading, delete any driver files from earlier projects that this project doesn't use.

### Test each part first

Before we combine the components, we run each one's own example from the tutorial files. If an example doesn't work, we fix it now: check the cable, the address switches and the driver files.

| Component | Example to run | Expected result |
| --- | --- | --- |
| | | |

## 3. Create the program

Now that every component works, we can write the program. Every example in this course uses the same structure. We will use it for our own programs too, because it keeps our code organised and makes problems easier to find and fix.

### The structure

A micro:bit program has three parts, always in this order:

| Part | Runs | What goes here |
| --- | --- | --- |
| Imports | once, first | the libraries and drivers our program uses |
| `# Setup` | once, before the loop | creating sensors and devices, and variables with starting values |
| `# Main loop` | over and over, forever | the code that reads inputs, makes decisions and controls outputs |

#### Imports

Imports bring in code that someone else has already written, so we can use it in our program.

- Every program starts with `from microbit import *`. This gives us the display, buttons, sensors and `sleep()`.
- Add other modules our program needs, such as `import music`, `import radio` or a PiicoDev driver.

#### `# Setup`

Code under `# Setup` runs **once**, when the program starts. We use it for things that only need to happen once:

- creating PiicoDev devices, for example `sensor = PiicoDev_VL53L1X()`
- setting up variables with their starting values, for example `score = 0`
- settings that don't change, for example `radio.config(group=7)`

If our program doesn't need any setup, we can leave this part empty.

#### `# Main loop`

`while True:` starts a loop that repeats forever. A micro:bit program usually never finishes: it keeps checking its inputs and updating its outputs until it is turned off.

Everything **indented** under `while True:` is inside the loop.

### Input, process, output

Inside the main loop, we organise our code into three steps:

1. **Input** → read the information our program needs, such as a button, a sensor or a radio message.
2. **Process** → work out what to do with it, using calculations and decisions (`if` statements).
3. **Output** → show the result, using the display, sounds, LEDs or motors.

Short examples in this course often combine these steps. In our own programs, we use `# Input`, `# Process` and `# Output` comments to keep them separate.

We end the loop with a short `sleep()`, so the micro:bit isn't checking faster than it needs to.

### Template

!!! warning "New program, new folder"
    Every program needs its own folder with its own `main.py`. Before we start a new program, we create a new folder for it. See [Create a new program](../micropython/first-program.md#create-a-new-program) for how.

Copy this into a new `main.py` to start a program. It is also in the `micropython/template` folder of your tutorial files.

```python linenums="1"
--8<-- "examples/micropython/template/main.py"
```

## Worked example: Too Hot Alarm

Let's put the three stages together to build the Too Hot Alarm.

### 1. Choose the components

Our sentence: *the alarm shows whether the room is comfortable or too hot*.

- the room's temperature → input
- a colour we can see from across the room → output
- a face on the display → output
- a beep → output

| Component | Input or output | What it does in our project | Page |
| --- | --- | --- | --- |
| Atmospheric Sensor | Input | measures the air temperature | [Atmospheric Sensor](../piicodev-inputs/atmospheric.md) |
| 3x RGB LED | Output | shows green or red | [3x RGB LED](../piicodev-outputs/rgb-led.md) |
| Display | Output | shows a happy or sad face | [Display](../microbit/display.md) |
| Speaker | Output | beeps when it is too hot | [Sound](../microbit/sound.md) |

!!! tip "Built-in or PiicoDev?"
    The micro:bit has its own [temperature sensor](../microbit/temperature.md), so why use the Atmospheric Sensor? The built-in sensor is inside the processor, which warms up as it runs. That means it reads a few degrees above the room temperature. The Atmospheric Sensor measures the air, so it gives us a more accurate reading.

### 2. Wire them up

1. Unplug the micro:bit.
2. Plug it into the adapter.
3. Chain the modules: adapter → Atmospheric Sensor → 3x RGB LED.
4. Check that both modules' ASW switches are off.
5. Plug the micro:bit back in.

Our program folder, `too_hot`, needs four files: `main.py`, `PiicoDev_Unified.py`, `PiicoDev_BME280.py` and `PiicoDev_RGB.py`.

Then we test each part:

| Component | Example to run | Expected result |
| --- | --- | --- |
| Atmospheric Sensor | `atmospheric/values` | the Shell shows the temperature, pressure and humidity every second |
| 3x RGB LED | `rgb_led/fill` | all three LEDs turn purple |
| Display | `micropython/first_program` | the display scrolls "Hello world!" and shows a heart |

### 3. Create the program

#### Step 1: Plan

Before we write any code, we list the inputs, processing and outputs:

| Step | What happens |
| --- | --- |
| Input | read the temperature from the Atmospheric Sensor |
| Process | check if the temperature is above the limit |
| Output | green lights and a happy face if it isn't; red lights, a sad face and a beep if it is |

#### Step 2: Imports

The display is in the `microbit` library, and the beep needs the `music` module. Each PiicoDev module needs its driver.

```python
from microbit import *
from PiicoDev_BME280 import PiicoDev_BME280
from PiicoDev_RGB import PiicoDev_RGB
import music
```

#### Step 3: Setup

We only need to create the sensor and the LEDs once, so they go in setup. The temperature limit also only needs to be set once. Storing it in a variable means we only need to change one line to adjust the alarm.

```python
# Setup
sensor = PiicoDev_BME280()
leds = PiicoDev_RGB()
limit = 25
```

#### Step 4: Main loop

Now we add the loop, then fill in the input, process and output steps from our plan.

```python
# Main loop
while True:
    # Input
    temp, pressure, humidity = sensor.values()

    # Process
    too_hot = temp > limit

    # Output
    if too_hot:
        leds.fill([255, 0, 0])
        display.show(Image.SAD)
        music.pitch(880, 200)
    else:
        leds.fill([0, 255, 0])
        display.show(Image.HAPPY)
    sleep(1000)
```

#### The complete program

This is also in the `micropython/too_hot` folder of your tutorial files, with its driver files.

```python linenums="1"
--8<-- "examples/micropython/too_hot/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → imports all the commands from the `microbit` library.
    - **line 2** → imports the Atmospheric Sensor driver.
    - **line 3** → imports the 3x RGB LED driver.
    - **line 4** → imports the `music` module.
    - **line 7** → creates the Atmospheric Sensor and stores it in `sensor`.
    - **line 8** → creates the 3x RGB LED and stores it in `leds`.
    - **line 9** → stores the temperature limit, `25` °C, in `limit`.
    - **line 12** → starts an endless loop.
    - **line 14** → **input**: reads the temperature, pressure and humidity, and stores each one in its own variable.
    - **line 17** → **process**: checks if `temp` is greater than `limit`, and stores `True` or `False` in `too_hot`.
    - **line 20** → **output**: if `too_hot` is `True`…
    - **line 21** → …turns all three LEDs red…
    - **line 22** → …shows a sad face…
    - **line 23** → …and beeps.
    - **line 24** → otherwise…
    - **line 25** → …turns all three LEDs green…
    - **line 26** → …and shows a happy face.
    - **line 27** → waits 1 second before checking again.

#### Step 5: Test

1. **Run** the program. You should see green lights and a happy face.
2. Hold the Atmospheric Sensor between two fingers, or breathe on it, to warm it up.
3. If the temperature doesn't go over the limit, change `limit` on line 9 to a number a little lower than the current temperature and run it again.
4. When the temperature passes the limit, you should see red lights and a sad face, and hear a beep.
5. Let the sensor cool down. The lights should go back to green and the face back to happy.

When the program works, [upload](../micropython/piicodev.md#upload-the-files) `main.py` so the alarm runs without the computer.
