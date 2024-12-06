from microbit import *

# --- SETUP
# start sensors

# store variables

# --- RUNNING
display.clear()

while True:
    # read sensor data
    a_pressed = button_a.was_pressed()
    b_pressed = button_b.was_pressed()
    
    # process data
    
    # output data
    if a_pressed:
        display.show(Image.HAPPY)
    elif b_pressed:
        display.show(Image.SAD)