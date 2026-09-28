from microbit import *

# Main loop
while True:
    heading = compass.heading()
    if heading > 337 or heading < 23:
        display.show("N")
    else:
        display.clear()
    sleep(100)
