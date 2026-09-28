from microbit import *

# Main loop
while True:
    level = microphone.sound_level()
    display.scroll(level)
    sleep(500)
