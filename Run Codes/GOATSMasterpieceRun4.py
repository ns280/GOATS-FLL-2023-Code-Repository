from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase, GyroDriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

left_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.D)

drive_base = GyroDriveBase(left_motor, right_motor, wheel_diameter=62.5, axle_track=136)
drive_base.settings(400,500,100,200)

Left_arm = Motor(Port.A, Direction.COUNTERCLOCKWISE, [24, 12, 12, 24])
Right_arm = Motor(Port.E, Direction.COUNTERCLOCKWISE, [24, 12, 12, 24])

speed = 200

#Code starts here!                                                                                                         Secrets Lie Here  ---->                                                                                  Hey, don't look!                                                                                 Please, I'll give you -$0.02!                                                                                             There's nothing I'm telling you!                                                                       Please, don't go any further!                                                            I'll ban you from the Earth!!!                                                   I'll call your mommy!!!                                                                      I'll call MY mommy, my daddy, my uncles and aunties, all my weird relatives if it means keeping this secret from the likes of you!!!                                                     Okay, fine...                                                                         Strawberries eat humans who disrespect pasta.                                             How did you guess that that wasn't my real secret?                                                         Eh, I guess I made it easy enough...                                                                                   No WAY I'm telling you the real secret! That's all you're getting!                                                                        OK, fine, I'll tell you the real secret...                                                                You're persistent, aren't you?                                                                        OK, I'll stop stalling...                                                                                 You're a menace to society, you know?                                                        You ready for this?????                                                                                   What do you mean, obviously?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!                                                                                Here we go...                                                                                                         Zero doesn't exist, because zero is nothing, but to speak of nothing is to speak of something.                                                                                                                               SHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DON'T TELL ANYONE!!!

#Drive parallel to rolling camera
    drive_base.straight(300)
    
    Lower left arm into the pocket next to the rolling camera
    Left_arm.run_angle(500,-415)
    
    #Drive forward, pushing the rolling camera and bringing the arm back up at the same time
    drive_base.straight(135)
    Left_arm.run_angle(500,415,wait=False)
    
    #Push the boat
    drive_base.straight(220)

    #Come back from pushing the boat
    drive_base.straight(-220)

    #Turn
    drive_base.curve(100,13) 

    #Move forward 320 mm
    drive_base.straight(320)

    #Curve to face exactly in front of the Light Show
    drive_base.curve(100,77)
    drive_base.curve(10,2.5)

    #Drive closer to the light show
    drive_base.straight(20)

    #Increase duty cycle for more power and activate chopper arm; finish M11, drop expert and audience, and drop audience into light show area
    Right_arm.dc(100)
    Right_arm.run_angle(10000000,-3700) 
    Right_arm.run_angle(1000,20)

    #Move back and turn to face Noah the Sound Engineer
    drive_base.straight(-150)
    drive_base.turn(-45)
    
    #Move to pick up Noah and turn full 180 to face home
    drive_base.straight(242)
    drive_base.turn(80)
    drive_base.straight(-80)
    drive_base.turn(60)
    
    #Drive back really fast
    drive_base.settings(800,1000,100,200)
    drive_base.straight(1100)
