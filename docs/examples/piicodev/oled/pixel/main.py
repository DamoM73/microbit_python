from microbit import *
from PiicoDev_SSD1306 import *

# Setup
oled = create_PiicoDev_SSD1306()

# Main loop
while True:
    oled.pixel(64, 32, 1)
    oled.show()
