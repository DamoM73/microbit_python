from microbit import *
from PiicoDev_RV3028 import PiicoDev_RV3028

# Setup
rtc = PiicoDev_RV3028()
start = 0

# Main loop
while True:
    if button_a.was_pressed():
        start = rtc.getUnixTime()
        display.show(Image.YES)
    if button_b.was_pressed():
        seconds = rtc.getUnixTime() - start
        display.scroll(seconds)
