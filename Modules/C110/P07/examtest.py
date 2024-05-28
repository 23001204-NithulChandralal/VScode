lower = int(input("Enter lower bound:"))
upper = int(input("Enter upper bound:"))

y = 0 
sum = 0 

while upper >= lower:  
    if upper % 4 == 0:
        sum = sum + upper
        upper = upper - 1
    else:
        sum = sum
        upper = upper - 1
print("The total sum:",sum)

