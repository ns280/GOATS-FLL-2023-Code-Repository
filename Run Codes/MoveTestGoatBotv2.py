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

# Initialize the drive base. In this example, the wheel diameter is 62.5mm.
# The distance between the two wheel-ground contact points is 112mm.
drive_base = GyroDriveBase(left_motor, right_motor, wheel_diameter=62.5, axle_track=136)

drive_base.settings(300,1000,100,200)

Right_arm = Motor(Port.E, Direction.COUNTERCLOCKWISE, [24, 12, 12, 24])
Left_arm = Motor(Port.A, Direction.COUNTERCLOCKWISE, [24, 12, 12, 24])

# We'll use a speed of 200 deg/s in all our commands.
speed = 800
# Drive forward by xxmm 
drive_base.straight(300)

# Turn around clockwise by 180 degrees.
drive_base.turn(40)

# Drive forward by xxmm 
drive_base.straight(170)
Right_arm.run_target(speed, -300)