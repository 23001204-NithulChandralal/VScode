"""
Calculating pay of part-time workers
"""

#input
hours_worked = float(input("Enter hours worked:"))
NS = input("Have to completed your NS? (y/n)")

#process
salary = hours_worked * 9 
if NS == "y":
    salary = salary + 6.50

# output
print ("The salary of the worker is $",salary)