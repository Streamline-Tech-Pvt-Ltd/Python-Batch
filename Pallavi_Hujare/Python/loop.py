# Loop: Loop is used to repeat a block of code until this given condition is true.

# for loop : for loops iterate over a sequence of items.(list,tuple)
# syntax: for i in range():
        #    statement
#Example
# fact = 1
# for i in range(5):
#     fact= fact*(i+1)
# print(fact)   #120



# while loop : while loop is used to execute a block of statements while a condition is true.
# i = 0
# while(i <= 10):
#     print(i)
#     i = i + 1


#even
# i = 0
# while(i<=10):
#     print(i)
#     i=i+2


#odd
# i = 1
# while(i<=10):
#     print(i)
#     i=i+2

#practice questions:
# 1. Write a Python program to find the sum of the first n natural numbers using a for loop and while loop.

#To print the first n natural numbers:

# num = 5
# for i in range(1, num + 1):
#     print(i)


#sum of the first n natural numbers
#for loop
# num =int(input("Enter The number : "))
# sum = 0
# for i in range(1 , num+1):
#     sum = sum+i
# print(sum)

#while loop
# num =int(input("Enter The number : "))
# sum = 0
# i = 0
# while i <= num:
#     sum = sum+i
#     i = i+1
# print(sum)


# 2. Write a Python program to take a number from the user and find its factorial using a for loop and while loop.
#for
# num =int(input("Enter Factorial No:"))
# fact = 1
# for num in range(num):
#      fact= fact*(num+1)
# print(fact)


#while 
# num =int(input("Enter the Number :"))
# fact = 1
# i = 1
# while i <= num:
#     fact = fact*i
#     i = i +1
# print(fact)


# 3. Take a number from the user and print its multiplication table up to 10.
#for
# num =int(input("Enter the Number :"))
# for i in range(1,11):
#      print(num*i)

#While
# num = int(input("Enter a number: "))
# i = 1
# while i <= 10:
#     print(num * i)
#     i += 1




# 4. Take a number n and print squares of numbers from 1 to n.
#for
# n = int(input("Enter a number: "))
# for i in range(1, n + 1):
#      print(i, ":", i * i)

#While
# n = int(input("Enter a number: "))
# i = 1
# while i <= n:
#     print(i, ":", i * i)
#     i += 1


# 5. Take a number n from the user and print the first n terms of the Fibonacci series using a while loop.
#For
# num= int(input("Enter the number of terms: "))
# a = 0
# b = 1
# for i in range(num):
#     print(a, end=" ")
#     c = a + b
#     a = b
#     b = c

#While
# num = int(input("Enter the number of terms: "))
# a = 0
# b = 1
# i = 1
# while i <= num:
#     print(a, end=" ")
#     c = a + b
#     a = b
#     b = c
#     i += 1

# 6. Take a number from the user and check whether it is a palindrome or not.
#For
# num = int(input("Enter a number: "))
# temp = num
# rev = 0
# for i in str(num):
#     digit = num % 10
#     rev = rev * 10 + digit
#     num = num // 10
# if temp == rev:
#     print("Palindrome Number")
# else:
#     print("Not a Palindrome Number")

#While

# num = int(input("Enter a number:"))
# temp = num
# reverse = 0
# while (temp > 0):
#     remainder = temp % 10
#     reverse = (reverse * 10) + remainder
#     temp = temp // 10
# if (num == reverse):
#     print("Palindrome Number")
# else:
#     print("Not Palindrome number")


# 7. Write a program to take a user input and find a odd and even number using for and while loop.

# for
# num = int(input("Enter a number: "))
# for i in range(1, num + 1):
#     if i % 2 == 0:
#         print("Number is Even")
#     else:
#         print("Number is Odd")


# while
# num = int(input("Enter a number: "))
# i = 1
# while i <= num:
#     if i % 2 == 0:
#         print(i, "Even")
#     else:
#         print(i, "Odd")
#     i += 1


# 1 TO 100
# i = 1
# while i<=100:
#     print(i ,end=" ")
#     i+=1        


#print 1 to 100 in reverse
# i = 100
# while i>=1:
#     print(i , end=" ")
#     i-=1

#Print List 
# num = [1,4,9,16,25,36,49,64,81,100]
# i = 0
# while i < len(num):
#      print(num[i])
#      i +=1
    
