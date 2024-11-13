from microbit import *
import radio

# --- SETUP
# start sensors

# store variables

# --- RUNNING
while True:
    # -- transmitting
    # read sensor data
    a_pressed = button_a.was_pressed()
    b_pressed = button_b.was_pressed()
    
    # process data
    
    # output data
    if a_pressed:
        radio.send("happy")
        display.show("A")
    elif b_pressed:
        radio.send("sad")
        display.show("B")
        
    # -- recieving
    # read sensor data
    incoming = radio.receive()
    
    # process data
    
    # output data
    if incoming == "happy":
        display.show(Image.HAPPY)
    elif incoming == "sad":
        display.show(Image.SAD)

