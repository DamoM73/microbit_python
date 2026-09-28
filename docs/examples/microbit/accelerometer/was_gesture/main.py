from microbit import *

# Main loop
while True:
    sleep(3000)
    if accelerometer.was_gesture("shake"):
        display.show(Image.HAPPY)
    else:
        display.show(Image.SAD)
