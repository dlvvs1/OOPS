# A Small Example of a Private Method

class student:
    __name = "anonymous"  # private attribute

    def __hello(self): # private method
        return "Hello, " + self.__name
    
    def welcome(self): 
        return self.__hello()  # public method to access private method
    
s1 = student()
print(s1.welcome())  # Accessing private method via public method
print(s1.__name)  # This will raise an AttributeError since '__name' is private
print(s1.__hello())  # This will raise an AttributeError since '__hello' is private 