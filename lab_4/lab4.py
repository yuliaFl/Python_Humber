# Create dictionary objects that contains students’ information
# Student dictionary should contain id, name, age, and school_name
# Student dictionary should have nested dictionaries for completed courses and ongoing courses
students = [
    {
        'id': '123',
        'name': 'Yulia',
        'age': 18,
        'school_name': 'Humber College',
        'completed_courses': {
            'Java': 95,
            'Network': 88,
            'React': 78
        },
        'ongoing_courses': {
            'Java': 59,
            'Network': 88,
            'React': 87
        }
    },
    {
        'id': '223',
        'name': 'Misha',
        'age': 19,
        'school_name': 'Humber College',
        'completed_courses': {
            'Java': 67,
            'Network': 78,
            'React': 76
        },
        'ongoing_courses': {
            'Java': 76,
            'Network': 87,
            'React': 67
        }
    },
    {
        'id': '323',
        'name': 'Pavel',
        'age': 18,
        'school_name': 'Humber College',
        'completed_courses': {
            'Java': 69,
            'Network': 87,
            'React': 87
        },
        'ongoing_courses': {
            'Java': 96,
            'Network': 78,
            'React': 78
        }
    },
]
# On program start ask user if they would like to:
while True:
    choice = input ('\nChoose option you would like to see: \n 1 to see all students information \n 2 Specific student \n 3 Ongoing grades \n 4 Completed grades \n 5 Average completed grades \n 6 Specific Grades \n or 7 to exit    :')
    if choice == '1' :
        # View all students’ information
        for student in students:
            print('==============================')
            print(f"Student ID: {student['id']}")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"School Name: {student['school_name']}")
            print(f"Completed Courses: {student['completed_courses']}")
            print(f"Ongoing Courses: {student['ongoing_courses']}")
            print("=============================================\n")
    # View all information on specific student, ask for id if selected
    elif choice == '2':
        id = input('Enter student id: ')
        for student in students:
            if student['id'] == id:
                print('==============================')
                print(f"Student ID: {student['id']}")
                print(f"Name: {student['name']}")
                print(f"Age: {student['age']}")
                print(f"School Name: {student['school_name']}")        
                print(f"Completed Courses: {student['completed_courses']}")
                print(f"Ongoing Courses: {student['ongoing_courses']}")
                print('==============================')
                break
    # View all ongoing grades of specific student, ask for id if selected
    elif choice == '3':
        id = input('Enter student id: ')
        for student in students:
            if student['id'] == id:
               for course, status in student['ongoing_courses'].items():
                    print(f"{course}: {status}")
    # View all completed grades of specific student, ask for id if selected
    elif choice == '4':
        id = input('Enter student id: ')
        for student in students:
            if student['id'] == id:
               for course, status in student['completed_courses'].items():
                    print(f"{course}: {status}")
    # View average completed grades of student, ask for id if selected
    elif choice == '5':
        id = input('Enter student id: ')
        for student in students:
            if student['id'] == id:
                completed_courses = student['completed_courses'].values()
                if len(completed_courses) > 0:
                    average_grade = sum(completed_courses) / len(completed_courses)
                    print(f"Average {average_grade:.2f}")
                else:
                    print("No completed courses found.")
    # View specific grade of specific student, ask for id and course name
    elif choice == '6':
        id = input('Enter student id: ')
        name = input('Enter student name: ')
        for student in students:
            if student['id'] == id:
                if name in student['completed_courses']:
                    grade = student['completed_courses'][name]
                    print(f"Grade {grade}")
                    break
                else:
                    print(f"{student['name']} has not completed {name}.")
                    break
    # After exit the program each operation ask user if they would like to perform another query or
    # Include error handling if user id or course name does not exist
    elif choice == '7':
        # Exit the program
        break
    
    else:
        print('Incorrect choice')