class student:
    def __init__(self , name , age): #__init__ method is a constructoe which executes automatically when an object is created
        self.name = name
        self.age = age
        print("the student name is {} and age is {}".format(self.name , self.age))

    
S = student("dandu" , 21) # S is an object of class student