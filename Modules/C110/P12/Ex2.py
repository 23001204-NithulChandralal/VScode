def find_lower(sentence):
    count = 0
    for i in sentence:
        if i.islower():
            count += 1
    return count

def find_upper(sentence):
    count = 0
    for i in sentence:
        if i.isupper():
            count += 1
    return count

sentence = input("Enter your string: ")

print("The number of lowercase letters is:", find_lower(sentence))
print("The number of uppercase letters is:", find_upper(sentence))
