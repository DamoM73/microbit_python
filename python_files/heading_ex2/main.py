# heading exercise 2

from microbit import *
compass.calibrate()

while True:
    if button_a.was_pressed():
        print(bearing)
        if bearing < 22.5 or bearing > 337.5:
            display.show('N')
        elif 22.5 < bearing < 67.5:
            display.scroll('NE')
        elif 67.5 <= bearing < 112.5:
            display.show('E')
        elif 112.5 <= bearing < 157.2:
            display.scroll('SE')
        elif 157.5 <= bearing < 202.5:
            display.show('S')
        elif 202.5 <= bearing < 247.5:
            display.scroll('SW')
        elif 247.5 <= bearing < 292.5:
            display.show('W')
        elif 292.5 <= bearing < 337.5:
            display.scroll('NW')    
