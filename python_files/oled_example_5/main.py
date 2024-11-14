from microbit import *
from PiicoDev_SSD1306 import *

# --- SETUP
# start sensors
oled = create_PiicoDev_SSD1306()

# store variables
x = 10
y = 10

x_speed = 1
y_speed = 1

rect_width = 2
rect_height = 2
rect_colour = 1

# --- RUNNING
while True:
    # read sensor data
    
    # process data
    
    # output data
    oled.fill(0)
    
    # Upsdate coordinate values
    if x == 0 or x + 2 == 127:
        x_speed = x_speed * -1
    if y == 0 or y + 2 == 63:
        y_speed = y_speed * -1
    
    x += x_speed
    y += y_speed
    
    ### Draw a square    
    oled.rect(x,y,rect_width,rect_height,rect_colour)
    
    ### Update display ###
    oled.show()
