from microbit import *

# Main loop
while True:
    if microphone.current_event() == SoundEvent.LOUD:
        display.show(Image.HEART)
        sleep(200)
    else:
        display.show(Image.HEART_SMALL)
