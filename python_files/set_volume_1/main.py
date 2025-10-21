from microbit import *
import music

# --- SETUP
# start components

# store variables

# --- RUNNING
while True:
    set_volume(255)			    # sets volume to maximum
    music.play(music.BADDY)
    set_volume(127)			    # sets volume to middle
    music.play(music.BADDY)
    set_volume(0)				    # sets volume to minimum
    music.play(music.BADDY)