from microbit import *

# Main loop
while True:
    display.show(Image.YES)
    sleep(3000)
    gestures = accelerometer.get_gestures()
    print(gestures)
    display.show(Image.NO)
    sleep(2000)
