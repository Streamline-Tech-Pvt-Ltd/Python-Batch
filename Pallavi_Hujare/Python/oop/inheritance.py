# Inheritance

# Definition:
# Inheritance is an OOP concept that allows one class (child class) to acquire the properties (attributes) 
# and behaviors (methods) of another class (parent class).

# Syntax
# class Parent:
#     # Parent class code

# class Child(Parent):
#     # Child class code


# Parent Class
# The class whose properties are inherited.
# Also called:
# Base Class
# Super Class

# Example
# class Animal:
#     pass
# Animal is Parent.

# Child Class
# The class that inherits another class.
# Also called
# Derived Class
# Sub class
# Example
# class Dog(Animal):
#     pass

# Types of Inheritance

# Python supports 5 Types of Inheritance.

# Type                                            	Description
# Single                                      	One Parent → One Child
# Multiple	                                One Child inherits from Multiple Parents
# Multilevel                                  	Grandparent → Parent → Child
# Hierarchical	                              One Parent → Multiple Children
# Hybrid	                                        Combination of Multiple Types

# 1. Single Inheritance
# Animal
#    │
#    |
#  Dog

# class Animal:
#     def sound(self):
#         print("Animal Sound ")
# class Dog(Animal):
#      def bark(self):
#          print("Dog bark")
# d = Dog()
# d.sound()
# d.bark()

class Parent:
    def property(self):
        print("parent property")
class Child(Parent):
    def life(self):
        print("Child class")
c = Child()
c.life()
c.property()


# 2 . Multiple Inheritance
# Father      Mother
#     │          │
#     └────┬─────┘
#          ▼
#        Child


class Father:
    def money(self):
        print("Father's Money")
class Mother:
    def gold(self):
        print("Mother's Gold")
class Child(Father, Mother):
    pass
c = Child()
c.money()
c.gold()

# Output
# Father's Money
# Mother's Gold


# 3. Multilevel Inheritance
# Grandparent
#    │
#    ▼
#  parent
#    │
#    ▼
#  chiled

class Animal:

    def eat(self):
        print("Eating")


class Dog(Animal):

    def bark(self):
        print("Barking")


class Puppy(Dog):
    pass


p = Puppy()

p.eat()


# 4. Hierarchical Inheritance
#         Animal
#        /      \
#      Dog      Cat
class Animal:

    def eat(self):
        print("Eating")


class Dog(Animal):
    pass


class Cat(Animal):
    pass


d = Dog()
c = Cat()

d.eat()
c.eat()


# 5. Hybrid Inheritance

# Hybrid inheritance is a combination of two or more inheritance types.

#         Animal
#        /      \
#     Dog       Cat
#        \      /
#         Puppy

# Example:

class Animal:

    def eat(self):
        print("Eating")


class Dog(Animal):

    def bark(self):
        print("Bark")


class Cat(Animal):

    def meow(self):
        print("Meow")


class Puppy(Dog, Cat):
    pass


p = Puppy()

p.eat()
p.bark()
p.meow()


# D → B → C → A




# class College:
#     def __init__(self, college_name):
#         self.name = college_name
#         print("college name")

# class Student(co):
#     def __init__(self,student_nmae,):
#         self.student_name = student_name
#         print("This is Student class")
# s1= Student()
# s1.

# class College:
#     def __init__(self, name):
#         self.name = name
#     def admission(self,name):
#             return f"This is my college Name {self.name}"

# class Student(College):
#     def __init__(self,name):
#         self.name = name
#     def Learning(self,name):
#             return f"This is my course name {self.name}"
# s1 = Student('pallavi')
# print(s1.admission("kkw"))
# print(s1.Learning("py"))


