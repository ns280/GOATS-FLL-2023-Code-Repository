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
Right_arm = Motor(Port.E, Direction.COUNTERCLOCKWISE, [12, 24, 12, 24])
Left_arm = Motor(Port.A, Direction.CLOCKWISE, [12, 24, 12, 48])

# CODE from start position to move Orange Stop / M08 and M09 completion 
Right_arm.run_angle(200, 260, wait=False)
Left_arm.run_angle(180, 260, wait=False)
drive_base.straight(250)
drive_base.straight(50)
Right_arm.run_angle(900, -270)
drive_base.settings(90, 800, 100, 200)
drive_base.straight(-115)
drive_base.turn(-40)
drive_base.settings(400, 800, 100, 200) 
# ORANGE STOP LIFTED(M08) and M09 COMPLETE


# START MOVING ROBOT TO EXECUTE M01
Left_arm.run_angle(500, -50)
Left_arm.run_angle(500, -210, wait=False)
drive_base.turn(-65)
drive_base.straight(390)
wait(100)
drive_base.turn(-73)
drive_base.settings(100, 800, 100, 200)
Right_arm.run_angle(260, 360, wait=False)
drive_base.straight(135)
wait(100)
#Right_arm.run_angle(400, 320)
drive_base.straight(-60)
Right_arm.run_angle(400, -270)
drive_base.settings(400, 800, 100, 200)
# M01 COMPLETE

# START MOVING ROBOT TO COLLECT SAM STAGE MANAGER AND EXECUTE M02
drive_base.straight(-70)
drive_base.turn(85)
Right_arm.run_angle(200, 280, wait=False)
drive_base.straight(290)
#Right_arm.run_angle(400, 400)
drive_base.settings(100, 800, 30, 200)
drive_base.turn(-19)
Right_arm.run_angle(300, -160)
drive_base.turn(-16)
drive_base.settings(200, 800, 100, 200)
drive_base.straight(90)
drive_base.straight(-90)
# COMPLETE COLLECT SAM STAGE MANAGER AND EXECUTE M02

# HEAD TO M03 AND EXECUTE
drive_base.turn(100)
drive_base.settings(300, 800, 100, 200)
drive_base.straight(190)
drive_base.turn(28)

Left_arm.run_angle(400, 270)
drive_base.settings(60, 800, 20, 200)
drive_base.turn(-22)

Left_arm.dc(80)
Left_arm.run_angle(400, -280, wait=False)
wait(400)
drive_base.straight(-70)
# COMPLETE  M02

# HEAD TO M05 AND EXECUTE
drive_base.settings(600, 800, 200, 400)
drive_base.turn(15)
Left_arm.run_angle(900, 280, wait=False)
drive_base.straight(570)
drive_base.turn(-25)
drive_base.straight(40)
drive_base.settings(600, 800, 300, 400)
drive_base.turn(60)
# COMPLETE M05

# HEAD TO M06 and M07 AND EXECUTE
drive_base.settings(400, 600, 100, 200)
Left_arm.run_angle(500, -280, wait=False)
Right_arm.run_angle(400, -30, wait=False)
drive_base.straight(250)
drive_base.turn(-28)
wait(10)
drive_base.straight(340)

drive_base.turn(-36)
wait(10)
Left_arm.run_angle(400, 280)
drive_base.settings(80, 200, 200, 400)
drive_base.turn(-10)
drive_base.straight(30)
Left_arm.run_angle(400, -50)
drive_base.turn(-10)
