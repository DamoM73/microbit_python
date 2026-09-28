from microbit import *

# Main loop
while True:
    display.scroll(compass.get_field_strength())
