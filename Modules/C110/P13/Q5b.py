#Q5b. Revision

occupiedList = []
show = 0

for show in range(5):
    show = show + 1
    x = input("Enter number of seats occupied for show " + str(show) + ": ")
    occupiedList.append(int(x))


total_seat_occupied = sum(occupiedList)
total_capacity = 150 * 5 

utilisation_rate = (total_seat_occupied / total_capacity ) * 100 

print("Utilisation rate is", round(utilisation_rate,2))


