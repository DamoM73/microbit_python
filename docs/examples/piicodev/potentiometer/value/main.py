from microbit import *
from PiicoDev_Potentiometer import PiicoDev_Potentiometer

# Setup
pot = PiicoDev_Potentiometer()

# Main loop
while True:
    print(pot.value)
    sleep(100)
