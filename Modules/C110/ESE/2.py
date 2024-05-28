word = input("Enter the string:")
characters = list(word.lower())
firstletter = word[0]

if firstletter == "a" or firstletter == "e" or firstletter == "i" or firstletter == "o" or firstletter == "u":
    for char in characters:
        print(char)
