from microbit import *

# --- SETUP
# start components

# store vraiables

# --- RUNNING
while True:
    # read sensor data
    gesture = accelerometer.current_gesture()
    
    # process data
    
    # output data
    print(gesture)
    sleep(1000)