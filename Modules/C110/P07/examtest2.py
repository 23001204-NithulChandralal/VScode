groups = int(input(("Enter # of numbers:")))
largest = 0 
smallest = 0 
median = 0 

if groups % 2 == 0:
    for x in range(groups):
        num = float(input("Enter your number:"))
        if num >= largest:
            largest = num
            add = num + 0 
        elif num <= smallest:
            smallest = num  
            add = num + 0 
        else:
            add = num + 0
            
    median =(add + add )/ 2 
    print("Median is",median)
else:
    print("Error: Even collection of sorted numbers expected")
