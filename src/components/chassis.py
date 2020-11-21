import wpilib
from wpilib import drive

class Chassis():

    l_motor: wpilib.interfaces.SpeedController
    r_motor: wpilib.interfaces.SpeedController
    fore_exp: float
    rot_exp: float

    def on_enable(self):
        self.drive = drive.DifferentialDrive(self.l_motor, self.r_motor)
        self.fore_vel = 0.0
        self.rot_vel = 0.0
        self.value2vel = lambda x, exp: (abs(x)**exp) * (x/abs(x))
        
    def execute(self):
        self.drive.arcadeDrive(self.fore_vel, self.rot_vel)
    
    def set_vel_from_joystick(self, fore_value, rot_value):
        """
            A non-linear mapping (exp) from joystick input to vel,
            enable us to ctrl chassis more precisely.
        """
        fore_vel = self.value2vel(fore_value, self.fore_exp)
        rot_vel = self.value2vel(rot_value, self.rot_exp)
        self.set_vel(fore_vel, rot_vel)

    def set_vel(self, fore_vel, rot_vel):
        self.fore_vel, self.rot_vel = fore_vel, rot_vel