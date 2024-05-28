numList = []
num = int(input("Enter an integer (or 0 to exit): "))

while num != 0:
    numList.append(num)
    num = int(input("Enter an integer (or 0 to exit): "))

print("Original numList:", numList)

min_count = numList.count(min(numList))
print("Number of occurrences of the minimum number:", min_count)

max_index = numList.index(max(numList))
print("Index value of the maximum number:", max_index)

numList.sort()
print("Sorted numList (ascending order):", numList)
