from microbit import *
from PiicoDev_SSD1306 import *

# Setup
oled = create_PiicoDev_SSD1306()
oled.text("On and off", 0, 0, 1)
oled.show()

# Main loop
while True:
    oled.poweroff()
    sleep(1000)
    oled.poweron()
    sleep(1000)
