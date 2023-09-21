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
drive_base.settings(300,500,100,200)

Right_arm = Motor(Port.E, Direction.COUNTERCLOCKWISE, [24, 12, 12, 24])
Left_arm = Motor(Port.A, Direction.COUNTERCLOCKWISE, [24, 12, 12, 24])

speed = 100

#Choose a letter
selected = hub_menu("F","D","Z","V")

#Code Starts here!

def Sahas_Nik():
    drive_base.straight(100)
    drive_base.turn(180)
    drive_base.straight(100)
    drive_base.turn(180)

def Sahas_Vikram():
    Left_arm.run_target(speed, 400)

def Vihaan_Aarush():
    drive_base.straight(250)
    drive_base.straight(-100)
    drive_base.turn(80)
    drive_base.straight(390)
    drive_base.straight(-90)
    drive_base.turn(15)
    drive_base.straight(375)
    drive_base.turn(-90)
    drive_base.straight(350)
    drive_base.turn(270)

#Based on Selection, run the program
if selected == "F":
    Sahas_Nik()
elif selected == "D":
    Sahas_Vikram()
elif selected== "Z":
    Mahati()
elif selected == "V":
    Vihaan_Aarush()