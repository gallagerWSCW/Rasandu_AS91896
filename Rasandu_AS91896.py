import random
good_comments=["Perfect","Nice! Outsmarted me again!","Amazing work", "You're on fire", "You tricked me!!", "That was clever", "You fooled me!", "Good thinking!", "You're doing great!"]
bad_comments=["Oops, not close", "you missed it", "Keep trying", "well tried", "Try to focus", "Not quite.", "Nope, wrong one.", "Better luck next time.", "Think harder!", ]
print("Welcome to the Guess & Strike game")
print("In this game, you and the program take turns. \nWhen it's your turn to strike, you’ll enter a number between 1 and 5. The program will try to guess your number.\nIf it guesses correctly, you're out.\nIf it guesses wrong, your number is added to your score.\nWhen it's the program's turn to strike, your score is saved and you try to guess the program’s number. Same thing will happen when the prgram scores. \nThe player with the higher score wins the game!")
def play_turn(user_turn,target_score=None):
    times_gotcorrect=0
    score=0
    got_out=False
    if user_turn:
        print("Now you are striking.")
        if target_score is not None:
            print("Your target is {}.".format(target_score))
    else:
        print("Now you are guessing the program's number.")
        if target_score is not None:
            print("Try to guess the number before the program strikes more than your score. The program's target is {}".format(target_score))
    while True:
        if target_score is not None:
            if user_turn and score>=target_score:
                break
            if not user_turn and score>=target_score:
                break
        guess=random.randint(1,5)
        try:
            input_no=int(input("Enter a number between 1-5:"))
            if 0<input_no<6:
                if user_turn:
                    if guess==input_no:
                        print("The program guessed it. You are out!!! \n{} is your final score. {} is how many times you have played the game without letting the program guess your number".format(score,times_gotcorrect))
                        got_out=True
                        break
                    else:
                        print("The program didn't guess it. {} is what the program guesssed".format(guess))
                        score+=input_no
                        if target_score is None or score<target_score:
                            print(random.choice(good_comments))
                        times_gotcorrect+=1
                else:
                    if guess==input_no:
                        print("You guessed the correct number. The program is out!!!\n{} is the program's final score. {} is how many times the program has played without letting you guess its number".format(score,times_gotcorrect))
                        got_out=True
                        break
                    else:
                        print("Your guess is wrong. {} is what the program thought".format(guess))
                        score+=guess
                        if target_score is None or score<target_score:
                            print(random.choice(bad_comments))
                        times_gotcorrect+=1
            else:
                print("please enter a number between 1-5")
        except ValueError:
            print("Invalid input")
    return score,got_out
play="yes"
while play=="yes"or play=="y":
    while True:
        try:
            selction=input("What do you wanna do first? If you wanna strike frst, please type 1. If you wanna guess the program's number first, please type 2.").strip()
            if selction=="1":
                user_score, user_out=play_turn(user_turn=True)
                program_score, program_out=play_turn(user_turn=False, target_score=user_score+1)
                break
            elif selction=="2":
                program_score,program_out=play_turn(user_turn=False)
                user_score,user_out=play_turn(user_turn=True, target_score=program_score+1)
                break
            else:
                print("Please enter 1 or 2")
        except ValueError:
            print("Invalid input")

    if user_score>program_score:
        if not user_out:
            print(f"Congratulations you won this game without getting out!!! {user_score} is your score and {program_score} is the program's score.")
        else:
            print("Congratulations you won this game!!!!. You won by {} runs".format(user_score-program_score))
    elif user_score==program_score:        
        print("The game is drawn. Great effort!!!")
    else:
        if not program_out:
            print(f"The program win the game without getting out {user_score} is your score and {program_score} is the program's score.")
        else:
            print("You lost this game!!!!. You lost by {} runs".format(program_score-user_score))
    while True:
        play=input("Do you want to play again? (Yes/No):").lower()
        if play in ["yes","no","y","n"]:
            break
        else:
            print("Please enter yes or no")
print("Thank you very much for playing this game!!!")

