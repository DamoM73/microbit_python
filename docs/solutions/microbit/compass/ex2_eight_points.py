from microbit import *

# Setup
points = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]

# Main loop
while True:
    if button_a.was_pressed():
        heading = compass.heading()
        index = ((heading + 22) // 45) % 8
        display.scroll(points[index])
