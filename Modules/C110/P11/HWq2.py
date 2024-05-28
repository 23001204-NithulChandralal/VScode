paragraph = input("Enter text :")
"""
Homework Q2
2.	Write a Python program that reads a paragraph of text and prints all words in the paragraph that are even in length and a summary of the number of such words against the total number of words in the paragraph.
"""
words = paragraph.split() 
totalwords = len(words)
evenwords = []

for word in words:
    if len(word) % 2 == 0:
        evenwords.append(word)

evenwordscount = len(evenwords)

print("The words with even length are:")
for word in evenwords:
    print(word)
print("Number of even words/total words:",evenwordscount,"/",totalwords)