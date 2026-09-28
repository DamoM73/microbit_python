from microbit import *

# Main loop
while True:
    display.scroll(compass.heading())
