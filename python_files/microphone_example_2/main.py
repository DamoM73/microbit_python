from microbit import *

# --- SETUP
# start sensors

# store variables

# --- RUNNING
while True:
    # read sensor data
    sound = microphone.sound_level()
    
    # process data
    
    # output data
    display.scroll(sound)
    sleep(500)