myData = {
    "hello" :["hola","bonjour","ni hao"],
    "goodbye" :["adidos","au revoir","zai jian"]
}
lang_list = ["Spanish","French","Mandarin"]


print("Current available language(s):",lang_list)
new_lang = input("Add New Foreign Language Equivalent, or 'Quit' to end program:")

while new_lang != "Quit":
    hello_input = input(new_lang + " for hello is:")
    print("")
    goodbye_input = input(new_lang + " for goodbye is:")
    print("")
    print(new_lang + " has been added") 
    lang_list.append(new_lang)
    myData["hello"].append(hello_input)
    myData["goodbye"].append(goodbye_input)
    print("")
    print("Current available language(s): ",lang_list)
    new_lang = input("Add New Foreign Language Equivalent, or 'Quit' to end program:")

for i in myData:
    print("Word in English:",i)
    for j in myData[i]:
        print("Equivalenet word:",j)
    print("")


    

