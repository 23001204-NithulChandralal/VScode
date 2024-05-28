def calculate_mean(data):
    total = 0
    for value in data:
        total += value
    mean = total / len(data)
    return mean

def calculate_median(data):
    n = len(data)
    mid = n // 2
    if n % 2 == 0:
        median = (data[mid - 1] + data[mid]) / 2
    else:
        median = data[mid]
    return median

def main():
    rainfallList = []
    done = False
    
    while not done:
        rainfall = input("Enter rainfall press done to end: ")
        if rainfall == 'done':
            done = True
        else:
            is_valid = True
            for char in rainfall:
                if not char.isdigit() and char != '.':
                    is_valid = False
                    print("Invalid input. Please enter a valid rainfall value.")
                    break
            
            if is_valid:
                rainfall = float(rainfall)
                rainfallList.append(rainfall)

    if len(rainfallList) == 0:
        print("No data entered.")
    else:
        mean = calculate_mean(rainfallList)
        median = calculate_median(rainfallList)
        

        print("Mean is:",mean)
        print("Median is:",median)

main()
