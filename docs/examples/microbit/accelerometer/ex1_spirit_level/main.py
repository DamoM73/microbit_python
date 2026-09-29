# Exercise 1
# Can you make a spirit level that shows - if the micro:bit is level left to
# right, L if the left side is too high, or R if the right side is too high?

from microbit import *

# Main loop
while True:
    x = accelerometer.get_x()
    print(x)
    sleep(100)
