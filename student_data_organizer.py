print("Welcome to the Student Data Organizer!")

students = {}

while True:
    print("Select an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display Subjects")
    print("0. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Enter student details:")
        student_id = int(input("Student ID: "))
        name = input("Name: ")
        age = int(input("Age: "))
        grade = input("Grade: ")
        dob = input("Date of Birth (YYYY-MM-DD): ")        
        subjects_input = input("Subjects (comma-separated): ")

        subjects = set(subjects_input.split(","))

        identity = (student_id, dob)

        students[identity] = {
            "name": name,
            "age": age,
            "grade": grade,
            "subjects": subjects
        }

        print("Student added successfully!")

    elif choice == 2:
        print("--- Display All Students ---")

        for identity in students:
            info = students[identity]

            print(
                "Student ID:", identity[0],
                "| Name:", info["name"],
                "| Age:", info["age"],
                "| Grade:", info["grade"],
                "| DOB:", identity[1],
                "| Subjects:", end=" "
            )

            subject_list = []
            for sub in info["subjects"]:
                subject_list.append(sub)

            for i in range(len(subject_list)):
                if i == 0:
                    print(subject_list[i], end="")
                else:
                    print(" , " + subject_list[i], end="")

            print()

    elif choice == 3:
        student_id = int(input("Enter Student ID to update: "))
        found = False

        for identity in students:
            if identity[0] == student_id:
                students[identity]["age"] = int(input("Enter new age: "))
                subjects_input = input("Enter new subjects (comma-separated): ")
                students[identity]["subjects"] = set(subjects_input.split(","))
                print("Student updated successfully!")
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == 4:
        student_id = int(input("Enter Student ID to delete: "))
        found = False

        for identity in list(students):
            if identity[0] == student_id:
                print("Student deleted:", students[identity]["name"])
                del students[identity]
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == 5:
        print("--- Subjects Offered ---")

        all_subjects = set()

        for identity in students:
            for sub in students[identity]["subjects"]:
                all_subjects.add(sub)

        subject_list = []
        for sub in all_subjects:
            subject_list.append(sub)

        for sub in subject_list:
            print(sub)

    elif choice == 0:
        print("Thank you for using the Student Data Organizer!")
        break

    else:
        print("Invalid choice. Please try again.")
