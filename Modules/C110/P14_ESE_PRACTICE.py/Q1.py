age = int(input("Enter your age:"))
situps = int(input("Enter no. of sit-ups in 1 min:"))

if age >= 12 and age <= 14:
    if situps > 41:
        print("A")
    elif situps >= 36 and situps <= 41:
        print("B")
    else:
        print("No matching performance grade is found for data given")
elif age >= 15 and age <= 19:
    if situps > 43:
        print("A")
    elif situps >= 38 and situps <= 43:
        print("B")
    else:
        print("No matching performance grade is found for data given")
else:
    print("No matching performance grade is found for data given")