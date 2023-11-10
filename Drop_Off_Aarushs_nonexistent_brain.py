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

speed = 500





#Right_arm.run_angle(200,175)
#drive_base.curve(100,-30)
#drive_base.straight(30)
#Right_arm.run_angle(200, -400)
#drive_base.curve(100,-30)
#Drop off little experts and audience members
drive_base.turn(-5) 
drive_base.straight(795)
drive_base.turn(-45)
Right_arm.run_angle(200,225)
wait(10)
drive_base.turn(-60)
drive_base.straight(300)
drive_base.curve(280,80)
drive_base.straight(-80)
drive_base.curve(-282,55)
drive_base.curve(1500,10)
Right_arm.run_angle(400,800,wait=False)
drive_base.straight(400)


