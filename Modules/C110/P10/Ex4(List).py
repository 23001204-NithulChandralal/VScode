"""
List Exercise #4
"""
numList = []
num = int(input("Enter an integer (or 0 to exit):"))

while num != 0:
    numList.append(num)
    num = int(input("Enter an integer (or 0 to exit):"))

print("Numbers stored in numList:", numList)
print("Number of integers stored:", len(numList))
print("Minimum value:", min(numList))
print("Maximum value:", max(numList))