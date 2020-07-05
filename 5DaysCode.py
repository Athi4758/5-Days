import sys,time,os

def ending():
    os.system("cls")
    print("Invalid choice! You should've answered an option, now there is no one to save our world. YOU LOST!\nTo play our game again, restart the program.")
    message = """     ___    _____         ___    _____  _   _  ___    ___   
    (  _`\ (  _  )/'\_/`\(  _`\ (  _  )( ) ( )(  _`\ |  _`\ 
    | ( (_)| (_) ||     || (_(_)| ( ) || | | || (_(_)| (_) )
    | |___ |  _  || (_) ||  _)_ | | | || | | ||  _)_ | ,  / 
    | (_, )| | | || | | || (_( )| (_) || \_/ || (_( )| |\ \ 
    (____/'(_) (_)(_) (_)(____/'(_____)`\___/'(____/'(_) (_)"""
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0009)
def typewriter():
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char == ".":
            time.sleep(0.1)
        elif char == ",":
            time.sleep(0.1)
        elif char == "?":
            time.sleep(0.1)
        elif char == "!":
            time.sleep(0.1)
        elif char == ":":
            time.sleep(0.1)
        else:
            time.sleep(SLEEP)

def breakfast():
    print("----------------------------------------------------------------------------")
    print("                                 ;)(;")
    print("                                :----:     o8Oo.")
    print("                               C|====| ._o8o8o8Oo_.")
    print("                                |    |  \\========/")
    print("                                `----'    `------'")
    print("----------------------------------------------------------------------------")
def car():
    print("----------------------------------------------------------------------------")
    print("                        ____________________\ ")
    print("                     //|           |        \\\ ")
    print("                   //  |           |          \\\ ")
    print("      ___________//____|___________|__________()\\__________________\ ")
    print("    /__________________|_=_________|_=___________|_________________\{\}\ ")
    print("    [           ______ |           | .           | ==  ______      \{ \}\ ")
    print("  __[__        /##  ##\\|           |             |    /##  ##\\    _\{# \}_\ ")
    print(" \{_____)______|##    ##|___________|_____________|___|##    ##|__(______\}\ ")
    print("             /  ##__##                              /  ##__##        \\\ ")
    print("----------------------------------------------------------------------------")
def bar():
    print("----------------------------------------------------------------------------")
    print("                           _\ ")
    print("                         \{_\}\ ")
    print("                         |(|\ ")
    print("                         |=|\ ")
    print("                        /   \\\ ")
    print("                        |.--|\ ")
    print("                        ||  |\ ")
    print("                        ||  |    .    ' .\ ")
    print("                        |'--|  '     \\~~~/\ ")
    print("                        '-=-' \\~~~/   \\_/\ ")
    print("                               \\_/     Y\ ")
    print("                                Y     _|_\ ")
    print("                               _|_\ ")
    print("----------------------------------------------------------------------------")
def cooking_bowl():
    print("----------------------------------------------------------------------------")
    print("                 (\\\ ")
    print("                \\ \\\ ")
    print("           __    \\/ ___,.-------..__        __\ ")
    print("          //\\\\ _,-'\\\\               `'--._ //\\\\\ ")
    print("          \\\\ ;'     \\\\                   `: //\ ")
    print("         `(          \\\\                   )'\ ")
    print("          :.          \\\\,----,         ,;\ ")
    print("            `.`--.___   (    /  ___.--','\ ")
    print("              `.     ``-----'-''     ,'\ ")
    print("                 -.               ,-\ ")
    print("                    `-._______.-'\ ")
    print("----------------------------------------------------------------------------")
def bed():
    print("----------------------------------------------------------------------------")
    print("   ()___ ")
    print(" ()//__/)_________________()")
    print(" ||(___)//#/_/#/_/#/_/#()/||")
    print(" ||----|#| |#|_|#|_|#|_|| ||")
    print(" ||____|_|#|_|#|_|#|_|#||/||")
    print(" ||    |#|_|#|_|#|_|#|_||")
    print("----------------------------------------------------------------------------")
def library():
    print("----------------------------------------------------------------------------")
    print("                      .--.                   .---.")
    print("                  .---|__|           .-.     |~~~|")
    print("               .--|===|--|_          |_|     |~~~|--.")
    print("               |  |===|  |'\     .---!~|  .--|   |--|")
    print("               |%%|   |  |.'\    |===| |--|%%|   |  |")
    print("               |%%|   |  |\.'\   |   | |__|  |   |  |")
    print("               |  |   |  | \  \  |===| |==|  |   |  |")
    print("               |  |   |__|  \.'\ |   |_|__|  |~~~|__|")
    print("               |  |===|--|   \.'\|===|~|--|%%|~~~|--|")
    print("               ^--^---'--^    `-'`---^-^--^--^---'--'")
    print("----------------------------------------------------------------------------")
def cleaning():
    print("----------------------------------------------------------------------------")
    print("   || ")
    print("   || ")
    print("   || ")
    print("   || ")
    print("   || ")
    print("   || ")
    print("   || ")
    print("  /||\ ")
    print(" /||||\ ")
    print(" ======   __|__ ")
    print(" ||||||  / ~@~ \ ")
    print(" |||||| |-------| ")
    print(" |||||| |_______| ")
    print("----------------------------------------------------------------------------")
def bus():
    print("----------------------------------------------------------------------------")
    print("                          __")
    print(" .-----------------------'  |")
    print("/| _ .---. .---. .---. .---.|")
    print("|j||||___| |___| |___| |___||")
    print("|=|||=======================|")
    print("[_|j||(O)\__________|(O)\___]")
    print("----------------------------------------------------------------------------")
def cake():
    print("----------------------------------------------------------------------------")
    print("              (        (")
    print("             ( )      ( )          (")
    print("      (       Y        Y          ( )")
    print("     ( )     |'|      |'|          Y")
    print("      Y      | |      | |         |'| ")
    print("     |'|     | |.-----| |---.___  | | ")
    print("     | |  .--| |,~~~~~| |~~~,,,,'-| | ")
    print("     | |-,,~~'-'___   '-'       ~~| |._ ")
    print("    .| |~       // ___            '-',,'. ")
    print("   /,'-'     <_// // _  __             ~,\ ")
    print("  / ;     ,-,     \\_> <<_______________;_) ")
    print("  | ;    {(_)} _,      . |================| ")
    print("  | '-._ ~~,,,           | ,,             | ")
    print("  |     '-.__ ~~~~~~~~~~~|________________|  ")
    print("  |\         `'----------| ")
    print("  | '=._                 | ")
    print("  :     '=.__            | ")
    print("   \         `'==========| ")
    print("    '-._                 | ")
    print("        '-.__            | ")
    print("             `'----------| ")
    print("----------------------------------------------------------------------------")
def laptop():
    print("----------------------------------------------------------------------------")
    print(" ______________")
    print("||            || ")
    print("||            || ")
    print("||            || ")
    print("||            || ")
    print("||____________|| ")
    print("|______________| ")
    print(" \\############\\ ")
    print("  \\############\\ ")
    print("   \      ____    \   ")
    print("    \_____\___\____\ ")
    print("----------------------------------------------------------------------------")
def shirt():
    print("----------------------------------------------------------------------------")
    print("  __   __  ")
    print(" /  `-'  \ ")
    print("/_| Can |_\ ")
    print("  | Hack|   ")
    print("  |Bramp|  ")
    print("  |_____| ")
    print("----------------------------------------------------------------------------")




SLEEP = (0.00007)
SLEEP_AFTER_ASCII = (2)

