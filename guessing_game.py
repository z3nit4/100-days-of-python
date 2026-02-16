# Goal: The computer picks a random number between 1 - 10, and the user keeps guessing until they get it right.

"""
Pseudocode

Computer picks a random number between 1-10
Tells the user to guess
While they haven't guessed correctly:
    Check if the guess is higher or lower than the number
    Give feedback
    Let them guess again
For loop to give a countdown of remaining attempts
"""

import random

secret_number = random.randint(1, 10)

attempts = 3

print("**************************************")
print("Welcome To The Guessing Game")
print("**************************************")


guess = int(input("Guess the number from 1 - 10: "))

while guess != secret_number:
    if guess > secret_number:
        print("**************************************")
        print("Too high")
    elif guess < secret_number:
        print("**************************************")
        print("Too low")
    
    attempts -= 1
    print(f"You have {attempts} guesses left")
    print("**************************************")

    guess = int(input("Incorrect Guess. Guess again: "))
    
    if attempts == 0:
        print("**************************************")
        print("You are out of guesses. Game over!")
        print("**************************************")
        break

if guess == secret_number:
        print(f"You guessed correctly! The secret number was {secret_number}")

