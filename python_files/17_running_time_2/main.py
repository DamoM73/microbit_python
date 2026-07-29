# countdown timer
from microbit import *
import music


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
        running = True                          
        start = running_time()
    if running:
        lapsed_time = running_time() - start
        if timer - lapsed_time < 0:
            music.pitch(500,250, wait=False)
            running = False
    
    # output data
    