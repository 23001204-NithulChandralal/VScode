"""
A program that reads a letter of the alphabet
"""

letter = input("Enter a letter:")

if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
    print ("Letter is a vowel")
elif letter == "y" :
    print ("Sometimes y is a vowel and sometimes a consonant")
else :
    print ("Letter is a consonant")