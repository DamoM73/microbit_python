from microbit import *
from PiicoDev_Switch import PiicoDev_Switch

# --- SETUP
# start sensors 
button = PiicoDev_Switch()

# store variables


# --- RUNNING
while True:
    # read sensor data
    button_pressed = button.was_double_pressed
    
    # process data
    
    # output data
    if button_pressed:
        display.show(Image.HAPPY)
    else:
        display.show(Image.SAD)
    sleep(100)