# print("Hello World")

# import keyword
# print(keyword.kwlist)
# print(len(keyword.kwlist))

# num=int(input("Enter the NUmber:"))
# if num % 2 == 0:
#     print("Even ")
# else:
#     print("Odd")

# for i in range(2,11,2):
#     print(i,end=" ")

# for i in range(1,11,2):
#     print(i,end=" ")

# num1 = int(input("Enter the Number :"))
# num2 =int(input("Enter the number :"))
# num3 =int(input("Enter the number :"))
# large = max(num1,num2,num3)
# print("largest no. is :",large)

# num =int(input("ENter the Number :"))
# fact = 1
# for i in range(1 ,num +1):
#     fact = fact * i
# print(fact)

# num = int(input("enter the Number :"))
# a = 0
# b = 1
# for i in range(1,num+1):
#     print(a ,end=" ")
#     c = a + b
#     a = b
#     b = c
#     num  = num-1

# def fabonacci(n):
#     a = 0
#     b = 1 
#     while n > 0:
#         yield a
#         c =a + b
#         a =b
#         b =c
#         n = n-1
# for i in fabonacci(5):
#     print(i)


#Reverse the string 
# text =input("Enter The text ")
# print("Reversed string is :",text[::-1])


#string is pellindrome or not
# num =input("Enter  the Number :")
# if num==num[::-1]:
#     print("Pellindrome")
# else:
#     print("Not Pellindrome")

#Whether perfect Number or Not
# num = int(input("Enter the Number :"))
# sum = 0
# for i in range(1,num):
#     if num % i ==0:
#         sum = sum+i
# if sum == num:
#     print("Number is Perfect")
# else:
#     print("Not Perfect Number") 

#revere the number 
# num =int (input("Enter The number :"))
# rev = 0
# while num>0:
#     rev = rev*10+num%10
#     num =num //10
# print(rev)

#Number is pellindeome or not
# num =int (input("Enter The number :"))
# rev=0
# temp=num
# while num >0:
#     rev = rev *10+num%10
#     num =num //10
# if temp ==rev:
#     print("pellindrome")
# else:
#     print("not pellindrome")


#Amstrong Number 
# num = int(input("Enter the Number :" ))
# temp =num
# sum = 0
# digitss = len(str(num))
# while num > 0:
#     digit = num % 10
#     sum = sum + digit**digitss
#     num = num // 10
# if sum == temp:
#     print("Number is amstrong")
# else:
#     print("Number is not amstrong")


num = int(input("Enter the Number :"))
rev =0
temp = num
while num > 0:
    rev = rev * 10 + num % 10
    num = num // 10
if temp == rev:
    print("P")
else:
    print("NP")

num  = int(input("Enter the Number :"))
if num == 0:
    print("Number is Zero")
elif num > 0:
    print("Number is Positive")
else:
    print("Number is Negative")


text = input("Enter the text :")
if text == text[::-1]:
    print("String is pellindrome")
else:
    print("Not Pellindrome")



text = input("Enter the text :")
rev = text[::-1]
print(rev)
