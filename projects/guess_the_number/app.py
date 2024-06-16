import random

def guess(x):
    random_number = random.randint(1,x)
    guess,moves_used = 0
    while guess != random_number:
        guess = int(input(f"Guess the number (1,{x}): "))
        moves_used+=1
        if(random_number > guess):
            print("Guess a higher number")
        elif random_number < guess:
            print("Guess a low number.")
        
    print(f"You guess it right. {random_number}")
    print(f"Moves used: {moves_used}")


def computer_guess(x):
    low,high = 1,x
    feedback = ""
    while(feedback != 'c'):
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f"Is {guess} too hight (H) too low (L), or correct (C)??").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
            
    print(f"yay computer guess your number {guess}")

computer_guess(10)
