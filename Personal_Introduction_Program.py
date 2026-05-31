print("\nHello! This is your Hayoon.\nI'm here to learn your details for futher help.\nPersonal Introduction page:")
details = {}
name=input(f"{'\nWhat should we call you?\t':<30}")
try:
        age=input(f"{'May we know your age?\t':<34}")
        age = int(age)
except ValueError:
        print("\nInvalid input. Please enter a valid age.")
        exit()

if age>=18:
    details["name"] = name
    details["age"] = age
    print(f"\nHi! {name} we are glad to meet you!")
    print(f"Since you meet our required age policy with {age} you are welcomed to use our service!\n")
    print("****************")
    while True:
        print("\nWhich of our services are you interested in?\n1.Check the stored details\n2.Add more details\n3.Check you age after certain years later\n4.Exit")
        try:
            option = input("\nEnter the option number you want to choose: ")
            option = int(option)
        except ValueError:
            print("\nInvalid input. Please enter a valid option number.")
            continue
        match option:
            case 1:
                print("\n****************")
                print(details)
                print("\n****************")

            case 2:
                favourite_color = input("Favourite color: ")
                favourite_kpop = input("Favourite K-Pop band: ")
                details["fav_color"] = favourite_color
                details["fav_band"] = favourite_kpop
                print("Yeah! Details added!")
                print("\n****************")
                print(details)
                print("\n****************")

            case 3:
                try:
                    years = input("\nEnter the number of years you want to check your age after: ")
                    years = int(years)
                    future_age = age + years
                    print("\n****************")
                    print(f"\nYour age after {years} years will be: {future_age}")
                    print("\n****************")
                except ValueError:
                    print("\nInvalid input. Please enter a valid number of years.")

            case 4:
                print("\n****************")
                print("\nthanks for choosing our service, we are still improving it.\nWe hope to see you again in the future!\n")
                print("\n****************")
                break
            case _:
                print("\n****************")
                print("\nInvalid option. Please try again.")
                print("\n****************")
else:
    print("\nOops... You aren't above our age requirement. You can't access our service.")