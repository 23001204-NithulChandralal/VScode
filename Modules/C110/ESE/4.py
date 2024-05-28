negativeintegers = []
positiveintegers = []
zeros = []

integer = int(input("Enter an integer:"))
if integer < 0:
    negativeintegers.append(integer)
elif integer > 0:
    positiveintegers.append(integer)
elif integer == 0:
    zeros.append(integer)

while integer != -99:
    integer = int(input("Enter an integer:"))
    if integer < 0:
        negativeintegers.append(integer)
    elif integer > 0:
        positiveintegers.append(integer)
    elif integer == 0:
        zeros.append(integer)

negativeintegers.remove(integer)
for neg in negativeintegers:
    print(neg, end = ' ')
    
for ze in zeros:
    print(ze,end = ' ')
    
for pos in positiveintegers:
    print(pos, end = ' ')
    

