greeting = "hello"
print(greeting.upper())


class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age 

    def add_one(self, x):
        return x + 1

    def bark(self):
        print("bark")


class Student:

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade #0-100

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)

s1 = Student("Vinh",25, 95)
s2 = Student("Tim", 19, 85)
s3 = Student("Jill",20, 98)
s4 = Student("Mike", 24, 70)

course = Course("Science", 3)
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)

print(course.students[0].name)
print(course.students[1].name)
print(course.students[2].name)

print(course.get_average_grade())