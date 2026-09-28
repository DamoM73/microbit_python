from microbit import *
from PiicoDev_Potentiometer import PiicoDev_Potentiometer

# Setup
pot = PiicoDev_Potentiometer()
pot.minimum = 0
pot.maximum = 9

# Main loop
while True:
    print(pot.value)
    sleep(100)
