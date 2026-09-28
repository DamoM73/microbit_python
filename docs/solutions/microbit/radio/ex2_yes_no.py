from microbit import *
import radio

# Setup
radio.config(group=23)
radio.on()

# Main loop
while True:
    if button_a.was_pressed():
        radio.send("yes")
    if button_b.was_pressed():
        radio.send("no")
    answer = radio.receive()
    if answer == "yes":
        display.show(Image.YES)
        sleep(500)
        display.clear()
    elif answer == "no":
        display.show(Image.NO)
        sleep(500)
        display.clear()
