# 1. print Arithematic operators using fun

def add(a,b):
    print(a+b)
add(10,20)

def sub(a,b):
    print(a - b)
sub(30,20)

def mul(a,b):
    print(a * b)
mul(30,60)

def div(a,b):
    print(a / b)
div(20,2)

# 2. print a number is natural or not using a fun

def check_natural(num):
    if num >= 1:
        print("number is natural.")
    else:
        print("number is not natural.")

number = input("Enter a no:- ")

check_natural(number)


# Example using user defined function:-

def check_number(num):
    if num % 2 == 0:
        print("No. Is Even")
    else:
        print("No. Is Odd")
    
number = int(input("Enter a number:-"))

check_number(number)

# Example using Lambda Function:-

num = number = int(input("Enter a number:-"))
res = lambda num : "Even" if num % 2 == 0 else "Odd"
print(res(num))

cities = ["Mumbai","Chennai","Delhi","Bangalore","Kerala"]
heros = ["Iron Man","Cap. America","Thor","Spidy","Hulk"]

print(cities[0:6:2])

# WAF to print length Of list:-
def print_len(list):
    print(len(list))

print_len(cities)
print_len(heros)


# WAF to Print items of list in single line:-
def print_list(list):
    for i in list:
        print(i,end=" ")

print_list(cities)
print()
print_list(heros)

# WAF to print Factorial of number:-

def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)

n = int(input("Enter a number:-"))

print(factorial(n))

# WAF to convert USD into INR:

def usd_inr(n):
    x = n * 95.96
    print(n,"USD =",x,"INR")

y = int(input("Enter a Number:- "))
usd_inr(y)