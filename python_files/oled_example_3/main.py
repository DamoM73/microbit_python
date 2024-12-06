from microbit import *
from PiicoDev_SSD1306 import *

# --- SETUP
# start sensors
oled = create_PiicoDev_SSD1306()

# store variables
myString = "this is me"
myNumber = 123.4567

# --- RUNNING
while True:
    # read sensor data
    
    # process data
    
    # output data
    # display literal string
    oled.text("Hello, World!", 0,0, 1)
    
    # display string variable
    oled.text(myString, 0,15, 1)
    
    # display litereal number
    oled.text(str(100), 0, 30)
    
    # display number variable
    oled.text(str(myNumber), 0, 45)
    
    oled.show()
    sleep(3000)
    
    # clear screen
    oled.fill(0)
    oled.show()
    

