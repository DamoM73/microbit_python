from microbit import *

# --- SETUP
# start components

# store vairables

# --- RUNNING
while True:
    # read sensor data
    a_pressed = button_a.is_pressed()
    b_pressed = button_b.is_pressed()
    
    # process data
    
    # output data
    if a_pressed:
        display.show(Image.HAPPY)
    elif b_pressed:
        break
    else:
        display.show(Image.SAD)

display.clear()