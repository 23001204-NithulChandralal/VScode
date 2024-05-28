"""
determine the number of crates needed to pack the number of oranges
"""

#input
oranges = int(input("Enter the amount of oranges:"))

#Calculation
onecrate = 30 
fullcrate = oranges // onecrate 
unpacked = oranges % onecrate 
print("oranges packed =", fullcrate)
print ("oranges unpacked =", unpacked,"unpacked")

if unpacked > 0:
    total_crates = fullcrate = fullcrate + 1 
print ("Total crates required =", total_crates)
