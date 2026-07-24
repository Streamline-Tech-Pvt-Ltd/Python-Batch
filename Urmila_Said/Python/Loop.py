#Loop: Loop is used to repeat a block of code until this given condition is true.

# for loop : for loops iterate over a sequence of items.(list,tuple)
# syntax: for i in range():
        #    statement

# while loop : while loop is used to execute a block of statements while a condition is true.

#odd numbers using for loop
for i in range(1,12,2):
     print(a, end = " ")

fact = 1
for i in range(5):
     fact = fact * (i+1)
print(fact)

print a table using for loop
for i in range(2,21,2):
     print(i)


print odd number using while loop
i = 1
while(i <= 10):
     print(i)
     i = i + 2

#practice questions:

# 1. Write a Python program to find the sum of the first n natural numbers using a for loop and while loop.
# For Loop
n = int(input("Enter the no n:"))
sum = 0
for i in range(1, n + 1):
      sum = sum + i
 print(sum)

# While Loop
n = int(input("Enter the no n:"))
i = 0
sum = 0
while(i <= n):
     sum = sum + i
     i = i + 1
 print(sum)    


# 2. Write a Python program to take a number from the user and find its factorial using a for loop and while loop.
# For Loop
n = int(input("Enter the no n:"))
fact = 1
for i in range(n):
      fact = fact * (i+1)
 print(fact)

# While Loop
n = int(input("Enter the no n:"))
fact = 1
i = 1
while(i <= n):
      fact = fact * i
      i = i + 1
 print(fact)    

# 3. Take a number from the user and print its multiplication table up to 10.
# For Loop
n = int(input("Enter the no n:"))
for i in range(1,11):
      print(n * i)

# While Loop
n = int(input("Enter the no n:"))
i = 1
while(i <= 10):
     print(n * i)
    i += 1


# 4. Take a number n and print squares of numbers from 1 to n.
# For Loop
n = int(input("Enter the no n:"))
for i in range(1,n + 1):
       square = i * i
print(square)

# While Loop
n = int(input("Enter the no n:"))
i = 1
while( i <= n):
       square = i * i
       i = i + 1
print(square)      


# 6. Take a number n from the user and print the first n terms of the Fibonacci series using a while loop.
# For Loop
n = int(input("Enter the no n:"))
a = 0
b = 1
for i in range(n):
     print(a)
     c = a + b
     a = b
     b = c


# While Loop
n = int(input("Enter the no n:"))
a = 0
b = 1
count = 0
while count < n:
     print(a)
     c = a + b
     a = b
     b = c
     count += 1

    
# 7. Take a number from the user and check whether it is a palindrome or not.
# While Loop
num = int(input("Enter a number:"))
temp = num
reverse = 0
while (temp > 0):
      remainder = temp % 10
      reverse = (reverse * 10) + remainder
      temp = temp // 10

if (num == reverse):
      print("Palindrome Number")
else:
      print("Not Palindrome number")
    

# 8. Write a program to take a user input and find a odd and even number using for and while loop
# For Loop
 n = int(input("Enter the no n:"))
for i in range(1):
         if n % 2 == 0:
                 print("Even Number:")
         else:
                 print("Odd Number:")

# While Loop
n = int(input("Enter the no n:"))
while True:
         if n % 2 == 0:
                 print("Even Number:")
         else:
                 print("Odd Number:")
         break



