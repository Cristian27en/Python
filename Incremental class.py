# create class Student
class Student:
    # the class starts with 0 students
    num_student = 0

    # inside the class Student create a function in order to create new students
    def __init__(self, name):
        self.name = name
        Student.num_student = Student.num_student + 1

# create new students
s1 = Student('Maria')
s2 = Student('David')

# print how many students are in the class Student
print(Student.num_student)
