class Student:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Student name:", self.name)

s = Student("Leela")
s.show()
