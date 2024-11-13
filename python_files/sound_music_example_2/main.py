from microbit import *
import music

# --- SETUP
# start sensors

# store variables
tune = ["C4:4", "D4:4", "E4:4", "C4:4",
        "C4:4", "D4:4", "E4:4", "C4:4",
        "E4:4", "F4:4", "G4:8",
        "E4:4", "F4:4", "G4:8"]

# --- RUNNING
while True:
    # read sensor data
    
    # process data
    
    # output data
    music.play(tune)
    
    sleep(500)
    