from microbit import *
from PiicoDev_SSD1306 import *

# Setup
oled = create_PiicoDev_SSD1306()

# Main loop
while True:
    oled.fill_rect(10, 10, 40, 30, 1)
    oled.show()
