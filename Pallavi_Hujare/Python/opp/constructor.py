# Definition

# A constructor is a special method in Python named __init__() that is automatically called when an object is created. 
# It is used to initialize the object's attributes (instance variables).

# Syntax
# class ClassName:
#     def __init__(self):
        # Initialization code


#1. Default Constructor
# Definition
# A default constructor is a constructor that does not take any arguments except self. 
# It is used to perform default initialization or execute code when an object is created.

# Example
class Student:
    def __init__(self):
        print("Hello")

s1 = Student()

# Output
# Hello


# 2. Parameterized Constructor
# Definition
# A parameterized constructor is a constructor that accepts parameters in addition to self. I
# t is used to initialize object attributes with values provided when the object is created.

# Example
class Student:
    def __init__(self, id, name, city):
        self.id = id
        self.name = name
        self.city = city

s1 = Student(1, "Pallavi", "Nashik")

print(s1.id)
print(s1.name)
print(s1.city)

# Output
# 1
# Pallavi
# Nashik


# Destructor

# A destructor is a special method in Python named __del__() that is automatically
#  called when an object is about to be destroyed or deleted. 
# It is mainly used to perform cleanup tasks, such as releasing resources or closing files.

# Syntax
# class ClassName:
#     def __del__(self):
        # Cleanup code
# Example
class Student:
    def __del__(self):
        print("Object Destroyed")

s1 = Student()
del s1

# Output
# Object Destroyed