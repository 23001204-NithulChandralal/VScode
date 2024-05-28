"""
Def area and volume
"""
#function for selection
def fn_select ():
    choice = input("Enter a-for area or v-for volume of cone:")
    while choice != "a" and choice != "v":
        choice = input("Enter a-for area or v-for volume of cone:")
    #if ans == 'a' or ans =='v':
    return choice
            
        

# calculate area or volume of cone
choice = fn_select()
pi = 3.14
if choice == "a":
    r = float(input("Enter radius:"))
    # -------------------------------------------------