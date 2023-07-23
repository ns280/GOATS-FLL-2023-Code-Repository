from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase, GyroDriveBase
from pybricks.tools import wait, StopWatch


hub = InventorHub()


left_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.D)
wheel_diameter = 44
axel_track = 96

drive_base = GyroDriveBase(left_motor, right_motor, wheel_diameter,axel_track)
drive_base.settings(300,500,100,200)


def I_AM_WAITING():
    count = 0
    l=2
    while (count < l) :
        drive_base.turn(360)
        drive_base.straight(100)
        count = count +1
    

    if count == l :
        drive_base.straight(400)
        count = count -1
    

    if not count == 0 :
        drive_base.straight(-400)
        count = count +1
         


def I_AM_WAITING_NOT():
    wait (200)
    drive_base.straight(100)
    drive_base.turn(90)
    drive_base.straight(100)
    drive_base.turn(90)
    drive_base.straight(100)
    drive_base.turn(90)
    drive_base.straight(100)
    drive_base.turn(90)



while True:
    pressed = hub.buttons.pressed() 
    if (Button.LEFT in pressed):
        drive_base.straight(100)
        I_AM_WAITING()
        hub.light.on(Color.GREEN)

    if (Button.RIGHT in pressed):
        I_AM_WAITING_NOT()
        hub.light.on(Color.RED)