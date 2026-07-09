#Encapsulation is the process of wrapping (binding) data

# Real-Life Example
# ATM Machine
# When you use an ATM:
# You can deposit money
# You can withdraw money
# You can check balance
# But you cannot directly access or modify the bank database.
# Instead, you interact through specific methods.

# Syntax
# class ClassName:
#     def __init__(self):
#         self.variable = value
#     def method(self):
#         pass

# access Specifiers in Python

# Python provides three types of access specifiers.

# Access Specifier	            Symbol                  	    Access
# Public	                      No underscore	                Anywhere
# Protected	                    _variable	          Inside class and subclasses (by convention)
# Private	                   __variable	            Only inside the class

# This is Encapsulation.

# class Bank:
#     def __init__(self,name,acc_type,balance):
#         self.name = name
#         self._acc_type = acc_type
#         self.__balance = balance
# b1 = Bank("Pallavi","Saving",500000)
# print(b1.name)
# print(b1._acc_type)
# print(b1.__balance)



# class Bank:

#     def __init__(self, name, acc_type, balance, password, age):
#         self.name = name              # Public attribute
#         self._acc_type = acc_type     # Protected attribute
#         self.__balance = balance      # Private attribute
#         self.__password = password    # Private attribute
#         self._age = age               # Protected attribute

#     def get_balance(self):
#         return self.__balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             return f"Deposited {amount}. New balance is {self.__balance}"
#         else:
#             return "Invalid deposit amount"

#     def receipt(self):
#         print("Receipt is generated")
#         print("Name :", self.name)
#         print("Account Type :", self._acc_type)
#         print("Balance :", self.__balance)


# # Object Creation
# b1 = Bank("Pallavi", "Saving", 100000, "abc123", 22)
# print("Name :", b1.name)
# print("Account Type :", b1._acc_type)
# # print(b1.__balance)   # Error (Private Attribute)
# print("Balance :", b1.get_balance())
# print(b1.deposit(1000))
# print("Updated Balance :", b1.get_balance())
# print("\n==============================\n")
# b1.receipt()

#1. Student Management System

# class Student:
#     def __init__(self, name, course, marks, password):
#         self.name = name               # Public
#         self._course = course          # Protected
#         self.__marks = marks           # Private
#         self.__password = password     # Private

#     def get_marks(self):
#         return self.__marks

#     def add_marks(self, marks):
#         self.__marks += marks

#     def display(self):
#         print("Student Name :", self.name)
#         print("Course :", self._course)
#         print("Marks :", self.__marks)

# s1 = Student("Pallavi", "MCA", 85, "abc123")
# print(s1.name)
# print(s1._course)
# print(s1.get_marks())
# print("\n==============================\n")
# s1.add_marks(10)
# print("Updated Marks :", s1.get_marks())
# s1.display()


class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self._department = department
        self.__salary = salary
    def get_salary(self):
        return self.__salary
    def increment(self, amount):
        self.__salary += amount
    def display(self):
        print("Employee :", self.name)
        print("Department :", self._department)
        print("Salary :", self.__salary)
e1 = Employee("Pallavi", "CS", 5000000)
print(e1.name)
print(e1._department)
print(e1.get_salary())
e1.increment(500000)
print("Updated Salary :", e1.get_salary())
e1.display()



        
