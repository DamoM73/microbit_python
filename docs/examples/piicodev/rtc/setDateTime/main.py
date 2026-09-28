from microbit import *
from PiicoDev_RV3028 import PiicoDev_RV3028

# Setup
rtc = PiicoDev_RV3028()
rtc.year = 2026
rtc.month = 9
rtc.day = 28
rtc.hour = 14
rtc.minute = 30
rtc.second = 0
rtc.ampm = "24"
rtc.setDateTime()
