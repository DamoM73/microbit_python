from microbit import *
import music

# Setup
def beep():
    music.pitch(880, 100)

run_every(beep, s=1)

# Main loop
while True:
    display.scroll("Hello")
