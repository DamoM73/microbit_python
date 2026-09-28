from microbit import *
from PiicoDev_SSD1306 import *

# Setup
oled = create_PiicoDev_SSD1306()
graph = oled.graph2D(minValue=0, maxValue=255)

# Main loop
while True:
    oled.fill(0)
    oled.updateGraph2D(graph, display.read_light_level())
    oled.show()
