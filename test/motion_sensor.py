from gpiozero import MotionSensor, LED
from signal import pause

pir = MotionSensor(14)


def print_motion():
    print("motion")


def print_no_motion():
    print("no_motion")


pir.when_motion = print_motion
pir.when_no_motion = print_no_motion

pause()
