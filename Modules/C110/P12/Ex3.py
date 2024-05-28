def find_vowel_words(alist, blist):
    vowel = []
    for word in alist:
        if word and word[0] in blist:
            vowel.append(word)
    return vowel

phrase = input("Enter a sentence: ")
words = phrase.split()

blist = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

vowel = find_vowel_words(words, blist)

print(vowel)
