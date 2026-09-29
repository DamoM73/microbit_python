from microbit import *
from PiicoDev_RV3028 import PiicoDev_RV3028

# Setup
rtc = PiicoDev_RV3028()

# Main loop
while True:
    if button_a.was_pressed():
        rtc.getDateTime()
        if rtc.hour < 12:
            display.scroll("Good morning")
        elif rtc.hour < 18:
            display.scroll("Good afternoon")
        else:
            display.scroll("Good evening")
