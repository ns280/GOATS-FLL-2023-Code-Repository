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
