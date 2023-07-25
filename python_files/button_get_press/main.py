# button.get_press example

from microbit import *

sleep(5000)
display.scroll(str(button_a.get_presses()))