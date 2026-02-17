# Student Grade Tracker
"""
Uses: 
Dictionary → store students + grades
List → store multiple grades per student
Tuple → store fixed student info (like name + age)

What It Should Do:
Let user add students
Store their grades
Calculate average
Display class summary
"""

students = {}

while True:
    print("\n--- Student Grade Tracker ---")
    print("1. Add Student")
    print("2. Add Grade")
    print("3. View Student")
    print("4. View All Students")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter Student Full Name: ")
        age = int(input("Enter Student Age: "))
        students[name] = {
            'info':(name, age),
            'final_grade': []}
        print(f"Student: {name} has been successfully added.")
        print(students)
    
    elif choice == "2":
        student_name = input("Enter Full Student's Name: ")
        if student_name in students:
            grade = int(input(f"Enter {student_name}'s Final Grade: "))
            students[student_name]['final_grade'].append(grade)
            print(f"{student_name}'s Final Grade: {students[student_name]['final_grade']}")
        else:
            print(f"Student {student_name} not found. Try adding them first.")

    elif choice == "3":
        view_student = input("Enter Full Student's Name: ")
        if view_student in students:
            print(students[view_student])
        else:
            print(f"Student {view_student} not found. Try adding them first.")

    elif choice == "4":
        for student_name, data in students.items():
            print(f"Name: {student_name}")
            print(f"Info: {data['info']}")
            print(f"Final Grade: {data['final_grade']}")
            print("------")
    
    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
