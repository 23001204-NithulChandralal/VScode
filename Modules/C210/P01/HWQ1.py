#Homeowrk Q1

def hex_to_bin(hex_string):
    hex_to_bin_dict = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
    }

    binary_result = ''
    for hex_digit in hex_string:
        if hex_digit.upper() in hex_to_bin_dict:
            binary_result += hex_to_bin_dict[hex_digit.upper()]
        else:
            return "Invalid hexadecimal character in the input."

    return binary_result

# Test the function
hex_string = input("Enter string of hexadecimals:")
binary_result = hex_to_bin(hex_string)
print(binary_result)
