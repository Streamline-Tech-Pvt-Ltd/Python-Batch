# print("Hello World")

# #Sum of Two Numbers
# a = 10
# b = 20
# sum = a + b
# print("Sum is :",sum)

# #Print of even and odd
# num = int(input("Enter the Number :"))
# if num % 2 ==0:
#     print("Even Number ")
# else:
#     print("Odd Number ")

# #Print Even Number
# for i in range(2,11,2):
#     print(i, end= " ")
# 2
# #print odd Number 
# for i in range(1,11,2):
#     print(i, end=" ")

# #Print Natural Numbers
# num = int(input("Enter the Number :"))
# for num in range(1 ,num+1):
#     print(num)

# #print factorial Number 
# num = int(input("Enter the Number :"))
# fact = 1
# for i in range(1,num+1):
#     fact = fact * i
# print(fact)

# #Print Reverse Number
# num =int(input("Enter Number :"))
# rev = 0
# while num > 0:
#     rev = rev * 10 + num % 10
#     num = num // 10
# print(rev)

# #print pellindrom is not
# num =int(input("Enter Number :"))
# temp = num
# rev = 0
# while num> 0:
#     rev = rev * 10 + num % 10
#     num = num // 10
# if temp == rev:
#     print("Pellindrome")
# else:
#     print("Not Pellindrome")

# #Fibonacci series
# num =int(input("Enter Number :"))
# a = 0
# b = 1
# while num >0:
#     print(a, end=" ")
#     c = a + b
#     a = b
#     b = c
#     num = num - 1


# #Amstrong number or not 
# num = int(input("Enter Number: "))
# temp = num
# count = 0
# sum = 0
# while temp > 0:
#     count += 1
#     temp = temp // 10
# temp = num
# while temp > 0:
#     sum = sum + temp % 10 ** count
#     temp = temp // 10
# if sum == num:git 
#     print("Armstrong Number")
# else:
#     print("Not Armstrong Number")




# num = int(input("Enter The Number :"))
# temp = num
# sum = 0
# count  = 0
# while temp > 0:
#     count = count + 1
#     temp = temp // 10
# temp = num
# while temp > 0:
#     sum = sum + temp % 10 ** count
#     temp = temp // 10
# if sum == num:
#     print("Amstrong Number ")
# else:
#     print("Not amstrong Number ")





# num = int(input("Enter the number :"))
# fact = 1
# for i in range (1,num+1):
#     fact = fact*i
# print(fact)




num = int(input("Enter the Number :"))
rev = 0
temp = num
while num > 0:
    rev = rev*10+num%10
    num = num // 10
if temp == rev:
    print("Pellindrome") 
else:
    print("Not Pellindrome")


num =int(input("Enter the Number :"))
temp = num
sum = 0
count = 0
while num > 0:
    count = count + 1
    temp = temp //10
temp = num
while num > 0:
    sum = sum  + temp % 10 **count
    temp  = temp // 10
if temp == num :
    print("Amstrong Number")
else:
    print("Not Amstrong Number :")













