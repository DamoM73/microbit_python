# Read the PiicoDev Potentiometer value
from PiicoDev_Potentiometer import PiicoDev_Potentiometer
from PiicoDev_Unified import sleep_ms
 
pot = PiicoDev_Potentiometer() # Initialise the potentiometer
pot.maximum = 42 # set the range of output values
pot.minimum = 16   # if minimum or maximum are ommitted, they will default to 0 and 100 respectively

while True:
    print(pot.value) # read the pot and print the result
    sleep_ms(100)