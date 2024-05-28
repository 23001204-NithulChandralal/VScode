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


students = int(input("Enter number of students"))
passing = int(input("Enter passing score:"))
count = 0 

for i in range(students):
    str_input = input("Enter the symbols for student",i+1,":")
    result = translate_to_score(str_input)
    if result >= passing:
    
 print("The score for symbols", str_input,"is",result)