os.system("cls")
message = "Welcome! Today you will play a game called 5 days. Over the course of the next 5 days,\nyou will make a series of small choices regarding everyday events.\nWhat you may not notice, however, is that these small choices can lead to drastic events...\nThroughout the next 5 days, we will see how the actions you choose to take affect the world as a\nwhole, and we'll see whether you have what it takes to save the world... or destroy it.\n"
typewriter()
answer = input("Press [x] to read the instructions\n")
if answer == "x":
    os.system("cls")
    answer = input("1. Make sure that you type the exact letter for the choice you would like to choose - check capitalization and extra spaces!\n2. Just as any small mistakes can cause big harm to the environment, small mis-clicks or spelling errors will result in immediate loss of the game! Be careful!\n3. Press the enter key after typing in your selection.\n4. Have fun and feel free to play more than once. There are many different paths to follow in this game!\nPress [x] to start the game now!\n")
    if answer == "x":
        os.system("cls")
        message = "STARTO!"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
        os.system("cls")
        name = input("Please enter your name: ")
        answer = input("Nice to meet you " + name + "!\nPress [x] to continue!\n")
        if answer == "x":
            os.system("cls")
            message = "You wake up to the sounds of birds chirping outside your window and leaves blowing in the wind. However, what grabs your attention the most is the sound of your alarm blaring through your skull.\n"
            typewriter()
            answer = input("Press [x] to turn off your alarm.\n")
            if answer == ("x"):
                os.system("cls")
                message = "You slowly roll out of bed and check the time on your phone.\n30 minutes till work.\nIs that really enough time to get ready and head to work?\nNot really.\nSo you sprint to the bathroom and grab your toothbrush.\nWhile brushing your teeth, you pull your work clothes from the closet and begin to put them on.\nYou don't have time to shower right now, you'll do it tonight.\nAs you rinse your mouth, you realize that your toothbrush is absolutely destroyed and should have been replaced weeks ago.\nYou toss it in the bin and head downstairs, where your girlfriend is making you breakfast; scrambled eggs and toast with jam.\n"
                typewriter()
                breakfast()
                time.sleep(SLEEP_AFTER_ASCII)
                answer = input("Press [x] to continue the story.\n")
                if answer == ("x"):
                    os.system("cls")
                    message = "As she set plates on the table, you zoom past her towards the door, grabbing a granola bar off the table.\nGirlfriend: What about breakfast?!\n" + name + ": Sorry! Late for work!\n"
                    typewriter()
                    answer = input("Press [x] to continue the story.\n")
                    if answer == "x":
                        os.system("cls")
                        message = "You head outside, eyes darting between your car, which may or may not break down any day now, and the bus stop across the street.\nWhich method of transportation do you choose?\n"
                        typewriter()
                        answer = input("[x] car\n[c] bus\n")
                        if answer == "x":
                            os.system("cls")
                            car()
                            time.sleep(SLEEP_AFTER_ASCII)
                            message = "As you drive to work, you think about this morning's events.\nThough your mind is filled primarily with the thought of being late for work, a small part of you feels guilty for not eating breakfast with your girlfriend this morning.\nIt wasn't the first time you've done this, and if you keep it up, it definitely won't be the last.\nShe has been seeming pretty closed off lately...\n"
                            typewriter()
                            answer = input("Press [x] to continue the story.\n")
                            if answer == "x":
                                os.system("cls")
                                message = "You stop at a red-light and snack on your granola bar.\nThe light turns to green.\nYou press on the pedal, but the car doesn't move forward.\n"
                                typewriter()
                                message = ".\n.\n.\n"
                                for char in message:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(1)
                                message = "Great. It broke down. In the distance however, you see a bus stop.\n"
                                typewriter()
                                answer = input("Press [x] to take the bus for the remaining distance to work.\n")
                                if answer == "x":
                                    os.system("cls")
                                    message = "Boss: " + name + ", again?\n" + name + ": I'm really sorry, it's just that my car broke down and-\nBoss: I'm sorry, but I'm done with all of your excuses. It seems that your heart and mind are not in the right place here at our company. I'm truly sorry, but I believe I'm going to have to let you go.\n" + name + ": What?\nBoss: Today will be your last day. Thank you for the work you have done here, and I wish you the best moving forward.\n.\n.\n.\nOops. It seems you have been fired.\n"
                                    typewriter()
                                    answer = input("Press [x] to continue the story.\n")
                                    if answer == "x":
                                        os.system("cls")
                                        message = "You exit the building, filled with shock, anger and resentment.\nBut deep down, you understand that maybe you could have been a better employee.\nNow that you have the rest of the day off, it is up to you to decide: should you return home, to your already disappointed girlfriend, or spend the day out?\n"
                                        typewriter()
                                        answer = input("[x] Spend the day out\n[c] Return home\n")
                                        if answer == "x":
                                            os.system("cls")
                                            message = "After wandering around aimlessly throughout the day, you stumble upon a bar.\n"
                                            typewriter()
                                            answer = input("Press [x] to enter the bar.\n")
                                            if answer == "x":
                                                os.system("cls")
                                                bar()
                                                time.sleep(SLEEP_AFTER_ASCII)
                                                message = "You enter the bar and take a seat. Using money from your now nonexistent income, you decide to order a drink.\nBut one drink turns to two.\nThen three\nThen four\n.\n.\n.\nYou then decide that you would like to go home.\n"
                                                typewriter()
                                                answer = input("Press [x] to go home and fall asleep.\n")
                                                if answer == "x":
                                                    os.system("cls")
                                                    message = "You wake up; head pounding, stomach hurting.\nThe house is silent.\nWhat happened last night?\nYou head downstairs. The house feels different. It feels... empty. As if you fell asleep on a tree, but woke up on the floor.\nA piece of paper is on the counter.\n"
                                                    typewriter()
                                                    answer = input("Press [x] to open the paper\n")
                                                    if answer == "x":
                                                        os.system("cls")
                                                        message = "'Dear " + name + ", I'm sorry, but it has been tough lately.\nI'll always have a special place in my heart for you. At times, our relationship felt like it was the best thing that had ever happened to me, but lately everything has felt wrong.\nThrough your habits and your actions I feel hurt, ignored, and disappointed. It pains me to admit this, but my love for you has faded away.\nI can't stay in a relationship where there is no love, and it isn't fair to you to be stuck in a relationship that's a lie. I hope that you're able to move on, and meet someone who will love you the way you deserve to be loved.\nSincerely,\nGirlfriend\n.\n.\n.\nUh oh, it seems like your girlfriend broke up with you.'\n"
                                                        typewriter()
                                                        answer = input("Press [x] to put down the letter.\n")
                                                        if answer == "x":
                                                            os.system("cls")
                                                            message = "It's not like you didn't expect this to happen. But look at you now. You're jobless and relationshipless. With no energy to go on, you decide to go back to sleep.\n"
                                                            typewriter()
                                                            answer = input("Press [x] to go back to bed.\n")
                                                            if answer == "x":
                                                                os.system("cls")
                                                                message = "You wake up after a few hours, realizing that you don't really know how to cook or make much food for yourself since you relied on your girlfriend to do so much for you.\nThankfully, however, there is a flyer for cooking class on the counter.\n'Environmentally Sustainable Cooking! Learn how to cook for yourself, while making sure that nature can feed itself too!'\nDo you attend the cooking class?\n"
                                                                typewriter()
                                                                answer = input("[x] Yes\n[c] No\n")
                                                                if answer == "x":
                                                                    os.system("cls")
                                                                    cooking_bowl()
                                                                    time.sleep(SLEEP_AFTER_ASCII)
                                                                    message = "You attend the class. It's your first day. And even though it's just your first day, you already feel like you've learned so much.\nYou learned about the environmental effects that come from the food that you eat.\nWho would have known that meat, especially beef, plays one of the biggest roles in climate change?\nWith a good first experience, you make it a point to attend the weekly classes from now on.\n"
                                                                    typewriter()
                                                                    answer = input("Press [x] to return from the class.\n")
                                                                    if answer == "x":
                                                                        os.system("cls")
                                                                        message = "You return home, and find yourself cooking one of the meals you learned today. You feel proud, making it a point to use all reusable cutlery, cooking tools and plates.\n"
                                                                        typewriter()
                                                                        answer = input("Press [x] to eat your dinner.\n")
                                                                        if answer == "x":
                                                                            os.system("cls")
                                                                            message = "After dinner, you put your new knowledge to use, and use less water when washing the dishes, and you decide to throw out all the plastic kitchenware while you're at it.\nCompared to yesterday, you feel a little happier.\nThis whole eco-friendly stuff is starting to grow on you.\n"
                                                                            typewriter()
                                                                            answer = input("Press [x] to go to bed.\n")
                                                                            if answer == "x":
                                                                                os.system("cls")
                                                                                message = "BEEP! BEEP! BEEP!\nYour alarm rings. You wake up surprised; after all, you thought you turned it off. You check your phone, only to realize that this isn't any ordinary alarm. It's a reminder to buy a car!\nAll the saving up over the past few months has finally made its purpose.\n"
                                                                                typewriter()
                                                                                answer = input("Press [x] to visit the car dealership.\n")
                                                                                if answer == "x":
                                                                                    os.system("cls")
                                                                                    car()
                                                                                    time.sleep(SLEEP_AFTER_ASCII)
                                                                                    message = "You visit the car dealership, ready to wait long hours, bargain, and haggle with the dealers. You're choosing between two cars; both on sale, since you want to save money (it's not like you have a job anymore anyways).\nThe first car is an electric car. A few days ago, you would have definitely picked the second option.\nBut today, with your newfound knowledge about environmental sustainability, you understand that an electric car like this one is much more environmentally friendly, and you wouldn't mind picking driving this one in the future.\nThe second car is an old model, but one that you've had your eyes on for quite some time. It may not be the hottest car on the market, but it holds a lot of sentimental value.\nHowever, it does use a lot of fossil fuels and releases lots of pollution into the atmosphere.\nWhich car do you choose?\n"
                                                                                    typewriter()
                                                                                    answer = input("[x] Electric Car\n[c] Old Car\n")
                                                                                    if answer == "x":
                                                                                        os.system("cls")
                                                                                        message = "Dealer: Great! Thank you " + name + ". We appreciate your choice of using our dealership to purchase your vehicle. Here's a free oil change and car wash on the house!\n" + name + ": Thanks!\nExcited, you call your friend Barton and decide to meet up with them at the park.\n"
                                                                                        typewriter()
                                                                                        answer = input("Press [x] to drive to the park.\n")
                                                                                        if answer == "x":
                                                                                            os.system("cls")
                                                                                            message = "You decide to take a stroll while you wait for Barton to arrive, but you unexpectedly see him doing the same thing.\nThe two of you sit down at a bench and you begin to tell him about your new cooking class hobby.\nBarton: No but really, all this eco-friendly stuff, it's just a bunch of nonsense isn't it? You know I believe in the philosophy of having a good time, not a long time, you know?\nSurprisingly you feel a little shocked and surprised by Bartons comments.\nYou know that had you not taken this cooking class, you would have reacted the same way.\nAfter all, the reason why people don't make environmentally friendly choices nowadays is because they just don't know where to begin.\nSo you understand where Barton is coming from. But you also understand that the only way to make change, is to educate.\nBut, at the same time, with your girlfriend and boss being gone, you are scared of losing your last friend due to something small like differing opinions.\n"
                                                                                            typewriter()
                                                                                            answer = input("Do you...\n[x] Educate Barton on the importance of being Environmentally sustainable.\n[c] Agree with Barton to save yourself the risk of losing a friend.\n")
                                                                                            if answer == "x":
                                                                                                os.system("cls")
                                                                                                message = "You educate Barton. He seems to understand, and even seems motivated to embark on his journey of environmental sustainability.\n"
                                                                                                typewriter()
                                                                                                answer = input("Press [x] to return home.\n")
                                                                                                if answer == "x":
                                                                                                    os.system("cls")
                                                                                                    message = "With your 5 long days coming to an end, you decide to fall asleep.\n"
                                                                                                    typewriter()
                                                                                                    answer = input("Press [x] to end the game.\n")
                                                                                                    if answer == "x":
                                                                                                        os.system("cls")
                                                                                                        message = ".\n.\n.\nEvery time we are encouraged to make a change, we always think to ourselves: what good does it make if only one person changes?\nWhat we don't realize, however, is that if everyone took it upon themselves to make a change, good change would happen.\nSurprise " + name + "!\nIn this game, not only were you representing yourself, but you were representing the entire world.\nBecause if everyone takes it upon themselves to make a good decision, imagine how much better the world would be.\nAnd it is much better, because of you.\nThis game may not have seemed like it was made to educate others on Environmental Sustainability, but what it really shows us is that the difference between a sustainable world and the one we live in now,\nlies in the small everyday decisions we make throughout our lives, like recycling, not using plastic, and reducing our individual pollution levels.\nAnd I think it's safe to say that you, " + name + ", have made some pretty good decisions these past 5 days.\nAnd you know what that means.\nIf you made some pretty good decisions, then that means the ENTIRE WORLD made some pretty good decisions.\nCongratulations " + name + "! Thanks to you and your environmentally sustainable decision making thought process, you put the world on a path to environmental sustainability.\nYou have won the game!\nThank you for playing, and we wish you the best on your journey to saving the world!\nTHE END!\n"
                                                                                                        typewriter()
                                                                                                        
                    
                                                                                                    else:
                                                                                                        ending()
                                                                                                else:
                                                                                                    ending()




                                                                                              
                                                                                            elif answer == "c":
                                                                                                os.system("cls")
                                                                                                message = "You agree with Barton. The conversation slowly gets more and more empty and awkward until the two of you decide to head home.\n"
                                                                                                typewriter()
                                                                                                answer = input("Press [x] to return home.\n")
                                                                                                if answer == "x":
                                                                                                    os.system("cls")
                                                                                                    message = "With your 5 long days coming to an end, you decide to fall asleep.\n"
                                                                                                    typewriter()
                                                                                                    answer = input("Press [x] to end the game.\n")
                                                                                                    if answer == "x":
                                                                                                        os.system("cls")
                                                                                                        message = ".\n.\n.\nEvery time we are encouraged to make a change, we always think to ourselves: what good does it make if only one person changes?\nWhat we don't realize, however, is that if everyone took it upon themselves to make a change, good change would happen.\nSurprise " + name + "!\nIn this game, not only were you representing yourself, but you were representing the entire world.\nBut the problem is, you didn't really make good change.\nSure, you made some really good environmental decisions, but like we mentioned earlier.\nThat's right. Remember your conversation with Barton?\n'the reason why people don't make environmentally friendly choices nowadays is because they just don't know where to begin.'\nYou see, what you did," + name + ", was you hid your knowledge about saving the planed from others, like Barton. And if no one ever shared any of this eco-friendly knowledge with you, would you have ever known that your everyday choices were destroying the planet?\nExactly.\nI'm sorry " + name + ", but you lost the game.\nIf you don't do your duty as a citizen of the Earth to make others aware of how they must protect the planet, you're letting the world continue exactly the world is today.\nAnd as you know, it's not really heading on a path of recovery.\nThank you for playing, and we wish you the best on your journey to saving the world.\nTHE END!\n"
                                                                                                        typewriter()
                                                                                                       
                                                                                                    else:
                                                                                                        ending()
                                                                                                else:
                                                                                                    ending()




                                                                                            else:
                                                                                                ending()
                                                                                        else:
                                                                                            ending()






