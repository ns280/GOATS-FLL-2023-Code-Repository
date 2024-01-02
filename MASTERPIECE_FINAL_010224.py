from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase, GyroDriveBase
from pybricks.tools import wait, StopWatch
from pybricks.tools import hub_menu

#GLOBAL SETTINGS FOR GOATBOTv2 | OPTIMIZED FOR THE NEW ROBOT!!PLEASE CHECK
hub = PrimeHub()
left_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.D)
drive_base = GyroDriveBase(left_motor, right_motor, wheel_diameter=62.5, axle_track=136)
drive_base.settings(300,600,100,200)
Right_arm = Motor(Port.E, Direction.COUNTERCLOCKWISE, [24, 12, 12, 24])
Left_arm = Motor(Port.A, Direction.COUNTERCLOCKWISE, [24, 12, 12, 24])

speed = 400

#MENU FOR RUNS | Choose a letter                                                                                          Secrets Lie Here  ---->                                                                                  Hey, don't look!                                                                                 Please, I'll give you -$0.02!                                                                                             There's nothing I'm telling you!                                                                       Please, don't go any further!                                                            I'll ban you from the Earth!!!                                                   I'll call your mommy!!!                                                                      I'll call MY mommy, my daddy, my uncles and aunties, all my weird relatives if it means keeping this secret from the likes of you!!!                                                     Okay, fine...                                                                         Strawberries eat humans who disrespect pasta.                                             How did you guess that that wasn't my real secret?                                                         Eh, I guess I made it easy enough...                                                                                   No WAY I'm telling you the real secret! That's all you're getting!                                                                        OK, fine, I'll tell you the real secret...                                                                You're persistent, aren't you?                                                                        OK, I'll stop stalling...                                                                                 You're a menace to society, you know?                                                        You ready for this?????                                                                                   What do you mean, obviously?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!                                                                                Here we go...                                                                                                         Zero doesn't exist, because zero is nothing, but to speak of nothing is to speak of something.                                                                                                                               SHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DON'T TELL ANYONE!!!
selected = hub_menu("1","2", "3","4")

#Code Starts here!
def Sahas_Nik():
#Run 1 Code
    drive_base.settings(400, 900, 100, 200) 
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
    drive_base.straight(398)
    wait(100)
    drive_base.turn(-75)
    drive_base.settings(100, 800, 100, 200)

# Parllel arm down with robot moving...risky but helps with speed
#Right_arm.run_angle(170, 520, wait=False)
    drive_base.straight(100)
    Right_arm.run_angle(1000, 590)
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
    drive_base.straight(283)
#Right_arm.run_angle(400, 400)
    drive_base.settings(100, 800, 30, 200)
    drive_base.turn(-15)
    Right_arm.run_angle(380, -360)
    drive_base.turn(-22)
    drive_base.settings(200, 800, 100, 200)
    drive_base.straight(90)
    drive_base.straight(-100)

#STOP CODE HERE FOR PINK BALL
#CODE FOR ORANGE BALL
    wait(200)
    drive_base.straight(100)
    drive_base.straight(-90)
# COMPLETE COLLECT SAM STAGE MANAGER AND EXECUTE M02

# HEAD TO M03 AND EXECUTE
    drive_base.turn(100)
    drive_base.settings(300, 800, 100, 200)
    drive_base.straight(193)
    drive_base.turn(38)
    Left_arm.run_angle(1000, -1050)
    drive_base.settings(60, 800, 20, 200)
    drive_base.turn(-23)
    Left_arm.dc(75)
    Left_arm.run_angle(500, 1050, wait=False)
    wait(400)
    drive_base.straight(-70)
# COMPLETE  M03


# HEAD TO M05 AND EXECUTE
    drive_base.settings(600, 800, 200, 400)
    drive_base.turn(15)
    Left_arm.run_angle(900, -850, wait=False)
    drive_base.straight(545)
    drive_base.turn(-28)
    drive_base.straight(83)
    drive_base.settings(600, 800, 300, 400)
    drive_base.turn(80)
# COMPLETE M05

# HEAD TO M06 and M07 AND EXECUTE
    drive_base.settings(400, 600, 100, 200)
    Left_arm.run_angle(500, 950, wait=False)
    drive_base.straight(140)

