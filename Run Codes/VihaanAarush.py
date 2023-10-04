from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase, GyroDriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

left_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.D)

drive_base = GyroDriveBase(left_motor, right_motor, wheel_diameter=62.5, axle_track=136)
drive_base.settings(300,500,100,200)

Right_arm = Motor(Port.E, Direction.COUNTERCLOCKWISE, [24, 12, 12, 24])
Left_arm = Motor(Port.A, Direction.COUNTERCLOCKWISE, [24, 12, 12, 24])

speed = 200

#Code doesn't start here!
drive_base.straight(290)
Left_arm.run_angle(800,160)
drive_base.straight(10)
Left_arm.run_angle(700,-550)

#drive_base.straight(450)
#drive_base.turn(80)
#drive_base.straight(390)
#drive_base.straight(-90)
#drive_base.turn(15)
#drive_base.straight(375)
#drive_base.turn(-90)
#drive_base.straight(350)
#drive_base.turn(270)
