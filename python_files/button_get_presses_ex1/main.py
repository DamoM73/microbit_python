from microbit import *

target_presses = 10
time_limit = 5000  # 5 seconds
count = 0

while True:
    button_presses = button_a.get_presses()
    count += button_presses

    if count >= target_presses:
        display.scroll("You win!")
        break

    if running_time() >= time_limit:
        display.scroll("Time's up!")
        break

    display.show(str(count))