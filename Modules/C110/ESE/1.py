age = int(input("Enter age:"))
residency = input("Enter residency (C or F):")

if age <= 2:
    if residency == "C":
        print("Free entry")
    elif residency == "F":
        print("Admission fee is $2.50")
elif age >= 3 and age <= 10:
    if residency == "C":
        print("Admission fee is $7.50")
    elif residency == "F":
        print("Admission fee is $11.50")
elif age > 10 and age < 65:
    if residency == "C":
        print("Admission fee is $21.80")
    elif residency == "F":
        print("Admission fee is $25.00")
elif age >= 65:
    if residency == "C":
        print("Admission fee is $15.00")
    elif residency == "F":
        print("Admission fee is $17.50")
