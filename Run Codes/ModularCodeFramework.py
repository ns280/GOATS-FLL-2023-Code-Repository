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

speed = 400

#Choose a letter
selected = hub_menu("F","N", "D","Z","V")

#Code Starts here!

def Sahas_Nik():
    drive_base.straight(470)
    Left_arm.run_target(speed, 190)
    Left_arm.run_target(speed, -70)
    drive_base.straight(-120)
    drive_base.curve(radius=-90, angle=92)
    drive_base.straight(-480)
    Left_arm.run_target(speed, 218)
    drive_base.straight(250)
    drive_base.turn(-130)
    drive_base.straight(-40)
    Right_arm.run_until_stalled(speed, duty_limit=30)
    drive_base.straight(-20)
    drive_base.straight(-162)
    

def Sahas_Vikram():
    Left_arm.run_target(speed, 50)

def Nik_2():
    Left_arm.run_target(speed, -50)
    drive_base.straight(580)
    drive_base.turn
    Left_arm.run_target(800, 50)
    Left_arm.run_target(speed, 50)






def Mahati_Aarush():
    #Right_arm.run_until_stalled(speed, duty_limit=10)
    Right_arm.run_target(speed, 10)
    drive_base.straight(50)
    Right_arm.run_target(speed + 60, -20)
    drive_base.straight(-15)
    drive_base.turn(-10)   
    #Right_arm.run_target(speed, 30)

#Based on Selection, run the program
if selected == "F":
    Sahas_Nik()
elif selected == "N":
    Nik_2()
elif selected == "D":
    Sahas_Vikram()
elif selected== "Z":
    Mahati_Aarush()
elif selected == "V":
    Vihaan_Aarush()