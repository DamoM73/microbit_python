# Exercise 1
# Can you make the micro:bit show N when it is pointing North?

from microbit import *

# Main loop
while True:
    heading = compass.heading()
    display.scroll(heading)
    sleep(500)
