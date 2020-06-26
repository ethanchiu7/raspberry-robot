from gpiozero import Robot, Motor
from time import sleep


class RaspberryRobot(object):
    def __init__(self):
        self.front_left_motor = Motor(7, 8)
        self.front_right_motor = Motor(10, 9)
        self.rear_left_motor = Motor(6, 13)
        self.rear_right_motor = Motor(26, 19)

    def stop(self):
        print("stop")
        self.front_left_motor.stop()
        self.front_right_motor.stop()
        self.rear_left_motor.stop()
        self.rear_right_motor.stop()

    def forward(self):
        print("go forward")
        self.front_left_motor.forward()
        self.front_right_motor.forward()
        self.rear_left_motor.forward()
        self.rear_right_motor.forward()

    def backward(self):
        print("go backward")
        self.front_left_motor.backward()
        self.front_right_motor.backward()
        self.rear_left_motor.backward()
        self.rear_right_motor.backward()

    def left(self):
        print("left")
        self.front_left_motor.forward(0)
        self.front_right_motor.forward()
        self.rear_left_motor.forward(0)
        self.rear_right_motor.forward()

    def right(self):
        print("right")
        self.front_left_motor.forward()
        self.front_right_motor.forward(0)
        self.rear_left_motor.forward()
        self.rear_right_motor.forward(0)


if __name__ == '__main__':
    robot = RaspberryRobot()
    robot.backward()
    sleep(60)

