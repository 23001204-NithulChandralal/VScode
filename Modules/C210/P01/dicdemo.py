stud_list = [ 'Alice','Bob', 'Carrie','David','Ella','Fendy','Grace']
score_list = [90,87,37,65,89,77,90]

# how to define a dictionary

students = {
    "Alice":90,
    "Bob":87,
    "Carrie":37
}

print(students["Carrie"])

contacts = {
    "david": 97866402,
    "elsa" : 85180955,
    "Fendy":89005355
}

contacts["david"] = 82394923 # deplace and change the number to the new one [ replace an existing value]
contacts["elle"] = 89323243  # add an item into dictionary

name = input("Enter a name")
if name  in contacts:
    print(contacts[name],"found")
else:
    print(name,"not found")