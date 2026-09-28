from microbit import *
from PiicoDev_SSD1306 import *

# Setup
oled = create_PiicoDev_SSD1306()

# Main loop
while True:
    oled.arc(64, 32, 25, 0, 180, 0.3, 1)
    oled.show()
