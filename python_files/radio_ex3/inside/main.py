from microbit import *
import radio

outdoorTemp = '-'

while True:
    message = radio.receive()
    if message:
        outdoor_temp = message
    if button_a.was_pressed():
        display.scroll(str(temperature()))
    if button_b.was_pressed():
        display.scroll(outdoor_temp)