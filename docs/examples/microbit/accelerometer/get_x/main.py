from microbit import *

# Main loop
while True:
    x = accelerometer.get_x()
    print(x)
    sleep(100)
