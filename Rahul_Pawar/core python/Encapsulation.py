#  Encapsulation :-  Data Binding

# encapsulation

# Access specifier :-
        # public( ) :- accessible outside of the class
        # protected(_) :- accessible but avoid it
        # private(__) :-  It is not accessible outside of the class.
# getter  method  :- syntax:- get_<attribute_name>(self):
# setter method   :- syntax:- set_<attribute_name>(self):


# Employee
#  name
#  role
#  salary
#  age


# class Employee:
#     def _init_(self,name,role,salary,age):
#         self.name = name        # public
#         self._role = role       # protected
#         self.__salary = salary  # Private
#         self.age = age          # Public
    
#     def pn(self):
#         return f"{self.name} is my name"
    
#     # getter  method  syntax:- get_<attribute_name>(self):
#     def get_salary(self):
#         return self.__salary
    
    
#     # setter method  syntax:- set_<attribute_name>(self):
#     # pramod ==> salary == 50000  ===> 70000
    
#     def set_salary(self,sal):
#         if sal >= 50000 :
#             self.__salary = sal
#         else:
#             print("Invalid salary")
            
        
    
# obj = Employee("pramod","Full stack python developer",50000,21)
# print(obj.pn())
# print(obj.name)
# print(obj._role)
# print(obj.__salary)
# print(obj.age)
# print("Original salary:", obj.get_salary())

# obj.set_salary(40000)
    

# print("Updated salary:", obj.get_salary())


