from microbit import *
import music

# --- SETUP
# start sensors

# store variables
min_pitch = 880
max_pitch = 1760
steps = 16
duration = 20

# --- RUNNING
while True:
    for freq in range(min_pitch, max_pitch, steps):
        music.pitch(freq, duration)
    for freq in range(max_pitch, min_pitch, -steps):
        music.pitch(freq, duration)