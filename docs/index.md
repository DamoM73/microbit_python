# Python meets micro:bit

Short, practical examples for programming the BBC micro:bit v2, PiicoDev modules and the Glowbit Rainbow in MicroPython using Thonny.

## How to use this site

1. Start with the **MicroPython** section to set up Thonny and learn how to create, upload and run a program.
2. Then go to the page for the component you want to use:
    - **micro:bit** → the display, buttons, sensors, sound and radio built into the micro:bit
    - **PiicoDev Inputs** → add-on sensors, dials, buttons and a real time clock
    - **PiicoDev Outputs** → add-on LEDs, screen and servo motors
    - **Other** → the Glowbit Rainbow
3. **Reference** has an overview of every component, a guide to Thonny's debugger, and the solutions to every exercise.

## How each page works

Every component page follows the same layout:

- **Connect it** → wiring, switches and the files you need
- **Set it up** → the code needed before using the component
- **Methods** → a table of every method, followed by a short example of each
- **Code explanation** → click to open a line-by-line explanation of each example
- **Exercises** → practice tasks, with solutions on the [Exercise Solutions](reference/solutions.md) page

## Callouts

Coloured boxes called **callouts** highlight different kinds of information. Each type of callout has its own colour and icon, so we can tell at a glance what it's for.

!!! learn "Learning intentions"
    This callout is at the top of every tutorial page. It lists what we will learn on that page.

!!! terms "Terminology"
    This callout comes straight after the learning intentions. It lists the new technical terms on the page, with a short definition of each. Every term is also on the [Glossary](reference/glossary.md) page.

!!! primm "PRIMM"
    This callout comes after each example program. It asks us to **predict** what the code will do, **run** it, and **investigate** how it works. Sometimes it asks us to **modify** the code.

!!! note "Code explanation"
    This callout comes after each PRIMM callout and gives a line-by-line explanation of the example program. On the tutorial pages it starts closed, so we can make our own prediction first. Click its title to open it.

!!! tip "Tip"
    This callout gives extra information, such as definitions, background facts, comparisons and hints.

!!! warning "Warning"
    This callout warns us about mistakes that are easy to make, or things that will stop our program or micro:bit working.

## Code blocks

Programs are shown in **code blocks** like this one:

```python linenums="1"
from microbit import *

display.scroll("Hello")
```

- The **line numbers** on the left match the line numbers used in the Code explanation.
- The **copy** button in the top-right corner of a code block copies the code, so we can paste it into Thonny.

## Tutorial files

Download all the examples and exercise starter files: [microbit_tutorials.zip](downloads/microbit_tutorials.zip). See [Setting up Thonny](micropython/thonny.md#tutorial-files) for how to use them.
