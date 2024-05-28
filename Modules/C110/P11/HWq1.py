"""
Homeowork Question 1 
1.	Write a program that reads and stores words entered by a user into a List called wordList until "." is keyed in. Display the number of characters for each word in wordList in ascending alphabetical order. An example of the program’s execution is as follows: 
"""
wordList = []


word = input("Enter a word: ")
while word != ".":
    wordList.append(word)
    word = input("Enter a word: ")

wordList.sort()

for word in wordList:
    if len(word) < 5:
        print(word, len(word))
