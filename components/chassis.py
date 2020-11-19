import wpilib
from wpilib import drive

class Chassis():

    l_motor: wpilib.interfaces.SpeedController
    r_motor: wpilib.interfaces.SpeedController

    def init(self):
        self.drive = drive.DifferentialDrive(self.l_motor, self.r_motor)
        self.x_speed = 0.0
        self.z_rot = 0.0
    
    def set_speed(self, x_speed, z_rot):
        self.x_speed, self.z_rot = x_speed, z_rot
        
    def execute(self):
        self.drive.arcadeDrive(self.x_speed, self.z_rot)

