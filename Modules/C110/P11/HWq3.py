"""
Homework Question 3
3.	Given the following List:
paint = ["red", "blue", "black", "yellow", "green"]

Write a program with a loop that allows a user to specify the text to search in the variable paint.  If there are colour(s) found, it will print the colour(s) that contain the search text.  Otherwise, it will print “No such colour” once.
"""

paint = ["red", "blue", "black", "yellow", "green"]
search_text = input("Enter search text: ")

found_colours = []
for colour in paint:
    if search_text in colour:
        found_colours.append(colour)

if found_colours:
    for colour in found_colours:
        print(colour)
else:
    print("No such colour")

