"""
Write a program that reads a word and iterates 
through each character of the word and displays their 
ASCII values
"""
word = input("Enter a word: ")

for word in word:
    ascii = ord(word)
    print(word,"-",ascii)
