import random
import time
from colorama import init, Fore, Back, Style
name=input(Fore.BLACK+Style.BRIGHT+"Please enter your first name:\n"+Style.RESET_ALL).capitalize().strip()
#List of comments
good_comments=[Fore.GREEN+"Perfect"+Style.RESET_ALL,Fore.GREEN+"Nice! Outsmarted me again!"+Style.RESET_ALL,Fore.GREEN+"Amazing work"+Style.RESET_ALL, Fore.GREEN+"You're on fire"+Style.RESET_ALL, Fore.GREEN+"You tricked me!!"+Style.RESET_ALL, Fore.GREEN+"That was clever"+Style.RESET_ALL, Fore.GREEN+"You fooled me!"+Style.RESET_ALL, Fore.GREEN+"Good thinking!"+Style.RESET_ALL, Fore.GREEN+"You're doing great!"+Style.RESET_ALL]
bad_comments=[Fore.RED+"Oops, not close"+Style.RESET_ALL, Fore.RED+"You missed it"+Style.RESET_ALL, Fore.RED+ "Keep trying"+Style.RESET_ALL, Fore.RED+ "well tried"+Style.RESET_ALL, Fore.RED+ "Try to focus"+Style.RESET_ALL, Fore.RED+ "Not quite."+Style.RESET_ALL, Fore.RED+ "Nope, wrong one."+Style.RESET_ALL, Fore.RED+"Better luck next time."+Style.RESET_ALL, Fore.RED+"Think harder!"+Style.RESET_ALL]

#===================================================================================================================================
#===================================================      Guess & Strike game       ================================================
#===================================================================================================================================

#Introduction of the game
print(Style.BRIGHT+Fore.WHITE+f"{name}!!! Welcome to the Guess and Strike Game\nIn this game, you and the program take turns. \nWhen it's your turn to strike, you’ll enter a number between 1 and 5. The program will try to guess your number.\nIf it guesses correctly, you're out.\nIf it guesses wrong, your number is added to your score.\nWhen it's the program's turn to strike, your score is saved and you try to guess the program’s number. Same thing will happen when the prgram scores. \nThe player with the higher score wins the game!"+Style.RESET_ALL)
#This is the function that controls rounds of the game. It controls one round at a time 
def play_turn(user_turn,target_score=None):
    times_gotcorrect=0      #number of succesful rounds played before getting out
    score=0     #Total score of the round
    got_out=False       #This is to check if the player got out during this round
    #Splitting into different sections based on the player type(eg:user or the program)
    if user_turn:
        print("Now you are striking.")
        if target_score is not None:
            print(Style.BRIGHT+Fore.BLACK+f"Your target is {target_score}."+Style.RESET_ALL)
    else:
        print("Now you are guessing the program's number.")
        if target_score is not None:
            print(Style.BRIGHT+Fore.BLACK+f"Try to guess the number before the program strikes more than your score. The program's target is {target_score}"+Style.RESET_ALL)
    #main loop for the turn
    while True:
        #check if the target score is reached only if there is a target score
        if target_score is not None:
            if user_turn and score>=target_score:
                break
            if not user_turn and score>=target_score:
                break
        #program randomly selects a number
        guess=random.randint(1,5)
        try:
            #user iput a number between 1 and 5
            input_no=int(input(Fore.BLUE+"Enter a number between 1-5:"+Style.RESET_ALL))
            if 0<input_no<6:
                if user_turn:
                    #check if the program has guesed the number
                    if guess==input_no:
                        print(Style.BRIGHT+Fore.RED+f"The program guessed it. You are out!!! \n{score} is your final score. {times_gotcorrect} is how many times you have played the game without letting the program guess your number"+Style.RESET_ALL)
                        got_out=True
                        break
                    else:
                        print("The program didn't guess it. {} is what the program guesssed".format(guess))
                        score+=input_no
                        #print a good comment from the list
                        if target_score is None or score<target_score:
                            print(random.choice(good_comments))
                        times_gotcorrect+=1
                else:
                    #check if the user has guessed the program's number
                    if guess==input_no:
                        print(Style.BRIGHT+Fore.YELLOW+f"You guessed the correct number. The program is out!!!\n{score} is the program's final score. {times_gotcorrect} is how many times the program has played without letting you guess its number"+Style.RESET_ALL)
                        got_out=True
                        break
                    else:
                        print("Your guess is wrong. {} is what the program thought".format(guess))
                        score+=guess
                        #print a bad comment
                        if target_score is None or score<target_score:
                            print(random.choice(bad_comments))
                        times_gotcorrect+=1
            #Tell the user to enter a number between 1-5 if the user enter something less than 1 or a higher no than 5
            else:
                print(Fore.WHITE+"please enter a number between 1-5"+Style.RESET_ALL)
        #Show value error if there is
        except ValueError:
            print("Invalid input")
    return score,got_out #Return values
