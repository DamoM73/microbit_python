from microbit import *

# Main loop
while True:
    display.scroll(display.read_light_level())
