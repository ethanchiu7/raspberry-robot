from time import sleep
from gpiozero import MotionSensor, LED
from robot import RaspberryRobot
from signal import pause

pir = MotionSensor(14)

robot = RaspberryRobot()


def dance():
    robot.backward()
    sleep(5)
    robot.right()
    sleep(5)
    robot.stop()


def print_no_motion():
    print("no_motion")


pir.when_motion = dance
pir.when_no_motion = robot.stop

pause()
