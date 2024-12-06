from microbit import *

# --- SETUP
# start sensors

# store variables

# --- RUNNING
while True:
    display.show(Image.YES)
    sleep(3000)
    # read sensor data
    presses = button_a.get_presses()
    
    # process data
    
    # output data
    display.show(presses, delay=1000)
    display.clear()
    sleep(1000)
    