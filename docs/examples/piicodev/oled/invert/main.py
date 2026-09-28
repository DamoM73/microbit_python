from microbit import *
from PiicoDev_SSD1306 import *

# Setup
oled = create_PiicoDev_SSD1306()
oled.text("Invert", 0, 0, 1)
oled.show()

# Main loop
while True:
    oled.invert(1)