#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------electric or old car?
                                                                                    elif answer == "c":
                                                                                        os.system("cls")
                                                                                        message = "Dealer: Great! Thank you " + name + ". We appreciate your choice of using our dealership to purchase your vehicle. Here's a free oil change and car wash on the house!\n" + name + ": Thanks!\nExcited, you call your friend Barton and decide to meet up with them at the park.\n"
                                                                                        typewriter()
                                                                                        answer = input("Press [x] to drive to the park.\n")
                                                                                        if answer == "x":
                                                                                            os.system("cls")
                                                                                            message = "You decide to take a stroll while you wait for Barton to arrive, but you unexpectedly see him doing the same thing.\nThe two of you sit down at a bench and you begin to tell him about your new cooking class hobby.\nBarton: No but really, all this eco-friendly stuff, it's just a bunch of nonsense isn't it? You know I believe in the philosophy of having a good time, not a long time, you know?\nSurprisingly you feel a little shocked and surprised by Bartons comments.\nYou know that had you not taken this cooking class, you would have reacted the same way.\nAfter all, the reason why people don't make environmentally friendly choices nowadays is because they just don't know where to begin.\nSo you understand where Barton is coming from. But you also understand that the only way to make change, is to educate.\nBut, at the same time, with your girlfriend and boss being gone, you are scared of losing your last friend due to something small like differing opinions.\n"
                                                                                            typewriter()
                                                                                            answer = input("Do you...\n[x] Educate Barton on the importance of being Environmentally sustainable.\n[c] Agree with Barton to save yourself the risk of losing a friend.\n")
                                                                                            if answer == "x":
                                                                                                os.system("cls")
                                                                                                message = "You educate Barton. He seems to understand, and even seems motivated to embark on his journey of environmental sustainability.\n"
                                                                                                typewriter()
                                                                                                answer = input("Press [x] to return home.\n")
                                                                                                if answer == "x":
                                                                                                    os.system("cls")
                                                                                                    message = "With your 5 long days coming to an end, you decide to fall asleep.\n"
                                                                                                    typewriter()
                                                                                                    answer = input("Press [x] to end the game.\n")
                                                                                                    if answer == "x":
                                                                                                        os.system("cls")
                                                                                                        message = ".\n.\n.\nEvery time we are encouraged to make a change, we always think to ourselves: what good does it make if only one person changes?\nWhat we don't realize, however, is that if everyone took it upon themselves to make a change, good change would happen.\nSurprise " + name + "!\nIn this game, not only were you representing yourself, but you were representing the entire world.\nBut the problem is, you didn't really make good change.\nSure, you made some environmentally conscious decisions, but, like we mentioned earlier, if everyone took it upon themselves to make a big change, big change would happen.\nThe only problem is, if everyone made the decisions you did, our world wouldn't really be heading on a path to recovery.\nIt would stay the way it is today in the real world and I'm not really sure that's a good thing.\nSure, you may have educated your friend on environmentalism, but it seems that you yourself have not made enough decisions to follow an eco-friendly lifestyle.\nSo I'm sorry " + name + ", but you lost the game.\nThank you for playing, and we wish you the best on your journey to save the world.\nTHE END!\n"
                                                                                                        typewriter()
                                                                                                        
                                                                                                    else:
                                                                                                        ending()
                                                                                            elif answer == "c":
                                                                                                os.system("cls")
                                                                                                message = "You agree with Barton. The conversation slowly gets more and more empty and awkward until the two of you decide to head home.\n"
                                                                                                typewriter()
                                                                                                answer = input("Press [x] to return home.\n")
                                                                                                if answer == "x":
                                                                                                    os.system("cls")
                                                                                                    message = "With your 5 long days coming to an end, you decide to fall asleep.\n"
                                                                                                    typewriter()
                                                                                                    answer = input("Press [x] to end the game.\n")
                                                                                                    if answer == "x":
                                                                                                        os.system("cls")
                                                                                                        message = ".\n.\n.\nEvery time we are encouraged to make a change, we always think to ourselves: what good does it make if only one person changes?\nWhat we don't realize, however, is that if everyone took it upon themselves to make a change, good change would happen.\nSurprise " + name + "!\nIn this game, not only were you representing yourself, but you were representing the entire world.\nBut the problem is, you didn't really make a good change. The decisions you made weren't entirely eco-friendly and like we mentioned earlier,\n'the reason why people don't make environmentally friendly choices nowadays is because they just don't know where to begin.'\nYou see, what you did " + name + ", was you hid your knowledge about saving this planet from others, like Barton.\nAnd if no one ever shared any of this eco-friendly knowledge with you, would you have ever known that your everyday choices were destroying the planet?\nExactly.\nI'm sorry " + name + ", but you lost the game. Your decisions, when placed on a global scale, led the world down an unsettling path of environmental deterioration and destruction\nThank you for playing, and we wish you the best on your journey to save the world.\nTHE END!\n"
                                                                                                        typewriter()
                                                                                                        
                                                                                                    else:
                                                                                                        ending()
                                                                                                else:
                                                                                                    ending()        
                                                                                            else:
                                                                                                ending()               











                                                                                    else:
                                                                                        ending()
                                                                                
                                                                                else:
                                                                                    ending()
                                                                            else:
                                                                                ending()
                                                                        else:
                                                                            ending()
                                                                    else:
                                                                        ending()





#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------cooking class or nah?
                                                                elif answer == "c":
                                                                    os.system("cls")
                                                                    message = "You sit down at the table, tossing the flyer into the recycling bin.\nIt can be recycled, right? That's allowed?\nYou're starting to think that you should have taken that eco-friendly cooking class, for maybe it would have taught you more about recycling.\nWith no appetizing meals in the house, you think about heading out once again to party the night away.\nAfter all, it's not like you have anyone monitoring you.\nDo you party?\n"
                                                                    typewriter()
                                                                    answer = input("[x] Yes\n[c] No\n")
                                                                    if answer == "x":
                                                                        os.system("cls")
                                                                        bar()
                                                                        time.sleep(SLEEP_AFTER_ASCII)
                                                                        message = "You party the night away, eating multiple steaks, having one too many glasses of beer, and you eventually find yourself walking home with 3 empty bottles of soju in a paper bag.\nYou could throw the entire contraption in the trashcan right next to you, or you could walk about 50 metres to the recycling can.\nDo you...\n"
                                                                        typewriter()
                                                                        answer = input("[x] Recycle\n[c] Toss it in the trash\n")
                                                                        if answer == "x":
                                                                            os.system("cls")
                                                                            message = "As you reach the recycling bin, a poster catches your attention and moves you to tears.\nYou learn about the environmental effects of using non-recyclable products, and the extinction of wildlife and plantlife that has resulted because of such.\nYou feel proud to be recycling your bottles and bags right now.\nBut you also feel tired.\nIt has been a long 5 days.\n"
                                                                            typewriter()
                                                                            answer = input("Press [x] to return home and go to bed.\n")
                                                                            if answer == "x":
                                                                                os.system("cls")
                                                                                answer = input("Press [x] to end the game.\n")
                                                                                if answer == "x":
                                                                                    os.system("cls")
                                                                                    message = ".\n.\n.\nEvery time we are encouraged to make a change, we always think to ourselves: what good does it make if only one person changes?\nWhat we don't realize, however, is that if everyone took it upon themselves to make a change, good change would happen.\nSurprise " + name + "!\nIn this game, not only were you representing yourself, but you were representing the entire world.\nBut the problem is, you didn't really take good actions.\nMany of the decisions you made weren't entirely eco-friendly.\nAnd though this may not seem like an issue if one person acts this way, think again.\nIf everyone thought of themselves as one person making poor decisions, where would the world be today?\nI'm sorry " + name + ", but you lost the game.\nYour decisions, when placed on a global scale, lead the world down an unsettling path of environmental deterioration and destruction.\nThank you for playing, and we wish you the best on your journey to save the world.\nTHE END!\n"
                                                                                    typewriter()
                                                                                    
                                                                                else:
                                                                                    ending()
                                                                            else:
                                                                                ending()




