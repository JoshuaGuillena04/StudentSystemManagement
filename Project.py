
students = []

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter your name: ")
        age = input("Enter age: ")
        course = input("Enter course: ")
        year = input("Enter year: ")
        address = input("Enter address: ")

        student = {
            "name": name,
            "age": age,
            "course": course,
            "year": year,
            "address": address
        }

        students.append(student)

        print("Student added successfully!")

    elif choice == 2:
        print("\n===== STUDENT LIST =====")

        if len(students) == 0:
            print("No students found.")
        else:
            for id, student in enumerate(students, start=1):
                print(
                    id, "|",
                    student["name"], "|",
                    student["course"], "|",
                    student["age"], "|",
                    student["year"], "|",
                    student["address"]
                )

    elif choice == 3:
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")
