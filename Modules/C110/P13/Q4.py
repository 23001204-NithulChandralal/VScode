# Revision Q4

CovidVar = ['B.1.1.7', 'B.1.351', 'P.1', 'B.1.617.2']
variant = input("Enter covid variant code:")
new_variant_upper = variant.upper()

if new_variant_upper in CovidVar:
    print(new_variant_upper,"is already found in the list")
else:
    confirm = input("Add to the List (Y/N)?")
    if confirm == "Y":
        CovidVar.append(variant)
        print(new_variant_upper,"is added to the list")





