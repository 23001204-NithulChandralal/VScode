#Revision Q9

def draw_triangle(height):
    for i in range(1, height + 1):
        for j in range(i):
            print("*", end="")
        print()

# Test case
height = int(input("Enter height:"))
draw_triangle(height)
