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
def check_even_odd(num):
    if num % 2 == 0:
     print(f"{num} is even")
    else:
     print(f"{num} is odd")

num = int(input("Enter The Number:"))
check_even_odd(num)



