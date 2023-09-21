from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase,GyroDriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
left_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.D)

drive_base = GyroDriveBase(left_motor, right_motor, wheel_diameter=62.5, axle_track=136)

drive_base.settings(300,1000,100,200)

Right_arm = Motor(Port.E, Direction.COUNTERCLOCKWISE, [24, 12, 12, 24])
Left_arm = Motor(Port.A, Direction.COUNTERCLOCKWISE, [24, 12, 12, 24])

speed = 400
#Code Starts here!

drive_base.straight(700)
drive_base.turn(-45)
drive_base.straight(-15)
Right_arm.run_target(speed, -360)
drive_base.straight(-60)
Right_arm.run_target(speed, 140)
drive_base.turn(100)
drive_base.straight(300)
Right_arm.run_target(speed, -180)