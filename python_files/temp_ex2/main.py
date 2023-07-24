# temperature exercise 1

from microbit import *

while True:
    current_temp = temperature()
    
    if current_temp < 20:
        display.show(Image.ARROW_S)
    elif current_temp > 22:
        display.show(Image.ARROW_N)
    else:
        display.show(Image.HAPPY)
        
        