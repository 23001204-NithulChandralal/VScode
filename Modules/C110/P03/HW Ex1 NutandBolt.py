"""
Homework Exercise 1. Nut and Bolt
"""

#input
Nut = float(input("Enter number of nuts:"))
Bolt = float(input("Enter number of bolts:"))

#Calculations
Nut_weight = Nut * 75 
Bolt_weight = Bolt * 102 
Total_Weight = Nut_weight + Bolt_weight

#Display
print("Total weight of the order is", Total_Weight, "grams")