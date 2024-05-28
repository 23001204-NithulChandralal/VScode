"""
Kisok
simulate a new range of such kiosks that can return change in the least number of notes and/or coins
"""

from math import floor

#Input
Amount_of_the_items = float(input("Enter Amount of the item :"))
Amount_received = float(input("Enter Amount received :"))

#Calculation
Amount_to_be_paid = Amount_received - Amount_of_the_items
Amount_after_10 = Amount_to_be_paid/10
Amount_to_be_paid_2 = floor (Amount_after_10)
Amount_to_be_paid_3 = Amount_to_be_paid - (Amount_to_be_paid_2 * 10)

Amount_after_1 = Amount_to_be_paid_3 / 1
Amount_to_be_paid_4 = floor ( Amount_after_1)
Amount_to_be_paid_5 = Amount_to_be_paid_3 - (Amount_to_be_paid_4 *1)

Amount_after_05 = Amount_to_be_paid_5 / 0.5
Amount_to_be_paid_6 = floor ( Amount_after_05)
Amount_to_be_paid_7 = Amount_to_be_paid_5 - (Amount_to_be_paid_6 * 0.5)

Amount_after_02 = Amount_to_be_paid_7 / 0.2
Amount_to_be_paid_8 = floor(Amount_after_02)
Amount_to_be_paid_9 = Amount_to_be_paid_7 - (Amount_to_be_paid_8 *0.2)

Amount_after_01 = Amount_to_be_paid_9 / 0.1
Amount_to_be_paid_10 = floor (Amount_after_01)
Amount_to_be_paid_11 = Amount_to_be_paid_9 - (Amount_to_be_paid_10 *0.1)

#Covertion
Amount_after_10= int(Amount_after_10) 
Amount_after_1= int(Amount_after_1) 
Amount_after_05= int(Amount_after_05)
Amount_after_02= int(Amount_after_02)
Amount_after_01= int(Amount_after_01)

#Displaying the answer
print(round(Amount_after_10,0),"- 10$ notes")
print(round(Amount_after_1,0),"- 1$ notes")
print(round(Amount_after_05,0),"- 0.50$ notes")
print(round(Amount_after_02,0),"- 0.20$ notes")
print(round(Amount_after_01,0),"- 0.10$ notes")


