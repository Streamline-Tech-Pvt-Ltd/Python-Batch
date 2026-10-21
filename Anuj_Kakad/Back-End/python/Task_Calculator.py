# creating calculator using input function:-

input1 = eval(input("Enter First Number:-"))
input2 = eval(input("Enter Second Number:-"))

print()
print(type(input1))
print(type(input2))

print()
print(id(input1))
print(id(input2))

print()
print("The Result of Addition is:-", input1 + input2)
print("The Result of Subtraction is:-", input1 - input2)
print("The Result of Multiplication is:-", input1 * input2)
print("The Result of Division is:-", input1 / input2)
