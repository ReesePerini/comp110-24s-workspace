"""Number guessing game."""
from random import randint

SECRET: int = randint(1,5)
correct: bool = False

while correct == False:
    guess: int = int(input("Guess a number: "))
    if guess == SECRET:
        print(f"Correct! {guess} is the secret number!")
        correct = True
    elif guess < SECRET:
        print(f"{guess} too low!")
        print("Try again")
    elif guess > SECRET:
        print(f"{guess} too high!")
        print("Try again!")
