from PiicoDev_Potentiometer import PiicoDev_Potentiometer
from PiicoDev_Unified import sleep_ms
import music

duration_pot = PiicoDev_Potentiometer(minimum=0, maximum=1000, id=[0,0,0,0])
frequency_pot = PiicoDev_Potentiometer(minimum=100, maximum=15000 ,id=[1,0,0,0])

while True:
    duration = int(duration_pot.value)
    frequency = int(frequency_pot.value)
    
    music.pitch(frequency,duration)