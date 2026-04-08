# Polymorphisum :-  Poly      ==> Many  
#                   morphisum ==> Forms

# compiletime 
# runtime

# types:- 1. method overloading  ==> dont support
        # 2. method overriding   ==> supported



#  Normal function

# l1 = [1,2,3,4,5]
# print(len(l1)) 

# s1 = "streamline"
# print(len(s1))


# 1. method overloading:-   compiletime 
# way 1:-
#  we can achive method overloading using default argument.

# def add(a,b,c=0):
#     return a + b + c

# result = add(2,3)
# print(result)

# result1 = add(2,3,10)
# print(result1)

#  Way 2:- 
# **args


# def add(*args):
#     return sum(args)

# result = add(2,3)
# print(result)

# result1 = add(2,3,10,54)
# print(result1)


# method overriding :-  runtime


# A person :
    #  studnet
    #  leader
    #  employee
    #  hr


#  Air :
    #  fan
    #  ac
    #  cooler


# class Person:
#     def age(self):
#         print("this is the age of person")
    
# class Student(Person):
#     def age(self):
#         return "this is the age of Student"
    
# class Leader(Person):
#     def age(self):
#         return "this is the age of leader"

# class Employee(Person):
#     def age(self):
#         return "this is the age of employee"
    
# class Hr(Person):
#     def age(self):
#         return "this is the age of HR"
    

# p1 = Person()
# p1.age()


# obj1 = Student()
# obj1.age()

# obj2 = Leader()
# print(obj2.age())

# obj3 = Employee()
# print(obj3.age())

# obj4 = Hr()
# print(obj4.age())


# difference betwwen overloading and overriding

# parameter                  overloading                       overriding
# same method                  yes                              yes
# inheritance                  no                               yes
# time                         compile time                     Runtime
# supported                    no                                 yes
# through                    functional programing              oop


# example 2

class Bank:
    def interest(self):
        return "bank gives 5% interest"
    
class UBI(Bank):
    def interest1(self):
        return "bank gives 7% interest"
    
class SBI(Bank):
    def interest(self):
        return "bank gives 8% interest"
    
    
class HDFC(Bank):
    def interest(self):
        return "bank gives 32% interest"
    
o1 = UBI()
print(o1.interest())

o2 = HDFC()
print(o2.interest())