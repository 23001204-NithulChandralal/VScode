
stud_instrument = {} 

instrument1 = "test"
name = input("Enter the name of the new student: ")
while instrument1 != "end":
    instrument1 = input("Enter a musical instrument (or 'end' to finish)")
    stud_instrument[name] = [instrument1]
print("Student added.")
 



stud_instrument = {
    "Alex": ["Piano", "Drums"], 
    "Bella": ["Guitar", "Trumpet"]
}

tt = input("Enter the name of a musical instrument: ")
instruments = stud_instrument.get(name, [stud_instrument]) 
if len(stud_instrument) == 0:
    print("No student played the: " + input)
else:   
    for student in instruments:
        print("The students are " + instruments)
        
