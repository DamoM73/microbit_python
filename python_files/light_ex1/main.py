# light exercise 1

from microbit import *

prev_level = display.read_light_level()

while True:
    current_level = display.read_light_level()
    
    if current_level > prev_level:
        display.show(Image.ARROW_N)
        prev_level = current_level
    elif current_level < prev_level:
        display.show(Image.ARROW_S)
        prev_level = current_level
    else:
        display.show("-")
    sleep(2000)
    display.clear()