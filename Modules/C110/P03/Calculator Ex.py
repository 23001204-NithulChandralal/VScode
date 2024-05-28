"""
Determining the result of each of the followng calculation
"""

#Input
f = float(input("Enter first number :"))
s = float(input("Enter second number :"))

#Calculation
Addition = f + s
Subtraction = f - s
Multiplication = f * s
Division = f/s
Integer_Divison = f//s
Modulus= f % s

#Display Answer
print("Addition =", round(Addition,3))
print("Subtraction =", round(Subtraction,3))
print("Multiplication =", round(Multiplication,3))
print("Division =", round(Division,3))
print("Integer Division =", round(Integer_Divison,3))
print("Modulus =", round(Modulus,3))

