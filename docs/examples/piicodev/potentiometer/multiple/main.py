from microbit import *
from PiicoDev_Potentiometer import PiicoDev_Potentiometer

# Setup
knob = PiicoDev_Potentiometer(id=[0, 0, 0, 0])
slider = PiicoDev_Potentiometer(id=[1, 0, 0, 0])

# Main loop
while True:
    print(knob.value, slider.value)
    sleep(100)
