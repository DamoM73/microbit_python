from microbit import *

# --- SETUP
# start components

# store variables

# --- RUNNING
while True:
    display.show(3)
    sleep(1000)
    display.show(2)
    sleep(1000)
    display.show(1)
    sleep(1000)
    display.show(0)
    # read sensor data
    gestures = accelerometer.get_gestures()

    # process data
    
    # output data
    for gesture in gestures:
        print(gesture)
    display.show(Image.NO)
    sleep(5000)