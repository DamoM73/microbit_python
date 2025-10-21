from microbit import *

def reduce_time():
    '''
    this function will run every second, but what it does but what
    it does depends on running variable set in the main program
    '''
    
    global timer, running           # allow function to change main program variables
    
    if running:                     # only reduce time if running is True
        timer = timer - 1
        if timer == 0:
            display.show(Image.NO)
            sleep(1000)
            running = False
    else:                           # reset timer when not running is not True
        timer = 5
    

# --- SETUP
# start components

# store vairables
running = False
timer = 5

# --- RUNNING
run_every(reduce_time,s=1)          # runs reduce_time() every second

while True:
    # read data
    button_a_pressed = button_a.was_pressed()
    
    # process data
    if button_a_pressed:
        running = True
    
        
    # output data
    display.show(timer, 100)