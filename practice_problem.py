class stubent:
    def __init__(self , sub1 , sub2 , sub3 , marks1 , marks2 , marks3):
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def average(self):
        print(f"the average of three subjects is {(self.marks1 + self.marks2 + self.marks3)/3}")

sub1 = input("enter the subject 1 name: ")
sub2 = input("enter the subject 2 name: ")
sub3 = input("enter the subject 3 name: ") 

marks1 = int(input(f"enter the marks of {sub1}: "))
marks2 = int(input(f"enter the marks of {sub2}: "))
marks3 = int(input(f"enter the marks of {sub3}: "))

S = stubent(sub1 , sub2 , sub3 , marks1 , marks2 , marks3)
S.average()