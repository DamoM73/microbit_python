from microbit import *
from PiicoDev_Switch import PiicoDev_Switch

# Setup
button = PiicoDev_Switch()

# Main loop
while True:
    print(button.press_count)
    sleep(2000)
