from microbit import *

# Main loop
while True:
    x = accelerometer.get_x()
    if x > 100:
        display.show("L")
    elif x < -100:
        display.show("R")
    else:
        display.show("-")
    sleep(100)
