# Scrabble letter scores
# Used abit of ChatGPT because i am not sure how to do 
letter_scores = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4,
    'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3,
    'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8,
    'Y': 4, 'Z': 10
}

word = input("Enter a word (7 characters max): ").upper()
double_letter = input("Specify a letter for double letter score (or press Enter): ").upper()
double_word = input("Specify double word score (Y/N): ").strip().lower() == "y"

total_score = 0
for letter in word:
    if letter == double_letter:
        total_score += 2 * letter_scores[letter]
    else:
        total_score += letter_scores[letter]

if double_word:
    total_score *= 2

print("The score of",word, "is",total_score)
