cmark = str(input("mark at c :"))
tmark = str(input("mark at t:"))

if cmark == "y"and tmark == "n":
    print("negative")
elif cmark == "y" and tmark == "y":
    print("positive")
elif cmark == "n" and tmark == "y":
    print("invalid")