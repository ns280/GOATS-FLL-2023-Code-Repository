from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase, GyroDriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

# Initialize both motors. In this example, the motor on the
# left must turn counterclockwise to make the robot go forward.
left_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.D)

# Initialize the drive base. In this example, the wheel diameter is 62.5mm (LEGO WHEELS).
# The distance between the two wheel-ground contact points is 136mm.
drive_base = GyroDriveBase(left_motor, right_motor, wheel_diameter=62.5, axle_track=136)

drive_base.settings(400, 800, 100, 200) 
Right_arm = Motor(Port.E, Direction.COUNTERCLOCKWISE, [24, 12, 24])
Left_arm = Motor(Port.A, Direction.CLOCKWISE, [24, 12, 24])

# CODE from start position to move Orange Stop / M08 and M09 completion 
Right_arm.run_angle(250, 510, wait=False)
drive_base.straight(250)
#Right_arm.run_angle(400, 510)
Left_arm.run_angle(400, 350)
drive_base.straight(40)
Right_arm.run_angle(600, -250)
drive_base.settings(80, 800, 100, 200)
drive_base.straight(-115)
drive_base.turn(-40)
drive_base.settings(400, 800, 100, 200) 
# ORANGE STOP LIFTED(M08) and M09 COMPLETE

# START MOVING ROBOT TO EXECUTE M01
Left_arm.run_angle(400, -250)
drive_base.turn(-65)
drive_base.straight(385)
wait(100)
drive_base.turn(-73)
drive_base.settings(100, 800, 100, 200)
Right_arm.run_angle(150, 400, wait=False)
drive_base.straight(100)
#Right_arm.run_angle(400, 320)
drive_base.straight(-60)
Right_arm.run_angle(400, -400)
drive_base.settings(400, 800, 100, 200)
drive_base.straight(-80)
# M01 COMPLETE

# START MOVING ROBOT TO COLLECT SAM STAGE MANAGER AND EXECUTE M02
drive_base.turn(80)
Right_arm.run_angle(200, 600, wait=False)
drive_base.straight(290)
#Right_arm.run_angle(400, 400)
drive_base.settings(100, 800, 30, 200)
drive_base.turn(-15)
Right_arm.run_angle(600, -280)
drive_base.turn(-13)
drive_base.settings(200, 800, 100, 200)
drive_base.straight(80)
drive_base.straight(-80)
# COMPLETE COLLECT SAM STAGE MANAGER AND EXECUTE M02
# Execute M03
drive_base.turn(100)

drive_base.settings(300, 800, 100, 200)
drive_base.straight(180)
drive_base.turn(20)
Left_arm.run_angle(600, 50)
drive_base.settings(25, 800, 20, 200)
drive_base.straight(6)
drive_base.turn(-18)
Left_arm.run_angle(400,50)
drive_base.straight(15)
Left_arm.run_angle(400, 350)