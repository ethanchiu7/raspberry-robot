from gpiozero import MotionSensor, LED
from robot import RaspberryRobot
from signal import pause

pir = MotionSensor(14)

robot = RaspberryRobot()


def print_motion():
    print("motion")


def print_no_motion():
    print("no_motion")


pir.when_motion = robot.forward()
pir.when_no_motion = robot.stop()

pause()
