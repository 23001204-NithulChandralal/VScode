#Exercise 1 

import random

def hiddenBoard():
    boardList = []
    for _ in range(5):
        num = random.randint(0, 8)
        boardList.append(num)
    return boardList

def guesses(guess, board):
    feedback = []
    for i in range(5):  # Adjust the range to match the length of the boardList
        if guess[i] == board[i]:
            feedback.append("Black")
        elif guess[i] in board:
            feedback.append("White")
        else:
            feedback.append("None")
    return feedback

def check(guess):
    if len(guess) != 5:
        print("Please enter exactly 5 numbers.")
        return False
    for num in guess:
        if not num.isdigit() or int(num) < 0 or int(num) > 8:
            print("Enter numbers between 0 and 8 only.")
            return False
    return True

board = hiddenBoard()
print("Hidden Board:", board)

x = 0 
while x < 7:
    x = x + 1
    guess = input("Enter a guess (5 numbers between 0 and 8 separated by spaces): ").split()
    if check(guess):
        guess = [int(num) for num in guess]  # Convert input to integers
        num_feedback = guesses(guess, board)
        print("Feedback:", num_feedback)
        if num_feedback.count("Black") == 5:
            print("Congratulations! You guessed all numbers correctly!")
            break
    else:
        print("Invalid input for guess.")

if x == 7:
    print("You have reached the maximum number of guesses. The hidden board was:", board)
