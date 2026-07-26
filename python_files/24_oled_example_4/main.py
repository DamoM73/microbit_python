from microbit import *
from PiicoDev_SSD1306 import *

# --- SETUP
# start sensors
oled = create_PiicoDev_SSD1306()
graph = oled.graph2D(minValue=0,maxValue=63)

# store variables
number = 0
change = 1

# --- RUNNING
while True:
    # read sensor data
    
    # process data
    
    # output data
    oled.fill(0)
    oled.updateGraph2D(graph, number)
    
    number = number + change
    
    if number == 0 or number == 63:
        change = change * -1
    
    oled.show()