play="yes" #Store play as yes
#loop until the play equals yes or y because at the end of the first round, the user is asked if they want to play the game again
while play=="yes"or play=="y":
    while True:
        try:
            #Ask the user if they want to strike or guess first
            selction=input(Style.BRIGHT+Fore.BLACK+"What do you wanna do first? If you wanna strike frst, please type 1. If you wanna guess the program's number first, please type 2."+Style.RESET_ALL).strip()
            if selction=="1":
                #user strikes first
                user_score, user_out=play_turn(user_turn=True)
                program_score, program_out=play_turn(user_turn=False, target_score=user_score+1)
                break
            elif selction=="2":
                #user guesses first
                program_score,program_out=play_turn(user_turn=False)
                user_score,user_out=play_turn(user_turn=True, target_score=program_score+1)
                break
            else:
                print(Fore.RED+"Please enter 1 or 2"+Style.RESET_ALL)
        except ValueError:
            print(Fore.RED+"Invalid input"+Style.RESET_ALL)
    #Announce the game winner
    if user_score>program_score:
        #announce that the user is the winner without saying the difference as the user is not still out
        if not user_out:
            print(Fore.CYAN+f"Congratulations you won this game without getting out!!! {user_score} is your score and {program_score} is the program's score."+Style.RESET_ALL)
        #Announce that the user is the winner with the differece
        else:
            print(Fore.CYAN+f"Congratulations you won this game!!!!. You won by {user_score-program_score} runs"+Style.RESET_ALL)
    #Say that the game is a tie if scores are equal
    elif user_score==program_score:        
        print(Fore.CYAN+"The game is drawn. Great effort!!!"+Style.RESET_ALL)
    else:
        if not program_out:
        #announce that the program is the winner without saying the difference as the program is not still out
            print(Fore.CYAN+f"The program win the game without getting out {user_score} is your score and {program_score} is the program's score."+Style.RESET_ALL)
        #Announce that the program is the winner with the differece
        else:
            print(Fore.CYAN+f"You lost this game!!!!. You lost by {program_score-user_score} runs"+Style.RESET_ALL)
    #Ask the user to play again
    while True:
        play=input(Fore.BLACK+"Do you want to play again? (Yes/No):"+Style.RESET_ALL).lower()
        #Check if the user input is either yes or no or y or n
        if play in ["yes","no","y","n"]:
            break
        else:
            print(Fore.RED+"Please enter yes or no"+Style.RESET_ALL)
#Thank you message at the end
print(Fore.MAGENTA+"Thank you very much for playing this game!!!"+Style.RESET_ALL)

#===================================================================================================================================
#========================================================    Jumanji    ============================================================
#===================================================================================================================================

#Introduction of the game
print(f"\n\n{name} Welcome to Jumanji\n\nIn this game, you’ll face a series of wild and dangerous challenges. First you will chose your character wisely, your survival will depend on their unique strength and weakness.")
time.sleep(0.5)
print("\nYou have 3 lives and 2 skips, which let you avoid a challenge if things get too risky.\nTo escape the world of Jumanji, you must successfully overcome 6 different challenges. Make smart choices, use your skills carefully, and stay alive.\n\n")
time.sleep(0.75)
#List of characters
Character=[
    {"name":"Dr. Smolder Bravestone", "skill":"Strength", "weakness":"None"},
    {"name":"Ruby Roundhouse", "skill":"Agility", "weakness":"Spiders"},
    {"name":"Franklin “Mouse” Finbar", "skill":"Animal Handling", "weakness":"Snakes"},
    {"name":"Prof. Shelly Oberon", "skill":"Intelligence", "weakness":"Endurance"},
    {"name":"Ming Fleetfoot", "skill":"Stealth", "weakness":"Switchblades"},
    {"name":"Blaze Rockwell", "skill":"Fire Knowledge", "weakness":"Water"},
    {"name":"Rex Vortex", "skill":"Speed", "weakness":"Slippery terrain"},
    ]
