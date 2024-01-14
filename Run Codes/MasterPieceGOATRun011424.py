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

#Right_arm = Motor(Port.E, Direction.COUNTERCLOCKWISE, [12, 24, 12, 24])
#Left_arm = Motor(Port.A, Direction.CLOCKWISE, [12, 24, 12, 48])

Right_arm = Motor(Port.E, Direction.COUNTERCLOCKWISE, [24, 12, 12, 24])
Left_arm = Motor(Port.A, Direction.COUNTERCLOCKWISE, [24, 12, 12, 24])

# CODE from start position to move Orange Stop / M08 and M09 completion 
Right_arm.run_angle(500, 550, wait=False)
Left_arm.run_angle(730, -1100, wait=False)
drive_base.straight(250)
drive_base.straight(50)
Right_arm.run_angle(900, -270)
drive_base.settings(90, 800, 100, 200)
drive_base.straight(-115)
drive_base.turn(-40)
drive_base.settings(400, 800, 100, 200) 
# ORANGE STOP LIFTED(M08) and M09 COMPLETE


# START MOVING ROBOT TO EXECUTE M01
Left_arm.run_angle(500, 250)
Left_arm.run_angle(1000, 800, wait=False)
drive_base.turn(-65)
drive_base.straight(400)
wait(100)
drive_base.turn(-75)
drive_base.settings(100, 800, 100, 200)

# Parllel arm down with robot moving...risky but helps with speed
#Right_arm.run_angle(170, 520, wait=False)
drive_base.straight(100)
Right_arm.run_angle(500, 490)
#Wait needed for parallel arm down
#wait(190)

#Right_arm.run_angle(400, 320)
drive_base.straight(-60)
Right_arm.run_angle(400, -270)

drive_base.settings(400, 800, 100, 200)
# M01 COMPLETE

# START MOVING ROBOT TO COLLECT SAM STAGE MANAGER AND EXECUTE M02
drive_base.straight(-70)
drive_base.turn(83)
Right_arm.run_angle(700, 300, wait=False)

drive_base.straight(270)
#Right_arm.run_angle(400, 400)
drive_base.settings(100, 800, 30, 200)
drive_base.turn(-16)
Right_arm.run_angle(380, -360)

drive_base.turn(-22)
drive_base.settings(200, 800, 100, 200)
drive_base.straight(90)
drive_base.straight(-90)

#STOP CODE HERE FOR PINK BALL
#CODE FOR ORANGE BALL
wait(200)
drive_base.straight(100)
drive_base.straight(-90)
# COMPLETE COLLECT SAM STAGE MANAGER AND EXECUTE M02

# HEAD TO M03 AND EXECUTE
drive_base.turn(100)
drive_base.settings(300, 800, 100, 200)
drive_base.straight(180)
drive_base.turn(38)

Left_arm.run_angle(1000, -1050)
drive_base.settings(50, 800, 20, 200)
drive_base.turn(-23)

Left_arm.dc(85)
Left_arm.run_angle(500, 1050, wait=False)
wait(400)
drive_base.straight(-80)
# COMPLETE  M03


# HEAD TO M05 AND EXECUTE
drive_base.settings(600, 800, 200, 400)
drive_base.turn(15)
Left_arm.run_angle(900, -900, wait=False)
drive_base.straight(539)
drive_base.turn(-28)
drive_base.straight(83)

drive_base.settings(600, 800, 500, 600)
drive_base.turn(80)
# COMPLETE M05

# HEAD TO M06 and M07 AND EXECUTE
drive_base.settings(400, 600, 100, 200)
Left_arm.run_angle(500, 950, wait=False)
drive_base.straight(170)

#POSITIONING THE ROBOT FOR M06 and M07
drive_base.turn(-46)
drive_base.straight(460)

drive_base.turn(-41)
drive_base.settings(80, 200, 200, 400)

#COMMENTED CODE HERE TO TURN ON LEFT LEVER FOR SPEAKER
#drive_base.straight(-70)

#LOWERING THE ARM FOR FLIPPING THE LEFT SPEAKER LEVER
#Left_arm.run_angle(400, -1000)
#drive_base.straight(60)

#Left_arm.run_angle(400, 200)
#drive_base.turn(-25)
#drive_base.straight(-80)
#Left_arm.run_angle(1000, 600)
#drive_base.turn(25)

#CODE FOR M06 and RIGHT LEVER STARTS HERE
drive_base.straight(120)
Right_arm.run_angle(400, 90)
drive_base.turn(15)
drive_base.straight(-120)
#FAILSAFE IF THE ARM GETS STUCK ON THE FRAME OF THE MUSIC STAGE
#drive_base.straight(20)
#Right_arm.run_angle(400, -100)
drive_base.settings(800, 900, 200, 400)
drive_base.turn(100)
drive_base.straight(600)
#RUN1 ENDS AND ROBOT BACK IN EAST HOMEBASE