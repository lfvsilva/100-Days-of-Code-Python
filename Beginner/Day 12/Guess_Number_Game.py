from art import logo
import random
import subprocess

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

def game(attempts):
    number = random.randint(1, 100)
    while attempts > 0:
        print(f"You have {attempts} remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if guess == number:
            print(f"You got it! The answer was {number}")
            return
        elif guess < number:
            print(f"Too low.")
        else:
            print("Too high.")
        attempts -= 1
    print("You've run out of guesses.")

playing = True
while playing:
    subprocess.call("cls||clear", shell=True)
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if(difficulty == "easy"):
        game(attempts=EASY_ATTEMPTS)
    elif(difficulty == "hard"):
        game(attempts=HARD_ATTEMPTS)

    playing = input("Wan't play again? Type 'y' or 'n'") == "y"
