from microbit import *

# Main loop
while True:
    if button_a.was_pressed():
        if accelerometer.was_gesture("3g"):
            display.show(Image.YES)
        else:
            display.show(Image.NO)
