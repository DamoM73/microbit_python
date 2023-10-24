# PiicoDev Atmospheric Sensor BME280 minimal example code
# This program reads Temperature, Pressure and Relative Humididty
# from the PiicoDev Atmospheric Sensor. An altitude reading is also
# available

from PiicoDev_BME280 import PiicoDev_BME280
from PiicoDev_Unified import sleep_ms # cross-platform compatible sleep function

def wbt(temp,hum):

    return (temp - ((1-hum)/5))

sensor = PiicoDev_BME280() # initialise the sensor

while True:
    # Print data
    tempC, press, humRH = sensor.values() # read all data from the sensor
    print("Here")
    #print(wbt(tempC, humRH))
    sleep_ms(1000)