# Creating Your Program

!!! learn "On this page we will learn"
    - the structure every program in this course uses: imports, setup and main loop
    - how to organise a program into input, process and output
    - how to plan, build and test a program step by step

!!! terms "Terminology"
    - **setup** – the part of a program that runs once when it starts, for creating devices and giving variables their starting values.
    - **main loop** – the part of a program, inside `while True:`, that repeats forever to read inputs, make decisions and control outputs.
    - **process** – the step where our program works out what to do with its inputs, using calculations and decisions.

Every example in this course uses the same structure. We will use it for our own programs too, because it keeps our code organised and makes problems easier to find and fix.

## The structure

A micro:bit program has three parts, always in this order:

| Part | Runs | What goes here |
| --- | --- | --- |
| Imports | once, first | the libraries and drivers your program uses |
| `# Setup` | once, before the loop | creating sensors and devices, and variables with starting values |
| `# Main loop` | over and over, forever | the code that reads inputs, makes decisions and controls outputs |

### Imports

Imports bring in code that someone else has already written, so we can use it in our program.

- Every program starts with `from microbit import *`. This gives you the display, buttons, sensors and `sleep()`.
- Add other modules your program needs, such as `import music`, `import radio` or a PiicoDev driver.

### `# Setup`

Code under `# Setup` runs **once**, when the program starts. We use it for things that only need to happen once:

- creating PiicoDev devices, for example `sensor = PiicoDev_VL53L1X()`
- setting up variables with their starting values, for example `score = 0`
- settings that don't change, for example `radio.config(group=7)`

If your program doesn't need any setup, you can leave this part empty.

### `# Main loop`

`while True:` starts a loop that repeats forever. A micro:bit program usually never finishes: it keeps checking its inputs and updating its outputs until it is turned off.

Everything **indented** under `while True:` is inside the loop.

## Input, process, output

Inside the main loop, we organise our code into three steps:

1. **Input** → read the information your program needs, such as a button, a sensor or a radio message.
2. **Process** → work out what to do with it, using calculations and decisions (`if` statements).
3. **Output** → show the result, using the display, sounds, LEDs or motors.

Short examples in this course often combine these steps. In our own programs, we use `# Input`, `# Process` and `# Output` comments to keep them separate.

We end the loop with a short `sleep()`, so the micro:bit isn't checking faster than it needs to.

## Template

!!! warning "New program, new folder"
    Every program needs its own folder with its own `main.py`. Before you start a new program, create a new folder for it. See [Create a new program](first-program.md#create-a-new-program) for how.

Copy this into a new `main.py` to start a program. It is also in the `micropython/template` folder of your tutorial files.

```python linenums="1"
--8<-- "examples/micropython/template/main.py"
```

## Worked example: Too Hot Alarm

Let's build a program that shows a happy face when the room is comfortable, and a sad face and a beep when it gets too hot.

### Step 1: Plan

Before we write any code, we list the inputs, processing and outputs:

| Step | What happens |
| --- | --- |
| Input | read the temperature |
| Process | check if the temperature is above the limit |
| Output | happy face if it isn't; sad face and a beep if it is |

### Step 2: Imports

The temperature sensor and display are in the `microbit` library. The beep needs the `music` module.

```python
from microbit import *
import music
```

### Step 3: Setup

The temperature limit only needs to be set once, so it goes in setup. Storing it in a variable means we only need to change one line to adjust the alarm.

```python
# Setup
limit = 25
```

### Step 4: Main loop

Now we add the loop, then fill in the input, process and output steps from our plan.

```python
# Main loop
while True:
    # Input
    temp = temperature()

    # Process
    too_hot = temp > limit

    # Output
    if too_hot:
        display.show(Image.SAD)
        music.pitch(880, 200)
    else:
        display.show(Image.HAPPY)
    sleep(1000)
```

### The complete program

```python linenums="1"
--8<-- "examples/micropython/too_hot/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → imports all the commands from the `microbit` library.
    - **line 2** → imports the `music` module.
    - **line 5** → stores the temperature limit, `25` °C, in `limit`.
    - **line 8** → starts an endless loop.
    - **line 10** → **input**: reads the temperature and stores it in `temp`.
    - **line 13** → **process**: checks if `temp` is greater than `limit`, and stores `True` or `False` in `too_hot`.
    - **line 16** → **output**: if `too_hot` is `True`…
    - **line 17** → …shows a sad face.
    - **line 18** → …and beeps.
    - **line 19** → otherwise…
    - **line 20** → …shows a happy face.
    - **line 21** → waits 1 second before checking again.

### Step 5: Test

1. **Run** the program. You should see a happy face.
2. Hold the micro:bit's processor (the back, near the top) or breathe on it to warm it up.
3. If the temperature doesn't go over the limit, change `limit` on line 5 to a number a little lower than the current temperature and run it again.
4. When the temperature passes the limit, you should see a sad face and hear a beep.
