student = []
courses = []
marks = []
def input_students():
    number_students = int(input("Insert number of students"))
    for _ in range(number_students):
        id = input("Student's id is")
        name = input("Student's name is")
        Dob = input("Student's dob is")
        student.append(id,name,Dob)
def input_courses():
    number_courses = int(input("Insert number of courses"))
    for _ in range(number_courses):
        id = input("Insert course's id:")
        name = input("Insert course's name:")
        courses.append(id,name)
def input_marks():
    course_id = input("Insert a course id")
    for student in student:
        mark = float(input("Enter mark for {student[1]} in {course_id[0]}"))
        marks[{student[0],course_id}] = mark
def list_courses():
    for course in courses:
        print(course)
def list_students():
    for student in student:
        print(student)
def show_student_marks():
    for student in student:
         print(f"Mark for student {student[1]} in course {course_id}: {marks[(student[0], course_id)]}"
               input_students()
input_courses()
input_marks()
list_courses()
list_students()
course_id = input("Enter course id to show marks: ")
show_marks(course_id)

    
    
    

