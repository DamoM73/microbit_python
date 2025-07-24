from microbit import *

# --- SETUP
# start components

# store variables

# --- RUNNING
while True:
    # read sensor data
    presses = button_a.get_presses()

    # process data
    
    # output data
    display.show(str(presses), delay=1000)
    sleep(1000)
    display.clear()
    
    