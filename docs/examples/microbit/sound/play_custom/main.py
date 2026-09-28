from microbit import *
import music

# Setup
tune = ["C4:4", "D4:4", "E4:4", "C4:4",
        "C4:4", "D4:4", "E4:4", "C4:4",
        "E4:4", "F4:4", "G4:8",
        "E4:4", "F4:4", "G4:8"]

# Main loop
while True:
    music.play(tune)
    sleep(500)
