class person:
    name = "Dandu Leela"
    @classmethod
    def ChangeName(cls, new_name):
        cls.name = new_name

print(person.name)  # Output: Dandu Leela
person.ChangeName("Leela Dandu")
print(person.name)  # Output: Leela Dandu