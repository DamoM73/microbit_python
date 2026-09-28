from microbit import *
from PiicoDev_SSD1306 import *

# Setup
oled = create_PiicoDev_SSD1306()

# Main loop
while True:
    oled.vline(10, 10, 40, 1)
    oled.show()
