# """A number-guessing game."""

# Put your code here
import random

# greet player
name = input("Hey! What is your name? ")

# get player name
print(f"{name}, I'm thinking of a number between 1 and 100")

# choose random number between 1 and 100
number = random.randint(1, 99)

# repeat forever:
#     get guess
print("Do you think you can guess it?")
guess = int(input("What is your guess? "))

#     if guess is incorrect:
#         give hint
#         increase number of guesses
n = 1
while number != guess:
    n = n + 1

    if guess < number:
        print("Your number is too low...try again.")
        guess = int(input("What is your guess? "))

    elif guess > number:
        print("Your number is too high...try again.")
        guess = int(input("What is your guess? "))
#      else:
#         congratulate player
    else:      
        break
    
print("Great job, " +name +"! You guessed my number in " +str(n) + " tries!")

        
