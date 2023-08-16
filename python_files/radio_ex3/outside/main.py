from microbit import *
import radio

while True:
    radio.send(str(temperature()))
    sleep(5000)