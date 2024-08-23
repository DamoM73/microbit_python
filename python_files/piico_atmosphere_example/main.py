# PiicoDev Atmospheric Sensor BME280 minimal example code
# This program reads Temperature, Pressure and Relative Humididty
# from the PiicoDev Atmospheric Sensor. An altitude reading is also
# available

from PiicoDev_BME280 import PiicoDev_BME280
from PiicoDev_Unified import sleep_ms # cross-platform compatible sleep function

sensor = PiicoDev_BME280() # initialise the sensor

while True:
    # Print data
    tempC, press, humRH = sensor.values() # read all data from the sensor
    print("Temp: " + str(tempC) + "\tHumidity: " + str(humRH) + "\tAir presure: " + str(press))
    sleep_ms(1000)