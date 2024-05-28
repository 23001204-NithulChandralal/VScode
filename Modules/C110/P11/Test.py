ans = input("Enter a word : ")
print(ans)
if ans.isupper():
    print ("UPPER CASE")
elif ans.islower():
    print("lower case")
elif ans.isnumeric():
    print("Numbers Entered")
elif ans.isalpha():
    print("ALPHABETS")
else:
    print ("Decide later")

