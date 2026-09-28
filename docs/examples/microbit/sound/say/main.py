from microbit import *
import speech

# Main loop
while True:
    speech.say("Hello world", speed=90, pitch=60)
    sleep(1000)
