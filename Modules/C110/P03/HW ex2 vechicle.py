"""
Homework Exercise 2. vehicle fuel efficiency in US to Singapore
"""

#input
US = float(input("Enter vehicle fuel efficiency in US:"))

#Calculation 
KM = US * 1.609
SG = KM/3.78

#Display
print("The fuel efficiency in Singapore will be", round(SG,2),"km/l")