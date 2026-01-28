class student:
    def __init__(self , DBMS , AI , Software_devolopment):
        self.DBMS = DBMS
        self.AI = AI
        self.Software_devolopment = Software_devolopment
        # self.percentage = (self.DBMS + self.AI + self.Software_devolopment) / 3. # calculate percentage

    @property
    def percentage(self):
        return (self.DBMS + self.AI + self.Software_devolopment) / 3. # calculate percentage

stud1 = student(85 , 90 , 80)
print(f"The percentage of student is {stud1.percentage}") # accessing percentage attribute

stud1.DBMS = 95  # modifying DBMS marks
print(stud1.DBMS)
print(f"The updated percentage of student is {stud1.percentage}") # accessing updated percentage attribute