from microbit import *
import music

# Setup
limit = 25

# Main loop
while True:
    # Input
    temp = temperature()

    # Process
    too_hot = temp > limit

    # Output
    if too_hot:
        display.show(Image.SAD)
        music.pitch(880, 200)
    else:
        display.show(Image.HAPPY)
    sleep(1000)
