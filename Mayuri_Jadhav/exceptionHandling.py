#Program to check ATM PIN with exception handling using for loop try,except ,else,finally


pin = 1234
i=0
for i in range(3):
    try:
        user_Pin = int(input("enter your pin:"))
        if user_Pin == pin:
            print("PIN is correct!")
            break
    except ValueError:
        print("Invalid input. Please enter a numeric pin.")
    else:
        print("Incorrect PIN. Please try again.")
    finally:
        print("Attempt completed.")

#Practice Question: 
# 1. Write a program that takes age as input.If age is less than 18, raise a ValueError.Otherwise print "You are eligible."Handle the exception using try-except.
try:
    age = int(input("Enter your age: ")) 
    if age<18:
        raise ValueError("age is less than 18")
    print("you are eligible")
except ValueError as e:
    print(e)


# 2.Login System
# Create a simple login system.
# Username: admin
# Password: 1234

# conditions:
# - Correct username and password → "Login successful"
# - Wrong credentials → raise ValueError
# - Handle the exception using try-except.
# - Use finally to print "Login process completed".

try:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == "admin" and password == "1234":
        print("Login successful")
    else:
        raise ValueError("Incorrect credentials")
except ValueError as e:
    print(e)
finally:
    print("Login process completed")

# 3.Bank Withdrawal 
# Write a program that:
# Balance = 10000

# Take withdrawal amount from the user.
# Conditions:
# - Amount must be a number.
# - Amount must be greater than 0.
# - Amount should not be greater than balance.
# - If balance is insufficient, raise ValueError.
# - Handle all exceptions.
# - Use else and finally.
 
balance =10000
try:
    withdrawal_amount=int(input("Enter withdrawal amount:"))
    if withdrawal_amount<=0:
        raise ValueError("Amount must be greater than 0.")
    elif withdrawal_amount > balance:
        raise ValueError("Insufficient balance.")
except ValueError as e:
    print(e)
finally:
    print("Transaction completed.")
