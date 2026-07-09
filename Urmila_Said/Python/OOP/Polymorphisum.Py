# Polymorphisum:
# Polymorphism means the same method or function can perform different tasks depending on the object.
# Poly = Many
# Morph = Forms
# Polymorphism means One thing, many forms.

# types: 
# 1. overloading :- does not support in python.
        # 1. Method overloading

# 2. Overriding :- Supoort in python 
        # 1. method overriding
        # 2. variable overriding

# n1 = 100
# n2 = 200
# print(n1.__add__(n2))
# print(n1 + n2)

# n1 = 500
# n2 = 700
# print(n1>n2)
# print(n1.__gt__(n2))

# class Book:
#     def __init__(self,name,pages):
#         self.name = name
#         self.pages = pages
#     def __add__(self,other):
#         return self.pages + other.pages

# B1 = Book("Automic Habit",200)
# B2 = Book("Garud Zep",300)
# total = B1.pages + B2.pages
# print(total)
# print(B1 + B2)


# Overloading in Python Example
# class Student:
#     def __init__(self,name):
#         print("First Constuctor")
#         self.name = name

#     def __init__(self,name,age):
#         print("Second Constructor")
#         self.name = name
#         self.age = age

#     def __init__(self,name,age,city):
#         print("Third constructor")
#         self.name = name
#         self.age = age
#         self.city = city

# S1 = Student("Urmila",21,"Nashik")
# print(S1)

# Overriding in python Example
# class Urmila:
#     def add(self,n1,n2):
#         return n1+n2
#     def sub(self,n1,n2):
#         return n1-n2
    
# class Pallavi(Urmila):
#     def mul(self,n1,n2):
#         return n1*n2
#     def div(self,n1,n2):
#         return n1/n2
#     def add(self,n1,n2,n3):
#         return n1+n2+n3
    
# p1 = Pallavi()
# print(p1.add(20,30,20))
# print(p1.sub(50,40))



# class Intern1:
#     name = "Urmila"
# class Intern2(Intern1):
#     name = "pallavi"
# i1 = Intern2()
# print(i1.name)


#Practice Example

# 1.Overriding

# class Person:
#     def work(self):
#         print("Person work")
# class Student(Person):
#     def work(self):
#         print("Student studies")

# S1 = Student()
# S1.work()

# class Bird:
#     def fly(self):
#         print("Bird fly")
# class Sparrow(Bird):
#     def fly(self):
#         print("Sparrow fly")

# B1 = Sparrow()
# B1.fly()


class Shape:
    def draw(self):
        print("Draw Shape")

class Circle(Shape):
    def draw(self):
        print("Draw Circle")

S1 = Circle()
S1.draw()