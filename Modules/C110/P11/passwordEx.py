"""
Demo #1
"""

password = input("Enter password : ")
if len(password) == 7:
    print("Length is OK")
    if password.count("$") + password.count("*") + password.count("#") <=1:
        print("$*#")
    else:
        print("ALL is NOT OK")
else:
    print("NOT OK")