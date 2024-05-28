"""
(while loop)Write the same multiplication program that will print multiplication tables
"""

i = 2 
while i <= 8:
    j = 2 
    while j <= 4:
        result = i * j 
        print(i,"X",j,"=", result)
        j += 1
    i = i + 2