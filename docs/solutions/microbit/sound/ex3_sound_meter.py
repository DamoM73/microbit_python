from microbit import *

# Main loop
while True:
    level = microphone.sound_level()
    rows = level // 51
    display.clear()
    for y in range(rows):
        for x in range(5):
            display.set_pixel(x, 4 - y, 9)
    sleep(100)
