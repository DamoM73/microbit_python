from microbit import *

# Main loop
while True:
    if pin_logo.is_touched():
        display.show(Image.HAPPY)
    else:
        display.show(Image.SAD)
