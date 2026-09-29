# Exercise 3
# What happens if you remove the while True: line (and the indenting under
# it)? Why?

from microbit import *

# Main loop
while True:
    display.scroll("Hello world!")
    display.show(Image.HEART)
    sleep(1000)
