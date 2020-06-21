from gpiozero import Robot
from time import sleep
robby = Robot(left=(7,8), right=(10, 9))
robby2 = Robot(left=(6,13), right=(26, 19))

def go_back():
    robby.backward()
    robby2.backward()
    print("go backward")
    sleep(100)
    return

go_back()