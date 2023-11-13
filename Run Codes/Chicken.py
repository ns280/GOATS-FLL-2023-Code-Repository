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
#Reach the girl
drive_base.straight(240)
#Pickup girl
Right_arm.run_target(500, -400)
#updating the speed
drive_base.settings(150,600,100,200)
#commenting the turn to test it out
#drive_base.turn(-1)
#Reach Chicken gear
drive_base.straight(123)
#Moving the chicken
Left_arm.run_target(1000, 3000)
#Aligning to lift the latch
drive_base.turn(-8)
#increasing velocity so latch comes up
drive_base.settings(300,600,100,200)
#Raising latch and coming back
drive_base.straight(-105)
#To get out of the way
#drive_base.curve(320,5) - did not work
#drive_base.curve(320,12) - original but not consistent
drive_base.curve(350,12)
#Updating the speed to go faster (600, 600, 200,200)
drive_base.settings(600,600,200,200)
#Coming back
drive_base.straight(-180)
#Pickup lady
drive_base.turn(-220)
#Get to the homezone
drive_base.straight(300)
