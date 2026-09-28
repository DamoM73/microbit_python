from microbit import *

# Main loop
while True:
    temp = temperature()
    display.scroll(str(temp) + "C")
    sleep(1000)
