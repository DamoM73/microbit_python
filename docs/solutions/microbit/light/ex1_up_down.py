from microbit import *

# Setup
last_light = display.read_light_level()

# Main loop
while True:
    sleep(2000)
    light = display.read_light_level()
    if light > last_light:
        display.show(Image.ARROW_N)
    elif light < last_light:
        display.show(Image.ARROW_S)
    last_light = light
