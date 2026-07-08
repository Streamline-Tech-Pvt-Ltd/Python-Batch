a = 100
b = 200
print(a.__add__(b))
print(a+b)

# a = 100
# b = 200
# print(a.__gt__(b))

# class Book:
#     def __init__(self,name,pages):
#         self.name = name
#         self.pages = pages
#     def __add__(self,other):
#         return self.pages + other.pages
# b1 = Book("AH",200)
# b2 = Book("GZ",200)
# total = b1.pages + b2.pages
# print(total)
# print(b1+b2)

# class Addition:
#     def __init__(self,n1):
#         print("First constructor")
#         self.n1 = n1
#     def __init__(self,n1,name):
#         print("2nd constructor")
#         self.n1 = n1
#         self.name = name
#     def __init__(self,n1,name,city):
#         print("3rd constructor")
#         self.n1 = n1
#         self.name = name
#         self.city = city
# a1 = Addition(1,"Pallavi","Nashik")

# print(a1)


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


# types: 
# 1. overloading :-   does not support in python.
        # 1. Method overloading
# 2. Overriding :- Supoort in python 
        # 1. method overriding
        # 2. variable overriding