#-------------------------------------------------------------------------------------------------------------------------------------------------------throw beer in recycle or trash?
                                                                        elif answer == "c":
                                                                            os.system("cls")
                                                                            message = "You drunkenly try to toss the bottles into the bin, only to miss and have them shatter on the floor.\nHaphazardly, you attempt to pick up some of the shards and toss them in, leaving most of the remains on the ground, and leaving you with bloody fingers.\nIt has been a long day. A long 5 days.\n"
                                                                            typewriter()
                                                                            answer = input("Press [x] to return home and go to bed\n")
                                                                            if answer == "x":
                                                                                os.system("cls")
                                                                                answer = input("Press [x] to end the game.\n")
                                                                                if answer == "x":
                                                                                    os.system("cls")
                                                                                    message = ".\n.\n.\nEvery time we are encouraged to make a change, we always think to ourselves: what good does it make if only one person changes?\nWhat we don't realize, however, is that if everyone took it upon themselves to make a change, good change would happen.\nSurprise " + name + "!\nIn this game, not only were you representing yourself, but you were representing the entire world.\nBut the problem is, you didn't really take good actions.\nMany of the decisions you made weren't entirely eco-friendly.\nAnd though this may not seem like an issue if one person acts this way, think again.\nIf everyone thought of themselves as one person making poor decisions, where would the world be today?\nI'm sorry " + name + ", but you lost the game.\nYour decisions, when placed on a global scale, lead the world down an unsettling path of environmental deterioration and destruction.\nThank you for playing, and we wish you the best on your journey to save the world.\nTHE END!\n"
                                                                                    typewriter()
                                                                                    
                                                                                else:
                                                                                    ending()
                                                                            else:
                                                                                ending()
                                                                            




                                                                        else:
                                                                            ending()
                                                            

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------party or nah?
                                                                    elif answer == "c":
                                                                        os.system("cls")
                                                                        message = "Hungry, you grab 3 granola bars off the counter and shove them into your mouth, one by one.\nWith no real purpose for the upcoming days, you make the sudden declaration that you will clean your room!\n"
                                                                        typewriter()
                                                                        answer = input("Press [x] to clean your room.\n")
                                                                        if answer == "x":
                                                                            os.system("cls")
                                                                            message = "It's 2AM and you have managed to clean the entire house.\nHas sorting the house helped you sort through your heavy, weighted emotions?\nNot really.\nAdding on, you are now left with a pile of trash, remains, and all things considered, items that need to be disposed of.\nDo you...\n"
                                                                            typewriter()
                                                                            answer = input("[x] Sort through the items and recycle each properly.\n[c] Bag it all up and to the garbage bin it goes!\n")
                                                                            if answer == "x":
                                                                                os.system("cls")
                                                                                message = "As you sort through the items, one by one, you begin to get a little emotional.\nYou realize that you haven't let yourself sort through your emotions yet, and though sorting through the house has not helped, facing your memories head on seems to be doing the trick.\nTearfully, you finish sorting the large pile of items in your house.\n"
                                                                                typewriter()
                                                                                answer = input("Press [x] to dispose of your items respectfully.\n")
                                                                                if answer == "x":
                                                                                    os.system("cls")
                                                                                    message = "'It has been a long day', you say, as you release a heavy sigh. And it really has been a long 5 days. It seems we are nearing the end.\n"
                                                                                    typewriter()
                                                                                    answer = input("Press [x] to fall asleep, and consequently end the game.\n")
                                                                                    if answer == "x":
                                                                                        os.system("cls")
                                                                                        message = ".\n.\n.\nEvery time we are encouraged to make a change, we always think to ourselves: what good does it make if only one person changes?\nWhat we don't realize, however, is that if everyone took it upon themselves to make a change, good change would happen.\nSurprise " + name + "!\nIn this game, not only were you representing yourself, but you were representing the entire world.\nBecause if everyone takes it upon themselves to make a good decision, imagine how much better the world would be.\nAnd it is better. Because of you.\nThis game may not have seemed like it was made to educate others on Environmental Sustainability, but what it really shows us is that the difference between a sustainable world and the one we live in now,\nlies in small everyday decisions we make throughout our lives, like recycling, not using plastic, and reducing our individual pollution levels.\nAnd I think it's safe to say that you, " + name + ", have made some pretty good decisions these past 5 days.\nAnd you know what that means.\nIf you made some pretty good decisions, then that means the ENTIRE WORLD made some pretty good decisions.\nCongratulations " + name + "! Thanks to you and your environmentally sustainable decision making thought process, you put the world on a path to environmental sustainability.\nYou have won the game!\nThank you for playing, and we wish you the best on your journey to save the world!\nTHE END\n"
                                                                                        typewriter()
                                                                                        
                                                                                    else:
                                                                                        ending()
                                                                                else:
                                                                                    ending()
                                                                            elif answer == "c":
                                                                                os.system("cls")
                                                                                message = "You haul the large bags to the garbage container outside the apartment complex.\nYou feel guilty about it.\nAll things considered, it has been a long day; a long 5 days to say the least.\n"
                                                                                typewriter()
                                                                                answer = input("Press [x] to go to bed, and consequently end the game.\n")
                                                                                if answer == "x":
                                                                                    os.system("cls")
                                                                                    message = ".\n.\n.\nEvery time we are encouraged to make a change, we always think to ourselves: what good does it make if only one person changes?\nWhat we don't realize, however, is that if everyone took it upon themselves to make a change, good change would happen.\nSurprise " + name + "!\nIn this game, not only were you representing yourself, but you were representing the entire world.\nBut the problem is, you didn't really take good actions.\nMany of the decisions you made weren't entirely eco-friendly.\nAnd though this may not seem like an issue if one person acts this way, think again.\nIf everyone thought of themselves as one person making poor decisions, where would the world be today?\nI'm sorry " + name + ", but you lost the game.\nYour decisions, when placed on a global scale, lead the world down an unsettling path of environmental deterioration and destruction.\nThank you for playing, and we wish you the best on your journey to save the world.\nTHE END!\n"
                                                                                    typewriter()
                                                                                    
                                                                                else:
                                                                                    ending()                   
                                                                            else:
                                                                                ending()
                                                                        else:
                                                                            ending()





                                                                    else:
                                                                        ending()






                                                                else:
                                                                    ending()
                                                            else:
                                                                ending()
                                                        else:
                                                            ending()
                                                    else:
                                                        ending()
                                                else:
                                                    ending()
                                            else:
                                                ending()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------spend day out or go home?
                                        elif answer == "c":
                                            os.system("cls")
                                            message = "You return home, feeling heavier than ever before.\nThe look of your concerned girlfriend just happened to be the last straw.\nTragically, you drop down onto the doorstep, tears unwillingly streaming down your face.\nYour girlfriend doesn't know what's wrong, but she's understanding.\nShe tells you it will all be ok.\nYou feel relieved.\n"
                                            typewriter()
                                            answer = input("Press [x] to go to bed.\n")
                                            if answer == "x":
                                                os.system("cls")
                                                message = "You wake up the next morning, head pounding from the drinks and tears of last night.\nYou groggily walk down the stairs to see your girlfriend sitting at the table with two cups of coffee.\nShe seems to be reading a flyer.\nGirlfriend: My friend gave me this flyer on my way home from work yesterday... want to read?\nShe passes you the flyer and you read the title.\n'Environmentally Sustainable Cooking! Learn how to cook for yourself, while making sure that nature can feed itself too!'\nDo you attend the cooking class?\n"
                                                typewriter()
                                                answer = input("[x] Yes\n[c] No\n")
                                                if answer == "x":
                                                    os.system("cls")
                                                    cooking_bowl()
                                                    time.sleep(SLEEP_AFTER_ASCII)
                                                    message = "You attend the class. It's your first day. And even though it's just your first day, you already feel like you've learned so much.\nYou learned about the environmental effects that come from the food that you eat.\nWho would have known that meat, especially beef, plays one of the biggest roles in climate change?\nWith a good first experience, you make it a point to attend the weekly classes from now on.\n"
                                                    typewriter()
                                                    answer = input("Press [x] to return from the class.\n")
                                                    if answer == "x":
                                                        os.system("cls")
                                                        message = "You return home, and find yourself cooking one of the meals you learned today. You feel proud, making it a point to use all reusable cutlery, cooking tools and plates.\n"
                                                        typewriter()
                                                        answer = input("Press [x] to eat your dinner.\n")
                                                        if answer == "x":
                                                            os.system("cls")
                                                            message = "After dinner, you put your new knowledge to use, and use less water when washing the dishes, and you decide to throw out all the plastic kitchenware while you're at it.\nCompared to yesterday, you feel a little happier.\nThis whole eco-friendly stuff is starting to grow on you.\n"
                                                            typewriter()
                                                            answer = input("Press [x] to go to bed.\n")
                                                            if answer == "x":
                                                                os.system("cls")
                                                                bed()
                                                                time.sleep(SLEEP_AFTER_ASCII)
                                                                message = "As you lie in bed, a sudden idea comes to you.\nNow that you don’t have a job anymore, why not create your own?\nYou suddenly get the idea to start up a new company, focused on helping other organizations stay environmentally sustainable.\nIt may be difficult to do, but with some hard work and dedication you believe that you can get it done.\nDo you...\n"
                                                                typewriter()
                                                                answer = input("[x] Take up the challenge and start the company\n[c] Dismiss the thought\n")
                                                                if answer == "x":
                                                                    os.system("cls")
                                                                    message = "Great! You decide to get started tomorrow.\n"
                                                                    typewriter()
                                                                    answer = input("Press [x] to go to bed.\n")
                                                                    if answer == "x":
                                                                        os.system("cls")
                                                                        message = "You wake up the next morning, excited to tell your girlfriend about the idea.\nExcitedly, you hop down the stairs, and discuss the topic with her.\nShe is interested and ready to embark on this journey with you!\nWithin just a few days, you already recieve many calls from investors looking to invest in your company and bring it to success.\nYou and your girlfriend are ecstatic!\nIt has been a long 5 days.\n"
                                                                        typewriter()
                                                                        answer = input("Press [x] to end the game.\n")
                                                                        if answer == "x":
                                                                            os.system("cls")
                                                                            message = ".\n.\n.\nEvery time we are encouraged to make a change, we always think to ourselves: what good does it make if only one person changes?\nWhat we don't realize, however, is that if everyone took it upon themselves to make a change, good change would happen.\nSurprise " + name + "!\nIn this game, not only were you representing yourself, but you were representing the entire world.\nBecause if everyone takes it upon themselves to make a good decision, imagine how much better the world would be.\nAnd it is much better, because of you.\nThis game may not have seemed like it was made to educate others on Environmental Sustainability, but what it really shows us is that the difference between a sustainable world and the one we live in now, lies in the small everyday decisions we make throughout our lives, like recycling, not using plastic, and reducing our individual pollution levels.\nAnd I think it's safe to say that you, " + name + ", have made some pretty good decisions these past 5 days.\nAnd you know what that means.\nIf you made some pretty good decisions, then that means the ENTIRE WORLD made some pretty good decisions.\nCongratulations " + name + "! Thanks to you and your environmentally sustainable decision making thought process, you put the world on a path to environmental sustainability.\nYou have won the game!\nThank you for playing, and we wish you the best on your journey to saving the world!\nTHE END!\n"
                                                                            typewriter()
                                                                            
                                                                        else:
                                                                            ending()
                                                                    else:
                                                                        ending()



#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------make company or nah?
                                                                elif answer == "c":
                                                                    os.system("cls")
                                                                    message = "You dismiss the thought. Starting up a company? Seemed impossible anyways.\n"
                                                                    typewriter()
                                                                    answer = input("Press [x] to go to bed.\n")
                                                                    if answer == "x":
                                                                        os.system("cls")
                                                                        message = "You wake up the next morning, the trees and birds seeming a little duller than a few days ago.\nA pang of sadness hits you as you remember that you are still unemployed.\n.\nAs you get ready for the day, you decide to attend the library to begin your job hunting search.\n"
                                                                        library()
                                                                        time.sleep(SLEEP_AFTER_ASCII)
                                                                        message = "You attend the library, searching through flyers, papers, and the computer for jobs that you could take up.\nEventually, this narrows down to two options:\nThe first option is at Lipton Tea, and environmentally sustainable company that aims to source all of its tea from environmentally friendly places by this year!\nThe location is a little far, but the base pay is good and there are some achievable benefits.\nThe second option is to take a job at Post Consumer Brands, a grocery store food company.\nThe name sounds familiar...\nOh right! It's the brand name on your cereal box at home!\nAnyways, the base pay is higher than Lipton Tea and the location is closer as well.\nHowever, this company is known to be one of the least environmentally sustainable food companies in the market, and they have no plans to fix this issue.\nHad you not taken that eco-friendly cooking class, this wouldn't have mattered to you!\nBut now, you do feel a little guilty taking a job from a company that you know is harming the Earth.\nWhere do you decide to work?\n"
                                                                        typewriter()
                                                                        answer = input("[x] Lipton Tea\n[c] Post Consumer Brands\n")
                                                                        if answer == "x":
                                                                            os.system("cls")
                                                                            message = "You apply for a job at Lipton Tea.\n.\n.\n.\nA few hours later, you recieve an email saying that they loved your application and they would like you to start tomorrow!\nExcited, you confirm your attendance and happily walk all the way home.\n.\nToday has been a good day. But it seems the past 5 days have come to an end.\n"
                                                                            typewriter()
                                                                            answer = input("Press [x] to go to sleep, and consequently end the game.\n")
                                                                            if answer == "x":
                                                                                os.system("cls")
                                                                                message = ".\n.\n.\nEvery time we are encouraged to make a change, we always think to ourselves: what good does it make if only one person changes?\nWhat we don't realize, however, is that if everyone took it upon themselves to make a change, good change would happen.\nSurprise " + name + "!\nIn this game, not only were you representing yourself, but you were representing the entire world.\nBecause if everyone takes it upon themselves to make a good decision, imagine how much better the world would be.\nAnd it is much better, because of you.\nThis game may not have seemed like it was made to educate others on Environmental Sustainability, but what it really shows us is that the difference between a sustainable world and the one we live in now, lies in the small everyday decisions we make throughout our lives, like recycling, not using plastic, or supporting eco-friendly companies.\nAnd I think it's safe to say that you, " + name + ", have made some pretty good decisions these past 5 days.\nAnd you know what that means.\nIf you made some pretty good decisions, then that means the ENTIRE WORLD made some pretty good decisions.\nCongratulations " + name + "! Thanks to you and your environmentally sustainable decision making thought process, you put the world on a path to environmental sustainability.\nYou have won the game!\nThank you for playing, and we wish you the best on your journey to saving the world!\nTHE END!\n"
                                                                                typewriter()
                                                                                 
                                                                            else:
                                                                                ending()




