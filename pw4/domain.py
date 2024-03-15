class Student:
    def __init__(self,id,name,Dob):
        self.id = id
        self.name = name
        self.Dob = Dob
        self.mark = {}
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
    def display(self):
        print(f"Course ID:{self.id}, Course name{self.name}, Course credit{self.credit}")