from microbit import *

# Main loop
while True:
    display.scroll(microphone.sound_level())
