# button.was_pressed exercise 1

from microbit import *

counter = 0

while True:
    display.scroll(str(counter))
    if button_a.was_pressed():
        counter += 1
        display.clear()
    
    if button_b.was_pressed():
        counter = 0
        display.clear()
    
    sleep(100)
