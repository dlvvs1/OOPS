class car: # class definition
    def __init__(self): #constructor method
        self.acc = False
        self.brk = False
        self.clutch = False

    def Start_car(self): # method to start the car
        self.acc = True
        self.clutch = True
        ''' above two lines are the steps to start a car
        But they are not shown in the output, 
        Because the class doesn't shows the implemntation details but interacts with user interface only.'''
        print("car started")

car1 = car() # object of car class
car1.Start_car() # calling the Start_car method of car class
