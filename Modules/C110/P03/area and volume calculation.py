"""
area = piR + (g+R)
volume = 1/3 pi R sq * h 
"""

# INPUT 
h = input("Enter h :")
h= float(h)
g = input("Enter g :")
g= float(g)
R = input("Enter R :")
R= float(R)

#Calculation
Area = 3.141 * R * (g+R)
Volume = 1/3 * 3.141 * R**2*h

# Display result 
print("Area = ", round(Area,2))
print("Volume = ", round(Volume,1))