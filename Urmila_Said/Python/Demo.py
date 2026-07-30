#1.Sum Of Two Digit
# a = int(input("Enter The Number:"))
# b = int(input("Enter The Number:"))

# sum = a + b
# print("sum =", sum)

#Using FUnction
# def add(a,b):
#     return a + b
# a = int(input("Enter The Number:"))
# b = int(input("Enter The Number:"))

# a = add(a,b)
# print("Sum =",a)


#2.Even or Odd
# num = int(input("Enter The Number:"))

# if num % 2 == 0:
#     print(f"{num} is even")
# else:
#     print(f"{num} is odd")

# Using Function
# def check_even_odd(num):
#     if num % 2 == 0:
#      print(f"{num} is even")
#     else:
#      print(f"{num} is odd")

# num = int(input("Enter The Number:"))
# check_even_odd(num)

#3.Print Natural Numbers
# num = int(input("Enter The Number:"))
# for num in range(1,num+1):
#     print(num)


#4.print reverse number
# num = int(input("Enter The Number:"))
# rev = 0
# while num > 0:
#      rev = rev * 10 + num % 10
#      num = num // 10

# print("Rverse Number:",rev)

#5.Print Factorial Number
# num = int(input("Enter The Number:"))
# fact = 1
# for i in range(1,num+1):
#     fact = fact * i

# print("Factorial:",fact)

#6.Pallindrom or Not
# num = int(input("Enter The Number:"))
# temp = num
# rev = 0
# while num > 0:
#     rev = rev * 10 + num % 10
#     num = num // 10
# if temp == rev:
#     print("Palindrome Number")
# else:
#     print("Not a Palindrome Number")

#7.Print The Fibonacci Series
# num = int(input("Enter The Number:"))
# a = 1
# b = 2
# print("Fibonacci Series:")
# for i in range(num):
#     print(a, end=" ")
#     c = a + b
#     a = b
#     b = c

#8.Amstrong number or not 
# num = int(input("Enter The Number: "))
# temp = num
# sum = 0

# while num > 0:
#     digit = num % 10
#     sum = sum + digit ** 3
#     num = num // 10

# if temp == sum:
#     print("Armstrong Number")
# else:
#     print("Not an Armstrong Number")


#9.Find the GCD(gretest common divisor) of two numbers
# a = int(input("Enter First Number: "))
# b = int(input("Enter Second Number: "))

# while b != 0:
#     a, b = b, a % b

# print("GCD =", a)

#Using for loop find the gcd of two numbers
# a = int(input("Enter First Number: "))
# b = int(input("Enter Second Number: "))
# gcd = 1
# for i in range(1, min(a, b) + 1):
#     if a % i == 0 and b % i == 0:
#         gcd = i

# print("GCD =", gcd)


#10.Find the LCM(Least common multiple) of two numbers.
# a = int(input("Enter First Number: "))
# b = int(input("Enter Second Number: "))

# max_num = max(a, b)

# while True:
#     if max_num % a == 0 and max_num % b == 0:
#         print("LCM =", max_num)
#         break
#     max_num += 1


#11.Print all prime number from 1 to n.
n = int(input("Enter The Number: "))

print("Prime Numbers is:")

for num in range(2, n + 1):
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(num, end=" ")




