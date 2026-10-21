print("Provide A Number To Calculate The Factorial Below:-")
# 1. Factorial Of Number:-

def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)

a = int(input("Enter a Number:-"))

print(factorial(a))

print()
print("Provide A Number To Print in Ascending Order Below:- ")
# 2. Print No From 1 to 5:-

def count(n):
    if n > a:
        return 0
    
    print(n, end = " ")
    count(n+1)

a = int(input("Enter a number to print Ascending Order:- "))
count(1)

print()
print("Provide A Number To Print in Descending Order Below:- ")
# 3. Print no from 5 to 1:-

def count1(num):
    if num == 0:
        return
    print(num, end = " ")
    count1(num-1)

a= int(input("Enter A number To print Descending Order:-"))

count1(a)

print()
print("Provide A Number to Calculate Sum Of Natural Numbers Below:- ")
# 4. Print Sum of Natural Numbers:-

def sum_natural(n):
    if n == 0:
        return 0
    else:
        return n + sum_natural(n-1)    

a = int(input("Enter a Natural No to Calculate Sum:-"))
print(sum_natural(a))

print()
print("Provide A Number To Print Fibonacci Series Below:- ")
# 5. Print Fibonacci Series of given No.:-

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

a = int(input("Enter number of terms:- "))

for i in range(a):
    print(fibonacci(i), end= " ")