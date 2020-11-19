#!/usr/bin/env python3

import wpilib
import wpilib.drive
from magicbot import MagicRobot
from components.chassis import Chassis

class MyRobot(MagicRobot):

    chassis: Chassis

    def createObjects(self):
        self.timer = wpilib.Timer()
        self.timer.reset()
        self.timer.start()
        
        self.chassis_l_motor = wpilib.SpeedControllerGroup(wpilib.Spark(0), wpilib.Spark(1))
        self.chassis_r_motor = wpilib.SpeedControllerGroup(wpilib.Spark(2), wpilib.Spark(3))

        self.joystick = wpilib.Joystick(0)

    def teleopInit(self):
        self.chassis.init()

    def teleopPeriodic(self):
        self.chassis.set_speed(self.joystick.getY(), self.joystick.getX())
        # self.chassis.set_speed(0.5, 0.2)


if __name__ == "__main__":
    wpilib.run(MyRobot)