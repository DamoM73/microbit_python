from microbit import *

# Main loop
while True:
    temp = temperature()
    if temp > 22:
        display.show(Image.ARROW_N)
    elif temp < 20:
        display.show(Image.ARROW_S)
    else:
        display.show(Image.HAPPY)
    sleep(1000)
