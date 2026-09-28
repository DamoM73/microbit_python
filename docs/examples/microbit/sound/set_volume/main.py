from microbit import *
import music

# Main loop
while True:
    set_volume(255)
    music.play(music.BA_DING)
    set_volume(50)
    music.play(music.BA_DING)
    sleep(1000)
