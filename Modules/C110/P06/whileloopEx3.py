"""
Write a computer game that plays a number guessing game.
"""
import random
radnom_number = random.randint(0,100)
attempts = 0 

print("Number guessing game!")
print("Im thinking of a number from 0 to 100, Can you guess it?")

while attempts <= 5:
    guess = int(input("Enter your guess:"))
    if guess == radnom_number:
        print("Congrats! You have guessed the number!")
    if guess < radnom_number:
        print("Too Low!")
    else:
        print("Too High!")
    attempts += 1 

print("Sorry, you've reached the maximum number of attempts.")
print("The secret number was",radnom_number ,"Better luck next time!")
    