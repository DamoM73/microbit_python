from microbit import *
from PiicoDev_RV3028 import PiicoDev_RV3028

# Setup
rtc = PiicoDev_RV3028()

# Main loop
while True:
    print(rtc.getUnixTime())
    sleep(1000)
