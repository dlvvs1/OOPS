class student:
    def __init__(self , name , age): 
        self.name = name
        self.age = age
        
    def __init__(self):
        print("the student name is {} and age is {}".format(self.name , self.age))

S = student("dandu" , 21) 