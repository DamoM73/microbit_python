from microbit import *

# Main loop
while True:
    if compass.is_calibrated():
        display.show(Image.YES)
    else:
        display.show(Image.NO)
    sleep(1000)
