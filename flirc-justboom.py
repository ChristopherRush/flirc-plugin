import keyboard  # using module keyboard
import os
while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('enter'):  # if key 'q' is pressed
            os.system("curl localhost:3000/api/v1/commands/?cmd=toggle")
            break  # finishing the loop
        else:
            pass
    except:
        break  # if user pressed a key other than the given key the loop will break
