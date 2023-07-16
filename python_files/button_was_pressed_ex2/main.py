from microbit import *
import random

# create random sequence
sequence = []
for _ in range(4):
    sequence.append(random.choice(["A","B"]))
    
# display sequence to user
for letter in sequence:
    display.show(letter)
    sleep(500)
    display.clear()
    sleep(500)

# get user input
display.show("?")

user_input = []

while len(user_input) < 4:
    if button_a.was_pressed():
        user_input.append("A")
    if button_b.was_pressed():
        user_input.append("B")

# check if user_input matches sequence
if user_input == sequence:
    display.show(Image.HAPPY)
else:
    display.show(Image.SAD)