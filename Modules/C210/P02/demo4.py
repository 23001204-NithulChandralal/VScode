def printDict(myData):
    print("*** Current Dictionary ***")
    for i in myData:
        print("Word in English:",i)
        for j in myData[i]:
            print("Equivalenet word:",j)
        print("")

def menu():
    print("*** Menu ***")
    print("1. Add New Foreign Language Equivalent")
    print("2. Remove a Foreign Language Equivalent")
    print("3.Quit")
    opt = input("Enter choice (1/2/3):")
    print("")
    return opt

lang_list = ["Spanish","French","Mandarin"]
myData = {
    "hello" :["hola","bonjour","ni hao"],
    "goodbye" :["adidos","au revoir","zai jian"]
}

print("Current available language(s):",lang_list)
printDict(myData)
opt = menu()

while opt != "3":
    if opt == '1':
        new_lang = input("Enter New Foreign Language Equivalent, or 'Quit' to end program:")
        print("")
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
        printDict(myData)
    elif opt == '2':
        del_lang = input("Enter Foreign Language Equivalent to remove:")
        if del_lang in lang_list:
            del_index = lang_list.index(del_lang)
            lang_list.pop(del_index)
            for i in myData:
                myData[i].pop(del_index)
            print("Records updated")
            print("")
        else:
            print("ERROR - Cannot find language")
            print("")
        print("Current available language(s):",lang_list)
        printDict(myData)
    else:
        print("Invalid Option")









