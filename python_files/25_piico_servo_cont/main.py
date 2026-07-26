from microbit import *
from PiicoDev_Servo import PiicoDev_Servo, PiicoDev_Servo_Driver

# --- SETUP
# --- start components
controller = PiicoDev_Servo_Driver()
continuous_servo = PiicoDev_Servo(controller, 1, midpoint_us=1500, range_us=1800)

# store variables

# --- RUNNING
while True:
    # read sensor data
    
    # process data
    
    # output data
    # fast forward
    continuous_servo.speed = 1    
    sleep(1000)
    # slow forward
    continuous_servo.speed = 0.2
    sleep(1000)
    # slow reverse
    continuous_servo.speed = -0.2
    sleep(1000)
    # slow reverse
    continuous_servo.speed = -1
    sleep(1000)
    # stop
    continuous_servo.speed = 0
    sleep(1000)