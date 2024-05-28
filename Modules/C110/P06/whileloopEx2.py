"""
Ex  2 Write a text based menu program to allow a user to repeatedly select between 3 geometric shapes
"""
#input
print("Calculating Surface Area and Volume of Shapes. Choose:")
print("'s' for Sphere")
print("'y' for Cyclinder")
print("'c' for Cone")
print("'q' to quit ")
shape = (input("Enter here:"))

#process
while shape != "q":
    if shape == "s":
        radius = float(input("Radius:"))
        SA = 4 * (22/7) * (radius**2)
        print ("SA =",round(SA, 2))
        Vol = (4/3) * (22/7) * (radius**3) 
        print ("Volume=",round(Vol,2))
        shape =(input("Enter Geometric Shape ( s / cy / c ) or q to quit:"))
    elif shape == "cy":
        radius = float(input("Radius:"))
        height = float(input("Height:"))
        SA = (2 * (22/7) * (radius**2)) + 2 * (22/7) * radius * height 
        print("SA =",round(SA, 2)) 
        Vol = (22/7) * (radius**2) * height
        print("Vol=",round(Vol,2))
        shape =(input("Enter Geometric Shape ( s / cy / c ) or q to quit:"))
    elif shape == "c":
        radius = float(input("Radius:"))
        height = float(input("Height:")) 
        slope = float(input("Slope:"))
        SA = ((22/7) * radius * slope) + ((22/7) * radius**2)
        print("SA=",round(SA, 2))
        Vol = (1/3) * (22/7) * (radius**2) * height 
        print("Vol=", round(Vol,2))
        shape =(input("Enter Geometric Shape ( s / cy / c ) or q to quit:"))
    else:
        print("Geometric Shape not detected")
        shape =(input("Enter Geometric Shape ( s / cy / c ) or q to quit:"))
print("Quit")

    
    



    
