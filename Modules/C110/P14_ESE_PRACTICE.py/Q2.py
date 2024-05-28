"""
i. Display the total number of items in the Python list places:
places = ['Yishun', 'Kallang', 'Newton', 'Novena', 'Orchard']
total_items = len(places)
print("Total number of items:", total_items)


ii. Update the value of the second item in the Python list places to "Woodlands":
places = ['Yishun', 'Kallang', 'Newton', 'Novena', 'Orchard']
places[1] = "Woodlands"
print(places)


iii. Add a new item "Jurong East" as the third item in the Python list places:
places = ['Yishun', 'Kallang', 'Newton', 'Novena', 'Orchard']
places.insert(2, "Jurong East")
print(places)

iv. Remove the item "Orchard" from the Python list places by value:
places = ['Yishun', 'Kallang', 'Newton', 'Novena', 'Orchard']
places.remove("Orchard") 
print(places)

if "orchard" in places: 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


v. Add a new item "Bedok" after "Novena" and before "Orchard" in the Python list places:
places = ['Yishun', 'Kallang', 'Newton', 'Novena', 'Orchard']
index = places.index("Novena")
places.insert(4, "Bedok")
print(places)


"""

# List of sample place names
places = ['Yishun', 'Kallang', 'Newton', 'Novena', 'Orchard']

letter = input("Enter the first letter:")
for p in places:
    if p[0].upper() == letter.upper():
        print(p)



