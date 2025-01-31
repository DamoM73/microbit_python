from microbit import *
from PiicoDev_Servo import PiicoDev_Servo, PiicoDev_Servo_Driver

# --- SETUP
# --- start components
controller = PiicoDev_Servo_Driver()
servo = PiicoDev_Servo(controller, 1, min_us=625, max_us=2750, degrees=180)

# store variables

# --- RUNNING
while True:
    # read sensor data
    
    # process data
    
    # output data
    # move to specific positions
    servo.angle = 0
    sleep(1000)
    servo.angle = 90
    sleep(1000)
    servo.angle = 180
    sleep(1000)
    servo.angle = 0
    sleep(2000)
    
    # sweep over range of servo
    for x in range(0,180,5):
        servo.angle = x
        sleep(40)
