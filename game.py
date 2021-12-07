"""A number-guessing game."""

# Put your code here
import random

# greet player
name = input("Hey! What is your name? ")

# get player name
print(f"{name}, I'm thinking of a number between 1 and 100")

# choose random number between 1 and 100
number = random.randint(1, 100)
print (number)
# repeat forever:
#     get guess
#     if guess is incorrect:
#         give hint
#         increase number of guesses
#     else:
#         congratulate player
