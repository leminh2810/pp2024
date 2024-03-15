import math
import numpy as np
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
        self.mark[course.name]= marks.floor(marks*10)/10.0
    def calculate_gpa(self,course):
        total_marks = 0
        total_credit =0
        for course in course:
                if course.name in self.mark:
                    total_marks += self.mark[course.name]* course.credit
                    total_credit += course.credit
                if total_credit == 0:
                    return 0
                else:
                    return total_marks/total_credit
        
    def display(self):
        print(f"Student ID:{self.id}, Student Name{self.name}, Student Dob{self.Dob}")
class course:
    def __init__(self,id,name,credit):
        self.id = id
        self.name = name
        self.credit = credit
    def input_number_of_course(self):
        return int(input("Enter number of course:"))
    def input(self):
        self.id = input("Enter course ID:")
        self.name = input("Enter course name")
        self.credit = input("Enter course credits:")
    def display(self):
        print(f"Course ID:{self.id}, Course name{self.name}, Course credit{self.credit}")
def main():
    Student =[]
    num_student = int(input("Insert number of student"))
    for _ in  range (num_student):
        Student = Student("","","")
        Student.input()
        Student.append(Student)
    Course = []
    num_course = int(input("Enter number of course"))
    for _ in range (num_course):
        course = course("","",0)
        course.input()
        course.append(course)
    for student in student:
        for course in course:
            student.input_mark(course)
    for student in student:
        gpa = student.calculate_gpa(course)
        print(f"Student ID: {student.id}, GPA: {gpa:.2f}")
    student.sort(key=lambda x: x.calculate_gpa(course), reverse=True)
    print("\nStudents sorted by GPA:")
    for student in students:
        print(f"Student ID: {student.id}, GPA: {student.calculate_gpa(course):.2f}")

if __name__ == "__main__":
    main()

    
    



    

    
    
        
