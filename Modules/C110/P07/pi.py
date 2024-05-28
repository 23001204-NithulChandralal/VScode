"""
Write a program that displays x approximations of pi
(rounded to 7 decimals points)

NOT SURE HOW TO DO 
"""
def calculate_pi_approximations(x):
    pi_approx = 3.0  # Starting with the first term of the infinite series
    denominator = 2.0
    sign = 1.0

    for i in range(1, +1):
        term = (4 / (denominator * (denominator + 1) * (denominator + 2))) * sign
        pi_approx += term
        denominator += 4
        sign *= -1

    return round(pi_approx, 7)
# Get user input for the number of approximations
num_approximations = int(input("Enter the number of approximations: "))

# Calculate and display the approximations of pi
approximations = calculate_pi_approximations(num_approximations)
print(f"{num_approximations} approximations of pi: {approximations}")



