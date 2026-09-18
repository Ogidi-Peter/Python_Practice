from random import randint


random_digit = randint(1, 100) 

user_selection = int(input("Guess a number"))

while(user_selection):
    if user_selection == random_digit:
        print("You guessed it right")
        break
    elif user_selection < random_digit:
        print("You guessed wrong, try a bigger number")
        user_selection = int(input("Guess a number"))
    else:
        print("You guessed wrong, try a smaller number")
        user_selection = int(input("Guess a number"))
        