# radio exercise 1

from microbit import *
import radio

while True:
    message = radio.receive()
    if message:
        display.show(Image.DUCK)
    if accelerometer.was_gesture('shake'):
        display.clear()
        radio.send('duck')