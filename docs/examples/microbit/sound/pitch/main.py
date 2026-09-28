from microbit import *
import music

# Main loop
while True:
    for freq in range(880, 1760, 16):
        music.pitch(freq, 20)
    for freq in range(1760, 880, -16):
        music.pitch(freq, 20)
