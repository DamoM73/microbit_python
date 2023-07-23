# current gestures

from microbit import *

while True:
    gesture = accelerometer.current_gesture()
    display.scroll(gesture)
    sleep(1000)