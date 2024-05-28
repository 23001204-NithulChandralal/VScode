"""
HW Q2 - Write a program that reads yearly bi-monthly rainfalls
"""
rainfallList = []


while True:
    rainfall = input("Enter rainfall (in inches) or 'done' to finish: ")
    if rainfall.lower() == 'done':
        break
    rainfallList.append(float(rainfall))


mean = sum(rainfallList) / len(rainfallList)

sortedRainfall = sorted(rainfallList)
n = len(sortedRainfall)
mid = n // 2

if n % 2 == 0:
    median = sum(sortedRainfall[mid-1:mid+1]) / 2
else:
    median = sortedRainfall[mid]


print("Mean is:", mean)
print("Median is:", median)
