from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase, GyroDriveBase
from pybricks.tools import wait, StopWatch
from pybricks.tools import hub_menu

hub = PrimeHub()

left_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.D)

drive_base = GyroDriveBase(left_motor, right_motor, wheel_diameter=62.5, axle_track=136)
drive_base.settings(300,600,100,200)


Right_arm = Motor(Port.E, Direction.COUNTERCLOCKWISE, [24, 12, 12, 24])
Left_arm = Motor(Port.A, Direction.COUNTERCLOCKWISE, [24, 12, 12, 24])

speed = 700

#Code Starts here!
drive_base.curve(100, -35)
drive_base.straight(240)
Right_arm.run_target(300, -400,wait=False)
wait(300)
drive_base.settings(150,600,100,200)
drive_base.turn(-0.5)
drive_base.straight(122)
Left_arm.run_target(1000, 3000)
drive_base.turn(-8)
drive_base.straight(-100)
drive_base.curve(320,12)
drive_base.settings(300,600,100,200)
drive_base.settings(999, 999, 999, 999)
drive_base.straight(-150)
drive_base.turn(-220)
drive_base.straight(300)
