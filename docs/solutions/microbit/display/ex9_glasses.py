from microbit import *

# Setup
glasses = Image("05050:"
                "99999:"
                "05050:"
                "90009:"
                "09990")

# Main loop
while True:
    display.show(glasses)
    sleep(1000)
