#Q8 Revision

plate_number = input("Enter a car licence plate number: ")

if len(plate_number) != 7:
    print("Invalid ")
elif plate_number[0] != 'Z':
    print("Invalid ")
elif not plate_number[1:3].isalpha():
    print("Invalid ")
elif not plate_number[3:].isdigit():
    print("Invalid ")
else:
    print("Valid ")
