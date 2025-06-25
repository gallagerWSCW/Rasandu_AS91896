import random
#List of comments
good_comments=["Perfect","Nice! Outsmarted me again!","Amazing work", "You're on fire", "You tricked me!!", "That was clever", "You fooled me!", "Good thinking!", "You're doing great!"]
bad_comments=["Oops, not close", "You missed it", "Keep trying", "well tried", "Try to focus", "Not quite.", "Nope, wrong one.", "Better luck next time.", "Think harder!"]
#Introduction of the game
print("In this game, you and the program take turns. \nWhen it's your turn to strike, you’ll enter a number between 1 and 5. The program will try to guess your number.\nIf it guesses correctly, you're out.\nIf it guesses wrong, your number is added to your score.\nWhen it's the program's turn to strike, your score is saved and you try to guess the program’s number. Same thing will happen when the prgram scores. \nThe player with the higher score wins the game!")
#This is the function that controls rounds of the game. It controls one round at a time 
def play_turn(user_turn,target_score=None):
    times_gotcorrect=0      #number of succesful rounds played before getting out
    score=0     #Total score of the round
    got_out=False       #This is to check if the player got out during this round
    #Splitting into different sections based on the player type(eg:user or the program)
    if user_turn:
        print("Now you are striking.")
        if target_score is not None:
            print("Your target is {}.".format(target_score))
    else:
        print("Now you are guessing the program's number.")
        if target_score is not None:
            print("Try to guess the number before the program strikes more than your score. The program's target is {}".format(target_score))
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
            input_no=int(input("Enter a number between 1-5:"))
            if 0<input_no<6:
                if user_turn:
                    #check if the program has guesed the number
                    if guess==input_no:
                        print("The program guessed it. You are out!!! \n{} is your final score. {} is how many times you have played the game without letting the program guess your number".format(score,times_gotcorrect))
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
                        print("You guessed the correct number. The program is out!!!\n{} is the program's final score. {} is how many times the program has played without letting you guess its number".format(score,times_gotcorrect))
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
                print("please enter a number between 1-5")
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
            selction=input("What do you wanna do first? If you wanna strike frst, please type 1. If you wanna guess the program's number first, please type 2.").strip()
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
                print("Please enter 1 or 2")
        except ValueError:
            print("Invalid input")
    #Announce the game winner
    if user_score>program_score:
        #announce that the user is the winner without saying the difference as the user is not still out
        if not user_out:
            print(f"Congratulations you won this game without getting out!!! {user_score} is your score and {program_score} is the program's score.")
        #Announce that the user is the winner with the differece
        else:
            print("Congratulations you won this game!!!!. You won by {} runs".format(user_score-program_score))
    #Say that the game is a tie if scores are equal
    elif user_score==program_score:        
        print("The game is drawn. Great effort!!!")
    else:
        if not program_out:
        #announce that the program is the winner without saying the difference as the program is not still out
            print(f"The program win the game without getting out {user_score} is your score and {program_score} is the program's score.")
        #Announce that the program is the winner with the differece
        else:
            print("You lost this game!!!!. You lost by {} runs".format(program_score-user_score))
    #Ask the user to play again
    while True:
        play=input("Do you want to play again? (Yes/No):").lower()
        #Check if the user input is either yes or no or y or n
        if play in ["yes","no","y","n"]:
            break
        else:
            print("Please enter yes or no")
#Thank you message at the end
print("Thank you very much for playing this game!!!")

