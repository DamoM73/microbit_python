from microbit import *

# Main loop
while True:
    y = accelerometer.get_y()
    print(y)
    sleep(100)
