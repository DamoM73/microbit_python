from microbit import *
import music
from PiicoDev_Potentiometer import PiicoDev_Potentiometer

# --- SETUP

# start sensors
duration_pot = PiicoDev_Potentiometer(minimum=0, maximum=1000, id=[1,0,0,0])
frequency_pot = PiicoDev_Potentiometer(minimum=100, maximum=15000 ,id=[0,0,0,0])

# store variables

# --- RUNNING
while True:
    # read sensor data
    duration = duration_pot.value
    frequency = frequency_pot.value
    
    # process data
    duration = int(duration)
    frequency = int(frequency)
    
    # output data
    print(duration, frequency)
    music.pitch(frequency,duration)
    
    
    