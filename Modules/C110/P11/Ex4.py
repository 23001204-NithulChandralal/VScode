"""
Write a program that implements a simple sentiment 
analysis of a given paragraph. Assume these 
paragraphs are collected from online surveys.
"""
posList = ['brilliant', 'loved', 'happy']
negList = ['dissatisfied', 'worst', 'terrible']


paragraph = input("Enter the paragraph: ")
words = paragraph.lower().split()
positive_count = 0
negative_count = 0


for i in words:
    if i in posList:
        positive_count = positive_count + 1
    elif i in negList:
        negative_count = negative_count + 1

# Determine the sentiment
if positive_count > negative_count:
    print("Positive")
elif negative_count > positive_count:
    print("Negative")
else:
    print("Neutral")


