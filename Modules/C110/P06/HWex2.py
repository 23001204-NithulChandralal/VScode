"""
HW Q2
create a program that allows them to :
a.	firstly, specify the number of days in the month 
b.	followed by entry of daily rainfall measurement for each day of the month
c.	finally, calculate and output the average rainfall for the month
"""

#input
num_days = int(input("Enter the number of days in the month: "))
rainfall = 0 
day = 1 

#Process
while day <= num_days:
    rainfall = float(input("Enter rainfall measurement for the day:"))
    day += 1 
    
#Calculation
average = rainfall / num_days

#Output
print("The average rainfall for the month is ", average,"units")

