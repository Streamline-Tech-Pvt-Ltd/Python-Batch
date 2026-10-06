# Inheritance:

        # one clsaa properties inherits of another class
        # Means parent clsaa properties inherits into  child class



#  child class === BASE class
# parent class === Derived class


# typs:

#1.  single Inheritance:
            #  only create child class object ,parent class is automatically access


# class Parent:
#     name = "rahul"
#     def property(self):
#         return "parent property"
        
# class Child(Parent):
#     def education(self):
#         return "education pursuing "
        
# obj2 = Child()
# print(obj2.education())
# print(obj2.property())
# print(obj2.name)



#2. Multiple Inheritance :- 

# class Father:
#     name = "rahul"
#     def property(self):
#         return "Father property"
        
# class Mother:
#     def property1(self):
#         return "mother property "
    
# class Child(Mother,Father):
#     def education(self):
#         return "education pursuing "
    
# obj = Child()
# print(obj.property())
# print(obj.property1())
# print(obj.education())



#3.  multilevel Inheritance :- 

# class GrandFather:
#     name = "rahul"
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


#4.  hierarchical Inheritance :- 

# class Father:
#     name = "rahul"
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


# 5. hybrid Inheritance:-

# class Family:
#     def member(self):
#         return " family member"
    
# class Father(Family):
#     def dad(self):
#         return "DAD"
    
    
# class Son1(Father):
#     def boy1(self):
#         return " BOY 1"
    
# class Son2(Father,Family):
#     def boy2(self):
#         return "BOY 2"
    
# obj = Son2()
# print(obj.boy2())

# obj1 = Son1()
# print(obj1.boy1())
# print(obj1.dad())
# print(obj1.member())

