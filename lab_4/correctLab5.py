# Create dictionary objects that contains students’ information
students = {}
# Student dictionary should contain id, name, age, and school_name
# Student dictionary should have nested dictionaries for completed courses and ongoing courses
def create_student(id, name, age, school_name):
    student = {
        "id": id,
        "name": name,
        "age": age,
        "school_name": school_name,
        "completed_courses": {},
        "ongoing_courses": {}
    }
    return student

def add_student(students, student):
    students[student["id"]] = student

student1= create_student(111,"Yulia", 18, "Humber" )
add_student(students, student1)
student2= create_student(222,"Misha", 18, "Humber" )
add_student(students, student2)
student3= create_student(333,"Ira", 18, "Humber" )
add_student(students, student3)
student4= create_student(444,"Kira", 18, "Humber" )
add_student(students, student4)

student1["ongoing_courses"]["Math"] = 90
student1["ongoing_courses"]["Science"] = 85
student1["ongoing_courses"]["History"] = 75

student2["ongoing_courses"]["Math"] = 80
student2["ongoing_courses"]["Science"] = 58
student2["ongoing_courses"]["History"] = 57

student3["ongoing_courses"]["Math"] = 70
student3["ongoing_courses"]["Science"] = 75
student3["ongoing_courses"]["History"] = 88

student4["ongoing_courses"]["Math"] = 70
student4["ongoing_courses"]["Science"] = 85
student4["ongoing_courses"]["History"] = 68

student1["completed_courses"]["Java"] = 90
student1["completed_courses"]["Python"] = 85
student1["completed_courses"]["Network"] = 75

student2["completed_courses"]["Java"] = 80
student2["completed_courses"]["Python"] = 58
student2["completed_courses"]["Network"] = 57

student3["completed_courses"]["Java"] = 70
student3["completed_courses"]["Python"] = 75
student3["completed_courses"]["Network"] = 88

student4["completed_courses"]["Java"] = 70
student4["completed_courses"]["Python"] = 85
student4["completed_courses"]["Network"] = 68

# View all students’ information
def view_all_students(students):
    for student in students.values():
        print(" ")
        print("ID:", student["id"])
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("School Name:", student["school_name"])
        print("Completed Courses:", student["completed_courses"])
        print("Ongoing Courses:", student["ongoing_courses"])
        print("\n")

# View all information on specific student, ask for id if selected
def view_one_student(students, student_id):
    student = students.get(student_id)
    if student:
        print(" ")
        print("ID:", student["id"])
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("School Name:", student["school_name"])
        print("Completed Courses:", student["completed_courses"])
        print("Ongoing Courses:", student["ongoing_courses"])
        print(" ")
    else:
        print("Student not found")
# View all ongoing grades of specific student, ask for id if selected
def view_ongoing_grades(students, student_id):
    student = students.get(student_id)
    if student:
        print("Ongoing Courses and Grades for Student:", student["name"])
        for course, grade in student["ongoing_courses"].items():
            print(f"Course: {course}, Grade: {grade}")
    else:
        print("Student not found")
# View all completed grades of specific student, ask for id if selected
def view_completed_grades(students, student_id):
    student = students.get(student_id)
    if student:
        print("Completed Courses and Grades for Student:", student["name"])
        for course, grade in student["completed_courses"].items():
            print(f"Course: {course}, Grade: {grade}")
    else:
        print("Student not found")
# View average completed grades of student, ask for id if selected
def view_average(students, student_id):
    student = students.get(student_id)
    if student:
        completed_courses = student["completed_courses"]
        if completed_courses:
            average_grade = sum(completed_courses.values()) / len(completed_courses)
            print(f"Average: {average_grade:.2f}")
        else:
            print("No completed courses")
    else:
        print("Student not found")
# View specific grade of specific student, ask for id and course name
def view_specific_grade(students, student_id, course_name):
    student = students.get(student_id)
    if student:
        completed_courses = student["completed_courses"]
        grade = completed_courses.get(course_name)
        if grade is not None:
            print(f"Grade for Student {student['name']} in Course {course_name}: {grade}")
        else:
            print("Course not found")
    else:
        print("Student not found")

# On program start ask user if they would like to:
while True:
    print("Your options are the following:")
    print("1. View all student's information")
    print("2. View specific student")
    print("3. View ongoing grades for a student")
    print("4. View completed grades for a student")
    print("5. View average completed grades for a student")
    print("6. View grade of a student")
    print("7. Exit")

    choice=input("Choose one: ")

    if choice == "1":
        view_all_students(students)
    elif choice == "2":
        student_id = int(input("Enter the student ID: "))
        view_one_student(students, student_id)
    elif choice == "3":
        student_id = int(input("Enter the student ID: "))
        view_ongoing_grades(students, student_id)
    elif choice == "4":
        student_id = int(input("Enter the student ID: "))
        view_completed_grades(students, student_id)
    elif choice == "5":
        student_id = int(input("Enter the student ID: "))
        view_average(students, student_id)
    elif choice == "6":
        student_id = int(input("Enter the student ID: "))
        course_name = input("Enter the course name: ")
        view_specific_grade(students, student_id, course_name)
    elif choice == "7":
        print("Exiting the program")
        break
    else:
        print("Invalid. Try again")
# After exit the program each operation ask user if they would like to perform another query or
# Include error handling if user id or course name does not exist