#POSITIONING THE ROBOT FOR M06 and M07
    drive_base.turn(-50)
    drive_base.straight(480)
    drive_base.turn(-41)
    drive_base.settings(300, 400, 200, 400)

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
    drive_base.straight(60)
    Right_arm.run_angle(400, 90)
    drive_base.turn(15)
    drive_base.straight(-120)
    drive_base.settings(800, 900, 200, 400)
    drive_base.turn(100)
    drive_base.straight(600)
#RUN1 ENDS AND ROBOT BACK IN EAST HOMEBASE

def A_M():
    #Run 2
#Code for Bot2 Starts here!
#Updating the speed to go faster (600, 600, 200,200)
    drive_base.settings(950,950,500,400)

    drive_base.curve(100, -35)
#Reach the girl
    drive_base.straight(240)
#Pickup izzy girl No wait false. Not enough distance
    Right_arm.run_target(575, -400)
    drive_base.turn(-0.55)
#Reach Chicken gear

    drive_base.straight(114)
#drive_base.turn(1)

#Moving the chicken
#wait(5000)
    Left_arm.run_target(1000, 3000)
    drive_base.straight(15)
    
    drive_base.turn(-1.50)
#Chicken done

#Aligning to lift the latch
    drive_base.straight(-7)
    drive_base.curve(-125,12)

#Raising latch and coming back
    drive_base.straight(-57)
#unhook the latch and coming back
    drive_base.straight(10)
    drive_base.turn(22)

#move back
    drive_base.straight(-100)

#Pickup Emily 
    drive_base.turn(-220)
#Get to the homezone
    drive_base.straight(200)
#End of Run 2



def Aarush_Vihaan():
    #Drive parallel to rolling camera
    drive_base.straight(300)
    
    #Lower left arm into the pocket next to the rolling camera
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
    drive_base.straight(237)
    drive_base.turn(80)
    drive_base.straight(-80)
    drive_base.turn(60)
    
    #Drive back really fast
    drive_base.settings(800,1000,100,200)
    drive_base.straight(1100)



def Mahati_Aarush():
#Run 4 Code 

#Updating the speed to go faster (450,600,100,200)
    drive_base.settings(450,600,100,200)

#Drop off little experts and audience members #Yay
    drive_base.straight(600)
    drive_base.turn(-10)
#drive_base.straight(195)
# (Main Code Numbers) drive_base.straight(205)
    drive_base.straight(210)
    drive_base.turn(-35)
# Main Code Right_arm.run_angle(200,225)
    Right_arm.run_angle(200,225)
    wait(10)
    Right_arm.run_angle(300, -35, wait=False)
    drive_base.turn(-10) # TESTING
    drive_base.straight(-70)
    drive_base.curve(50,-53)
#Turn to avoid flower
# MAIN CODE drive_base.curve(45,-63)
    drive_base.straight(235)
    wait(10)

#drop off innovation


    drive_base.curve(336,75) # New bot 1
    Right_arm.run_angle(200,265)

#disconnect Anna the curator
    drive_base.turn(-28)

#go back
    drive_base.straight(-180)
#turn for next position
    drive_base.turn(-40)
    drive_base.straight(200)
    drive_base.curve(695,31)

#IZZY dropoff

    Right_arm.run_angle(200,206)
    drive_base.turn(-28) 

#the last expert Emily
    Right_arm.run_angle(120,340,wait=False)
    drive_base.straight(65)
#wait(10)
    drive_base.curve(220,-52)
#Detach Emily
    drive_base.curve(25,-20) 
    Left_arm.run_angle(300,540,wait=False)
    drive_base.curve(800,30) 
    #drive_base.straight(-225)
    drive_base.straight(-220)

#Sound mixer
    Left_arm.dc(100)
#Left_arm.run_angle(100,-200,wait=False)
    Left_arm.run_angle(150,-300,wait=False)
#drive_base.settings(60, 800, 100, 200)
    drive_base.settings(55, 100, 100, 200)

    drive_base.straight(-70)
    wait(1500)
    drive_base.turn(15)
    wait(100)
    drive_base.turn(20)
    drive_base.straight(20)
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
 
