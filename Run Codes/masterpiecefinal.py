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
Right_armR1 = Motor(Port.E, Direction.COUNTERCLOCKWISE, [12, 24, 12, 24])
Left_armR1 = Motor(Port.A, Direction.CLOCKWISE, [12, 24, 12, 48])

speed = 400

#Choose a letter                                                                                                Secrets Lie Here  ---->                                                                                  Hey, don't look!                                                                                 Please, I'll give you -$0.02!                                                                                             There's nothing I'm telling you!                                                                       Please, don't go any further!                                                            I'll ban you from the Earth!!!                                                   I'll call your mommy!!!                                                                      I'll call MY mommy, my daddy, my uncles and aunties, all my weird relatives if it means keeping this secret from the likes of you!!!                                                     Okay, fine...                                                                         Strawberries eat humans who disrespect pasta.                                             How did you guess that that wasn't my real secret?                                                         Eh, I guess I made it easy enough...                                                                                   No WAY I'm telling you the real secret! That's all you're getting!                                                                        OK, fine, I'll tell you the real secret...                                                                You're persistent, aren't you?                                                                        OK, I'll stop stalling...                                                                                 You're a menace to society, you know?                                                        You ready for this?????                                                                                   What do you mean, obviously?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!                                                                                Here we go...                                                                                                         Zero doesn't exist, because zero is nothing, but to speak of nothing is to speak of something.                                                                                                                               SHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DON'T TELL ANYONE!!!
selected = hub_menu("1","2", "3","4")

#Code Starts here!

def Sahas_Nik():
#Run 1 Code
# CODE from start position to move Orange Stop / M08 and M09 completion 
    Right_armR1.run_angle(200, 260, wait=False)
    Left_armR1.run_angle(180, 260, wait=False)
    drive_base.straight(250)
    drive_base.straight(50)
    Right_armR1.run_angle(900, -270)
    drive_base.settings(90, 800, 100, 200)
    drive_base.straight(-115)
    drive_base.turn(-40)
    drive_base.settings(400, 800, 100, 200) 
# ORANGE STOP LIFTED(M08) and M09 COMPLETE

# START MOVING ROBOT TO EXECUTE M01
    Left_armR1.run_angle(500, -50)
    Left_armR1.run_angle(500, -210, wait=False)
    drive_base.turn(-65)
    drive_base.straight(390)
    wait(100)
    drive_base.turn(-73)
    drive_base.settings(100, 800, 100, 200)
    Right_armR1.run_angle(260, 360, wait=False)
    drive_base.straight(135)
    wait(100)
#Right_arm.run_angleR1(400, 320)
    drive_base.straight(-60)
    Right_armR1.run_angle(400, -270)
    drive_base.settings(400, 800, 100, 200)
# M01 COMPLETE

# START MOVING ROBOT TO COLLECT SAM STAGE MANAGER AND EXECUTE M02
    drive_base.straight(-70)
    drive_base.turn(85)
    Right_armR1.run_angle(200, 280, wait=False)
    drive_base.straight(290)
#Right_arm.run_angleR1(400, 400)
    drive_base.settings(100, 800, 30, 200)
    drive_base.turn(-19)
    Right_armR1.run_angle(300, -165)
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
    Left_armR1.run_angle(400, 270)
    drive_base.settings(60, 800, 20, 200)
    drive_base.turn(-22)
    Left_armR1.dc(75)
    Left_armR1.run_angle(350, -280, wait=False)
    wait(400)
    drive_base.straight(-70)
# COMPLETE  M02

# HEAD TO M05 AND EXECUTE
    drive_base.settings(600, 800, 200, 400)
    drive_base.turn(15)
    Left_armR1.run_angle(900, 280, wait=False)
    drive_base.straight(560)
    Right_armR1.run_angle(400, -20, wait=False)
    drive_base.turn(-20)
    drive_base.straight(65)
    drive_base.settings(600, 800, 300, 400)
    drive_base.turn(80)
# COMPLETE M05

# HEAD TO M06 and M07 AND EXECUTE
    drive_base.settings(400, 600, 100, 200)
    Left_armR1.run_angle(500, -280, wait=False)
    drive_base.straight(140)
    drive_base.turn(-53)
    wait(10)
    drive_base.straight(480)
    drive_base.turn(-40)
    drive_base.settings(80, 200, 200, 400)
    drive_base.straight(-30)
    Left_armR1.run_angle(400, 280)
    drive_base.straight(75)
    Left_armR1.run_angle(400, -50)
    drive_base.turn(-25)
    drive_base.straight(-80)
    Left_armR1.run_angle(400, -240)
    drive_base.turn(10)
    drive_base.straight(120)
    Right_armR1.run_angle(400, 60, wait=False)
    drive_base.turn(12)
    drive_base.straight(-120)
    drive_base.turn(100)
    drive_base.settings(800, 900, 200, 400)
    drive_base.straight(600)
# END OF RUN1

def A_M():
  #Run 2 Code
  #Code for Bot2 Starts here!
    drive_base.curve(100, -35)
#Reach the girl
    drive_base.straight(240)
#Pickup izzy girl No wait false. Not enough distance
    Right_arm.run_target(575, -400)
    drive_base.turn(-0.5)
#Reach Chicken gear
    drive_base.straight(124)
#Moving the chicken
    Left_arm.run_target(1000, 3000)
#Chicken done

#Aligning to lift the latch
    drive_base.straight(-7)
    drive_base.curve(-125,12)

#Raising latch and coming back
    drive_base.straight(-57)
#unhook the latch and coming back
    drive_base.straight(10)
    drive_base.turn(18)

#move back
    drive_base.straight(-100)

#Updating the speed to go faster (600, 600, 200,200)
    drive_base.settings(600,600,200,200)

#Pickup Emily 
    drive_base.turn(-220)
#Get to the homezone
    drive_base.straight(300)
#End of Run 2



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

def Mahati_Aarush():
#Run 4 Code 
#Drop off little experts and audience members #Yay

    drive_base.straight(600)
    drive_base.turn(-10)
    drive_base.straight(195)

    drive_base.turn(-35)
    Right_arm.run_angle(200,225)
    wait(10)
    Right_arm.run_angle(300, -35, wait=False)
    drive_base.straight(-70)
#Turn to avoid flower

    drive_base.curve(45,-63)
    drive_base.straight(200)
    wait(10)

#drop off innovation
    drive_base.curve(330,80)

    Right_arm.run_angle(200,240)
#disconnect curator
    drive_base.turn(-25)

#go back
    drive_base.straight(-180)
#turn for next position
    drive_base.turn(-40)
    drive_base.straight(200)
    drive_base.curve(700,25)

#IZZY dropoff
    Right_arm.run_angle(200,200)
    drive_base.turn(-30)
#drive_base.curve(520,60)
#the last expert Emily
    Right_arm.run_angle(200,340,wait=False)
    drive_base.straight(120)
    drive_base.curve(190,-60)
    wait(10000)
#The End!

#Based on Selection, run the program
if selected == "1":
    Sahas_Nik()
elif selected == "2":
    A_M()
elif selected== "3":
    Aarush_Vihaan()
elif selected == "4":
    Mahati_Aarush()
