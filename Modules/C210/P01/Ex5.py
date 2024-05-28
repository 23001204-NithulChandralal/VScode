def get_option():                                         #main program 
    print("1. Add country-city")
    print("2. Delete country-city")
    print("3.Update capital city")
    print("4. Display A country-city")
    print("5. Display ALL country-city")
    print("6. Quit")
    option = int(input("Enter an option:"))
    return option 

user_opt = get_option()
countries ={}
while user_opt != 6:
    if user_opt ==1:
        new_country = input("Enter the country:")
        new_capital = input("Enter the capital city:")
        if new_country in countries:
            print("Already exists")
        else:
            countries[new_country] = new_capital  
            print(countries[new_country],"is added")

    elif user_opt ==2:
        country = input("Enter country:")
        if country in countries:
            del countries[country]
            print(countries)
            print(country,"have been removeed")
        else:
            print("Country not found")    

    elif user_opt ==3:
        country = input("Enter country to be updated:")
        captial = input("Enter the capital to be updated:")
        countries[country] = captial
        print(countries[new_country],"has been updated")        

    elif user_opt == 4:
        country = input("Enter a country:")
        if country in countries:
            print(countries[country],"is the capital of",country)
        else:
            print(country,"not found")

    elif user_opt ==5:
        for i in countries:
            print("The capital of",i,"is",countries[i])
    else:
        print("Invalid Option")
    user_opt = get_option()


          