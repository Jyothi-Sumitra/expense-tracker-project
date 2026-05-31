students = []

def add_student(students):
    name = input("\nEnter the name of the student: ")
 
    while True:
        try:
            age = int(input("Enter the age of the student: "))
            break
        except ValueError:
            print("\nInvalid input. Please enter a valid age.")
    while True:
        try:
            marks = int(input("Enter the marks of the student: "))
            if marks < 0 or marks > 100:
                print("\nMarks should be between 0 and 100. Please try again.")
                continue
            break
        except ValueError:            
            print("Invalid input. Please enter valid marks.")

    students.append([name, age, marks])
    print("\nStudent added successfully!")

def grade_converter(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

def view_students(students):
    if not students:
        print("\nNo students found.")
    else:
        print("\n-------- Students --------")
        for student in students:
            print(f"Name: {student[0]}")
            print(f"Age: {student[1]}")
            print(f"Marks: {student[2]}")
            print(f"Grade: {grade_converter(student[2])}")
            print("--------------------------")
        print(f"Total number of students: {len(students)}")

        if not students:
                print("\nStudent not found...")

def avg_marks(students):
    if not students:
        print("\nNo student found...")
    else:
        total_marks = 0
        for student in students:
            total_marks += student[2]

        average = total_marks / len(students)
        print(f"\nAverage marks of the students: {average}")

def find_topper(students):
    if not students:
        print("\nNo student found...")
    else:
        topper = students[0]
        for student in students:
            if student[2] > topper[2]:
                topper = student
        print("\n-------- Students --------")
        print(f"\nTopper: {topper[0]}")
        print(f"with marks: {topper[2]}")
        print("--------------------------")

def search_student(students):
    search_name= input("\nEnter the name: ")
    search_name = search_name.lower()
    
    if not students:
        print("\nNo student found...")
    else:
        found = False
        for student in students:
            if student[0].lower() == search_name:
                print("\n-------- Students --------")
                print(f"Name: {student[0]}")
                print(f"Age: {student[1]}")
                print(f"Marks: {student[2]}")
                print(f"Grade: {grade_converter(student[2])}")
                print("--------------------------")
            
        if not found:
            print("\nStudent not found...")

def update_marks(students):
    name = input("\nEnter the name of the student: ")
    name = name.lower()
    
    if not students:
        print("No student found...")
    else:
        for student in students:
            if student[0].lower() == name:
                while True:
                    try:
                        new_marks = int(input("Enter the new marks: "))
                        if new_marks < 0 or new_marks > 100:
                            print("Marks should be between 0 and 100. Please try again.")
                            continue
                        break
                    except ValueError:
                        print("Invalid input. Please enter valid marks.")
                student[2] = new_marks
                print("Marks updated successfully!")
                return
        print("\nStudent not found...")

def remove_student(students):
        remove_name = input("\nEnter the name of the student to remove: ")
        remove_name = remove_name.lower()
        if not students:
            print("No student found...")
        else:
            for student in students:
                # found = False
                if student[0].lower() == remove_name:
                    students.remove(student)
                    print("Student removed successfully!")
                    return
                # if not found:
            print("Student not found...")

print("\nWelcome to the Student Management System!")
while True:
    print("\n1. Add Student\n2. View Students\n3. Average Marks\n4. Find Topper\n5. Search Student\n6. Update Marks\n7. Remove student\n8. Exit")

    while True:
        try:
            option = int(input("\nPlease choose an option (Enter the choice numbers): "))
            break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 8.")
            continue
        
    match option:
        case 1:
            add_student(students)
        case 2:
            view_students(students)
        case 3:
            avg_marks(students)
        case 4:
            find_topper(students)
        case 5:
            search_student(students)
        case 6:
            update_marks(students)
        case 7:
            remove_student(students)
        case 8:
            print("\nExiting the Student Management System...\n")
            exit()
        case _:
            print("\nInvalid option. Please choose a number between 1 and 8.")