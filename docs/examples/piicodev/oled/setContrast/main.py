from microbit import *
from PiicoDev_SSD1306 import *

# Setup
oled = create_PiicoDev_SSD1306()
oled.fill(1)
oled.show()

# Main loop
while True:
    oled.setContrast(10)
