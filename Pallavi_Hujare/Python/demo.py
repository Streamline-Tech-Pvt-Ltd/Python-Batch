# print("Hello World!")

# name =input("Enter Your name:")
# print("Hello",name)


# a=int(input("Enter The First Number:"))
# b=int(input("Enter The Secound Number:"))
# print("Sum is:",a+b)


# num = int(input("Enter The Number:"))
# if num % 2 == 0 :
#     print(f"{num} is even")
# else :
#     print(f"{num} is odd ")


# a=int(input("Enter The First Number:"))
# b=int(input("Enter The Secound Number:"))
# if a>b :
#     print("a is largest Number")
# else:
#     print("b is largest Number")


# name =input("Enter Your Name:")
# age =int(input("Enter Your age:"))
# city =input("Enter your city")

# print(f"My Name is:{name},\nMy age is:{age},\nMy city is:{city}")


#num = int(input("Enter the number : "))
# fact = 1
# for i in range(1,num+1):
#     fact = fact * i
# print(fact)


# num = int(input("Enter the number of terms: "))
# a = 0
# b = 1
# for i in range(num):
#     print(a, end=" ")
#     c = a + b
#     a = b
#     b = c

def add_details():
    ID =int(input("Enter Your ID:\n"))
    Name = input("Enter Your Name :\n")

    with open("sample.txt","a") as file:
        file.write(f"Id : {ID}\n")
        file.write(f"Name : {Name}\n")

def view():
     try:
        with open("sample.txt","r") as file:
            f1 = file.read()
            if f1:
                print(f1)
            else:
                print("file Record is not found")
     except FileNotFoundError:
        print("File dose not Exsit")

def update():
    try:
        old = input("Enter old value :")
        new = input("Enter Your new value :")
        with open("sample.txt","r") as file:
            f1 = file.read()
            if old in f1:
                f1 =f1.replace(old,new) 
                with open("sample.txt","w") as file:
                    file.write(f1)

                with open("sample.txt","r") as file:
                    print(file.read())
            else:
                print("Value is not found")
    except ValueError:
        print("Value Error")


while True:
    print("1:Add intern")
    print("2.viwe intern")
    print("3:Update")
    choise =int(input("Enter Your Choise:\n"))
    if choise == 1:
        add_details()
    elif choise ==2:
         view()
    elif choise ==3:
        update()
    else:
        print("Thank You")
