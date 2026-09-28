from microbit import *

# Main loop
while True:
    field = compass.get_field_strength()
    display.scroll(field)
    sleep(500)
