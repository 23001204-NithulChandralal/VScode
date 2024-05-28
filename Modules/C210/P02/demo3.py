# Exercise #4 - Removing Values from a Key
# Exercise #1 - Accessing a Dictionary
lang_list = ["Spanish","French","Mandarin"]
myData = {
    "hello" :["hola","bonjour","ni hao"],
    "goodbye" :["adidos","au revoir","zai jian"]
}


print("Current available language(s):",lang_list)
del_lang = input("Enter Foreign Language Equivalent to remove:")
if del_lang in lang_list:
    del_index = lang_list.index(del_lang)
    lang_list.pop(del_index)
    for i in myData:
        myData[i].pop(del_index)
    print("Records updated")
    print("")
else:
    print("Foreign Language not found")

print("Current available language(s):",lang_list)
for i in myData:
    print("Word in English:",i)
    for j in myData[i]:
        print("Equivalenet word:",j)
    print("")
    
