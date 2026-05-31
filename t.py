import math
class calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b
    
    def sub(self):
        return self.a - self.b
    
    def mul(self):
        return self.a * self.b
    
    def div(self):
        if self.b==0:
            print("Division can't be done with zero...")
        return self.a / self.b
    
    def pow(self):
        return self.a ** self.b

print("Hello! Welcome to our calculator!\n")

while True: 
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Power\n6. Exit\n")
    while True:
        try:
            option = int(input("Which opertion do you want to choose? (Enter the number of the opertaion you want to perform): "))
            break
        except ValueError:
            print("INVALID OPTION... RETRY AGAIN!\n")
        
    print("========== CALCULATOR ==========")

    while True:
        try:
            a = int(input("Enter value of a: "))
            break
        except ValueError:
            print("INVALID OPTION... RETRY AGAIN!\n") 
    
    while True:
        try:
            b = int(input("Enter value of b: "))
            break
        except ValueError:
            print("INVALID OPTION... RETRY AGAIN!\n")
    
    vals = calculator(a,b)
    match option:
        case 1:
            print("\tAddition\n")
            print(a," + ", b)
            print("Result: ", vals.add())
        
        case 2:
            print("\tSubtarction\n")
            print(a," - ", b)
            print("Result: ", vals.sub())

        case 3:
            print("\tMultiplication\n")
            print(a," * ", b)
            print("Result: ", vals.mul())
        
        case 4:
            print("\tDivision\n")
            print(a," / ", b)
            print("Result: ", vals.div())
        
        case 5:
            print("\tPower\n")
            print(a," ^ ", b)
            print("Result: ", vals.pow())
        
        case 6:
            print("\nThanks for choosing our service!")
            exit()
    
    print("===============================")

    print("\nWhat do you want to do next?")
    print("1. Use same numbers")
    print("2. Enter new numbers")
    print("3. Exit")

    next_choice = input("Enter choice: ")

    if next_choice == "1":
            continue

    elif next_choice == "2":
            break

    elif next_choice == "3":
            print("Thank you for using calculator!")
            exit()
            
    else:
            print("INVALID CHOICE!")