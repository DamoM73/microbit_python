from microbit import *

# Setup
display.set_pixel(2, 2, 5)

# Main loop
while True:
    brightness = display.get_pixel(2, 2)
    print(brightness)
    sleep(1000)
