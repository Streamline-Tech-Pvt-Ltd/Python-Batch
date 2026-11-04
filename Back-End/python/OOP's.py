# Class and Object Example:-
class Laptop:
    name = "HP"
    color = "Black"
    shape = "Rectangle"

    def Programming(self):
        return "Demo"

    def Gaming(self):
        return None

l1 = Laptop()

print(l1.name)
print(l1.Programming())

# Constructor with Parameter:-
class Laptop:
    def __init__(self, name):
        self.name = name

    def Programming(self):
        return f"My name is {self.name}"

    def Gaming(self):
        return None

l1 = Laptop("Raj")

print(l1.Programming())


# changing self parameter:-
class Laptop:
    def __init__(ak, name):
        ak.name = name

    def Programming(ak):
        return f"My name is {ak.name}"

    def Gaming(ak):
        return None

l1 = Laptop("Anuj")

print(l1.Programming())