# Exercise 4
# Can you make the micro:bit show a happy face when a magnet is touching its
# right side, and an angry face otherwise?

from microbit import *

# Main loop
while True:
    field = compass.get_field_strength()
    display.scroll(field)
    sleep(500)
