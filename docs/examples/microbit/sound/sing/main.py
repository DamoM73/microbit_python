from microbit import *
import speech

# Setup
solfa = ["#115DOWWWWWW", "#103REYYYYYY", "#94MIYYYYYY", "#88FAOAOAOAOR",
         "#78SOHWWWWW", "#70LAOAOAOAOR", "#62TIYYYYYY", "#58DOWWWWWW"]
song = "".join(solfa)

# Main loop
while True:
    speech.sing(song, speed=100)
    sleep(1000)
