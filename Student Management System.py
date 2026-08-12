# Student Management System

students = []


def add_student():
    student_id = input("Enter Student ID: ")


    for student in students:
        if student["id"] == student_id:
            print("Student ID already exists!")
            return

    name = input("Enter Student Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")
    marks = float(input("Enter Marks: "))

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course,
        "marks": marks
    }

    students.append(student)

    print("Student added successfully!")



def view_students():
    if not students:
        print("No student records found.")
        return



    for student in students:
        print(f"ID      : {student['id']}")
        print(f"Name    : {student['name']}")
        print(f"Age     : {student['age']}")
        print(f"Course  : {student['course']}")
        print(f"Marks   : {student['marks']}")
        print("-----------------------------")



def search_student():
    search = input("Enter Student ID or Name: ")

    found = False

    for student in students:
        if student["id"] == search or student["name"].lower() == search.lower():
            print("\n----- Student Found -----")
            print(f"ID      : {student['id']}")
            print(f"Name    : {student['name']}")
            print(f"Age     : {student['age']}")
            print(f"Course  : {student['course']}")
            print(f"Marks   : {student['marks']}")
            found = True

    if not found:
        print("Student not found.")



def update_student():
    student_id = input("Enter Student ID to update: ")

    for student in students:
        if student["id"] == student_id:

            print("\nEnter new details:")

            student["name"] = input("Enter Name: ")
            student["age"] = int(input("Enter Age: "))
            student["course"] = input("Enter Course: ")
            student["marks"] = float(input("Enter Marks: "))

            print("Student details updated successfully!")
            return

    print("Student not found.")



def delete_student():
    student_id = input("Enter Student ID to delete: ")

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")



while True:

    print("\n----- Student Management System -----")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice! Please enter a number from 1 to 6.")