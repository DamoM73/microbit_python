from microbit import *

# --- SETUP
# start components

# store variables
num_rows = 5
num_columns = 5
# --- RUNNING
display.clear()
while True:
    # read sensor data
    
    # process data
    
    # output data
    for col in range(num_columns):
        for row in range(num_rows):
            display.set_pixel(col, row, 9)
            sleep(50)
            display.clear()