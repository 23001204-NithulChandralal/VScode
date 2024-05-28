"""
Homework Exercise 3. To find out the cost of a meal
"""
#Input
Original =float(input("Enter original cost of meal:"))

#Calculation 
GST = Original * (8/100)
Tip = Original * (14.5/100)
Total = Original + GST + Tip 

#Display
print("The GST is $",round(GST,2),".The tip is $",round(Tip,2),".The Grand Total of the meal is $",round(Total,2))
