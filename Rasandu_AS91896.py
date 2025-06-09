import random
print("Welcome to the Guess & Strike game")
print("In this game, you and the program take turns. When it's your turn to strike, you’ll enter a number between 1 and 5. The program will try to guess your number.\nIf it guesses correctly, you're out.\nIf it guesses wrong, your number is added to your score.\nWhen it's the program's turn to strike, your score is saved and you try to guess the program’s number. The player who scores more before getting out wins the game!")
def play_turn(user_turn,target_score=None):
    times_gotcorrect=0
    score=0
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
                        print("The program guessed it. You have lost. {} is your final score. {} is how many times you have played it without letting the program guess your number".format(score,times_gotcorrect))
                        break
                    else:
                        print("The program didn't guess it. {} is what the program guesssed".format(guess))
                        score+=input_no
                        times_gotcorrect+=1
                else:
                    if guess==input_no:
                        print("You guessed the correct number. {} is the program's final score. {} is how many times the program has played without letting you guess its number".format(score,times_gotcorrect))
                        break
                    else:
                        print("Your guess is wrong. {} is what the program thought".format(guess))
                        score+=guess
                        times_gotcorrect+=1
            else:
                print("please enter a number between 1-5")
        except ValueError:
            print("Invalid input")
    return score
while True:
    try:
        selction=input("What do you wanna do first? If you wanna strike frst, please type 1. If you wanna guess the program's number first, please type 2.").strip()
        if selction=="1":
            user_score=play_turn(user_turn=True)
            program_score=play_turn(user_turn=False, target_score=user_score+1)
            break
        elif selction=="2":
            program_score=play_turn(user_turn=False)
            user_score=play_turn(user_turn=True, target_score=program_score+1)
            break
        else:
            print("Please enter 1 or 2")
    except ValueError:
        print("Invalid input")
if user_score>program_score:
    print("Congratulations you won this game!!!!. You won by {} runs".format(user_score-program_score))
else:
    print("You lost this game!!!!. You lost by {} runs".format(program_score-user_score))