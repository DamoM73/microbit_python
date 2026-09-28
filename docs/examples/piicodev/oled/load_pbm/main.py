from microbit import *
from PiicoDev_SSD1306 import *

# Setup
oled = create_PiicoDev_SSD1306()

# Main loop
while True:
    oled.load_pbm("piicodev-logo.pbm", 1)
    oled.show()
