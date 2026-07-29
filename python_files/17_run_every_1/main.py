from microbit import *
import music

def beep():
    music.pitch(880,250)

# --- SETUP
# start components

# store vairables

# --- RUNNING
run_every(beep, s=1)

# this is the main program that will 
# run independent of the beeping
while True:
    for number in range(1000):
        print(number)
