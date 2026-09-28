from microbit import *

# Main loop
while True:
    if button_a.was_pressed():
        display.show(Image.HAPPY)
    else:
        display.show(Image.SAD)
    sleep(2000)
