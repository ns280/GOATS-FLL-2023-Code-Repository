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

#Choose a letter                                                                                                Secrets Lie Here  ---->                                                                                  Hey, don't look!                                                                                 Please, I'll give you -$0.02!                                                                                             There's nothing I'm telling you!                                                                       Please, don't go any further!                                                            I'll ban you from the Earth!!!                                                   I'll call your mommy!!!                                                                      I'll call MY mommy, my daddy, my uncles and aunties, all my weird relatives if it means keeping this secret from the likes of you!!!                                                     Okay, fine...                                                                         Strawberries eat humans who disrespect pasta.                                             How did you guess that that wasn't my real secret?                                                         Eh, I guess I made it easy enough...                                                                                   No WAY I'm telling you the real secret! That's all you're getting!                                                                        OK, fine, I'll tell you the real secret...                                                                You're persistent, aren't you?                                                                        OK, I'll stop stalling...                                                                                 You're a menace to society, you know?                                                        You ready for this?????                                                                                   What do you mean, obviously?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!                                                                                Here we go...                                                                                                         Zero doesn't exist, because zero is nothing, but to speak of nothing is to speak of something.                                                                                                                               SHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DON'T TELL ANYONE!!!
selected = hub_menu("1","2", "3","4","5")

#Code Starts here!

def Sahas_Nik():
#Run 1 Code

def Mahati_Aarush():
#Run 2 Code

def Aarush_Vihaan():
    drive_base.straight(300)
    Left_arm.run_angle(500,-405)
    drive_base.straight(135)
    Left_arm.run_angle(500,405,wait=False)
    drive_base.straight(220)
    drive_base.straight(-220)
    drive_base.curve(100,13) 
    drive_base.straight(320)
    drive_base.curve(100,77)
    drive_base.curve(10,2.5)
    drive_base.straight(20)
    Right_arm.dc(100)
    Right_arm.run_angle(10000000,-3700) 
    Right_arm.run_angle(1000,20)
    drive_base.straight(-85)
    drive_base.turn(90)
    drive_base.settings(800,1000,100,200)
    drive_base.straight(1000)

def Mahati():
  #Run 4 Code
  

#Based on Selection, run the program
if selected == "1":
    Sahas_Nik()
elif selected == "2":
    Mahati_Aarush()
elif selected== "3":
    Aarush_Vihaan()
elif selected == "4":
    Mahati()
