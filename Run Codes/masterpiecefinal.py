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
selected = hub_menu("N","A", "V","M")

#Code Starts here!

def Sahas_Nik():
#Run 1 Code
    Left_arm = Motor(Port.A, Direction.COUNTERCLOCKWISE, [48, 12, 12, 24])
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
    Right_arm.run_angle(300, -165)
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

    Left_arm.dc(75)
    Left_arm.run_angle(350, -280, wait=False)
    wait(400)
    drive_base.straight(-70)
# COMPLETE  M02

# HEAD TO M05 AND EXECUTE
    drive_base.settings(600, 800, 200, 400)
    drive_base.turn(15)
    Left_arm.run_angle(900, 280, wait=False)
    drive_base.straight(560)
    Right_arm.run_angle(400, -20, wait=False)
    drive_base.turn(-20)
    drive_base.straight(65)
    drive_base.settings(600, 800, 300, 400)
    drive_base.turn(80)
# COMPLETE M05

# HEAD TO M06 and M07 AND EXECUTE
    drive_base.settings(400, 600, 100, 200)
    Left_arm.run_angle(500, -280, wait=False)
    drive_base.straight(140)
    drive_base.turn(-53)
    wait(10)
    drive_base.straight(480)
    drive_base.turn(-40)
    drive_base.settings(80, 200, 200, 400)
    drive_base.straight(-30)
    Left_arm.run_angle(400, 280)
    drive_base.straight(75)
    Left_arm.run_angle(400, -50)
    drive_base.turn(-25)
    drive_base.straight(-80)
    Left_arm.run_angle(400, -240)
    drive_base.turn(10)
    drive_base.straight(120)
    Right_arm.run_angle(400, 60, wait=False)
    drive_base.turn(12)
    drive_base.straight(-120)
    drive_base.turn(100)
    drive_base.settings(800, 900, 200, 400)
    drive_base.straight(600)

def Mahati_Aarush():
#Drop off little experts and audience members #Yay
    drive_base.turn(-5) 
    drive_base.straight(795)
    drive_base.turn(-45)
    Right_arm.run_angle(200,225)
    wait(10)
    Right_arm.run_angle(300, -35, wait=False)
    drive_base.straight(-70)
#Turn to avoid flower
#drive_base.turn(-57) replaced with curve
    drive_base.curve(45,-63)
    drive_base.straight(200)
wait(10)

#drop off innovation
    drive_base.curve(320,86)
    drive_base.straight(-50)
#drive_base.turn(-30)
    Right_arm.run_angle(200,240)
    drive_base.straight(-150)
    drive_base.turn(-50)
    drive_base.straight(400)
    drive_base.turn(10)
# IZZY dropoff
    Right_arm.run_angle(200,200)
    drive_base.turn(-30)
#drive_base.curve(520,60)
#the last expert
    Right_arm.run_angle(200,320,wait=False)
    drive_base.straight(120)
    drive_base.curve(350,-50)
    wait(10000)
#The End!

def Aarush_Vihaan():
    #Drive parallel to rolling camera
    drive_base.straight(300)
    Left_arm.run_angle(500,-415)
    drive_base.straight(135)
    Left_arm.run_angle(500,415,wait=False)
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

def A_M():
  #Run 4 Code
  #Code Starts here!
    drive_base.curve(100, -35)
    drive_base.straight(240)
    Right_arm.run_target(300, -400,wait=False)
    wait(300)
    drive_base.settings(150,600,100,200)
    drive_base.turn(-0.5)
    drive_base.straight(122)
    Left_arm.run_target(1000, 3000)
    drive_base.turn(-8)
    drive_base.straight(-100)
    drive_base.curve(320,12)
    drive_base.settings(300,600,100,200)
    drive_base.settings(999, 999, 999, 999)
    drive_base.straight(-150)
    drive_base.turn(-220)
    drive_base.straight(300)

#Based on Selection, run the program
if selected == "N":
    Sahas_Nik()
elif selected == "A":
    Mahati_Aarush()
elif selected== "V":
    Aarush_Vihaan()
elif selected == "M":
    A_M()
