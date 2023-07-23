# gestures exercise 2

from microbit import *

sleep(5000)

gestures = accelerometer.get_gestures()

num_of_shakes = gestures.count("shake")

display.show(num_of_shakes)