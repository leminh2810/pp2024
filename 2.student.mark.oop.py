class Student:
    def __init__(self,id,name,Dob):
        self.id = id
        self.name = name
        self.Dob = Dob
        self.mark = {}
    def input_number_of_student(self):
        return int(input("Enter number of students:"))
    def input(self):
        self.id = input("Enter student ID:")
        self.name = input("Enter student name:")
        self.Dob = input("Enter student date of birth")
    def input_mark(self):
        marks = float(input("Enter marks for student{self.id} in course{course.name}"))
        self.mark[course.name]= marks
    def display(self):
        print(f"Student ID:{self.id}, Student Name{self.name}, Student Dob{self.Dob}")
class course:
    def __init__(course,id,name):
        course.id = id
        course.name = name
    def input_number_of_course(course):
        return int(input("Enter number of course:"))
    def input(course):
        course.id = input("Enter course ID:")
        course.name = input("Enter course name")
    def display(course):
        print(f"Course ID:{course.id}, Course name{course.name}")
    

    
    
        
