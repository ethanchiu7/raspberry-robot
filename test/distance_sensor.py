from gpiozero import DistanceSensor, LED
from signal import pause


def in_range():
    print("in range")


def out_of_range():
    print("out of range")


sensor = DistanceSensor(23, 24, max_distance=0.5, threshold_distance=0.1)

sensor.when_in_range = in_range
sensor.when_out_of_range = out_of_range

pause()
