# sound exercise 3

from microbit import *

while True:
    sound_level = microphone.sound_level()
    print(sound_level)
    if sound_level > 200:
        brightness = sound_level - 200 // 5
        if brightness > 9:
            brightness = 9
        matrix = [9, 9, 9, 9, brightness]
    elif sound_level > 150:
        brightness = sound_level - 200 // 5
        if brightness > 9:
            brightness = 9
        matrix = [9, 9, 9, brightness, 0]
    elif sound_level > 100:
        brightness = sound_level - 200 // 5
        if brightness > 9:
            brightness = 9
        matrix = [9, 9, brightness, 0, 0]
    elif sound_level > 50:
        brightness = sound_level - 200 // 5
        if brightness > 9:
            brightness = 9
        matrix = [9, brightness, 0, 0, 0]
    else:
        brightness = sound_level // 5
        if brightness > 9:
            brightness = 9
        matrix = [brightness, 0, 0, 0 ,0]
    
    for x_index in range(5):
        for y_index in range(5):
            display.set_pixel(x_index, y_index, matrix[x_index])
            
    sleep(10)
    
    