#List of events with options and the right decision for each character type.   
events = [
    {
        "name":"Rhino attack",
        "description":"A herd of rhinos is attacking you!",
        "options":{
            "Throw rocks to intimidate":"Strength",
            "Climb a tree":"Agility",
            "Whistle to birds to distract rhinos":"Animal Handling",
            "Study herd movement to time a safe path":"Intelligence",
            "Hide behind vines":"Stealth",
            "Use fire to scare them away":"Fire Knowledge",
            "Dash sideways and sprint":"Speed"
        }
    },
    {
    "name":"Spider Lair",
    "description":"Venomous spiders hang in webs all around the path ahead.",
    "options":{
        "Knock webs down with a branch":"Strength",
        "Send birds to distract the spiders":"Animal Handling",
        "Observe the safest web-free path":"Intelligence",
        "Sneak slowly and quietly through shadows":"Stealth",
        "Burn outer webs to create a path":"Fire Knowledge",
        "Sprint past before they react":"Speed",
        },
    "danger":"Ruby Roundhouse"
    },
    {
    "name":"Snake Pit Crossing",
    "description":"A shallow ravine filled with coiled snakes separates you from the only exit path.!",
    "options":{
        "Throw a large rock to scatter the snakes":"Strength",
        "To balance along tree branch to bridge pit":"Agility",
        "Whistle to alert nearby mongooses to attack the snakes":"Animal Handling",
        "Identify the least hostile species and steer clear of them":"Intelligence",
        "Crawl silently through vegetation to stay unseen":"Stealth",
        "Burn dry leaves to send smoke over the snakes":"Fire Knowledge",
        "Run across exposed roots in one smooth motion":"Speed"
        },
    "danger":"Ruby Roundhouse"
    },
    {
    "name":"Flash Flood Warning",
    "description":"A wall of water surges down the valley.",
    "options":{
        "Stack debris to block and redirect the current":"Strength",
        "Scale a banyan tree to reach higher ground":"Agility",
        "Follow frogs and other animals to get to safe area.":"Animal Handling",
        "Identify the terrain slope to find the flood's weakest path":"Intelligence",
        "Slide behind a thick boulder and brace for impact":"Stealth",
        "Find a slope or ridge and sprint to it":"Speed"
        },
    "danger":"Blaze Rockwell"
    },
    {
    "name":"Foggy Ravine",
    "description":"A dense fog obscures a ravine. If you cross it wrong, you will fall down.",
    "options":{
        "Throw a tree trunk to create a makeshift bridge":"Strength",
        "Swing across the ravine using hanging vines":"Agility",
        "Send a trained monkey across with rope to form a tightrope bridge":"Animal Handling",
        "Throw small stones and listen to echoes to locate the narrowest crossing point and jump over it":"Intelligence",
        "Climb into the ravine and sneak through a hidden animal trail below":"Stealth",
        "Burn off moss and vines to expose better footing parts of the rock":"Fire Knowledge"
        },
    "danger":"Rex Vortex"
    },
    {
    "name":"Blade Trap Corridor",
    "description":"Blades swing rhythmically through a narrow stone hallway.",
    "options":{
        "Stick a broken spear into the trap to stop it moving":"Strength",
        "Roll and duck under the blades at the right time":"Agility",
        "Send a trained raccoon to walk ahead and trigger the traps":"Animal Handling",
        "Count how the blades move and step through when it’s safe":"Intelligence",
        "Use fire to damage the trap to make the metal bend and stop":"Fire Knowledge",
        "Wait for the right moment and sprint across before the blades swing again.":"Speed"
        },
    "danger":"Ming Fleetfoot"
    },
    {
    "name":"Sinking Sand Pit",
    "description":"The ground beneath you suddenly gives way. You’re caught in quicksand!",
    "options":{
        "Grab a vine and pull yourself out with all your strength":"Strength",
        "Leap to a tree root just before you sink, then pull yourself out using quick, light movements":"Agility",
        "Use hand signals to send a trained monkey to tie a vine around a branch":"Animal Handling",
        "Slowly change how your body is balanced and slide toward a hidden burrow under leaves":"Stealth",
        "Burn dry vines to uncover a buried plank you can use to escape":"Fire Knowledge",
        "Use nearby rocks to quickly step over it":"Speed"
        },
    "danger":"Prof. Shelly Oberon"
    
}
]
#ask the user to choose a character
def character_selection():
    print("Here are the charcaters you can choose:")
    time.sleep(1)
    for i in range (len(Character)):
        print(f"{i+1}. {Character[i]['name']} (Skills:{Character[i]['skill']}, Weakness:{Character[i]['weakness']})")
    time.sleep(0.25)
    while True:
        user_character=input("\nEnter the number of your character:\n")
        try:
            if 0<int(user_character)<=(len(Character)):
                return Character[int(user_character)-1]
            else:
                print("Not an option")
        except:
            print("Invalid input")
