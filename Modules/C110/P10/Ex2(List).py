"""
List Exercise #2
"""

numList = [12, 43 ,85, 72, 92, 34, 9, 58]
numListLen = len(numList)

average = 0 
for i in range (numListLen):
    average += numList[i]
    print(numList[i])
    
average = average / numListLen
print("Average =", average)
print("--------------------")

print("Values greater than 30:")
for i in numList:
    if i > 30:
        print(i)
print("--------------------")

print("Even numbered List only:")
for i in numList:
    if i % 2 == 0:
        print(i)
    else:
        i = i + 1
        print(i)