#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------PATH 10 LIPTON TEA OR POST CONSUMER BRANDS (athi coded this one)                                                                            
                                                                        elif answer == "c":
                                                                            os.system("cls")
                                                                            message = "You apply for a job at Post Consumer Brands.\n.\n.\n.\nA couple days later, you recieve an email saying that you have been accepted and they would like you to start tomorrow!\nYou feel guilty, but you accept the job anyways. You think,\n'It should be fine, it's only one company that hurts the environment this way.'\nIt has been a long day. A long 5 days in fact.\n"
                                                                            typewriter()
                                                                            answer = input("Press [x] to go to sleep, and consequently end the game.\n")
                                                                            if answer == "x":
                                                                                os.system("cls")
                                                                                message = ".\n.\n.\nEvery time we are encouraged to make a change, we always think to ourselves: what good does it make if only one person changes?\nWhat we don't realize, however, is that if everyone took it upon themselves to make a change, good change would happen.\nSurprise " + name + "!\nIn this game, not only were you representing yourself, but you were representing the entire world.\nBut the problem is, you didn't really take good actions.\nSure, you may have taken an eco-friendly cooking class, but you did try to take your car to work and you decided to work for the LEAST environmentally friendly company in your country!\nAs you can see, your decisions weren't entirely eco-friendly.\nI'm sorry " + name + ", but you lost the game.\nYour decisions, when placed on a global scale, lead the world down an unsettling path of environmental deterioration and destruction.\nThank you for playing, and we wish you the best on your journey to save the world.\nTHE END!\n"
                                                                                typewriter()
                                                                                
                                                                            else:
                                                                                ending()






                                                                        else:
                                                                            ending()
                                                                    else:
                                                                        ending()





                                                                else:
                                                                    ending()
                                                            else:
                                                                ending()
                                                        else:
                                                            ending()
                                                    else:
                                                        ending()       



                                                elif answer == "c":
                                                    os.system("cls")
                                                    message = "You tell your girlfriend that you wouldn't like to attend the class, and she seems a little disappointed.\nMaybe you should have said yes.\nWith the rest of the day left empty ahead of you, you decide to clean the house!\nIt has gotten a little dirty over the past couple weeks, seeing as you were too busy with work to do any housekeeping.\n"
                                                    typewriter()
                                                    answer = input("Press [x] to clean the house.\n")
                                                    if answer == "x":
                                                        os.system("cls")
                                                        cleaning()
                                                        time.sleep(SLEEP_AFTER_ASCII)
                                                        message = "It has been a long day of cleaning, and you are exhausted.\nYou decide it's time to go to bed.\n"
                                                        typewriter()
                                                        answer = input("Press [x] to go to bed.\n")
                                                        if answer == "x":
                                                            os.system("cls")
                                                            message = "You wake up this morning, the trees and birds seeming a little more sickly and dull compared to the days prior.\nA pang of sadness hits you as you remember that you are still unemployed.\nAs you get ready for the day, you decide to attend the library to begin your job hunting search.\n"
                                                            typewriter()
                                                            answer = input("Press [x] to go to the library.\n")
                                                            if answer == "x":
                                                                os.system("cls")
                                                                library()
                                                                time.sleep(SLEEP_AFTER_ASCII)
                                                                message = "You attend the library, searching through flyers, papers, and the computer for jobs that you could take up.\nEventually, this narrows down to two options:\nThe first option is at Lipton Tea, and environmentally sustainable company that aims to source all of its tea from environmentally friendly places by this year!\nThe location is a little far, but the base pay is good and there are some achievable benefits.\nThe second option is to take a job at Post Consumer Brands, a grocery store food company.\nThe name sounds familiar...\nOh right! It's the brand name on your cereal box at home!\nAnyways, the base pay is higher than Lipton Tea and the location is closer as well.\nHowever, this company is known to be one of the least environmentally sustainable food companies in the market, and they have no plans to fix this issue.\nHad you not taken that eco-friendly cooking class, this wouldn't have mattered to you!\nBut now, you do feel a little guilty taking a job from a company that you know is harming the Earth.\nWhere do you decide to work?\n"
                                                                typewriter()
                                                                answer = input("[x] Lipton Tea\n[c] Post Consumer Brands\n")
                                                                if answer == "x":
                                                                    os.system("cls")
                                                                    message = "You apply for a job at Lipton Tea.\n.\n.\n.\nA few hours later, you recieve an email saying that they loved your application and they would like you to start tomorrow!\nExcited, you confirm your attendance and happily walk all the way home.\n.\nToday has been a good day. But it seems the past 5 days have come to an end.\n"
                                                                    typewriter()
                                                                    answer = input("Press [x] to go to sleep, and consequently end the game.\n")
                                                                    if answer == "x":
                                                                        os.system("cls")
                                                                        message = ".\n.\n.\nEvery time we are encouraged to make a change, we always think to ourselves: what good does it make if only one person changes?\nWhat we don't realize, however, is that if everyone took it upon themselves to make a change, good change would happen.\nSurprise " + name + "!\nIn this game, not only were you representing yourself, but you were representing the entire world.\nBecause if everyone takes it upon themselves to make a good decision, imagine how much better the world would be.\nAnd it is much better, because of you.\nThis game may not have seemed like it was made to educate others on Environmental Sustainability, but what it really shows us is that the difference between a sustainable world and the one we live in now, lies in the small everyday decisions we make throughout our lives, like recycling, not using plastic, or supporting eco-friendly companies.\nAnd I think it's safe to say that you, " + name + ", have made some pretty good decisions these past 5 days.\nAnd you know what that means.\nIf you made some pretty good decisions, then that means the ENTIRE WORLD made some pretty good decisions.\nCongratulations " + name + "! Thanks to you and your environmentally sustainable decision making thought process, you put the world on a path to environmental sustainability.\nYou have won the game!\nThank you for playing, and we wish you the best on your journey to saving the world!\nTHE END!\n"
                                                                        typewriter()
                                                                        
                                                                    else:
                                                                        ending()

                                                                elif answer == "c":
                                                                    os.system("cls")
                                                                    message = "You apply for a job at Post Consumer Brands.\n.\n.\n.\nA couple days later, you recieve an email saying that you have been accepted and they would like you to start tomorrow!\nYou feel guilty, but you accept the job anyways. You think,\n'It should be fine, it's only one company that hurts the environment this way.'\nIt has been a long day. A long 5 days in fact.\n"
                                                                    typewriter()
                                                                    answer = input("Press [x] to go to sleep, and consequently end the game.\n")
                                                                    if answer == "x":
                                                                        os.system("cls")
                                                                        message = ".\n.\n.\nEvery time we are encouraged to make a change, we always think to ourselves: what good does it make if only one person changes?\nWhat we don't realize, however, is that if everyone took it upon themselves to make a change, good change would happen.\nSurprise " + name + "!\nIn this game, not only were you representing yourself, but you were representing the entire world.\nBut the problem is, you didn't really take good actions.\nAfter all, you did try to take your car to work, you declined an offer to take a class on eco-friendly cooking, AND you decided to work for the LEAST environmentally friendly company in your country!\nThis game may have not seemed like it was made to educate others on Environmental Sustainablility,\nbut what it really shows us is that the difference between a sustainable world and the one we live in now,\nlies in the small everyday decisions we make throughout our lives,\nlike recycling, not using plastic, or supporting companies that are eco-friendly.\nI'm sorry " + name + ", but you lost the game.\nYour decisions, when placed on a global scale, lead the world down an unsettling path of environmental deterioration and destruction.\nThank you for playing, and we wish you the best on your journey to save the world.\nTHE END!\n"
                                                                        typewriter()
                                                                        
                                                                    else:
                                                                        ending()

                                                                else:
                                                                    ending()
                                                            else:
                                                                ending()
                                                        else:
                                                            ending()

                                                    else:
                                                        ending()





                                                else:
                                                    ending()
                                            else:
                                                ending()    
                                        else:
                                            ending()
                                    else:
                                        ending()
                                else:
                                    ending()
                            else:
                                ending()



#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------bus or car?
                        elif answer == "c":
                            os.system("cls")
                            bus()
                            time.sleep(SLEEP_AFTER_ASCII)
                            message = "As you sit in your bus seat, you think about this morning's events.\nThough your mind is filled primarily with the thought of being late for work, a small part of you feels guilty for not eating breakfast with your girlfriend this morning.\nIt wasn't the first time you've done this, and if you keep it up, it probably won't be the last.\nShe has been seeming pretty closed off lately...\nIs she going to break up with me?\n.\n.\n.\nProbably not.\nBut it does seem that your boss is going to break up with you if you're late to work one more time.\n"
                            typewriter()
                            answer = input("Press [x] to get off the bus before you miss your stop.\n")
                            if answer == "x":
                                os.system("cls")
                                message = "Boss: Good morning " + name + "! Glad to see that you're early today! You know, I was this close to firing you.\n" + name + ": Oh, you and your sense of humour. Really make my day sir.\nBoss: You know me! Anyways, my senior supervisor let me know of a conference that's coming up.\nApparently it has to do with environmental sustainability and how to implement it in the workplace and at home.\nShe told me to bring you along. Would you like to come?\n" + name + ": When is it again sir?\nBoss: It's in a couple days during the evening.\n" + name + ": Hmm... I should be free then! I'll see you there!\nYou enter your office and take a seat, a little shocked, actually.\nYour boss is quite the fearsome man. First, he says he was going to fire you, then invites you to a conference?\nA weird man indeed. You get some work done and without realizing it, it turns to 5PM.\n"
                                typewriter()
                                answer = input("Press [x] to return home.\n")
                                if answer == "x":
                                    os.system("cls")
                                    message = "You return home, and your girlfriend mentions to you that her birthday is in a couple days.\nShe was hoping to spend the evening with you.\nYou were about to agree, when all of a sudden you remembered that you had the Eco-Conference for work that evening.\nYou definitely don't want to disappoint your girlfriend on her birthday, but you would also appreciate it if you could keep your job.\nDo you...\n"
                                    typewriter()
                                    answer = input("[x] Attend the conference\n[c] Spend the evening with your girlfriend\n")
                                    if answer == "x":
                                        os.system("cls")
                                        message = "You break the sad news to your girlfriend, who can't help but show her initial feelings of disappointment.\nAngry and saddened, she leaves the room to take a break from the situation.\n.\n.\n.\nA few hours later, she returns to your room, this time less emotional.\nShe understands that you should listen to your boss and the two of you decide to celebrate her birthday the day after.\n"
                                        typewriter()
                                        answer = input("Press [x] to go to bed\n")
                                        if answer == "x":
                                            os.system("cls")
                                            message = "A couple days have gone by, and you just finished attending the Eco-Conference with your boss.\nIt was just 2 hours, but you already feel like you learned so much.\nYou learned about the environmental effects that come from the manufacturing process,\nand the environmental disadvantages of the products you might even sell.\nNot only that, but you learned about the small ways that people harm the environment from home,\nsuch as using plastic utensils and not recycling.\nWith a good first experience, you head out to the store.\nAt the store, you see a couple reuseable straws, eco-friendly storage bags, and a compost starter.\nYou think about whether you should buy them, since you just learned about their benefits to the earth.\nDo you...\n"
                                            typewriter()
                                            answer = input("[x] Buy the eco-friendly utensils\n[c] Don't buy the eco-friendly utensils\n")
                                            if answer == "x":
                                                os.system("cls")
                                                message = "You buy the eco-friendly utensils. You feel transformed.\n"
                                                typewriter()
                                                answer = input("Press [x] to return home and go to bed.\n")
                                                if answer == "x":
                                                    os.system("cls")
                                                    message = "BEEP! BEEP! BEEP!\nYour alarm rings. You wake up surprised; after all, it's the weekend. You check your phone, only to realize that this isn't any ordinary alarm. It's a reminder to buy a car!\nAll the saving up over the past few months has finally made its purpose.\n"
                                                    typewriter()
                                                    answer = input("Press [x] to visit the car dealership.\n")
                                                    if answer == "x":
                                                        os.system("cls")
                                                        car()
                                                        time.sleep(SLEEP_AFTER_ASCII)
                                                        message = "You visit the car dealership, ready to wait long hours, bargain, and haggle with the dealers. You're choosing between two cars; both on sale, since you want to save money.\nThe first car is an electric car. A few days ago, you would have definitely picked the second option.\nBut today, with your newfound knowledge about environmental sustainability, you understand that an electric car like this one is much more environmentally friendly, and you wouldn't mind picking driving this one in the future.\nThe second car is an old model, but one that you've had your eyes on for quite some time. It may not be the hottest car on the market, but it holds a lot of sentimental value. However, it does use a lot of fossil fuels and releases lots of pollution into the atmosphere.\nWhich car do you choose?\n"
                                                        typewriter()
                                                        answer = input("[x] Electric Car\n[c] Old Car\n")
                                                        if answer == "x":
                                                            os.system("cls")
                                                            message = "Dealer: Great! Thank you " + name + ". We appreciate your choice of using our dealership to purchase your vehicle. Here's a free oil change and car wash on the house!\n" + name + ": Thanks!\nSatisfied, you drive your car home and decide to go to bed.\nAnd it also seems we have reached the end of our 5 days.\n"
                                                            typewriter()
                                                            answer = input("Press [x] to go to sleep, and consequently, end the game.\n")
                                                            if answer == "x":
                                                                os.system("cls")
                                                                message = ".\n.\n.\nEvery time we are encouraged to make a change, we always think to ourselves: what good does it make if only one person changes?\nWhat we don't realize, however, is that if everyone took it upon themselves to make a change, good change would happen.\nSurprise " + name + "!\nIn this game, not only were you representing yourself, but you were representing the entire world.\nBecause if everyone takes it upon themselves to make a good decision, imagine how much better the world would be.\nAnd it is much better, because of you.\nThis game may not have seemed like it was made to educate others on Environmental Sustainability, but what it really shows us is that the difference between a sustainable world and the one we live in now, lies in the small everyday decisions we make throughout our lives, like recycling, not using plastic, and reducing our individual pollution levels.\nAnd I think it's safe to say that you, " + name + ", have made some pretty good decisions these past 5 days.\nAnd you know what that means.\nIf you made some pretty good decisions, then that means the ENTIRE WORLD made some pretty good decisions.\nCongratulations " + name + "! Thanks to you and your environmentally sustainable decision making thought process, you put the world on a path to environmental sustainability.\nYou have won the game!\nThank you for playing, and we wish you the best on your journey to saving the world!\nTHE END!\n"
                                                                typewriter()
                                                                
                                                            else:
                                                                ending()




