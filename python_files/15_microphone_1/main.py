from microbit import *

# --- SETUP
# start sensors

# store variables

# --- RUNNING
while True:
    # read sensor data
    sound = microphone.current_event()
    
    # process data
    
    # output data
    if sound == SoundEvent.LOUD:
        display.show(Image.HEART)
        sleep(200)
    else:
        display.show(Image.HEART_SMALL)