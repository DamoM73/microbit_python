from microbit import *

# Main loop
while True:
    if button_a.was_pressed():
        seconds = running_time() // 1000
        display.scroll(seconds)
