"""
HOMEWORK Q2
program that reads a sound level in decibels from the user. 
"""

level = float(input("Enter the Decibel level :"))

if level == 130:
    print("Jackhammer")
elif level == 106 :
    print ("Lawnmower")
elif level == 70 :
    print("Alarm clock")
elif level == 40 :
    print ("Quiet room")
elif level >  130:
    print (" louder than an Jackhammer")
elif level < 130 and level > 106 :
    print (" softer than  a jack hammer and louder than a lawnmower")
elif level > 70 and level < 106 :
    print (" Quiter than a Lawnmower and louder than a alarm clock")
elif level > 40 and level < 70 :
    print (" Quiter than a Alarm clock and louder than a quiet room")
else :
    print (" Quiter than a quiet room")