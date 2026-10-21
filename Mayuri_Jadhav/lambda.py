## arithmetic operation using function
# def add(a,b):
#     print("Addition of:",a+b)
#     print ("subtraction of:",a-b)
#     print("Multiplication of:",a*b)
#     print("Division of :",a/b)
#     a=int(input("enter a number:"))
#     b=int(input("enter a number:"))
#     add(a,b)

#     # even add number
#     def even(a,b):
#        if a%2==0:
#          print("even number is :",a)
#        else:
#          print("odd number is :",a)
#          even(a,b):


         # even odd number
# def check_number(num):
#     if num%2==0:
#         print("even number is :",num)
#     else:
#         print("odd numb er is :",num)
# num=int(input("enter a number:"))
# check_number(num)
 

#lambda function genral syntax
# add=lambda a,b:a+b
# print("Addition of:",add (10,20))

## lambda funcction for addition of two numbers
# a=int(input("enter a number:"))
# b=int(input("enter a number:"))
# num=lambda a,b:a+b
# print(num(a,b))


#lambda function for even odd number

# num=int(input("enter a number:"))
# res=lambda num:"even"if num%2==0 else "odd"
# print(res(num))


#postive and negative number using lambda function
# num=int(input("enter a number:"))
# res=lambda num:"postive number"if num>0 else "negative number"
# print(res(num))

## lambda function for maximum number
# a=int(input("enter a number:"))
# b=int(input("enter a number:"))
# maximum=lambda a,b:a if a>b else b
# print("Maximum number is:",maximum(a,b))

##lambda function for age check
# age=int(input("enter a age:"))
# res=lambda age:"eligible for vote" if age>=18 else "not eligible for vote"
# print(res(age))


##labda functuion for pass or fail
# marks=int(input("enter a marks:"))
# student=lambda marks:"pass"if marks>=35 else "fail"
# print(student(marks))

## lambdafunction for area of circle
# radius=int(input("enter a radius:"))
# area=lambda radius:3.14*radius*radius
# print("area of circle is :",area(radius))

# lambda function for area of reactangle
# length=int(input("enter a length:"))
# breadth=int(input("enter a breadth:"))
# area=lambda length,breadth:length*breadth
# print("area of reactangle is :",area(length,breadth))

#lambda function for area of square
# side=int(input("enter a side:"))
# area=lambda side:side*side
# print("area of square is :",area(side))

#lambda function for triangle
# base=int(input("enter abase:"))
# height=int(input("enter a height:"))
# area=lambda base,height:0.5*base*height
# print("area of triangle is:",area(base,height))


