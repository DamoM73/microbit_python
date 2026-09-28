from microbit import *

# Main loop
while True:
    display.scroll("Hello world!")
    display.show(Image.HAPPY)
    sleep(1000)
    display.show(Image.DUCK)
    sleep(1000)
