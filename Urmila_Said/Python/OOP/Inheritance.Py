# Inheritance:

        # Inheritance means one class gets the properties and methods of another class.
        # Means parent class properties inherits into  child class


# child class === Derived class or Sub class
# parent class === Base class or Super class

# Object created the child class not a parent class.
# Inherit is class not a method.

# Types:

# 1. Single Inheritance:
#    One child class inherits from one parent class.
#     Parent
#       │
#      Child

# class Father:
#     def show(self):
#         print("Father Class")

# class Son(Father):
#     def display(self):
#         print("Son Class")

# s = Son()
# s.show()
# s.display()


# 2. Multiple Inheritance :
# A child class inherits from more than one parent class.
# Parent1    Parent2
#      \      /
#       Child

# class Father:
#     name = "Urmila"
#     def property(self):
#         return "Father property"
        
# class Mother:
#     def property1(self):
#        return "mother property "
    
# class Child(Mother,Father):
#     def education(self):
#         return "education pursuing "
    
# obj = Child()
# print(obj.property())
# print(obj.property1())
# print(obj.education())


# 3. Multilevel Inheritance :
# A class inherits from another child class.
#   Grandparent
#       │
#     Parent
#       │
#      Child 


# class GrandFather:
#     name = "Urmila"
#     def property(self):
#         return "GrandFather property"
        
# class Father(GrandFather):
#     def property1(self):
#         return "Father property "
    
# class Child(Father):
#     def education(self):
#         return "education pursuing "
    
# obj = Child()
# print(obj.name)
# print(obj.education())


# 4. Hierarchical Inheritance :
# One parent class has multiple child classes.
#        Parent
#       /      \
#   Child1   Child2

# class Father:
#     name = "Urmila"
#     def property(self):
#         return "Father property"
        
# class Son1(Father):
#     def education1(self):
#         return "Son 1 property "
    
# class Son2(Father):
#     def education2(self):
#         return "Son 2 Property"
    
# obj1 = Son1()
# print(obj1.education1())

# obj1 = Son2()
# print(obj1.property())


# 5. Hybrid Inheritance:
# Hybrid inheritance is a combination of two or more inheritance types.
#         A
#       /   \
#      B     C
#       \   /
#         D

# class Family:
#      def member(self):
#          return " Family member"
    
# class Father(Family):
#      def dad(self):
#          return "DAD"
       
# class Son1(Father):
#      def boy1(self):
#          return " BOY 1"
    
# class Son2(Father,Family):
#      def boy2(self):
#          return "BOY 2"
    
# obj = Son2()
# print(obj.boy2())

# obj1 = Son1()
# print(obj1.boy1())
# print(obj1.dad())
# print(obj1.member())

# Constructor through single inheritance

# class College:
#     def __init__(self,name):
#         self.F_name = self.name
        
        
# class Daughter(Father):
#     def __init__(Father):
#         print("Daughter class")

# D = Daughter()
# D = Father()

class College:
    def __init__(self,name):
        self.name = name
    def addmission(self,name):
        return f"This is my college name{self.name}"
        
class Student(College):
    def __init__(self,name):
        self.name = name
    def learning(self,name):
        return f"This is my{self.name}"
        
s1 = Student("D.Y.P")
print(s1.addmission("Urmila"))
print(s1.learning("Python"))
print(s1.name)