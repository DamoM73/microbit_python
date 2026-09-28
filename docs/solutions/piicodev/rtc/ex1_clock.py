from microbit import *
from PiicoDev_RV3028 import PiicoDev_RV3028

# Setup
rtc = PiicoDev_RV3028()

# Main loop
while True:
    if button_a.was_pressed():
        rtc.getDateTime()
        display.scroll("{:02}:{:02}".format(rtc.hour, rtc.minute))
    if button_b.was_pressed():
        rtc.getDateTime()
        display.scroll("{}/{}/{}".format(rtc.day, rtc.month, rtc.year))
