from microbit import *
from PiicoDev_Servo import PiicoDev_Servo, PiicoDev_Servo_Driver

# --- SETUP
# --- start components
controller = PiicoDev_Servo_Driver()
continuous_servo = PiicoDev_Servo(controller, 1, midpoint_us=1575, range_us=1800)

# store variables

# --- RUNNING
continuous_servo.speed = 0