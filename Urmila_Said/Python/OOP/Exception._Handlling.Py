 # Exception Handling: Exception Handling is the process of detecting, handling, and recovering 
 # from runtime errors using the try, except, else, and finally blocks.

# 1.try
# The try block contains code that may generate an exception.

# 2.except
# The except block handles the exception

# 3.else
# The else block executes only if no exception occurs.

# 4.finally
# The finally block always executes whether an exception occurs or not.

# Exception Type:
# Exception	                  Meaning

# ZeroDivisionError	       Dividing by zero
# ValueError	              Invalid value
# TypeError	             Wrong data type
# NameError	            Variable not defined
# IndexError	            List index out of range
# KeyError	               Dictionary key not found
# AttributeError	          Attribute or method not found
# ImportError	             Error while importing a module
# FileNotFoundError	        File does not exist
# ModuleNotFoundError	      Module not found
# OverflowError	           Number too large
# MemoryError	             Not enough memory



# print("Welcome to the bank of maharashtra")
# balance = 5000

# while True:
#    try:
#       withdraw_amount = int(input("Enter the amount to withdraw:"))
#       pin = int(input("Enter the Pin:"))


#       if withdraw_amount <= balance:
#          balance -= withdraw_amount
#          print("Withdraw successful.Remaining balance",balance)
#          print("Transaction Completed")
#          print("Thank you for using our banking services")

#       else:
#          print("Insufficient balance.Your current balance is:",balance)
#          print("Transaction failed")
#          print("Thank you for using our banking services")

#    except ValueError:
#       print("Invalid input.Please enter a valid amount:")
   

#Ex:

# 1.ZeroDivisionError
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
   
   