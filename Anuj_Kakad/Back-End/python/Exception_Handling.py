# Exception Handling in Python

# Example 1: Handling Division by Zero
password = 1234
i = 3

for i in range(i):
    try:
        pin = int(input("Enter the password:- "))

        if pin == password:
            print("Access Granted")
        else:
            remaining = 2 - i
            if remaining > 0:
                print("Incorrect PIN!")
            else:
                print("Incorrect PIN!")
                print("Your card has been BLOCKED.")
    
    except ValueError:
        print("Invalid Password! Please enter a valid integer.")

    # else:
    #     print("Access Granted")

    finally:
        print("Transaction completed.")


# Example 2: Check age eligibility for voting

age = int(input("Enter your age: "))
if age < 18:
    raise Exception("You are not eligible to vote. You must be at least 18 years old.")
print("You are eligible to vote.")

# Using try-except block to handle the exception:-

try:
    age = int(input("Enter your age:- "))
    if age < 18:
        raise Exception("You are not eligible to vote. You must be at least 18 years old.")
    print("You are eligible to vote.")

except ValueError:
    print("Invalid input! Please enter a valid integer for age.")

finally:
    print("Thank you for using the voting eligibility checker.")


# Example 3: Login System with Exception Handling:

username = "admin"
Password = 1234

user_input = input("Enter your username:- ")
pass_input = int(input("Enter your password:- "))
if username == user_input and Password == pass_input:
    print("Login successful!")

else:
    raise  ValueError("Invalid username or password. Please try again.")

# Using try-except block to handle the exception:-

username = "admin"
Password = 1234

try:
    user_input = input("Enter your username:- ")
    pass_input = int(input("Enter your password:- "))
    if username == user_input and Password == pass_input:
        print("Login successful!")
    else:
        print("Invalid username or password. Please try again.")

except ValueError:
    print("Invalid input! Please enter a valid username and password.")

finally:
    print("Thank you for using the login system.")


# Example 4: Bank Withdrawal with Exception Handling:

balance = 10000

amount = int(input("Enter the amount to withdraw:- "))
if amount > balance and amount <= 0:
    raise ValueError("Invalid amount. Please enter a valid withdrawal amount.")
print("Withdrawal successful! Your remaining balance is:", balance - amount)

# Using try-except block to handle the exception:-

balance = 10000

try:
    amount = int(input("Enter the amount to withdraw:- "))
    if amount < balance and amount > 0:
        print("Withdrawal successful!")
    
    else:
        print("Insufficient Balance. Please enter a valid withdrawal amount.")
    
except ValueError:
    print("Invalid input! Please enter a valid integer for the withdrawal amount.")

else:
    if amount < balance and amount > 0:
        print("Your remaining balance is:", balance - amount)

finally:
    print("Thank you for using the bank withdrawal system.")