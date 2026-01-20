class student:
    def __init__(self , name , age): 
        self.name = name
        self.age = age
        
    def __init__(self):
        print("the student name is {} and age is {}".format(self.name , self.age))

S = student("dandu" , 21) 

# here the second __init__ method will override the first __init__ method.
# constructor overloading is not possible in python like java.
# but we can achieve the same using default arguments or *args and **kwargs.