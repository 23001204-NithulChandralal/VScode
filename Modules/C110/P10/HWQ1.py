"""
HW Q1
"""

sentence = input("Enter your sentence: ")

characters = list(sentence.lower())

vowel_count = 0
space_count = 0
consonant_count = 0

for i in characters:
    if i in ['a', 'e', 'i', 'o', 'u']:
        vowel_count += 1
    elif i == ' ':
        space_count += 1
    else:
        consonant_count += 1


print("Vowel a:", characters.count('a'))
print("Vowel e:", characters.count('e'))
print("Vowel i:", characters.count('i'))
print("Vowel o:", characters.count('o'))
print("Vowel u:", characters.count('u'))
print("Spaces:", space_count)
print("Consonants:", consonant_count)
