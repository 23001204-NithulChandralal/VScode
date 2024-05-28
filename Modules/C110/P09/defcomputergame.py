"""
wrote a computer game that plays a number guessing game. The computer will choose a random number between 0 to 100 for a player to guess.
"""
import random

def lol():
    attempts = 0 
    while attempts <= 5:
        guess = int(input("Enter your guess:"))
        attempts += 1 
        if guess == radnom_number:
            print("Congrats! You have guessed the number!")
        if guess < radnom_number:
            print("Too Low!")
        else:
            print("Too High!")
    print("Sorry, you've reached the maximum number of attempts.")
    print("The secret number was",radnom_number ,"Better luck next time!")
radnom_number = random.randint(0,100)


print("Number guessing game!")
print("Im thinking of a number from 0 to 100, Can you guess it?")
lol()
    