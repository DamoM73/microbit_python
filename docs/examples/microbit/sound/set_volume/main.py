from microbit import *
import music

# Setup
set_volume(50)

# Main loop
while True:
    music.play(music.BA_DING)
    sleep(1000)
