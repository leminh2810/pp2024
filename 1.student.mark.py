class Student:
    def __int__(self,id,name,Dob):
        self.id=id
        self.name=name
        self.Dob=Dob
        self.mark={}
class Course:
    def __int__(self,id,name):
        self.id=id
        self.name=name
def input_courses():
    courses = []
    num_courses = int(input("Enter number of courses: "))
    for i in range(num_courses):
        id = input("Enter course id: ")
        name = input("Enter course name: ")
        courses.append(Course(id, name))
    return courses
def input_marks(students, courses):
    for course in courses:
        for student in students:
            student.marks[course.id] = input(f"Enter marks for {student.name} in {course.name}: ")
def list_courses(courses):
    print("Courses")
    for course in courses:
        print(f"ID:{course.id},{course.name}")
def list_Student(students):
    print("Student")
    for student in students:
        print(f"ID:{student.id},Name:{student.name},Dob:{student.Dob}")
def show_student_marks(students, course_id):
    print(f"Marks for course {course_id}:")
    for student in students:
        if course_id in student.marks:
            print(f"{student.name}: {student.marks[course_id]}")
students = input.students()
courses=input.courses()
input_marks(students,courses)
list_courses(courses)
list_Student(students)
course_id= input("Enter id course id for mark:")
show_student_marks(students, course_id)




    

    


        