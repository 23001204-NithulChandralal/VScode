#ex 5
#letter a-z 97-122
#number 0-9 48-57
"""
Write a Python program that implements the Caesar 
cipher for plaintext that is made up of lower-case 
characters a to z only (or ASCII values 97 to 122 only
"""

shift=3
alpha=input("enter a letter:")
encryp=""
for char in alpha:
    if 'a' <= char <= 'z':
        shifted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        encryp += shifted_char
    else:
        encryp += char
decrypted_text = ""
for char in encryp:
    if 'a' <= char <= 'z':
        shifted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        decrypted_text += shifted_char
    else:
        decrypted_text += char

print("Decrypted:", decrypted_text)
print("Encrypted:", encryp)