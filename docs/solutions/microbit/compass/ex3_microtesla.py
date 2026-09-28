from microbit import *

# Main loop
while True:
    field = compass.get_field_strength()
    display.scroll(field // 1000)
    sleep(500)
