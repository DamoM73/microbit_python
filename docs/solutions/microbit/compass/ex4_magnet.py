from microbit import *

# Main loop
while True:
    field = compass.get_field_strength()
    if field > 500000:
        display.show(Image.HAPPY)
    else:
        display.show(Image.ANGRY)
    sleep(100)
