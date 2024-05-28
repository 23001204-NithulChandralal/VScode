def countChar(word):
    return len(word)

def main():
    wordList = []
    word = input("Enter a word, or type '.' to finish: ")
    
    while word != ".":
        wordList.append(word)
        word = input("Enter a word, or type '.' to finish: ")

    if len(wordList) == 0:
        print("No words entered.")
    else:
        print("Number of characters for each word:")
        for word in wordList:
            char_count = countChar(word)
            print(word,":", char_count)

main()
