# Exercise 3
# Using the display.show() parameters in the methods table, can you show the
# same message repeatedly without the while True loop?

from microbit import *

# Main loop
while True:
    display.show(3.14159, delay=500)
    sleep(1000)
