# Conditional statement:in python are used to execute a block of code when a specific condition is true.

#1.if Statement: are used to execute a block of code when a if condition is true.
#syntax: 
# if (condition):
#     statement
# Ex:
x = 10
if(x > 5):
     print("x is grater than 5")


#2.else statement:are used to execute a block of code when a condition is false.
# Ex:
age = int(input("Enter a age:"))
if(age >= 18):
     print("Eligible for vote")
else:
     print("Not eligible for vote")


#3.elif Statement: It is used when you want to check multiple conditions
# Ex:
age = int(input("Enter a age:"))
if(age > 18):
     print("Eligible for voting.")
elif(age == 18 ):
      print("Also Eligible for voting.")
else:
     print("Not Eligible for voting.")

# Control Statement:Control statements are used to control the flow of execution of a program. 
# They decide which statement will execute, how many times it will execute, and when execution should stop.

# 1. break : execute code one by one
# Ex:
for i in range(1,11):
     if i == 5:
         break
     print(i)

# 2. continue: skip the current iteration and proceesed to the next iteration of the loop.
# Ex:
for i in range(1,11):
     if i == 5:
         continue
     print(i)

# 3. pass: null operation. and its useful as a placeholder for code
# Ex:
for i in range(1,11):
     if i == 2:
        pass  
    
# nested if-else statements:Nested If-Else statement means an if-else statement inside another if-else statement. 
# It is used when we need to check multiple conditions one after another.
#Ex:
age = int(input("Enter a age:"))
country = input("Enter a country:")
if(age >= 18):
     if(country == "USA" or country == "usa" ):
         print("You are eligible.")
     else:
         print("You are not eligible.")
else:
     print("You are not satisfied.")


# practice question:

#1.print a maximum of 3 number using elif statement.
num1 = int(input("Enter a first number:"))
num2 = int(input("Enter a second number:"))
num3 = int(input("Enter a third number:"))
if(num1 >= num2 and num1 >= num3):
      print("Maximum number is:", num1)
elif(num2 >= num1 and num2 >= num3 ):
       print("Maximum number is:", num2)
else:
      print("Maximum number is:", num3)

#2.check a number is even or odd.
n = int(input("Enter a number:"))
if(n % 2 == 0):
     print("Number is even")
else:
    print("Number is odd")

#3.print natural number/not.
n = int(input("Enter a number:"))
if(n > 0):
     print(" Natural Number:")
else:
     print("Not a natural number:")

#4.print sum of natural number using if-else (for and while loop)
#For Loop
n = int(input("Enter the no n:"))
if n > 0:
        sum = 0
        for i in range(1, n + 1):
             sum = sum + i
             print(sum)
else:
        print("Invalid Input")


# While Loop
n = int(input("Enter the no n:"))
if n > 0:
        sum = 0
        i = 1
        while(i <= n):
             sum = sum + i
             i = i + 1
             print(sum)
else:
       print("Invalid Input")    


#5.print a factorial number
n = int(input("Enter a number:"))
if(n >= 0):
      fact = 1
      for i in range(1,n + 1):
           fact = fact * i
      print(fact)
else:
      print("factorial Does not exit")


#6. nested if-else - 
# 1.Check Admission Eligibility
# Take percentage and entrance exam marks.
# Conditions:
# Percentage >= 60
# Entrance Marks >= 70 → Admission Granted
# Otherwise → Entrance Marks Too Low
# Percentage < 60 → Not Eligible

Percentage = float(input("Enter Your Percentage: "))
Marks = int(input("Enter Your Obtained Marks: "))
if Percentage >= 60:
      if Marks >= 70:
          print("You are eligible to take Admission")
      else:
          print("Your Entrance Marks are too low")
if Percentage < 60:
      print("Not Eligible to take addmition")


#2.Login System
# Take username and password.
# Conditions:
# Username is correct
# Password is correct → Login Successful
# Otherwise → Incorrect Password
# Otherwise → Invalid Username

username = input("Enter Your name: ")
password = int(input("Enter Password: "))
if username == "Urmila" and password == 12345:
    print("Login Successful")
elif username == "Urmila":
    print("Incorrect Password")
else:
    print("Invalid Username")
         










