# PiicoDev Servo Driver

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/7D_5JzoxYyo?si=QpRX2pQ_Y5oYp4yh" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Nothing makes a project more exciting like motion, and now it's easier than ever with the PiicoDev® Servo Driver. You can control up to four RC Servos independently to create angular or continuous rotational motion. Use it to open and close a gate, beat a drum or pluck a string, or even equip your robot army with grabby claws!

The PiicoDev Servo Driver features a dedicated PWM chip that takes care of generating the servo signals, all you need to do is tell it what angle or speed you want to set your servo. There are the regular daisy-chainable PiicoDev connectors so you can add this module to your project without soldering - and additional USB-C connectors to provide separate, high-current power to your servos. Better still, the Servo Driver has four addressing options set by the Address Switch (ASW) - you can daisy chain up to four Drivers together for a maximum of 16 servos! That ought to be enough for most projects.

## Getting set up

### Connect the PiicoDev module to your Micro:bit

Plug your Micro:bit into the PiicoDev adapter (buttons LED matrix facing up), connect your module to the adapter via the PiicoDev cable and connect your Micro:bit to your computer with a USB lead.

Now for the motors. Take a **continuous servo** and put a horn on the hub, then plug it into **channel 1** (the most left channel), with the orange wire lining up with the **sig** (so it is on the bottom).

Then take a micro servo and put a horn on the hub. Plug it into **channel 4** (the most right channel).

Final add power. Take the power cable, plug it into the power-point and then USB C connector. Turn the power on

Make sure that the ASW switch is in the off position (see below)

### Download the PiicoDev Modules

Create a new folder for this example. Then download the following files and save them to your new folder (Right Click > "Save Link As").

- **[`PiicoDev_Servo.py`](https://raw.githubusercontent.com/CoreElectronics/CE-PiicoDev-Servo-Driver-MicroPython-Module/main/PiicoDev_Servo.py)** - The device driver.
- **[`PiicoDev_Unified.py`](https://raw.githubusercontent.com/CoreElectronics/CE-PiicoDev-Unified/main/min/PiicoDev_Unified.py)** - The PiicoDev Unified Libraries: Drives I2C communications for PiicoDev modules


## Examples

The PiicoDev OLED Module screen has 128 pixels x 64 pixels, with the `(0,0)` coordinate in the top lefthand corner.

### Continuous Servo

**Create** a `main.py` file in the folder and add the code below.

**[Upload](./12_piicodev_intro.md#upload)** `main.py` along with `PiicoDev_Unified.py`, `PiicoDev_SSD1306.py`, `font-pet-me-128.dat` and `piicodev-logo.pbm` to the micro:bit and then **run** it.

```{literalinclude} ./python_files/piico_servo_cont/main.py
:linenos:
```

### Micro Servo

Change the code in `main.py` to the code below. 

**[Upload](./12_piicodev_intro.md#upload)** `main.py` along with `PiicoDev_Unified.py`, `PiicoDev_SSD1306.py`, `font-pet-me-128.dat` and `piicodev-logo.pbm` to the micro:bit and then **run** it.

```{literalinclude} ./python_files/piico_servo_micro/main.py
:linenos:
```
