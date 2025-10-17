# countdown timer
from microbit import *
import music

'''
To create a countdown timer, we will use a built-in function called running_time().
running_time() keeps a running count of the number of the time since
the micro:bit started in milliseconds.
'''

# --- SETUP
# start components

# store variables
running = False
timer = 5000

# --- RUNNING
while True:
    # read sensor data
    a_pressed = button_a.was_pressed()
    
    # process data
    if a_pressed:    
        running = True                          # start the countdown timer
        start = running_time()                  # records the starting time
    if running:
        lapsed_time = running_time() - start    # calculates how long since button press
        if timer - lapsed_time < 0:             # checks if countdown has reached 0
            music.pitch(500,250, wait=False)
            running = False                     # stops the timer
    
    # output data
    