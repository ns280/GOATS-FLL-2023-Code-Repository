from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase, GyroDriveBase
from pybricks.tools import wait, StopWatch
from pybricks.tools import hub_menu

hub = PrimeHub()

left_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.D)
# Initialize the drive base. In this example, the wheel diameter is 62.5mm (LEGO WHEELS).
drive_base = GyroDriveBase(left_motor, right_motor, wheel_diameter=62.5, axle_track=136)
drive_base.settings(350,650,100,200)


Right_arm = Motor(Port.E, Direction.COUNTERCLOCKWISE, [24, 12, 12, 24])
Left_arm = Motor(Port.A, Direction.COUNTERCLOCKWISE, [24, 12, 12, 24])

#speed = 500

#Drop off little experts and audience members #Yay

drive_base.straight(600)
drive_base.turn(-10)
drive_base.straight(195)

drive_base.turn(-35)
Right_arm.run_angle(200,225)
wait(10)
Right_arm.run_angle(300, -35, wait=False)
drive_base.straight(-70)
#Turn to avoid flower

drive_base.curve(45,-63)
drive_base.straight(200)
wait(10)

#drop off innovation

drive_base.curve(330,80)

Right_arm.run_angle(200,240)
#disconnect curator
drive_base.turn(-25)

#go back
drive_base.straight(-180)
#turn for next position
drive_base.turn(-40)
drive_base.straight(200)
drive_base.curve(700,25)

#IZZY dropoff
Right_arm.run_angle(200,200)
drive_base.turn(-30)
#drive_base.curve(520,60)
#the last expert
Right_arm.run_angle(200,340,wait=False)
drive_base.straight(120)
drive_base.curve(190,-60)
wait(10000)
#The End!
