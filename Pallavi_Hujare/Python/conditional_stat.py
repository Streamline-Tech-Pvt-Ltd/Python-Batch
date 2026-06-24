
# Conditional Statements : in python are used to execute a block of code when a specific condition is true.

# 1. if statement: are used to execute a block of code when a if condition is true.
# syntax: 
# if (condition):
#     statement

# 2. else statements: are used to execute a block of code when a condition is false.
# x = 10
# if(x > 5):
#     print("x is grater than 5")


# age = int(input("Enter a age:"))
# if(age >= 18):
#     print("Eligible for vote")
# else:
#     print("Not eligible for vote")


# 3.elif statement: 
# age = int(input("Enter a age:"))
# if(age > 18):
#     print("Eligible for voting.")
# elif(age == 18 ):
#      print("Also Eligible for voting.")
# else:
#     print("Not Eligible for voting.")

# Control Statement:
# 1. break : execute code one by one
# 2. continue: skip thecurrent iteration and proceesed to the next iteration of the loop.
# 3. pass: null operation. and its useful as a placeholder for code


# for i in range(1,11):
#     if i == 5:
#         break
#     print(i)

# for i in range(1,11):
#     if i == 5:
#         continue
#     print(i)

# for i in range(1,11):
#     if i == 2:
#         pass  
    
# nested if-else statements:

# age = int(input("Enter a age:"))
# country = input("Enter a country:")
# if(age >= 18):
#     if(country == "USA" or country == "usa" ):
#         print("You are eligible.")
#     else:
#         print("You are not eligible.")
# else:
#     print("You are not satisfied.")

# practice question:
#1.print a maximum of 3 number using elif statement.
# num1 = int(input("Enter 1st Number : "))
# num2 =int (input("Enter 2nd  Number :"))
# num3 =int (input("Enter 3nd  Number :"))
# if (num1 >= num2 and num1 >= num3):
#     print("Maximum Number" ,num1)
# elif (num2 >= num1 and num2 >= num3):
#     print("Maximum Number" ,num2)
# else:
#     print("Maximum Number" ,num3)


#2.check a number is even or odd.
# n = int(input("Enter The Number :"))
# if n % 2 ==0:
#     print("Number is even")
# else:
#     print("Number is odd")

#3.print natural number/not.
# n = int(input("Enter The Number :"))
# if n >=1:
#     print("Number is natural")
# else:
#     print("Number is Not Natural")

#4.print sum of natural number using if-else (for and while loop)
# num=int(input("Enter The Number:"))
# if num >0:
#     sum = 0
#     for i in range(1,num+1):
#         sum = sum + i
#     print("Sum is : ",sum)
# else:
#     print("Please Enter Positive Number:")

#5.print a factorial number
# num = int(input("Enter a number: "))
# if num < 0:
#     print("Factorial does not exist for negative numbers")
# else:
#     fact = 1
#     for i in range(1, num + 1):
#         fact = fact * i
#     print("Factorial is : =", fact)


#6. nested if-else - 
# 1.Check Admission Eligibility
# Take percentage and entrance exam marks.
# Conditions:
# Percentage >= 60
# Entrance Marks >= 70 → Admission Granted
# Otherwise → Entrance Marks Too Low
# Percentage < 60 → Not Eligible

# Percentage = float(input("Enter Your Percentage: "))
# Marks = int(input("Enter Your Obtained Marks: "))
# if Percentage >= 60:
#     if Marks >= 70:
#         print("You are eligible to take Admission")
#     else:
#         print("Your Entrance Marks are too low")
# if Percentage < 60:
#     print("Not Eligible to take addmition")



#2.Login System
# Take username and password.
# Conditions:
# Username is correct
# Password is correct → Login Successful
# Otherwise → Incorrect Password
# Otherwise → Invalid Username

username = input("Enter Your name: ")
password = int(input("Enter Password: "))
if username == "Pallavi" and password == 123456:
    print("Login Successful")
elif username == "Pallavi":
    print("Incorrect Password")
else:
    print("Invalid Username")
         