#----------------------------------------------------------------------------------------------------------------------------------------------------------------------electric or old car?
                                                        elif answer == "c":
                                                            os.system("cls")
                                                            message = "Dealer: Great! Thank you " + name + ". We appreciate your choice of using our dealership to purchase your vehicle. Here's a free oil change and car wash on the house!\n" + name + ": Thanks!\nSatisfied, you drive your car straight to the Bright Stars Restaurant,\nwhere your girlfriend decided to host her birthday party with her friends.\n"
                                                            typewriter()
                                                            answer = input("Press [x] to enter Bright Stars Restaurant\n")
                                                            if answer == "x":
                                                                os.system("cls")
                                                                cake()
                                                                time.sleep(SLEEP_AFTER_ASCII)
                                                                message = "You enter the restaurant and see that everyone has already arrived and started eating!\nThankfully, your girlfriend already ordered for you.\n.\n.\n.\nEveryone enjoys the night, especially your girlfriend.\nBut it has finally reached the time to return home.\nOne of your girlfriend's friends stares at her leftovers, then reaches into her bag, pulls out some reusable containers, and packs her food away.\nYou were amazed and happy to see that she was making such an eco-friendly decision,\nwith both not wasting her food and using environmentally friendly containers.\nThat's when you realized, you have yours too!\nThey're just in the car. You stare at your leftovers, and wonder if you should do the same thing.\nDo you...\n"
                                                                typewriter()
                                                                answer = input("[x] Get the containers from the car and pack the food away\n[c] Waste the food\n")
                                                                if answer == "x":
                                                                    os.system("cls")
                                                                    message = "You got your containers from the car and packed away the food. You feel proud.\nWith this long day coming to a close, you and your girlfriend head home and go to bed.\nThe past 5 days have ended so quickly. But it's time to finish up.\n"
                                                                    typewriter()
                                                                    answer = input("Press [x] to end the game.\n")
                                                                    if answer == "x":
                                                                        os.system("cls")
                                                                        message = ".\n.\n.\nEvery time we are encouraged to make a change, we always think to ourselves: what good does it make if only one person changes?\nWhat we don't realize, however, is that if everyone took it upon themselves to make a change, good change would happen.\nSurprise " + name + "!\nIn this game, not only were you representing yourself, but you were representing the entire world.\nBecause if everyone takes it upon themselves to make a good decision, imagine how much better the world would be.\nAnd it is much better, because of you.\nThis game may have not seemed like it was made to educate others on Environmental Sustainability,\nbut what it really shows us is that the difference between a sustainable world and the one we live in now, lies in the small everyday decisions we make throughout our lives,\nlike recycling, not using plastic, and reducing our individual pollution levels.\nAlthough you may not have bought an electric car, you did choose to use the bus to get to work, and you committed yourself to a lifelong learning experience of environmental sustainability.\nAnd I think it's safe to say that you, " + name + ", have made some pretty good decisions these past 5 days.\nAnd you know what that means.\nIf you made some pretty good decisions, then that means the ENTIRE WORLD made some pretty good decisions.\nCongratulations " + name + "! Thanks to you and your environmentally sustainable decision making thought process, you put the world on a path to environmental sustainability.\nYou have won the game!\nThank you for playing, and we wish you the best on your journey to saving the world!\nTHE END!\n"
                                                                        typewriter()
                                                                        
                                                                    else:
                                                                        ending()






#----------------------------------------------------------------------------------------------------------------------------------------------------------get container from car for food or no?                                                                   
                                                                elif answer == "c":
                                                                    os.system("cls")
                                                                    message = "You wasted the food, with fear of what the others would say if you got up and went to your car.\nYou feel guilty.\n"
                                                                    typewriter()
                                                                    answer = input("Press [x] to return home and go to bed.\n")
                                                                    if answer == "x":
                                                                        os.system("cls")
                                                                        message = "It has been a long 5 days of making decisions for a life you have never known, but it has all come to and end.\n"
                                                                        typewriter()
                                                                        answer = input("Press [x] to end the game.\n")
                                                                        if answer == "x":
                                                                            os.system("cls")
                                                                            message = ".\n.\n.\nEvery time we are encouraged to make a change, we always think to ourselves: what good does it make if only one person changes?\nWhat we don't realize, however, is that if everyone took it upon themselves to make a change, good change would happen.\nSurprise " + name + "!\nIn this game, not only were you representing yourself, but you were representing the entire world's population.\nBut the problem is, you didn't really take good actions.\nYou chose a gas-run car instead of the electric one, and you chose to waste your food even in the presence of reusable containers.\nMany of the decisions you made weren't entirely eco-friendly.\nAnd though this may not seem like an issue if one person acts this way, think again.\nIf everyone thought of themselves as one person making poor decisions, where would the world be today?\nI'm sorry " + name + ", but you lost the game.\nYour decisions, when placed on a global scale, lead the world to imitate our current world, but that isn't good enough.\nThank you for playing, and we wish you the best on your journey to save the world.\nTHE END!\n"
                                                                            typewriter()
                                                                            
                                                                        else:
                                                                            ending()
                                                                    else:
                                                                        ending()





                                                                else:
                                                                    ending()

                                                            else:
                                                                ending()









                                                        else:
                                                            ending()
                                                    else:
                                                        ending()
                                                else:
                                                    ending()




#-------------------------------------------------------------------------------------------------------------------do or don't buy eco-friendly utensils?                                                
                                            elif answer == "c":
                                                os.system("cls")
                                                message = "You choose not to buy the eco-friendly utensils, and just buy a can of soda instead.\nYou feel guilty.\n"
                                                typewriter()
                                                answer = input("Press [x] to go home and go to bed.\n")
                                                if answer == "x":
                                                    os.system("cls")
                                                    message = "You wake up the next morning, the trees and birds looking more sickly and dull than the days prior.\nYour phone rings. You pick it up, it's your old friend Barton, who's asking if you would like to meet up at the park and hang.\n"
                                                    typewriter()
                                                    answer = input("Press [x] to get ready and go to the park.\n")
                                                    if answer == "x":
                                                        os.system("cls")
                                                        message = "The two of you sit down at a bench by the lake, and you begin to tell him about the eco-conference you went to.\nBarton: No but really, all this eco-friendly stuff, it's just a bunch of nonsense isn't it? You know I believe in the philosophy of having a good time, not a long time, you know?\nSurprisingly you feel a little shocked and surprised by Bartons comments.\nYou know that had you not attended this conference, you would have reacted the same way.\nAfter all, the reason why people don't make environmentally friendly choices nowadays is because they just don't know where to begin.\nSo you understand where Barton is coming from. But you also understand that the only way to make change, is to educate.\nAt the same time, you're not a man with many friends, so you are scared of losing one of the few close ones that you have due to something small like differing opinions.\nDo you...\n"
                                                        typewriter()
                                                        answer = input("[x] Agree with Barton to save yourself the risk of losing a friend\n[c] Educate Barton on the importance of being environmentally sustainable\n")
                                                        if answer == "x":
                                                            os.system("cls")
                                                            message = "You agree with Barton. But as you speak to him, his face slowly turns into your own.\nInstead of just agreeing with Barton to stay friends, you realize that you in fact are lying to yourself,\ntelling yourself that it is okay if you ignore the Earth's continuing deterioration.\nYou realize that this whole time, you were just making excuses to save yourself the trouble of living a sustainable life.\n.\n.\n.\nThe conversation slowly gets more and more empty and awkward until the two of you decide to head home.\n"
                                                            typewriter()
                                                            answer = input("Press [x] to return home.\n")
                                                            if answer == "x":
                                                                os.system("cls")
                                                                message = "Still shocked and saddened by the realization you had at the park, you decide to go to bed early today.\n"
                                                                typewriter()
                                                                answer = input("Press [x] to go to bed.\n")
                                                                if answer == "x":
                                                                    os.system("cls")
                                                                    message = "You wake up the next morning. The sky seems somber, the trees have withered, and the birds no longer sing.\nWithout the will to carry on, you head back to bed.\n"
                                                                    typewriter()
                                                                    answer = input("Press [x] to fall back asleep.\n")
                                                                    if answer == "x":
                                                                        os.system("cls")
                                                                        message = "Well... it seems your 5 days have come to an end.\n"
                                                                        typewriter()
                                                                        answer = input("Press [x] to end the game.\n")
                                                                        if answer == "x":
                                                                            os.system("cls")
                                                                            message = ".\n.\n.\nEvery time we are encouraged to make a change, we always think to ourselves: what good does it make if only one person changes?\nWhat we don't realize, however, is that if everyone took it upon themselves to make a change, good change would happen.\nSurprise " + name + "!\nIn this game, not only were you representing yourself, but you were representing the entire world's population.\nBut the problem is, you didn't really take good actions.\nYou didn't put your environmental knowledge into action, and you didn't share this knowledge with anyone else.\nWhat you did was hide knowledge, that could save the world, from your friends, yet not even use it yourself.\nAnd though this may not seem like an issue if one person acts this way, think again.\nIf everyone thought of themselves as one person making poor decisions, where would the world be today?\nI'm sorry " + name + ", but you lost the game.\nYour decisions, when placed on a global scale, lead the world down an unsettling path of environmental deterioration and destruction.\nThank you for playing, and we wish you the best on your journey to save the world.\nTHE END!\n"
                                                                            typewriter()
                                                                            
                                                                        else:
                                                                            ending()
                                                                    else:
                                                                        ending()
                                                                else:
                                                                    ending()
                                                            else:
                                                                ending()




#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------educate barton or no?
                                                        elif answer == "c":
                                                            os.system("cls")
                                                            message = "You educate Barton. He seems to understand, and even seems motivated to embark on his journey of environmental sustainability.\nBut as you educate him, you feel guilty. How could someone preach this way of life without even practicing it themselves?\nEventually, the conversation comes to an end and you decide to head back to the store to give yourself a second chance.\n"
                                                            typewriter()
                                                            answer = input("Press [x] to head to the store.\n")
                                                            if answer == "x":
                                                                os.system("cls")
                                                                message = "You arrive at the store, and find yourself once again standing in front of the shelf on which there are reusable straws, eco-friendly storage bags and a compost starter.\nDo you...\n"
                                                                typewriter()
                                                                answer = input("[x] Buy them\n[c] Leave them and return home\n")
                                                                if answer == "x":
                                                                    os.system("cls")
                                                                    message = "You buy the items, feeling proud of yourself.\nIt has been quite the 5 days, but they have now come to an end.\n"
                                                                    typewriter()
                                                                    answer = input("Press [x] to return home and consequently, end the game.\n")
                                                                    if answer == "x":
                                                                        os.system("cls")
                                                                        message = ".\n.\n.\nEvery time we are encouraged to make a change, we always think to ourselves: what good does it make if only one person changes?\nWhat we don't realize, however, is that if everyone took it upon themselves to make a change, good change would happen.\nSurprise " + name + "!\nIn this game, not only were you representing yourself, but you were representing the entire world.\nBecause if everyone takes it upon themselves to make a good decision, imagine how much better the world would be.\nAnd it is much better, because of you.\nThis game may not have seemed like it was made to educate others on Environmental Sustainability,\nbut what it really shows us is that the difference between a sustainable world and the one we live in now, lies in the small everyday decisions we make throughout our lives,\nlike recycling, not using plastic, and reducing our individual pollution levels.\nAlthough you may not have initially bought the sustainable utensils, you eventually did AND you did choose to use the bus to get to work.\nSo, I think it's safe to say that you, " + name + ", have made some pretty good decisions these past 5 days.\nAnd you know what that means.\nIf you made some pretty good decisions, then that means the ENTIRE WORLD made some pretty good decisions.\nCongratulations " + name + "! Thanks to you and your environmentally sustainable decision making thought process, you put the world on a path to environmental sustainability.\nYou have won the game!\nThank you for playing, and we wish you the best on your journey to saving the world!\nTHE END!\n"
                                                                        typewriter()
                                                                        
                                                                    else:
                                                                        ending()





