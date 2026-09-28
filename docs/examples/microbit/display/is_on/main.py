from microbit import *

# Setup
display.show(Image.HAPPY)

# Main loop
while True:
    display.off()
    print(display.is_on())
    sleep(1000)
    display.on()
    print(display.is_on())
    sleep(1000)
