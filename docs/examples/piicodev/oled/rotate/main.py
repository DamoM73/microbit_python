from microbit import *
from PiicoDev_SSD1306 import *

# Setup
oled = create_PiicoDev_SSD1306()
oled.text("Rotate", 0, 0, 1)

# Main loop
while True:
    oled.rotate(0)
    oled.show()
