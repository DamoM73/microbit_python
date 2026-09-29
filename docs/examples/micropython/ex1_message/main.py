# Exercise 1
# Can you make it show a different message?

from microbit import *

# Main loop
while True:
    display.scroll("Hello world!")
    display.show(Image.HEART)
    sleep(1000)
