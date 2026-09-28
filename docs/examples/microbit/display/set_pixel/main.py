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
