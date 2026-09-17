# #Sum of first n natural numbers using for loop
n = int(input("Enter a number: "))

sum = 0

for i in range(1, n + 1):
    sum = sum + i

print("Sum =", sum)





# # Factorial of a number
n = int(input("Enter a number: "))

fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Factorial =", fact)




# #Multiplication table up to 10
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)