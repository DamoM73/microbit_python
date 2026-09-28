from microbit import *

# Main loop
while True:
    sleep(3000)
    print(accelerometer.get_gestures())
