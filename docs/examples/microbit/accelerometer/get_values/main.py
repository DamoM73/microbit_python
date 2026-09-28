from microbit import *

# Main loop
while True:
    x, y, z = accelerometer.get_values()
    print(x, y, z)
    sleep(100)
