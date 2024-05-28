#Q6 Revision


def translate_to_score(symbols):
    total_score = 0 
    for symbol in symbols:
        if symbol == '$':
            total_score += 5
        elif symbol == '@':
            total_score += 3 
        elif symbol == '#':
            total_score += 1 
    return total_score

symbols = input("Enter symbols: ")
total_score = translate_to_score(symbols)
print("Total score:", total_score)
