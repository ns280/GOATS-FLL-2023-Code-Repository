from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
hub.display.char("A")
wait(2000)

Right_arm = Motor(Port.E, Direction.COUNTERCLOCKWISE, [24, 12, 12, 24])
Left_arm = Motor(Port.A, Direction.COUNTERCLOCKWISE, [24, 12, 12, 24])

# We'll use a speed of 200 deg/s in all our commands.
speed = 200

# Run the motor in reverse until it hits a mechanical stop.
# The duty_limit=30 setting means that it will apply only 30%
# of the maximum torque against the mechanical stop. This way,
# you don't push against it with too much force.
Left_arm.run_until_stalled(-speed, duty_limit=30)
Right_arm.run_until_stalled(-speed, duty_limit=30)
# Reset the angle to 0. Now whenever the angle is 0, you know
# that it has reached the mechanical endpoint.
Left_arm.reset_angle(0)
Right_arm.reset_angle(0)

# Now make the motor go back and forth in a loop.
# This will now work the same regardless of the
# initial motor angle, because we always start
# from the mechanical endpoint.
for count in range(5):
    Left_arm.run_target(speed, 180)
    Left_arm.run_target(speed, 90)
    Right_arm_arm.run_target(speed, 180)
    Right_arm_arm.run_target(speed, 90)