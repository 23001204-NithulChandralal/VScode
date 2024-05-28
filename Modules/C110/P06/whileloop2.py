"""
Arithmetic Sequence
1, 3, 9, 27, 81
1, -2, 4, -8, 16, -32
"""

total = 0 
i = 1
print(i)
while i < 81:
    i = 3 * i
    print(i)
    total = total + i 
print("The sum is", total )

print("=====================")

 

value = 0 
i = 0
while i < 6:
    value = 2 **i 
    if i % 2 != 0:
        value = value * (-1)
    print(value)
    i = i + 1 

