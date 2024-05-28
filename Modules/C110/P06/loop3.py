"""
Arithmetic Sequence
1, 3, 9, 27, 81
1, -2, 4, -8, 16, -32
"""

for i in range(0,5,1):
    print(3**i)


value = 0 
for i in range(0,6,1):
    value = 2 **i
    if i % 2 != 0:
        value = value * (-1)
    print(value)