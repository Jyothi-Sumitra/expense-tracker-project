print("Hello! Welcome to the Expenses Tracker Program!\n")
name = input(f"{'Can we know your name?':<30}")
print(f"Welcome, {name}! We are glad to have you here!\n")
print("This is your personal expenses tracker, you can use it to track your daily expenses and manage your budget effectively.\n")
print("In this program, we use food, shopping, and travel as the main categories for expenses, but you can also add more categories if you want.\n")
while True:
    try:
        food_expenses = input("\nEnter your Food Expenses: ")
        food_expenses = float(food_expenses)
        break
    except ValueError:
        print("INVALID AMOUNT. PLEASE TRY AGAIN!\n")

while True:
    try:
        travel_expenses = input("Enter your Travel Expenses: ")
        travel_expenses = float(travel_expenses)
        break
    except ValueError:
        print("INVALID AMOUNT. PLEASE TRY AGAIN!\n")

while True:
    try:
        shopping_expenses = input("Enter your Shopping Expenses: ")
        shopping_expenses = float(shopping_expenses)
        break
    except ValueError:
        print("INVALID AMOUNT. PLEASE TRY AGAIN!\n")

expenses = {}
expenses["Food"] = food_expenses
expenses["Travel"] = travel_expenses
expenses["Shopping"] = shopping_expenses

total_expense = food_expenses + travel_expenses + shopping_expenses

while True:
    print("\nWhat do you want to do?\n1. Check the expenses\n2. Add categories\n3. Budget Warning\n4. Exit")
    try:
        option = input("Enter your option number: ")
        option = int(option)
    except ValueError:
        print("Invalid option is choosen. Try again!")
        continue

    match option:

        case 1:
            print("\n-------- Expense Summary --------")
            print(f"Food Expenses     : {food_expenses}")
            print(f"Travel Expenses   : {travel_expenses}")
            print(f"Shopping Expenses : {shopping_expenses}")
            print(f"\nTotal Expenses    : {total_expense}")
            print("---------------------------------")
        
        case 2:
            new_category = input("\nEnter the category you want to add: ")
            try:
                new_expenses = input(f"Enter your {new_category} Expenses: ")
                new_expenses = float(new_expenses)
            except ValueError:
                print("INVALID AMOUNT. PLEASE TRY AGAIN!\n")
            
            expenses["new"] = new_expenses
            
            total_expense = food_expenses + travel_expenses + shopping_expenses + new_expenses
            total_expense = float(total_expense)

            print("\n-------- Expense Summary --------")
            print(f"Food Expenses      : {food_expenses}")
            print(f"Travel Expenses    : {travel_expenses}")
            print(f"Shopping Expenses  : {shopping_expenses}")
            print(f"{new_category} Expenses : {new_expenses}")
            print(f"\nTotal Expenses     : {total_expense}")
            print("---------------------------------")
        
        case 3:
            if total_expense>=1000:
                print(f"\nWARNING! You crossed your monthly budget!\nYour total expenses for this month is {total_expense}")
            else:
                print("Good! You're within your budget.")
        
        case 4:
            print("\nThanks for choosing our service!")
            exit()