class car: 
    def __init__(self , type):
        self.type = type

    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")

class BMW(car): 
    def __init__(self , name , type):
        super().__init__(type)  # calling the constructor of the parent class
        self.name = name 


Car1 = BMW("X5" , "petrol") 
print(Car1.type)  # accessing inherited attribute