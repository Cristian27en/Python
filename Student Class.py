# create class Students

class Students:
    # this is a counter. the class starts with 0 students
    num_people = 0

    # create function in order to be able to create new students
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # the counter will increment with new students
        Students.num_people = Students.num_people + 1

# create students
s1 = Students('Maria', 10)
s2 = Students('David', 9)

# print students
print('Student number 1: ', s1.name, s1.age)
print('Student number 2: ', s2.name, s2.age)
# print how many entries are in the class Students
print('How many students are: ', Students.num_people)

# move to list
student_list = [s1, s2]

# print student list
for student in student_list:
    print(f'Name: {student.name}, Age: {student.age}')