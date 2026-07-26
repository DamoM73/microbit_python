from microbit import *

# --- SETUP
# start sensors

# store variables

# --- RUNNING
while True:
    # read sensor data
    values = accelerometer.get_values()
    
    # process data
    x_reading = values[0]
    y_reading = values[1]
    z_reading = values[2]
    
    # output data
    print(x_reading, y_reading, z_reading)
    
    sleep(100)