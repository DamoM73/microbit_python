from microbit import *

# Main loop
while True:
    heading = compass.heading()
    display.scroll(heading)
    sleep(500)
