from microbit import *

# Main loop
while True:
    light = display.read_light_level()
    display.scroll(light)
    sleep(500)
