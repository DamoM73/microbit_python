# Exercise 2
# Can you make the micro:bit show which of the 8 compass directions in the
# image above it is pointing (N, NE, E, SE, S, SW, W, NW) when button A is
# pressed?

from microbit import *

# Main loop
while True:
    heading = compass.heading()
    display.scroll(heading)
    sleep(500)
