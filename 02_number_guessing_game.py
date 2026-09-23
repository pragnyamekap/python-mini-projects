import random

number = random.randint(1, 50)
guess = 0

while guess != number:
    guess = int(input("Guess the number (1-50): "))
    
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("Correct! You guessed it!")