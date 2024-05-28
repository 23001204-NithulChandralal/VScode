"""
 (for loop)Write the same multiplication program that will print multiplication tables
"""

for i in range(2,9):
    for j in range(1,4):
        if i % 2 != 0 :
            break
        else:
            print(i,"X",j,"=", i*j)

