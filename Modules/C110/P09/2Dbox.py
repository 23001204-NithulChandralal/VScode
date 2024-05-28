"""
Exercise #4
Write a function called checkCoord() that will determine if any given coordinate is located inside (return True) or outside (return False) of a given 2-dimensional or 2D box.
"""
def checkCoord(x, y, box_x1, box_y1,box_x2,box_y2):
    if box_x1 <= x <= box_x2 and box_y1 <= y <= box_y2:
        print("Located inside")
        return True
    else:
        return False


box_x1 = int(input("Enter bottom left x coordinate:"))
box_y1 = int(input("Enter bottom left y coordinate:"))
box_x2 = int(input("Enter upper right x coordinate:"))
box_y2 = int(input("Enter upper right y coordinate:"))
x = int(input("Your x coordinate:"))
y = int(input("Your y coordinate:"))
if not checkCoord(x, y, box_x1, box_y1,box_x2,box_y2):
    print("Not located inside")









    