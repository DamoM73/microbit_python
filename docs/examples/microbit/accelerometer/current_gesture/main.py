from microbit import *

# Main loop
while True:
    gesture = accelerometer.current_gesture()
    print(gesture)
    sleep(500)
