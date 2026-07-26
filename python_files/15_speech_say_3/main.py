from microbit import *
import speech

# --- SETUP
# start sensors

# store variables
solfa = [
    "#115DOWWWWWW",   # Doh
    "#103REYYYYYY",   # Re
    "#94MIYYYYYY",    # Mi
    "#88FAOAOAOAOR",  # Fa
    "#78SOHWWWWW",    # Soh
    "#70LAOAOAOAOR",  # La
    "#62TIYYYYYY",    # Ti
    "#58DOWWWWWW",    # Doh
    ]

song = ''.join(solfa)

# --- RUNNING
while True:
    # read sensor data
    
    # process data
    
    # output data
    speech.sing(song)
    
    sleep(1000)