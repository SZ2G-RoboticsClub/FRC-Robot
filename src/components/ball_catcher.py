import wpilib

class BallCatcher():

    solenoid: wpilib.Solenoid

    def on_enable(self):
        pass

    def execute(self):
        pass

    def set(self, output):
        self.solenoid.set(output)
