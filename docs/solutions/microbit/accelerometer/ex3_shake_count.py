from microbit import *

# Main loop
while True:
    display.show(Image.YES)
    accelerometer.get_gestures()
    sleep(5000)
    gestures = accelerometer.get_gestures()
    shakes = gestures.count("shake")
    display.scroll(shakes)
    sleep(1000)
