from microbit import *
from PiicoDev_SSD1306 import *

# --- SETUP
# start sensors
oled = create_PiicoDev_SSD1306()

# store variables
unfilled_x = 10
unfilled_y = 10
unfilled_width = 20
unfilled_height = 50
unfilled_colour = 1

white_filled_x = 50
white_filled_y = 10
white_filled_width = 50
white_filled_height = 40
white_filled_colour = 1

black_filled_x = 60
black_filled_y = 20
black_filled_width = 30
black_filled_height = 20
black_filled_colour = 0

# --- RUNNING
while True:
    # read sensor data
    
    # process data
    
    # output data
    # unfilled rectangle
    oled.rect(unfilled_x, unfilled_y, unfilled_width, unfilled_height, unfilled_colour)
    
    # filled rectangle (white)
    oled.fill_rect(white_filled_x, white_filled_y, white_filled_width, white_filled_height, white_filled_colour)
    
    # filled rectangle (black)
    oled.fill_rect(black_filled_x, black_filled_y, black_filled_width, black_filled_height, black_filled_colour) 
    
    oled.show()
    sleep(3000)
    
    # clear screen
    oled.fill(0)
    oled.show()
    

