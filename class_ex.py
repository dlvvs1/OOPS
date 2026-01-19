class car:
    def __init__(self , speed , brand):
        self.speed = speed
        self.brand = brand

    def display(self):
        return("the car brand is {} so the 2nd gear speed is {}".format(self.brand , self.speed))
    
c = car(70 , "benz")
print(c.display()) 