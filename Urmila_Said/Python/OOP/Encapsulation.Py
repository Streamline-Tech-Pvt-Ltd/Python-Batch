# Encapsulation: Encapsulation means wrapping data (variables) and methods (functions) into a single unit (class) 
# and protecting the data from direct access.


# Access Modifier:
# 1.Public : A public member can be accessed from anywhere (inside and outside the class).
# 2.Protected : A protected member is intended to be accessed within the class and by its child classes.
#               depending on condition.
#               it is indicated by a single underscore (_).
# 3.Private :A private member cannot be accessed directly from outside the class.
#            It is created using double underscores (__).


# Example:
# Bank Account
# You cannot directly change your bank balance
# Instead, you use
# Deposit
# Withdraw
# Check Balance
# The balance is protected.
# This is encapsulation.


class Bank:
    def __init__(self,name,acc_type,balance):
        self.name = name
        self._acc_type = acc_type
        self.__balance = balance

B1 = Bank("Urmila","Saving",50000)
print(B1.name)
print(B1._acc_type)
print(B1.__balance)
      

# Using Getter and Setter Method:

# class Bank:
#     def __init__(self,name,acc_type,balance):
#         self.name=name              # Public attribute
#         self._acc_type=acc_type     # Protected attribute
#         self.__balance=balance      # Private attribute
        
#     def get_balance(self):
#         return self.__balance
    
#     def deposit(self,amount):
#         if amount > 0: # 1000
#             self.__balance += amount
#         else:
#             print("Invalid deposit amount")
#         return f"Deposited {amount}. New balance is {self.__balance}"

#     def recipt(self):
#         print("Recipt is generated")
#         print("Name:",self.name)
#         print("Account Type:",self._acc_type)
#         print("Balance:",self.__balance)
    

# b1 = Bank("urmila","Saving",10000)
# # print(b1.name)
# # print(b1._acc_type)
# # print(b1.__balance)  
# # print(b1.get_balance())
# print(b1.get_balance())
# b1.deposit(1000)
# print(b1.get_balance())
# print("\n===============================\n")
# b1.recipt()


# class Student:
#     def __init__(self,name,roll_no,marks):
#         self.name = name
#         self._roll_no = roll_no
#         self.__marks = marks

#     def get_roll_no(self):
#         return self._roll_no
    
#     def marks(self,marks):
#         return self.__marks
    
#     def receipt(self):
#         print("Addmission Receipt")
#         print("name:",self.name)
#         print("roll_no:",self._roll_no)
#         print("marks:",self.__marks)

# S1 = Student("Saniya",15,90)
# # print(S1.name)
# # print(S1.roll_no)              
# # print(S1.__marks)              # Occur the Attribute error
# print(S1.get_roll_no())          # Access get through method
# S1.receipt()


# class Phone:
#     def __init__(self,name,email,contact_no):
#         self.name = name
#         self._email = email
#         self.__contact_no = contact_no

#     def get_email(self):
#         return self._email
    
#     def contact(self,contact_no):
#         return self.__contact_no
    
#     def details(self):
#         print("My Phone Details")
#         print("name:",self.name)
#         print("email:",self._email)
#         print("contact_no:",self.__contact_no)

# P1 = Phone("Samsung","urmi07@gmail.com",8767389329,)
# # print(P1.name)
# # print(P1.get_email())         
# # print(P1.__contact_no)           # Occur the attribute error
# P1.details()