selected_character=character_selection()
complete=0
lives=3
quit=2
time.sleep(0.75)
print(f"\n\n{selected_character['name']} is the character you chose. \n\nSkill of your character: {selected_character['skill']}\nWeakness of your character: {selected_character['weakness']}")
time.sleep(0.25)
print("\nYou have to sucessfully complete 5 challenges before you lose 3 lives. You also have a chance to skip 2 challenges")
time.sleep(1)
print("Remember every action matters!\n\n")
input("Press enter to start the game")
time.sleep(2.5)
while complete<5 and lives>0:
    event=random.choice(events)
    def game_events():
        print(f"\n\nNAME:  {event['name']}\nDESCRIPTION:  {event['description']}\n")
        correct_option=None
        wrong_options=[]
        for desc_event,skill in event['options'].items():
            if skill==selected_character['skill']:
                correct_option=desc_event
            else:
                wrong_options.append(desc_event)
        random.shuffle(wrong_options)
        if correct_option==None:
            selected_options=[]+wrong_options[:4]
        else:
            selected_options=[correct_option]+wrong_options[:3]
        random.shuffle(selected_options)
        for i in range (len(selected_options)):
            print(f"{i+1}. {selected_options[i]}")
        return selected_options, correct_option
    selected_options, correct_option=game_events()
    while True:
        try:
            user_decision=input("\nPlease enter the number of your choice(1-4). \nIf you have skips remaining and want to skip this challenge please try typing skip or 5\n")
            print("")
            time.sleep(1)
            #Evaluating the answer
            if user_decision=='5' or user_decision=='skip':
                if quit>0:
                    quit-=1
                    print(f"You skipped the challenge. {quit} is the number of skips remaining")
                    time.sleep(3)
                    break
                else:
                    print("You have alredy skiped 2 times, so you have 0 skips remaining.")
            elif event.get("danger")==selected_character["name"]:
                print("❌You failed this challenge.\nYour character's weakness was triggered in this event.")
                time.sleep(3)
                break
            elif user_decision.isdigit():
                user_decision=int(user_decision)
                if 0<(user_decision)<=4:
                    chosen_action=selected_options[int(user_decision)-1]
                    if correct_option==chosen_action:
                        time.sleep(1)
                        print("🎉You have succefully completed this challenge\n\n")
                        time.sleep(3)
                        complete+=1
                        break
                    else:
                        time.sleep(1)
                        print("❌You failed this challenge.")
                        lives-=1
                        if lives>1:
                            print(f"You lost a life. 💔 Only {lives} lives are remaining.\n\n")
                            time.sleep(3)
                        else:
                            print(f"You lost a life. 💔 Only {lives} life is remaining.\n\n")
                            time.sleep(3)
                        break
                else:
                    print("Enter a number between 1-4")
        except:
            print("Invalid input")
if complete==5:
    print("Congratulations 🎉🎉🎉 You survived all stages and escaped Jumanji. Well done!!!!")
else:
    print("💀You were defeated by the wild world of Jumanji....")
