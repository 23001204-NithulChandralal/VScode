"""
Write a program that will sum the squares of a list of numbers 
starting from 1 to n. The value n is specified by the user
"""

def square(num):
    num2 = num * num 
    return num2

def sum_of_squares(n):
    sum = 0 
    for i in range(1, n+1):
        sum = sum + square(i)
    return sum

n = int(input("Enter value of n :"))
results = sum_of_squares(n)
print("The sum of squares from 1 to",n,"is",results)