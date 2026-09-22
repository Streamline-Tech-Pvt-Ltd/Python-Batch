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