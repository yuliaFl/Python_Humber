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
# View all completed grades of specific student, ask for id if selected
# View average completed grades of student, ask for id if selected
# View specific grade of specific student, ask for id and course name
# After exit the program each operation ask user if they would like to perform another query or
# Include error handling if user id or course name does not exist

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
    elif choice == "7":
        print("Exiting the program")
        break