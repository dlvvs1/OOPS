# A Small example of Inheritance

class car: # Base class
    color = "blue" # class attribute
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")

class BMW(car): # child class
    def __init__(self , name):
        self.name = name # instance attribute


Car1 = BMW("X5") # object of class BMW
Car2 = BMW("X3") # another object of class BMW

print(Car1.color) # accessing inherited class attribute
print(Car1.start()) # calling inherited method
print(Car2.stop())  # calling inherited method 


# we can say this type of inheritance known as "Single-Level Inheritance".