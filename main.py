# Number Guessing Game Objectives:
import random
from art import logo
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

# Generate a list containing integers from 1 to 100
numbers_list = []
for number in range(1, 101):
    numbers_list.append(number)
# a random number to be guessed
random_num = random.choice(numbers_list)
# print(random_num)
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
# choose the difficulty
difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty_level == "easy":
    attempt = 10
    right_guess = False
    # this keep looping till right_guess = True
    while not right_guess:
        # when user run out of guesses, the program will stop
        # otherwise, it will continue to figure out if user guessed the number and still have more attempts
        if attempt == 0:
            right_guess = True
            print("You've run out of guesses, You lose")
        else:
            print(f"You have {attempt} attempts remaining to guess the number")
            guess = int(input("Make a guess: "))
            if guess < random_num:
                attempt -= 1
                right_guess = False
                print("Too low")
                print("Guess again")
            elif guess > random_num:
                attempt -= 1
                right_guess = False
                print("Too high")
                print("Guess again")
            elif guess == random_num:
                right_guess = True
                print(f"you got it. the answer was {guess}")

elif difficulty_level == "hard":
    attempt = 5
    right_guess = False
    # this keep looping till right_guess = True
    while not right_guess:
        # when user run out of guesses, the program will stop
        # otherwise, it will continue to figure out if user guessed the number and still have more attempts
        if attempt == 0:
            right_guess = True
            print("You've run out of guesses, You lose")
        else:
            print(f"You have {attempt} attempts remaining to guess the number")
            guess = int(input("Make a guess: "))
            if guess < random_num:
                attempt -= 1
                right_guess = False
                print("Too low")
                print("guess again")
            elif guess > random_num:
                attempt -= 1
                right_guess = False
                print("Too high")
                print("guess again")
            elif guess == random_num:
                right_guess = True
                print(f"You got it! The answer was {guess}.")


                
# another version using functions
# from random import randint
#
# easy_level = 10
# hard_level = 5
#
#
# def difficulty():
#     level = input("Choose a difficulty. Type 'easy' or 'hard': ")
#     if level == "easy":
#         return easy_level
#     else:
#         return hard_level
#
#
# def check(guess, answer, num_turns):
#     if guess < answer:
#         print("Too low.")
#         return num_turns - 1
#     elif guess > answer:
#         print("Too high.")
#         return num_turns - 1
#     else:
#         print(f"You got it! The answer was {answer}.")
#
#
# print("Welcome to the Number Gussing Game.")
# print("I'm thinking of a number between 1 and 100.")
# answer = randint(1, 100)
#
#
# # print(f"Pssst, the correct answer is {answer}")
#
# def game():
#     num_turns = difficulty()
#     guess = 0
#     while guess != answer:
#         print(f"You have {num_turns} attempts remaining to guess the number.")
#         guess = int(input("Make a guess: "))
#         num_turns = check(guess, answer, num_turns)
#         if num_turns == 0:
#             print("You've run out of guesses, you lose.")
#             return
#         elif guess != answer:
#             print("Guess again.")
#
#
# game()

