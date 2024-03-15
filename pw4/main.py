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