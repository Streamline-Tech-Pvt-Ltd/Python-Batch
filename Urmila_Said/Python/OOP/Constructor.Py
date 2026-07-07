#Constructor: A Constructor in Python is a special method that is called automatically when an object is created.
#             It is used to initialize (assign values to) the object's attributes.

#EX: class Student:
#     def __init__(self):
#         print("Constructor is called")

# s1 = Student()

# __init__() is the constructor. It runs automatically when Student() creates an object.


# parametrized Constructor
# It accepts additional arguments to initialize object data.

# class Student:
#     def _init_(self,id,name,city):
#         self.id=id
#         self.name=name
#         self.city=city
#     def write(self,name):
#             return f"My name is :{self.name}"
# S1 = Student(1,"Pallavi","Nashik")
# print(S1.id)
# print(S1.name)
# print(S1.city)


#Default Counstructor
# It does not take any parameters except self.

# class Student:
#     def _init_(self):
#         print("Hello")

# Student()


#Destructor
# A destructor is a special method named __del__() that is automatically called when an object is destroyed.
#  It is used to perform cleanup tasks before the object is removed from memory.

# class Student:
#     def _del_(self):
#        print("Hello")
# s1= Student()
# print(id(s1))
# del s1
# print(id(s1))


