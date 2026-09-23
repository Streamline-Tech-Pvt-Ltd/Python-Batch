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