class Student:
    school = "Sandip" # class attribute

    def __init__(self , nmae , marks): # instance attributes
        self.name = nmae
        self.marks = marks


S1 = Student("Dandu" , 85) # S1 is an object of class Student
S2 = Student("Leela" , 90) # S2 is another object of class Student

print(S1.name) # accessing instance attribute
S1.marks = 95 # modifying instance attribute
print(S1.marks)