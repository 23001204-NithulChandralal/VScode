"""
 Write a main program that read a value x as the number of approximations to be calculated for pi◦ x must be checked to start from 1 onward i.e. at least one approximation
"""
#function calcTerm
def calcTerm(start):
    term = 4/(start*(start+1)*(start+2))
    return term 

#function CalcPI
def calcPI(x):
    start = 2*x 
    term_result = calcTerm(start)
    if x % 2 == 0:
        term_result = term_result * (-1)
    return term_result 


#main program 
x = int(input("Enter your approximation :"))
total = 0 
if x >= 1:
    for i in range(1,x+1): 
        Pi= calcPI(i)
        total = total + Pi 
    Pi =  total + 3 
    print("Pi = ", Pi)
else:
    print("Enter a number > 1 for x ")