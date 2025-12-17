students = []

def add_student():
    sid = input("Enter Student ID: ")

    for s in students:
        if s["id"] == sid:
            print("Student ID already exists.")
            return

    try:
        student = {
            "id": sid,
            "name": input("Enter Name: "),
            "age": int(input("Enter Age: ")),
            "course": input("Enter Course: "),
            "marks": int(input("Enter Marks: "))
        }
    except ValueError:
        print("Age and Marks must be numbers.")
        return

    students.append(student)
    print("Student added successfully.")

def view_students():
    if not students:
        print("No students found.")
        return

    print("ID\tName\tAge\tCourse\tMarks")
    for s in students:
        print(f'{s["id"]}\t{s["name"]}\t{s["age"]}\t{s["course"]}\t{s["marks"]}')

def search_student():
    name = input("Enter name to search: ").lower()
    found = False

    print("ID\tName\tAge\tCourse\tMarks")
    for s in students:
        if s["name"].lower() == name:
            print(f'{s["id"]}\t{s["name"]}\t{s["age"]}\t{s["course"]}\t{s["marks"]}')
            found = True

    if not found:
        print("Student not found.")

def update_student():
    sid = input("Enter Student ID to update: ")

    for s in students:
        if s["id"] == sid:
            print("1. Name  2. Age  3. Course  4. Marks")
            choice = input("Choose field to update: ")

            try:
                if choice == "1":
                    s["name"] = input("Enter new name: ")
                elif choice == "2":
                    s["age"] = int(input("Enter new age: "))
                elif choice == "3":
                    s["course"] = input("Enter new course: ")
                elif choice == "4":
                    s["marks"] = int(input("Enter new marks: "))
                else:
                    print("Invalid choice.")
                    return
            except ValueError:
                print("Invalid input.")
                return

            print("Student updated successfully.")
            return

    print("Invalid Student ID.")

def delete_student():
    sid = input("Enter Student ID to delete: ")

    for s in students:
        if s["id"] == sid:
            students.remove(s)
            print("Student deleted successfully.")
            return

    print("Invalid Student ID.")

# ---------------- Main Menu ----------------
while True:
    print("""
===== Student Management System =====
1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
""")

    choice = input("Enter your choice: ")

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
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Try again.")
