from microbit import *

# Setup
display.set_pixel(2, 2, 5)

# Main loop
while True:
    print(display.get_pixel(2, 2))
    sleep(1000)
