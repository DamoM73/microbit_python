from microbit import *
import music

def beep():                             # the function that will be called
    music.pitch(880,250)

# --- SETUP
# start components

# store vairables

# --- RUNNING
run_every(beep, s=1)                    # sets beep to be called every second

# this is the main program that will 
# run independent of the beeping
while True:
    for number in range(1000):
        print(number)
