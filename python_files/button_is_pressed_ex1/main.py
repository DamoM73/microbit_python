# button.is_presses exercise 1

from microbit import *
import time
import random

# select button
button = random.choice(["A","B"])

# display the countdown
for num in ["3","2","1"]:
    display.show(num)
    sleep(1000)

display.show(button)

# start the timer
start_time = time.ticks_ms()

# wait for correct button to be pressed
while True:
    if button == "A" and button_a.is_pressed():
        break
    if button == "B" and button_b.is_pressed():
        break
    
# stop the timer
end_time = time.ticks_ms()

# calculate the elapsed time in seconds
elapsed_time = (end_time - start_time) / 1000.0

# display the elapsed time
display.scroll(str(elapsed_time) + " seconds")
