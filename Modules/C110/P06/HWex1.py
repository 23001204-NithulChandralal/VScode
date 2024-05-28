"""
HW Q1
Write a program that can read the letter module grade of 5 modules and converts each letter grade to their numeric equivalent 
"""

fmodule = input("Enter module letter grade:")
smodule = input("Enter module letter grade:")
tmodule = input("Enter module letter grade:")
foumodule = input("Enter module letter grade:")
fivmoudle = input("Enter module letter grade:")

#process
if fmodule == "A":
    fmodule = 4
elif fmodule == "B":
    fmodule = 3 
elif fmodule == "C":
    fmodule = 2 
elif fmodule == "D":
    fmodule = 1 
elif fmodule == "F":
    fmodule = 0 

if smodule == "A":
    smodule = 4
elif smodule == "B":
    smodule = 3 
elif smodule == "C":
    smodule = 2 
elif smodule == "D":
    smodule = 1 
elif smodule == "F":
    smodule = 0 

if tmodule == "A":
    tmodule = 4
elif tmodule == "B":
    tmodule = 3 
elif tmodule == "C":
    tmodule = 2 
elif tmodule == "D":
    tmodule = 1 
elif tmodule == "F":
    tmodule = 0 

if foumodule == "A":
    foumodule = 4
elif foumodule == "B":
    foumodule = 3 
elif foumodule == "C":
    foumodule = 2 
elif foumodule == "D":
    foumodule = 1 
elif foumodule == "F":
    foumodule = 0 

if fivmoudle == "A":
    fivmoudle = 4
elif fivmoudle == "B":
    fivmoudle = 3 
elif fivmoudle == "C":
    fivmoudle = 2 
elif fivmoudle == "D":
    fivmoudle = 1 
elif fivmoudle == "F":
    fivmoudle = 0 

#Calculations
GPA = (fmodule + smodule + tmodule + foumodule + fivmoudle) / 5

#output
print ("Grade point average obtained:", round(GPA,2))