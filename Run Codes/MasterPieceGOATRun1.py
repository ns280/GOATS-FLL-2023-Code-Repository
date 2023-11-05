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
Right_arm.run_angle(200, 270, wait=False)
Left_arm.run_angle(200, 270, wait=False)
drive_base.straight(250)
drive_base.straight(50)
Right_arm.run_angle(700, -270)
drive_base.settings(90, 800, 100, 200)
drive_base.straight(-115)
drive_base.turn(-40)
drive_base.settings(400, 800, 100, 200) 
# ORANGE STOP LIFTED(M08) and M09 COMPLETE


# START MOVING ROBOT TO EXECUTE M01
Left_arm.run_angle(500, -260)
drive_base.turn(-65)
drive_base.straight(390)
wait(100)
drive_base.turn(-73)
drive_base.settings(100, 800, 100, 200)
Right_arm.run_angle(280, 320, wait=False)
drive_base.straight(130)
wait(500)
#Right_arm.run_angle(400, 320)
drive_base.straight(-60)
Right_arm.run_angle(400, -270)
drive_base.settings(400, 800, 100, 200)
# M01 COMPLETE

# START MOVING ROBOT TO COLLECT SAM STAGE MANAGER AND EXECUTE M02
drive_base.straight(-70)
drive_base.turn(80)
Right_arm.run_angle(200, 280, wait=False)
drive_base.straight(285)
#Right_arm.run_angle(400, 400)
drive_base.settings(100, 800, 30, 200)
drive_base.turn(-15)
Right_arm.run_angle(400, -175)
drive_base.turn(-16)
drive_base.settings(200, 800, 100, 200)
drive_base.straight(90)
drive_base.straight(-70)
# COMPLETE COLLECT SAM STAGE MANAGER AND EXECUTE MISSION 02
#Turn after bumping
drive_base.turn(106)

#Skipping Mission 03


#Going to execute Mission 04
drive_base.settings(300, 800, 100, 200)
drive_base.straight(170)
drive_base.turn(15)
drive_base.straight(570)
drive_base.turn(-33)
Left_arm.run_angle(250, 260)
drive_base.straight(35)
drive_base.turn(50)
wait (100)
drive_base.straight(-100)
Left_arm.run_angle(400, -270)
#Mission 04 done
# Going to execute Mission 6 and Mission 7
drive_base.turn(25)
drive_base.straight(180)
drive_base.turn(-25)
drive_base.straight(340)
drive_base.turn(-35)
Left_arm.run_angle(400, 270)
drive_base.straight(190)
Left_arm.run_angle(400, -260)
