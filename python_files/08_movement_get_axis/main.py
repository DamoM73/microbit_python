from microbit import *

# --- SETUP
# start sensors

# store variables

# --- RUNNING
while True:
    # read sensor data
    x_reading = accelerometer.get_x()
    y_reading = accelerometer.get_y()
    z_reading = accelerometer.get_z()
    
    # process data
    
    # output data
    print(x_reading, y_reading, z_reading)
    
    sleep(100)
