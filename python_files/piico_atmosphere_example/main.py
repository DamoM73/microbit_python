from microbit import *
from PiicoDev_BME280 import PiicoDev_BME280

# --- SETUP

# start sensors
sensor = PiicoDev_BME280()

# store variables
bom_air_pressure = 1014.6 # taken from web
sea_level = sensor.altitude(bom_air_pressure)


# --- RUNNING
while True:
    # read sensor data
    temp, air_pressure, humidity = sensor.values()
    altitutde = sensor.altitude()
    
    # process data
    temp = str(temp)
    air_pressure = str(air_pressure / 100) # convert from Pascals -> hPa
    humidity = str(humidity)
    altitutde = str(sea_level - altitutde)
    
    # output data
    print(temp, air_pressure, humidity, altitutde)
    
    sleep(100)
