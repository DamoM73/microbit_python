# light example

from microbit import *

while True:
    if button_a.was_pressed():
        light_level = display.read_light_level()
        sleep(100)
        display.scroll(light_level)
    display.clear()
    sleep(500)
    display.set_pixel(2,2,9)
    sleep(500)