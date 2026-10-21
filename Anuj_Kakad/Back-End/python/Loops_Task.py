# 5. program to print a factorial number:-

# take a no from user
# conditions:-
# calculate the factorial
# provide the output

print("Provide a no to calculate factorial:-")

num = int(input("Enter a Number:-"))
fact = 1

for i in range(1, num + 1):
    fact = fact * i

print("Factorial of",num,"is:-",fact)