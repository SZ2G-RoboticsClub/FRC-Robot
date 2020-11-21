#!/usr/bin/env python3

import wpilib
import wpilib.drive
from magicbot import MagicRobot
from components.chassis import Chassis
from components.ball_catcher import BallCatcher

class MyRobot(MagicRobot):

    chassis: Chassis
    catcher: BallCatcher

    def createObjects(self):
        self.timer = wpilib.Timer()
        self.timer.reset()
        self.timer.start()
        
        self.chassis_l_motor = wpilib.SpeedControllerGroup(wpilib.Spark(0), wpilib.Spark(1))
        self.chassis_r_motor = wpilib.SpeedControllerGroup(wpilib.Spark(2), wpilib.Spark(3))
        self.chassis_fore_exp = 1.5
        self.chassis_rot_exp = 2.0

        self.catcher_solenoid = wpilib.Solenoid(moduleNumber=0, channel=0)

        self.joystick = wpilib.Joystick(0)

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        self.chassis.set_vel_from_joystick(self.joystick.getY(), self.joystick.getX())
        # self.chassis.set_speed(0.5, 0.2)


if __name__ == "__main__":
    wpilib.run(MyRobot)