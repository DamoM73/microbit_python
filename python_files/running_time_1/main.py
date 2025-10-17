# running_time()
from microbit import *

'''
The microbit has a very simple timing mechanism called running_time().
It keeps a running count of the number of the time since
the micro:bit started in milliseconds.
'''

while True:
    print(running_time())