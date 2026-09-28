from microbit import *

# Main loop
while True:
    presses = button_a.get_presses()
    display.show(presses)
    sleep(1000)
