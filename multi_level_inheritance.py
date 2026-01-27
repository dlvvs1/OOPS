# A small example for multi-level Inheritance

class car: # Base Class
    color = "blue" # class attribute
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")

class ToyotoCar(car): # Parent class
    def __init__(self , brand):
        self.brand = brand # instance attribute

class Fortuner(ToyotoCar): # child class
    def __init__(self , type):
        self.type = type


Car1 = Fortuner("diesel")
Car1.start()