# Read the PiicoDev Potentiometer value
from PiicoDev_Potentiometer import PiicoDev_Potentiometer
from PiicoDev_Unified import sleep_ms
 
pot = PiicoDev_Potentiometer() # Initialise the potentiometer

while True:
    print(pot.value) # read the pot and print the result
    sleep_ms(100)