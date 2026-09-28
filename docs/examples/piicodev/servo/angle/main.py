from microbit import *
from PiicoDev_Servo import PiicoDev_Servo, PiicoDev_Servo_Driver

# Setup
controller = PiicoDev_Servo_Driver()
servo = PiicoDev_Servo(controller, 4, min_us=625, max_us=2750, degrees=180)

# Main loop
while True:
    servo.angle = 90