#-------------------------------------------------------------------------------------------------------------------------------------------------------second chance at store - buy utensils or nah?                                                                   
                                                                elif answer == "c":
                                                                    os.system("cls")
                                                                    message = "Still feeling guilt-ridden from your experience at the store today, you decide to go to bed early today.\n"
                                                                    typewriter()
                                                                    answer = input("Press [x] to go to bed.\n")
                                                                    if answer == "x":
                                                                        os.system("cls")
                                                                        message = "You wake up the next morning. The sky seems somber, the trees have withered, and the birds no longer sing.\nWithout the will to carry on, you head back to bed.\n"
                                                                        typewriter()
                                                                        answer = input("Press [x] to fall back asleep.\n")
                                                                        if answer == "x":
                                                                            os.system("cls")
                                                                            message = "Well... it seems your 5 days have come to an end.\n"
                                                                            typewriter()
                                                                            answer = input("Press [x] to end the game.\n")
                                                                            if answer == "x":
                                                                                os.system("cls")
                                                                                message = ".\n.\n.\nEvery time we are encouraged to make a change, we always think to ourselves: what good does it make if only one person changes?\nWhat we don't realize, however, is that if everyone took it upon themselves to make a change, good change would happen.\nSurprise " + name + "!\nIn this game, not only were you representing yourself, but you were representing the entire world's population.\nBut the problem is, you didn't really take good actions.\nSure, you may have shared your knowledge, but you yourself did not put any of it into action.\nAnd though this may not seem like an issue if one person acts this way, think again.\nIf everyone thought of themselves as one person making poor decisions, where would the world be today?\nI'm sorry " + name + ", but you lost the game.\nYour decisions, when placed on a global scale, lead the world to imitate our current world, which isn't good enough.\nThank you for playing, and we wish you the best on your journey to save the world.\nTHE END!\n"
                                                                                typewriter()
                                                                                
                                                                            else:
                                                                                ending()
                                                                        else:
                                                                            ending()
                                                                    else:
                                                                        ending()





                                                                else:
                                                                    ending()
                                                            else:
                                                                ending()





                                                        else:
                                                            ending()

                                                    else:
                                                        ending()
                                                else:
                                                    ending()





                                            else:
                                                ending()
                                        else:
                                            ending()







#-------------------------------------------------------------------------------------------------------------------------------------------attend conference or girlfriend birthday?
                                    elif answer == "c":
                                        os.system("cls")
                                        message = name + ": Of course I'll spend the evening with you! It's your birthday, after all, there isn't anything I wouldn't do for you.\nGirlfriend: Thank you so much! I can't wait till my birthday!\n"
                                        typewriter()
                                        answer = input("Press [x] to return to your room.\n")
                                        if answer == "x":
                                            os.system("cls")
                                            laptop()
                                            time.sleep(SLEEP_AFTER_ASCII)
                                            message = "You return to your room and open your laptop. After watching some netflix, you think about how you're going to break the news to your boss.\n.\n.\n.\nBut what if he fires you?\n.\n.\n.\nActually, there must be another way to do this. Why don't you lie to your boss?\nTell him that you attended the conference, but didn't see him there.\nWhat a great idea. But, maybe you should do research about the topic in case he asks you some questions.\nThat would be a lot of work though.\nDo you...\n"
                                            typewriter()
                                            answer = input("[x] Do research on environmental sustainability\n[c] Don't do research\n")
                                            if answer  == "x":
                                                os.system("cls")
                                                message = "You decide to do some research on the topic and within 45 minutes, you already feel like you've learned so much.\nYou learned about the environmental effects that come from the manufacturing process, and the environmental disadvantages of the products you might even sell.\nNot only that, but you learned about the small ways that people harm the environment from home, such as using plastic utensils and not recycling.\nInspired by your research, you head out to the store.\nAt the store, you see a couple reusable straws, eco-friendly storage bags, and a compost starter.\nYou think about whether you should buy them, since you just learned about their benefits to the earth.\nDo you...\n"
                                                typewriter()
                                                answer = input("[x] Buy the eco-friendly utensils\n[c] Don't buy the eco-friendly utensils\n")
                                                if answer == "x":
                                                    os.system("cls")
                                                    message = "You buy the eco-friendly utensils. You feel transformed.\n"
                                                    typewriter()
                                                    answer = input("Press [x] to return home and go to bed.\n")
                                                    if answer == "x":
                                                        os.system("cls")
                                                        message = "A few days have passed by, and your girlfriend's birthday evening has arrived.\nYou spend the evening with your girlfriend, watching movies and eating cake and ice cream.\nShe said it's the most fun she's ever had.\nAt the same time, you feel a little uneasy knowing that your boss is at the conference without you.\nYou decide not to let it bother you.\n"
                                                        typewriter()
                                                        answer = input("Press [x] to go to bed.\n")
                                                        if answer == "x":
                                                            os.system("cls")
                                                            message = "You wake up, ready to go shopping!\nThough yesterday may have been your girlfriend's birthday, today is the day she celebrates it at a restaurant with you and her friends.\nThat means you must go shopping for a nice shirt.\n"
                                                            typewriter()
                                                            answer = input("Press [x] to go shopping.\n")
                                                            if answer == "x":
                                                                os.system("cls")
                                                                shirt()
                                                                time.sleep(SLEEP_AFTER_ASCII)
                                                                message = "You see a shirt with the words 'Can Hack Bramp' on it.\nYou decide it's the perfect one to wear to the party.\n"
                                                                typewriter()
                                                                answer = input("Press [x] to buy the shirt and head straight to the party.\n")
                                                                if answer == "x":
                                                                    os.system("cls")
                                                                    cake()
                                                                    time.sleep(SLEEP_AFTER_ASCII)
                                                                    message = "You enter the restaurant and see that everyone has already arrived and started eating!\nThankfully, your girlfriend already ordered for you.\n.\n.\n.\nEveryone enjoys the night, especially your girlfriend.\nBut it has finally reached the time to return home.\nOne of your girlfriend's friends stares at her leftovers, then reaches into her bag, pulls out some reusable containers, and packs her food away.\nYou were amazed and happy to see that she was making such an eco-friendly decision,\nwith both not wasting her food and using environmentally friendly containers.\nThat's when you realized, you have yours too!\nThey're just in the car. You stare at your leftovers, and wonder if you should do the same thing.\nDo you...\n"
                                                                    typewriter()
                                                                    answer = input("[x] Get the containers from the car and pack the food away\n[c] Waste the food\n")
                                                                    if answer == "x":
                                                                        os.system("cls")
                                                                        message = "You got your containers from the car and packed away the food. You feel proud.\nWith this long day coming to a close, you and your girlfriend head home and go to bed.\nThe past 5 days have ended so quickly. But it's time to finish up.\n"
                                                                        typewriter()
                                                                        answer = input("Press [x] to end the game.\n")
                                                                        if answer == "x":
                                                                            os.system("cls")
                                                                            message = ".\n.\n.\nEvery time we are encouraged to make a change, we always think to ourselves: what good does it make if only one person changes?\nWhat we don't realize, however, is that if everyone took it upon themselves to make a change, good change would happen.\nSurprise " + name + "!\nIn this game, not only were you representing yourself, but you were representing the entire world.\nBecause if everyone takes it upon themselves to make a good decision, imagine how much better the world would be.\nAnd it is much better, because of you.\nThis game may not have seemed like it was made to educate others on Environmental Sustainability,\nbut what it really shows us is that the difference between a sustainable world and the one we live in now, lies in the small everyday decisions we make throughout our lives,\nlike recycling, not using plastic, and reducing our individual pollution levels.\nAlthough you may not have attended the conference, you did your own research on the topic, and you took the bus to work!\nSo, I think it's safe to say that you, " + name + ", have made some pretty good decisions these past 5 days.\nAnd you know what that means.\nIf you made some pretty good decisions, then that means the ENTIRE WORLD made some pretty good decisions.\nCongratulations " + name + "! Thanks to you and your environmentally sustainable decision making thought process, you put the world on a path to environmental sustainability.\nYou have won the game!\nThank you for playing, and we wish you the best on your journey to saving the world!\nTHE END!\n"
                                                                            typewriter()
                                                                            
                                                                        else:
                                                                            ending()






#-------------------------------------------------------------------------------------------------------------------------------------------------get containers from car or waste food? (path 20)                                                                      
                                                                    elif answer == "c":
                                                                        os.system("cls")
                                                                        message = "You wasted the food, with fear of what the others would say if you got up and went to your car. You feel guilty.\n"
                                                                        typewriter()
                                                                        answer = input("Press [x] to return home and go to bed.\n")
                                                                        if answer == "x":
                                                                            os.system("cls")
                                                                            message = ".\n.\n.\nEvery time we are encouraged to make a change, we always think to ourselves: what good does it make if only one person changes?\nWhat we don't realize, however, is that if everyone took it upon themselves to make a change, good change would happen.\nSurprise " + name + "!\nIn this game, not only were you representing yourself, but you were representing the entire world's population.\nBut the problem is, you didn't realy take good actions.\nYou didn't attend the eco-conference, and though you may have bought your own eco-friendly items, you did not put them to use in any way.\nAnd though this may not seem like an issue if one person acts this way, think again.\nIf everyone thought of themselves as one person making poor decisions, where would the world be today?\nI'm sorry " + name + ", but you lost the game.\nYour decisions, when placed on a global scale, lead the world to imitate our current world, which isn't good enough.\nThank you for playing, and we wish you the best on your journey to save the world.\nTHE END!\n"
                                                                            typewriter()
                                                                            
                                                                        else:
                                                                            ending()





                                                                    else:
                                                                        ending()
                                                                else:
                                                                    ending()
                                                            else:
                                                                ending()
                                                        else:
                                                            ending()
                                                    else:
                                                        ending()






#-----------------------------------------------------------------------------------------------------------------------------buy eco utensils or nah? (path 20)                                                   
                                                elif answer == "c":
                                                    os.system("cls")
                                                    message = "You choose not to buy the eco-friendly utensils, and just buy a can of soda instead.\nYou feel guilty about it.\n"
                                                    typewriter()
                                                    answer = input("Press [x] to go home and go to bed.\n")
                                                    if answer == "x":
                                                        os.system("cls")
                                                        message = "You wake up the next morning, the trees and birds looking more sickly and dull than the days prior.\nYour phone rings. You pick it up, it's your old friend Barton, who's asking if you want to hang at the park.\n"
                                                        typewriter()
                                                        answer = input("Press [x] to get reaady and go to the park.\n")
                                                        if answer == "x":
                                                            os.system("cls")
                                                            message = "The two of you sit down at a bench by the lake, and you begin to tell him about the eco-conference you went to.\nBarton: No but really, all this eco-friendly stuff, it's just a bunch of nonsense isn't it? You know I believe in the philosophy of having a good time, not a long time, you know?\nSurprisingly you feel a little shocked and surprised by Bartons comments.\nYou know that had you not attended this conference, you would have reacted the same way.\nAfter all, the reason why people don't make environmentally friendly choices nowadays is because they just don't know where to begin.\nSo you understand where Barton is coming from. But you also understand that the only way to make change, is to educate.\nAt the same time, you're not a man with many friends, so you are scared of losing one of the few close ones that you have due to something small like differing opinions.\nDo you...\n"
                                                            typewriter()
                                                            answer = input("[x] Agree with Barton to save yourself the risk of losing a friend\n[c] Educate Barton on the importance of being environmentally sustainable\n")
                                                            if answer == "x":
                                                                os.system("cls")
                                                                message = "You agree with Barton. But as you speak to him, his face slowly turns into your own.\nInstead of just agreeing with Barton to stay friends, you realize that you in fact are lying to yourself,\ntelling yourself that it is okay if you ignore the Earth's continuing deterioration.\nYou realize that this whole time, you were just making excuses to save yourself the trouble of living a sustainable life.\n.\n.\n.\nThe conversation slowly gets more and more empty and awkward until the two of you decide to head home.\n"
                                                                typewriter()
                                                                answer = input("Press [x] to return home.\n")
                                                                if answer == "x":
                                                                    os.system("cls")
                                                                    message = "Still shocked and saddened by the realization you had at the park, you decide to go to bed early today.\n"
                                                                    typewriter()
                                                                    answer = input("Press [x] to go to bed.\n")
                                                                    if answer == "x":
                                                                        os.system("cls")
                                                                        message = "You wake up the next morning. The sky seems somber, the trees have withered, and the birds no longer sing.\nWIthout the will to carry on, you head back to bed.\n"
                                                                        typewriter()
                                                                        answer = input("Press [x] to fall back asleep.\n")
                                                                        if answer == "x":
                                                                            os.system("cls")
                                                                            message = "Well... it seems your 5 days have come to an end.\n"
                                                                            typewriter()
                                                                            answer = input("Press [x] to end the game.\n")
                                                                            if answer == "x":
                                                                                os.system("cls")
                                                                                message = ".\n.\n.\nEvery time we are encouraged to make a change, we always think to ourselves: what good does it make if only one person changes?\nWhat we don't realize, however, is that if everyone took it upon themselves to make a change, good change would happen.\nSurprise " + name + "!\nIn this game, not only were you representing yourself, but you were representing the entire world's population.\nBut the problem is, you didn't really take good actions.\nYou didn't put your environmental knowledge into action, and you didn't share this knowledge with anyone else.\nWhat you did was hide knowledge, that could save the world, from your friends, yet not even use it yourself.\nAnd though this may not seem like an issue if one person acts this way, think again.\nIf everyone thought of themselves as one person making poor decisions, where would the world be today?\nI'm sorry " + name + ", but you lost the game.\nYour decisions, when placed on a global scale, lead the world down a path of destruction and deterioration.\nThank you for playing, and we wish you the best on your journey to save the world.\nTHE END!\n"
                                                                                typewriter()
                                                                                
                                                                            else:
                                                                                ending()
                                                                        else:
                                                                            ending()
                                                                    else:
                                                                        ending()
                                                                else:
                                                                    ending()





