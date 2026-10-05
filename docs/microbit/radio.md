# Radio

!!! learn "On this page we will learn"
    - how the micro:bit radio works
    - how to turn the radio on and choose a group
    - how to send and receive messages between micro:bits

!!! terms "Terminology"
    - **radio** – a way of sending and receiving messages without wires, using invisible radio waves.
    - **wireless** – communicating between devices without any cables or wires.
    - **group** – a number from 0 to 255 that sets which micro:bits can hear each other's radio messages.
    - **queue** – a line of waiting items where the oldest one is dealt with first, like received radio messages.
    - **None** – a special Python value meaning nothing, such as when no radio message has arrived.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/rvymAr6WqrQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

The radio sends and receives short wireless messages between micro:bits.

Possible uses:

- multiplayer games
- voting systems
- remote controls
- wireless sensors

## Connect it

The radio is built into the micro:bit, so we don't need to connect anything. We need **at least two micro:bits**.

- Each example is a `main.py` file. See [Your First Program](../micropython/first-program.md) for how to create, upload and run it. Upload the program to each micro:bit.
- Micro:bits only hear messages from micro:bits in the same **group** (`0`–`255`). Pick a group that other students aren't using.
- Received messages wait in a **queue**, like people in a line: the oldest message is read first. If the queue is full, new messages are lost.

!!! tip "How radio works"
    Imagine you and a friend on opposite sides of the classroom, each with a torch. By flashing the torch in an agreed code you can send "HELLO" without any wires. Radio works the same way, but uses invisible radio waves instead of light.

## Set it up

The radio has its own module. We import it after the `microbit` library:

```python linenums="1"
from microbit import *
import radio
```

## Methods

| Method | Parameters | Returns | Description |
| --- | --- | --- | --- |
| `radio.on()` | none | none | Turns the radio on. It is off by default to save power. |
| `radio.config(group=0)` | `group`: 0–255 | none | Sets the group. Only micro:bits in the same group hear each other. |
| `radio.send(message)` | `message`: string | none | Sends a message to every micro:bit in the group |
| `radio.receive()` | none | string or `None` | The oldest message in the queue, or `None` if there are none |

### `radio.on()`

Turns the radio on. It is off by default to save power, so every radio program needs this.

```python linenums="1"
--8<-- "examples/microbit/radio/on/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → imports all the commands from the `microbit` library.
    - **line 2** → imports the `radio` module.
    - **line 5** → turns the radio on.
    - **line 8** → starts an endless loop.
    - **line 9** → shows a tick to show the radio is ready.

### `radio.config()`

Changes the radio settings. The most useful setting is `group`, which chooses which micro:bits can hear each other.

```python linenums="1"
--8<-- "examples/microbit/radio/config/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → imports all the commands from the `microbit` library.
    - **line 2** → imports the `radio` module.
    - **line 5** → sets the radio group to `7`.
    - **line 6** → turns the radio on.
    - **line 9** → starts an endless loop.
    - **line 10** → shows the group number.

### `radio.send()`

Sends a message to every micro:bit in the same group.

```python linenums="1"
--8<-- "examples/microbit/radio/send/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → imports all the commands from the `microbit` library.
    - **line 2** → imports the `radio` module.
    - **line 5** → sets the radio group to `7`.
    - **line 6** → turns the radio on.
    - **line 9** → starts an endless loop.
    - **line 10** → checks if button **A** was pressed.
    - **line 11** → if it was, sends the message `"happy"` to group 7.

### `radio.receive()`

Returns the oldest message waiting in the queue, or `None` if no messages have arrived.

Run this on a second micro:bit while the first runs the `send()` example.

```python linenums="1"
--8<-- "examples/microbit/radio/receive/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → imports all the commands from the `microbit` library.
    - **line 2** → imports the `radio` module.
    - **line 5** → sets the radio group to `7`.
    - **line 6** → turns the radio on.
    - **line 9** → starts an endless loop.
    - **line 10** → gets the oldest message in the queue (or `None`) and stores it in `message`.
    - **line 11** → checks if the message is `"happy"`.
    - **line 12** → if it is, shows a happy face.

## Documentation

Documentation is the official guide written by the people who made the code library, and we can use it to look up every method and its parameters, including ones that aren't covered on this page.

- [BBC micro:bit MicroPython — radio](https://microbit-micropython.readthedocs.io/en/v2-docs/radio.html)

## Exercises

!!! primm "PRIMM"
    Time to **modify** the code and see what happens.

Starter files are in the `radio` folder of your tutorial files. Solutions are on the [Exercise Solutions](../reference/solutions.md#radio) page.

### Exercise 1

Starter: `radio/ex1_pass_image` (both micro:bits)

Can you move an image between two micro:bits? When the micro:bit showing the image is shaken, the image should disappear and appear on the other micro:bit.

### Exercise 2

Starter: `radio/ex2_yes_no` (both micro:bits)

Can you send a private yes or no answer? Your program should:

- press **A** to send yes, or **B** to send no
- show the answer on the other micro:bit for half a second
- use a group so nearby micro:bits don't receive your answer

### Exercise 3

Starters: `radio/ex3_outside` and `radio/ex3_inside`

Can you make a wireless thermometer? It should work like this:

- the **outside** micro:bit sends its temperature every 5 seconds
- the **inside** micro:bit shows its own temperature when button **A** is pressed, and the latest outside temperature when button **B** is pressed
