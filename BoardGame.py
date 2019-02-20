dice=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #This list contains all thirteen usable dice, in their usable states 

t=0 #This variable will randomly generate a number, which will determine the specific die that is being used(the color of the die)  

r1=0 #In the case that the result for die 1 is "Walk", t will be stored within this variable to ensure the same die is rolled the following turn
r2=0 #In the case that the result for die 2 is "Walk", t will be stored within this variable to ensure the same die is rolled the following turn
r3=0 #In the case that the result for die 3 is "Walk", t will be stored within this variable to ensure the same die is rolled the following turn

response="y" #This variable will determine whether the user would like to continue their turn

num=0 #This variable is used to refer to the current player

brains=0 #The number of brains aquired in the round will be accumulated in this variable
walks=0 #The number of brains aquired in each turn will be accumulated in this variable
shotguns=0 #The number of shotguns aquired in the round will be accumulated in this variable

rolled=0 #This variable is responsible for determining if the turn continues (to the point that three dice have been rolled) 

result1=0 #The result generated for die 1 in each turn will be stored within this variable 
result2=0 #The result generated for die 2 in each turn will be stored within this variable 
result3=0 #The result generated for die 3 in each turn will be stored within this variable 

unusable_dice=0 #The number of dice that have been used and are no longer usable will be stored within this variable 

Round=1 #The current round is stored within this variable

player_1=0 #The total brains aquired in the game by player one, are stored within this variable
player_2=0 #The total brains aquired in the game by player two, are stored within this variable

actual_1=0 #If thirteen or more brains have been aquired by player one, the brains are stored in this variable
actual_2=0 #If thirteen or more brains have been aquired by player two, the brains are stored in this variable

print ("\t\t\t\t  ZOMBIE DICE\n\t\t\t\tEat Braaaaiins!\n\nInstructions:\"http://www.sjgames.com/dice/zombiedice/img/ZDRules_English.pdf\"\n")
print ("ZOMBIES: The Amount of Players:2 ")

