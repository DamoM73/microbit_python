from microbit import *
from PiicoDev_Potentiometer import PiicoDev_Potentiometer

# --- SETUP
# start sensors 
pot = PiicoDev_Potentiometer()

# store variables


# --- RUNNING
while True:
    # read sensor data
    reading = pot.value
    
    # process data
    reading = str(reading)
    
    # output data
    print(reading)
    sleep(100)