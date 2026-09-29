# Exercise 7
# The starter code lights each pixel in turn, down each column. What happens
# if you remove sleep(50)? Why do you think this happens?

from microbit import *

# Setup
display.clear()

# Main loop
while True:
    for x in range(5):
        for y in range(5):
            display.set_pixel(x, y, 9)
            sleep(50)
            display.clear()
