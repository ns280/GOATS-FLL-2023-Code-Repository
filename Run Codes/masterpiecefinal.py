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
selected = hub_menu("1","2", "3","4","5")

#Code Starts here!

def Sahas_Nik():
#Run 1 Code


def Sahas_Nik2():
  #Run 5 Code


def Mahati_Aarush():
#MahatiAarush Code starts from here

def Aarush_Mahati():
  #Code starts from here for 4th run
def Aarush_Vihaan():
#Based on Selection, run the program
if selected == "1":
    Sahas_Nik()
elif selected == "2":
    Mahati_Aarush()
elif selected == "3":
    Aarush_Mahati()
elif selected== "4":
    Aarush_Vihaan()
elif selected == "5":
    Sahas_Nik2()
