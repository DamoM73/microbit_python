from microbit import *

# Main loop
while True:
    z = accelerometer.get_z()
    print(z)
    sleep(100)
