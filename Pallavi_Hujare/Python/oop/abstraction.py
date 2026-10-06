# Abstraction
# Abstraction is the process of hiding the implementation details and showing only the essential features to the user.


# How is Abstraction achieved in Python?

# Python provides the ABC (Abstract Base Class) module.
# We use

# from abc import ABC, abstractmethod

# Where

# ABC → Base class for abstract classes.
# @abstractmethod → Declares an abstract method.

# Abstract Class : An Abstract Class is a class that contains one or more abstract methods
#Syntax
# from abc import ABC, abstractmethod

# class Parent(ABC):

#     @abstractmethod
#     def show(self):
#         pass

# Abstract Method : An Abstract Method is a method that is declared but has no implementation.

# Example:

# @abstractmethod
# def display(self):
#     pass


# from abc import ABC, abstractmethod

# class Car(ABC):

#     @abstractmethod
#     def start(self):
#         pass

# class BMW(Car):

#     def start(self):
#         print("BMW Started")

# car = BMW()
# car.start()


# Summary Table
# Import Method	                                Example
# Import entire module                        	import math
# Import specific function	                from math import sqrt
# Import multiple functions	            from math import sqrt, factorial
# Import with alias	                          import math as m
# Import everything	                        from math import *