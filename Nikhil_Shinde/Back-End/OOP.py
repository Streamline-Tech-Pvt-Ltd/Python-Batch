# OOP: Object Oriented Programming

    # - oop is a programming approach where cod eis organized using objects and classes,
    # similar to real word things

    # class define using class keyword
     


    # what is an oop?
       # oop in python is a way of organaizing and designing code by creating "objects" that represent real-world things.
       # these object are combine Data(attributes) and behaviour(methods) into a single unit.
       #  making the code easier to manage , reuse and understand.
    
    # what is class in python?
       #  a class is defined with class keyword.
       # class is a blueprint for creating objects.
       # If define atrributes(Data) and method(behviour) that the objects will have
    
    #  what is object in python?
        #  A object is an instance of a class.
        #  It represent the real world entity with specificc value assigned to the attributes defined in the class.



# class
# object
# object referance
# constructor
# self first parameter
# initialization


#  example1:-

# class Student:
#     name = "Pramod"  # attributes
#     roll_no = 1
#     age = 21
#     std = "10th"
    
#     def study(self):    # method
#         return f"studeied....."
    
# obj = Student()
# print(obj.name)
# print(obj.study())


# Example:2

# class Car:
#     name = "BMW"
#     model = "Base"
#     color = "white"
    
#     def run(self):
#         print("running")
        
# obj1  = Car()
# print(obj1.run())
# print(obj1.color)




# constructor:- 


# example 1:


# class Person:
    
#     def _init_(self,name,age,city):    # constructor == use==> to initialise the object or variable
        
#         self.name = name    # initialization
#         self.age = age
#         self.city = city   
        
#     def demo(self):
#         return f"{self.name} <== this is my name"
    
    
    
# obj = Person("pramod",21,"Nagar")
# print(obj.name)
# print(obj.demo())



# Example 2:


# class Employee:
    
def __init__(self,name,emp_id,salary):
        
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

def show(self):
        return f"{self.name}"


obj = Employee("Nikhil",15,20000)

print(obj.show())




# # example 3:


# class Subject:
                                        
#     def __init__(self,name):
#         self.name = name
        
#     def subject(self):
#         return f"{self.name}<== subjects"
        
        
# o1 = Subject("math")
# print(o1.subject())



# example 4:

# class Book:
#     def __init__(self,title,author):
#         self.title = title
#         self.author = author

#     def data(self):
#       return f"{self.title}"


# obj = Book("lion story","xyz")
# print(obj.title)
# print(obj.data())


# example 5:


# class Rahul:

#     def __init__(self,age,std,):
#         self.age = age
#         self.std = std

#     def Age(self):
#         return f"{self.age}<===== My age"
    
# obj = Rahul(21,12)
# print(obj.std,"standard")
# print(obj.Age())








#  OOP pilleres:

      # oop pilleres used to design clean ,reusable and scalable code.


   # four pilleres: 
      #  Inheritance
      # polymorphism
      # abstraction
      # encapsulation