print ("-----------------------------------------------------------------------------\n\t\t\t\t    ROUND", Round, ":\n-----------------------------------------------------------------------------")
while player_1!=13 and player_2!=13 or turn==turn2: #The game will continue until both player one and player two have aquired thirteen brains, or both players have had the same number of turns 
    if num==2: #To ensure the correct player of the two players is referred to, once num has equaled 2, it once again becomes 0
        num=0 
        Round=Round+1
        import time
        time.sleep(1)
        print ("-----------------------------------------------------------------------------\n\t\t\t\t    ROUND", Round, ":\n-----------------------------------------------------------------------------")

    num=num+1

    dice=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #As the player has changed (indicated in the change of the value for num), all dice are now usable
    unusable_dice=0 #As the new player's turn has begun, all dice are usable
    
    brains=0 #After the previous player has not met the condition to continue rolling, the number of brains, for the next player, now equal 0
    shotguns=0 #After the previous player has not met the condition to continue rolling, the number of shotguns, for the next player, now equal 0
    walks=0 ##After the previous player has not met the condition to continue rolling, the number walks, for the next player, now equal 0

    result1=0 #Ensures that the rolling of a "Walk" as result in the previous turn does not have an impact on the current player
    result2=0
    result3=0

    import time
    time.sleep(1)
    response=input("Are you ready to munch on some BRAINS(y/n)!")

    while response!="y": #This is simply to ensure the player is prepared to play the game
        response=input("Are you ready to munch on some BRAINS(y/n)!")

    print ("\nRolling...\n")

    while response=="y" and shotguns<3: #While both of these conditions are met, the dice are rerolled for the player in the round
    
        walks=0 #Walks do not need to be stored; their purpose is to inform the player how many dice will be rerolled 
    
        if rolled==3: #Once rolled equals 3, it is changed to 0 so that three dice are rolled for the next turn
            rolled=0
        while rolled!=3: #Three dice must be rolled for the turn, which is why dice, under this loop are generated
        
            if unusable_dice>12: #Once unusable dice are greater than 12, meaning there are not enough dice to be rolled, all dice are once again usable 
                for t in range(0,12): #Each die is gone through and made available if they had not produced a "Shotgun" or do not equal 2
                    if dice[t]!=2:
                        dice[t]=0
                        unusable_dice=unusable_dice-1 #With each die available, the number of unusable dice decreases by 1
            
            if rolled==0 and result1!="Walk": #A new die is generated only if the previous one did not result in a walk
                import random
                t=random.randrange(0,len(dice))

            elif rolled==1 and result2!="Walk":
                import random
                t=random.randrange(0,len(dice))
            
            elif rolled==2 and result3!="Walk":
                import random
                t=random.randrange(0,len(dice))
                
            else:
                if rolled==0 and result1=="Walk": #rolled is currently 0 as none of the three dice have yet been rolled
                    t=r1 #If the result for the first die equaled "Walk", t will be the same as it was in the previous round 
                elif rolled==1 and result2=="Walk":
                    t=r2 #If the result for the second die equaled "Walk", t will be the same as it was in the previous round
                elif rolled==2 and result3=="Walk":
                    t=r3 #If the result for the third die equaled "Walk", t will be the same as it was in the previous round

            rolled=rolled+1 #A die has now been rolled, which is why the number of rolled dice is updated
        
            while dice[t]==1 or dice[t]==2: #Until a usable die is generated, t is randomly generated
                t=random.randrange(len(dice))
            
            if dice[t]!=1 and dice[t]!=2: #Only if the die is usable, will there be a die being rolled and producing a result

                import random 

                #6 dice are green, 4 dice are yellow and 3 dice are red, and the color of the current dice is decided based on this probability below
                
                if t<6:
                    die="green die"
                    column="Green Die:"
                    green_die=random.randrange(6)+1
                    if green_die==1 or green_die==2 or green_die==3: #Based on probability for the specific die color, a result will be rolled
                        brains=brains+1
                        result="Brain"
                    elif green_die==4 or green_die==5:
                        walks=walks+1
                        result="Walk"
                    else:
                        shotguns=shotguns+1
                        result="Shotgun"

                elif t>=6 and t<10:
                    die="yellow die"
                    column="Yellow Die:"
                    yellow_die=random.randrange(6)+1
                    if yellow_die==1 or yellow_die==2:
                        brains=brains+1
                        result="Brain"
                    elif yellow_die==3 or yellow_die==4:
                        walks=walks+1
                        result="Walk"
                    else:
                        shotguns=shotguns+1
                        result="Shotgun"

                else:
                    die="red die"
                    column="Red Die:"
                    red_die=random.randrange(6)+1
                    if red_die>=1 or red_die<=3:
                        shotguns=shotguns+1
                        result="Shotgun"
                    elif red_die==4 or red_die==5:
                        walks=walks+1
                        result="Walk"
                    else:
                        brains=brains+1
                        result="Brain"

                if rolled==1: #Indicated that the first die is being dealt with 
                    if result=="Walk":
                        r1=t #The die will be rerolled, which is why t is stored in the variable which is further dealt in the following rolling turn  
                    elif result=="Shotgun":
                        unusable_dice=unusable_dice+1
                        dice[t]=2
                    elif result!="Walk" and result!="Shotgun":
                        unusable_dice=unusable_dice+1 #The number of unusable dice has been updated
                        dice[t]=1 #The die is declared unusable
                    #All characteristics are results of the die now belong to the first die
                    if result1=="Walk":
                        die1=die1
                        column1=column1
                    else:
                        die1=die 
                        column1=column
                    result1=result

                elif rolled==2:
                    if result=="Walk":
                        r2=t
                    elif result=="Shotgun":
                        unusable_dice=unusable_dice+1
                        dice[t]=2
                    elif result!="Walk" and result!="Shotgun":
                        unusable_dice=unusable_dice+1
                        dice[t]=1
                    #All characteristics are results of the die now belong to the second die    
                    if result2=="Walk":
                        die2=die2
                        column2=column2
                    else: 
                        die2=die
                        column2=column
                    result2=result

                elif rolled==3:
                    if result=="Walk":
                        r3=t
                    elif result=="Shotgun":
                        unusable_dice=unusable_dice+1
                        dice[t]=2
                    elif result!="Walk" and result!="Shotgun":
                        unusable_dice=unusable_dice+1
                        dice[t]=1
                    #All characteristics are results of the die now belong to the third die, unless a walk had been rolled
                    if result3=="Walk":
                        die3=die3
                        column3=column3
                    else:
                        die3=die
                        column3=column
                    result3=result
    
                    #As all dice have been rolled, the player will be notified of the color of the dice and, in the form of a chart, the results they gathered
                    import time
                    time.sleep(1)
                    print ("ZOMBIE", num, ":", "you have been presented with a", die1 + ", " + die2 , "and", die3 + ".")
                    time.sleep(2) 
                    print ("\n-----------------------------------\nDICE RESULTS\n-----------------------------------\n", column1, result1, "\n" ,column2, result2, "\n",column3,result3, "\n-----------------------------------\nZOMBIE", num, "TALLY\n-----------------------------------\nBRAINS:", brains, "\nSHOTGUNS:", shotguns, "\nWALKS:", walks, "\n-----------------------------------")

        if shotguns>=3: #More than the allowed number of shotguns have been aquired, meaning that the turn is over
            brains=0 #No brains, if the condition is met, have been collected in this turn
            time.sleep(1)
            print ("\nTURN OVER---YOU HAVE BEEN SHOT 3 OR MORE TIMES---")
            
        else:
            time.sleep(2)
            response=input("\nWould you like to roll again (y/n)?") #With less than 3 shotguns, the player has the option of continuing their turn or ending it
            if response=="y":
                print ("\nROLLING...\n")

    if num==1:#The following informations pertains to player one
        player_1=player_1+brains #All brains aquired in the round are added to the current total amount for player one 
        time.sleep(2)
        print ("\n-----------------------------------\nZOMBIE", num, "TALLY\n-----------------------------------\nBRAINS:", player_1, "\n-----------------------------------\n")
        if player_1>=13:   
            actual_1=player_1 #The number of collected brains are stored in this variable 
            player_1=13 #To make the code easier, even if more than thirteen brains are aquired, they are converted to thirteen
    else: #The following information pertains to player two
        player_2=player_2+brains #All brains aquired in the round are added to the current total amount for player two
        time.sleep(2)
        print ("\n-----------------------------------\nZOMBIE", num, "TALLY\n-----------------------------------\nBRAINS:", player_2, "\n-----------------------------------\n")    
        if player_2>=13:
            actual_2=player_2
            player_2=13
    
    if player_1>13 or player_1==13 and turn==1 and turn2==0: #This statement ensures that player two will have a turn even after player one has earned 13 or more dice
        turn=turn2
    else:
        turn=1
        turn2=0       

