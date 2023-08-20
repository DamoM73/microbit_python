# animation example

from PiicoDev_SSD1306 import *
from PiicoDev_Unified import sleep_ms # cross-platform compatible sleep function

display = create_PiicoDev_SSD1306()

x = 10
y = 10

x_speed = 1
y_speed = 1

while True:
    ### Clear the display ###
    display.fill(0) # <- what happens if you comment this out?
    
    # Upsdate coordinate values
    if x == 0 or x + 2 == 127:
        x_speed *= -1
    if y == 0 or y + 2 == 63:
        y_speed *= -1
    
    x += x_speed
    y += y_speed
    
    ### Draw a square    
    display.rect(x,y,2,2,1)
    
    ### Update display ###
    display.show()
    