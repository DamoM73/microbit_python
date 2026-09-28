from microbit import *
from PiicoDev_Servo import PiicoDev_Servo, PiicoDev_Servo_Driver

# Setup
controller = PiicoDev_Servo_Driver()
motor = PiicoDev_Servo(controller, 1, midpoint_us=1500, range_us=1800)
motor.speed = 0