#--------------------------------------------------------------------------------------------------educate barton or nah?                                                               
                                                            elif answer == "c":
                                                                os.system("cls")
                                                                message = "You educate Barton. He seems to understand, and even seems motivated to embark on his journey of environmental sustainability.\nBut as you educate him, you feel guilty. How could someone preach this way of life without even practicing it themselves?\nThe conversation slowly gets more and more empty and awkward until the two of you decide to head home.\n"
                                                                typewriter()
                                                                answer = input("Press [x] to return home.\n")
                                                                if answer == "x":
                                                                    os.system("cls")
                                                                    message = ".\n.\n.\nEvery time we are encouraged to make a change, we always think to ourselves: what good does it make if only one person changes?\nWhat we don't realize, however, is that if everyone took it upon themselves to make a change, good change would happen.\nSurprise " + name + "!\nIn this game, not only were you representing yourself, but you were representing the entire world's population.\nBut the problem is, you didn't really take good actions.\nYou didn't attend the eco-conference, and though you may have educated Barton in his actions, you yourself did not use your own advice.\nAnd though this may not seem like an issue if one person acts this way, think again.\nIf everyone thought of themselves as one person making poor decisions, where would the world be today?\nI'm sorry " + name + ", but you lost the game.\nYour decisions, when placed on a global scale, imitated the world we have today.\nAnd as far as I know, the world we live in today is not on a path to recovery\nThank you for playing, and we wish you the best on your journey to save the world.\nTHE END\n"
                                                                    typewriter()
                                                                    
                                                                else:
                                                                    ending()




                                                                
                                                            else:
                                                                ending()
                                                        else:
                                                            ending()
                                                    else:
                                                        ending()








                                                else:
                                                    ending()








#---------------------------------------------------------------------------------------------------------do research on conf. topic or nah?
                                            elif answer == "c":
                                                os.system("cls")
                                                message = "You decide not to do research on the topic, and hope that your fake story will be enough to convince your boss.\n"
                                                answer = input("Press [x] to eat dinner and go to bed.\n")
                                                if answer == "x":
                                                    os.system("cls")
                                                    message = "A few days have passed by, and your girlfriend's birthday evening has arrived.\nYou spend the evening with your girlfriend, watching movies and eating cake and ice cream.\nShe said it's the most fun she's ever had.\nAt the same time, you feel a little uneasy knowing that your boss is at the conference without you.\nYou decide not to let it bother you.\n"
                                                    typewriter()
                                                    answer = input("Press [x] to go to bed.\n")
                                                    if answer == "x":
                                                        os.system("cls")
                                                        message = "You wake up the next morning, feeling a little uneasy.\nThough yesterday may have been your girlfriend's birthday, today is the day she celebrates it at a restaurant with you and her friends.\nBut at the same time, you still feel as if your boss is going to find out that you lied to him.\n.\n.\n.\nRING! RING! RING! You get a call from your boss.\nGuess your prediction was right.\n"
                                                        typewriter()
                                                        answer = input("Press [x] to pick up the call.\n")
                                                        if answer == "x":
                                                            os.system("cls")
                                                            message = "Boss: Hello?! " + name + " is this you?\n" + name + ": Yes sir it's me.\nBoss: " + name + ", I'm VERY disappointed in you. I checked with the attendance record at the conference and found out that you didn't attend! How could you like to your superior!\n" + name + ": I'm so sorry sir it's just that-\nBoss: Enough. I'm sorry but I'm done with all of your excuses. It seems that your heart and mind are not in the right place here at our company. I'm truly sorry, but I believe I'm going to have to let you go.\n" + name + ": What?\nBoss: Thank you for the work you have done here, and I wish you the best moving forward.\n.\n.\n.\nOops. It seems you have been fired.\n"
                                                            typewriter()
                                                            answer = input("Press [x] to put down the phone.\n")
                                                            if answer == "x":
                                                                os.system("cls")
                                                                message = "You put down the phone, filled with shock, anger and resentment.\nIn this state of mind, you're unsure whether you should attend your girlfriend's party as you don't want to cause any trouble there.\nDo you attend the party?\n"
                                                                typewriter()
                                                                answer = input("[x] Yes\n[c] No\n")
                                                                if answer == "x":
                                                                    os.system("cls")
                                                                    message = "You decide to attend the party. You search your closet and find a shirt that says 'Can Hack Bramp'.\nIt's the perfect thing to wear.\n"
                                                                    typewriter()
                                                                    shirt()
                                                                    time.sleep(SLEEP_AFTER_ASCII)
                                                                    answer = input("Press [x] to join your girlfriend at the party\n")
                                                                    if answer == "x":
                                                                        os.system("cls")
                                                                        message = "You enter the restaurant and see that everyone has already arrived.\nEveryone enjoys the night, especially your girlfriend.\nYou yourself have had quite a few bottles that night.\nBut it has finally reached the time to return home.\nOne of your girlfriend's friends stares at her leftovers, then reaches into her bag, and pulls out some reusable containers, and packs her food away.\nThis makes your drunken self angry, as you still feel the internal guilt from lying to your boss and getting fired.\n" + name + ": Look at you Becky, taking all your food home in those little, overpriced 'reusable' containers.\nWhy not just waste the rest of your meal like the rest of us?\nAll this eco-friendly stuff is just a bunch of nonsense.\nI don't know why people care so much, all it does is make people lie and lose their jobs!\n.\n.\n.\nEveryone is shocked at your reaction.\nYour girlfriend, especially, looks as if she is about to burst into tears.\nAngrily, you storm out of the restaurant and drive back home.\n"
                                                                        typewriter()
                                                                        answer = input("Press [x] to go to bed.\n")
                                                                        if answer == "x":
                                                                            os.system("cls")
                                                                            answer = input("Press [x] to end the game.\n")
                                                                            if answer == "x":
                                                                                os.system("cls")
                                                                                message = ".\n.\n.\nEvery time we are encouraged to make a change, we always think to ourselves: what good does it make if only one person changes?\nWhat we don't realize, however, is that if everyone took it upon themselves to make a change, good change would happen.\nSurprise " + name + "!\nIn this game, not only were you representing yourself, but you were representing the entire world's population.\nBut the problem is, you didn't really take good actions.\nYou chose to skip out on the conference, not conduct an research, and waste all your food at a restaurant.\nAs you can see, many of the decisions you made weren't entirely eco-friendly.\nAnd though this may not seem like an issue if one person acts this way, think again.\nIf everyone thought of themselves as one person making poor decisions, where would the world be today?\nI'm sorry " + name + ", but you lost the game.\nYour decisions, when placed on a global scale, lead the world down a path of destruction and deterioration.\nAnd as far as I know, the world we live in today is not on a path to recoverey\nThank you for playing, and we wish you the best on your journey to save the world.\nTHE END\n"
                                                                                typewriter()
                                                                                
                                                                            else:
                                                                                ending()
                                                                        else:
                                                                            ending()
                                                                    else:
                                                                        ending()




                                                                elif answer == "c":
                                                                    os.system("cls")
                                                                    message = "You decide not to attend the party, and you decide to go for a walk instead.\nEventually, you come across a convenience store and you decide to enter.\nYou entered the convenience store and left with a bag of alcohol in your hand. You take a seat on the bench, and begin to attempt to drink your problems away.\nHow will you get a new job?\nHow will you deal with your girlfriend after missing her party?\nNone of these questions were answered during your drinking session.\nAs you walked home, you feld that the bag of empty bottles was getting heavy.\nYou could throw the entire contraption in the trashcan right next to you, or you could walk about 50 metres to the recycling can.\nDo you...\n"
                                                                    typewriter()
                                                                    answer = input("[x] Recycle\n[c] Toss it in the trash\n")
                                                                    if answer == "x":
                                                                        os.system("cls")
                                                                        message = "As you reach the recycling bin, a poster catches your attention and moves you to tears.\nYou learn about the environmental effects of using non-recyclable products, and the extinction of wildlife and plantlife that has resulted because of such.\nYou feel proud to be recycling your bottles and bags right now.\nBut you also feel tired so you head home and pass out.\n"
                                                                        typewriter()
                                                                        answer = input("It has been a long 5 days.\nPress [x] to end the game\n")
                                                                        if answer == "x":
                                                                            os.system("cls")
                                                                            message = ".\n.\n.\nEvery time we are encouraged to make a change, we always think to ourselves: what good does it make if only one person changes?\nWhat we don't realize, however, is that if everyone took it upon themselves to make a change, good change would happen.\nSurprise " + name + "!\nIn this game, not only were you representing yourself, but you were representing the entire world's population.\nBut the problem is, you didn't really make good change.\nSure, you made some environmentally conscious decisions, but, like we mentioned earlier, if everyone took it upon themselves to make a change, big change would happen.\nSo sure, you may have skipped out on the party, where you would have probably wasted some food, but it seems that you yourself have not made enough eco-friendly decisions to follow a sustainable lifestyle.\nSo, I'm sorry " + name + ", but you lost the game.\nThank you for playing, and we wish you the best on your journey to save the world.\nTHE END\n"
                                                                            typewriter()
                                                                            
                                                                        else:
                                                                            ending()
                                                                    elif answer == "c":
                                                                        os.system("cls")
                                                                        message = "You toss the drink in the trash. You feel guilty. \nThis is a decision that your boss would not approve of.\n.\nYou eventually reach home. With feelings of drunkenness and guilt weighing down your body,\nyou decide it's best to fall asleep.\n"
                                                                        typewriter()
                                                                        answer = input("Press [x] to fall asleep.\n")
                                                                        if answer == "x":
                                                                            os.system("cls")
                                                                            message = "It has been a long 5 days.\n"
                                                                            typewriter()
                                                                            answer = input("Press [x] to end the game.\n")
                                                                            if answer == "x":
                                                                                os.system("cls")
                                                                                message = ".\n.\n.\nEvery time we are encouraged to make a change, we always think to ourselves: what good does it make if only one person changes?\nWhat we don't realize, however, is that if everyone took it upon themselves to make a change, good change would happen.\nSurprise " + name + "!\nIn this game, not only were you representing yourself, but you were representing the entire world's population.\n.\nBut the problem is, you didn't really take good actions. \nYou chose to skip out on the conference, not conduct any research, and throw all your recyclable items in the trash.\n As you can see, many of the decisions you made weren't entirely eco-friendly.\n And though this may not seem like an issue if one person acts this way, think again.\nIf everyone thought of themselves as one person making poor decisions, where would the world be today?\n.\nI'm sorry " + name + ", but you lost the game.\n Your decisions, when placed on a global scale, lead the world down an unsettling path of environmental deterioration and destruction.\n.\nThank you for playing, and we wish you the best on your journey to save the world.\n.\nTHE END\n"
                                                                                typewriter()
                                                                                
                                                                            else:
                                                                                ending()

                                                                        else:
                                                                            ending()

                                                                    else:
                                                                        ending()



                                                                else:
                                                                    ending()
                                                            else:
                                                                ending()
                                                        else:
                                                            ending() 
                                                    else:
                                                        ending()

                                                else:
                                                    ending()








                                            else:
                                                ending()
                                        else:
                                            ending()





                                    else:
                                        ending()
                                else:
                                    ending()
                            else:
                                ending()
                            





                        else:
                            ending()
                    else:
                        ending()
                else:
                    ending()    
            else: 
                ending()
        else:
            ending()
    else:
        ending()
else:
    ending()
