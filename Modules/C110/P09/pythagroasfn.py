"""
Exercise 2 
use the function to compute the length of the hypotenuse, and displays the result.
"""

def findHypotenuse(a,b):
    hyp = (a**2 + b**2 )** (1/2)
    return hyp 


a = float((input("Enter side 1:")))
b = float((input("Enter side 2:")))
hyp = findHypotenuse(a,b)
print("hypotenuse =",hyp )