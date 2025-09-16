from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")
difficultly = input("Choose a difficulty. Type 'easy' or 'hard': ")

lives = 0
num_to_guess = random.choice(range(1, 101))
active = True

def set_difficulty():
    global lives
    if difficultly == "easy":
        lives = 10
    else:
        lives = 5

def check_answer(user_guess, num_to_guess, turns):
    if user_guess > num_to_guess:
        print("Too high.")
        return turns - 1
    elif user_guess < num_to_guess:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {num_to_guess}")
        return turns

set_difficulty()

while active:
    print(f'You have {lives} attempts remaining to guess the number.')
    guess = int(input("Make a guess: "))
    lives = check_answer(guess, num_to_guess, lives)

    if guess == num_to_guess:
        active = False
    elif lives == 0:
        print(f"You ran out of lives. You lose. The correct answer was {num_to_guess}.")
        active = False
    else:
        print("Guess again.")
