class Student: # class definition
    def __init__(self , name): # constructor method
        self.name = name # instance attribute

S1 = Student("Leela") # object of Student class
print(S1.name) # printing the name attribute
del S1.name # deleting the name attribute
print(S1.name)  # This will raise an AttributeError since 'name' has been deleted