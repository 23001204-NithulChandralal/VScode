"""
 Write a main program that reads a series of numbers from a 
user until an exit condition and stores them into a List.
"""

def doubleList(numbers):
    doubled_numbers = [num * 2 for num in numbers]
    return doubled_numbers

number_list = []

user_input = input("Enter a number (or 'exit' to quit): ")
while user_input.lower() != 'exit':
    if user_input.isdigit() or (user_input[0] == '-' and user_input[1:].isdigit()):
        number = float(user_input)
        number_list.append(number)
    else:
        print("Invalid input. Please enter a valid number or 'exit' to quit.")
    
    user_input = input("Enter a number (or 'exit' to quit):")

doubled_numbers = doubleList(number_list)

print("Original list of numbers:", number_list)
print("Doubled list of numbers:", doubled_numbers)
