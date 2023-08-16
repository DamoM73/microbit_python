# radio example

from microbit import *
import radio

while True:
    # transmitting
    if button_a.was_pressed():
        radio.send("happy")
    if button_b.was_pressed():
        radio.send("sad")
    
    # receiving
    incoming = radio.receive()
    if incoming == "happy":
        display.show(Image.HAPPY)
    elif incoming == "sad":
        display.show(Image.SAD)