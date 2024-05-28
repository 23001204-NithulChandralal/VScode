"""
Write a program that reads a word and iterate through 
the word and print out the special characters found if 
they are one of '#', '$'and '%
"""

word = input("Enter a word :")


for i in word:
    if i == "$" or i =='#' or i == "%":
        print("Special character found :", i)


wordlen = len(word)
for j in range(wordlen):
    if word[j] == "$" or word[j] =='#' or word[j] == "%":
        print("Special character found :", word[j], "at index",j)

