from microbit import *

# Setup
all_on = Image("99999:99999:99999:99999:99999")

# Main loop
while True:
    display.clear()
    sleep(10)
    light = display.read_light_level()
    if light < 100:
        display.show(all_on)
        sleep(1000)
