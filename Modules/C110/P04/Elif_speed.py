"""
program that displays suitable messages that a vehicle can travel at on a highway
"""

speed = int(input("What is the speed? :"))
if speed <= 50:
    print ("Below 50kmh")
elif speed >= 50 and speed <= 80:
    print ("50-80 kmh")
else:
    print ("Above 80kmh")