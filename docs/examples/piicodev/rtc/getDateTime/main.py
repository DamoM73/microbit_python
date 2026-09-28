from microbit import *
from PiicoDev_RV3028 import PiicoDev_RV3028

# Setup
rtc = PiicoDev_RV3028()

# Main loop
while True:
    rtc.getDateTime()
    print(rtc.hour, rtc.minute)
    sleep(1000)
