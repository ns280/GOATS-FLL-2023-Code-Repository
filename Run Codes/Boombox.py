from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

    #Right_arm.run_until_stalled(speed, duty_limit=70)
    Right_arm.run_target(speed, -70)
    #drive_base.straight(100)

