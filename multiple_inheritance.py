class A:
    var1 = "Welcome to A"

class B:
    var2 = "Welcome to B"

class C(A, B):  # C inherits from both A and B
    var3 = "Welcome to C"


obj = C()
print(obj.var1)  # Accessing attribute from class A
print(obj.var2)  # Accessing attribute from class B
print(obj.var3)  # Accessing attribute from class C