# Exercise 3
# Can you change the get_field_strength() example to show the reading in
# microtesla with no decimal places? (1 microtesla = 1000 nanotesla)

from microbit import *

# Main loop
while True:
    field = compass.get_field_strength()
    display.scroll(field)
    sleep(500)
