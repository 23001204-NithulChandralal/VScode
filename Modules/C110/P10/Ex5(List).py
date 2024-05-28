"""
List - Exercise #5
"""
numList = []
num = int(input("Enter an integer (or 0 to exit):"))

while num != 0:
    numList.append(num)
    num = int(input("Enter an integer (or 0 to exit):"))

print("Orignal numList:", numList)

evenlist = []
odd_count = 0 

for num in numList:
    if num % 2 == 0:
        evenlist.append(num)
    else:
        odd_count = odd_count + 1 

numList = evenlist 

print("Number of odd numbers removed:", odd_count)
print("Updated numList:", numList)
print("Number of integers stored:", len(numList))
print("Minimum value:", min(numList))
print("Maximum value:", max(numList))