#The main game has been completed


if actual_2==0 or actual_1>actual_2: #If actual_2 is 0, it is indicated that player 1 obtained more than 13 brains, whereas player 2 has less than 13 brains
    time.sleep(2)
    print ("\nGAME OVER: ZOMBIE 1 has GOBBLED UP 13 or more BRAINS!")
elif actual_1==0 or actual_2>actual_1: #If actual_1 is 0, it is indicated that player 2 obtained more than 13 brains, whereas player 1 has less than 13 brains
    time.sleep(2)
    print ("\nGAME OVER: ZOMBIE 2 has GOBBLED UP 13 or more BRAINS!")
else:
    player_1=0
    player_2=0

    turn=0
    turn2=0
    
    time.sleep(1)
    print ("-----------------------------------------------------------------------------\n\t\t\t\t  TIEBREAKER :\n-----------------------------------------------------------------------------")
    while player_1==player_2 or turn!=turn2:
        if num==2: 
            num=0 
        num=num+1
        if num==1:
            turn=turn+1
        elif num==2:
            turn2=turn2+1
        
        dice=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
        unusable_dice=0 
    
        brains=0 
        shotguns=0 
        walks=0

        import time
        time.sleep(1)
        response=input("Are you ready to munch on some BRAINS(y/n)!")

        while response!="y": 
            response=input("Are you ready to munch on some BRAINS(y/n)!")

        print ("\nROLLING...\n")

        while response=="y" and shotguns<3: 
    
            walks=0 
    
            if rolled==3: 
                rolled=0
            while rolled!=3: 
        
                if unusable_dice>12: 
                    for t in range(0,12): 
                        if dice[t]!=2:
                            dice[t]=0
                            unusable_dice=unusable_dice-1 
            
                if rolled==0 and result1!="Walk": 
                    import random
                    t=random.randrange(len(dice))

                elif rolled==1 and result2!="Walk":
                    import random
                    t=random.randrange(len(dice))
            
                elif rolled==2 and result3!="Walk":
                    import random
                    t=random.randrange(len(dice))
                
                else:
                    if rolled==0 and result1=="Walk": 
                        t=r1  
                    elif rolled==1 and result2=="Walk":
                        t=r2 
                    elif rolled==2 and result3=="Walk":
                        t=r3 

                rolled=rolled+1 
    
                while dice[t]==1 or dice[t]==2: 
                    t=random.randrange(len(dice))
            
                if dice[t]!=1 and dice[t]!=2: 

                    import random 
                
                    if t<6:
                        die="green die"
                        column="Green Die:"
                        green_die=random.randrange(6)+1
                        if green_die==1 or green_die==2 or green_die==3: 
                            brains=brains+1
                            result="Brain"
                        elif green_die==4 or green_die==5:
                            walks=walks+1
                            result="Walk"
                        else:
                            shotguns=shotguns+1
                            result="Shotgun"

                    elif t>=6 and t<10:
                        die="yellow die"
                        column="Yellow Die:"
                        yellow_die=random.randrange(6)+1
                        if yellow_die==1 or yellow_die==2:
                            brains=brains+1
                            result="Brain"
                        elif yellow_die==3 or yellow_die==4:
                            walks=walks+1
                            result="Walk"
                        else:
                            shotguns=shotguns+1
                            result="Shotgun"

                    else:
                        die="red die"
                        column="Red Die:"
                        red_die=random.randrange(6)+1
                        if red_die>=1 or red_die<=3:
                            shotguns=shotguns+1
                            result="Shotgun"
                        elif red_die==4 or red_die==5:
                            walks=walks+1
                            result="Walk"
                        else:
                            brains=brains+1
                            result="Brain"

                    if rolled==1:
                        if result=="Walk":
                            r1=t 
                        elif result=="Shotgun":
                            unusable_dice=unusable_dice+1
                            dice[t]=2
                        elif result!="Walk" and result!="Shotgun":
                            unusable_dice=unusable_dice+1 
                            dice[t]=1 
                        die1=die 
                        column1=column
                        result1=result

                    elif rolled==2:
                        if result=="Walk":
                            r2=t
                        elif result=="Shotgun":
                            unusable_dice=unusable_dice+1
                            dice[t]=2
                        elif result!="Walk" and result!="Shotgun":
                            unusable_dice=unusable_dice+1
                            dice[t]=1    
                        die2=die
                        column2=column
                        result2=result

                    elif rolled==3:
                        if result=="Walk":
                            r3=t
                        elif result=="Shotgun":
                            unusable_dice=unusable_dice+1
                            dice[t]=2
                        elif result!="Walk" and result!="Shotgun":
                            unusable_dice=unusable_dice+1
                            dice[t]=1
                        die3=die
                        column3=column
                        result3=result

                        import time
                        time.sleep(1)
                        print ("ZOMBIE", num, ":", "you have been presented with a", die1 + ", " + die2 , "and", die3 + ".")
                        time.sleep(2)
                        print ("\n-----------------------------------\nDICE RESULTS\n-----------------------------------\n", column1, result1, "\n" ,column2, result2, "\n",column3,result3, "\n-----------------------------------\nZOMBIE", num, "TALLY\n-----------------------------------\nBRAINS:", brains, "\nSHOTGUNS:", shotguns, "\nWALKS:", walks, "\n-----------------------------------")

            if shotguns>=3: 
                brains=0
                time.sleep(1)
                print ("\nTURN OVER---YOU HAVE BEEN SHOT 3 OR MORE TIMES---")
            
            else:
                time.sleep(2)
                response=raw_input("\nWould you like to roll again (y/n)?") 
                if response=="y":
                    print ("\nROLLING...\n")

        if num==1:
            player_1=brains
            time.sleep(2)
            print ("\n-----------------------------------\nZOMBIE", num, "TALLY\n-----------------------------------\nBRAINS:", brains, "\n-----------------------------------\n")

        else:
            player_2=brains
            time.sleep(2)
            print ("\n-----------------------------------\nZOMBIE", num, "TALLY\n-----------------------------------\nBRAINS:", brains, "\n-----------------------------------\n")    


    if player_1>player_2:
            time.sleep(2)
            print ("ZOMBIE 1 HAS GOBBLED MORE BRAINS!")
    elif player_2>player_1:
            time.sleep(2)
            print ("ZOMBIE 2 HAS GOBBLED MORE BRAINS!")

import time #Credits are launched

time.sleep(1)
print ("\n\t\t\t\t  CREDITS:")
time.sleep(1)
print ("\n\t\t\t       Hussein Nagri")
