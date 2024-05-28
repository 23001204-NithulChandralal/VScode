"""
Convert the calculator program to use functions that 
determines the result of the following calculations when 2 
values are given as parameters
"""
def selection():
    f = float(input("Enter first number :"))
    s = float(input("Enter second number :"))
    return f,s

def Addition(f,s):
    ans = f + s
    print("Addition =", round(ans,3))

def Subtraction(f,s):
    ans = f - s
    print("Subtraction =", round(ans,3))

def Multiplication(f,s):
    ans = f * s
    print("Multiplication =", round(ans,3))

def Division(f,s):
    ans = f/s
    print("Division =", round(ans,3))

def Integer_Divison(f,s):
    ans = f//s
    print("Integer Division =", round(ans,3))

def Modulus(f,s):
    ans = f % s
    print("Modulus =", round(ans,3))

def menu():
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Integer Division")
    print("6. Modulus")
    print("q. Quit")

def calculation_selection():
    cal_select =str(input("Enter selection:"))
    return cal_select

menu()
cal_select = calculation_selection()
if cal_select != "q":
    f,s = selection()

if cal_select == 1:
    Addition(f,s)
elif cal_select == 2:
    Subtraction(f,s)
elif cal_select == 3:
    Multiplication(f,s)
elif cal_select == 4:
    Division(f,s)
elif cal_select == 5:
    Integer_Divison(f,s)
elif cal_select == 6:
    Modulus(f,s)
elif cal_select == "q":
    print("Quitted")


        