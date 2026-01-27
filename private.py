# A Small Example For Private attribute

class Account:
    def __init__(self,acc_name,acc_pass):
        self.acc_name = acc_name
        self.__acc_pass = acc_pass  # private attribute

Acc1 = Account("Leela","Leela@123")
print(Acc1.acc_name)  # printing the name
print(Acc1.__acc_pass)  # This will raise an AttributeError since '__acc_pass' is private