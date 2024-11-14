from microbit import *
from PiicoDev_SSD1306 import *

# --- SETUP
# start sensors
oled = create_PiicoDev_SSD1306()

# store variables
image = "piicodev-logo.pbm"
image_colour = 1

# --- RUNNING
while True:
    # read sensor data
    
    # process data
    
    # output data
    oled.load_pbm(image, image_colour)
    oled.show()
    sleep(2000)
    
    oled.fill(0)
    oled.show()
    
    
