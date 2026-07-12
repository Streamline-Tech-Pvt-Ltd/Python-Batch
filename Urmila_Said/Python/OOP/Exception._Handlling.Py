print("Welcome to the bank of maharashtra")
balance = 5000

while True:
   try:
      withdraw_amount = int(input("Enter the amount to withdraw:"))
      pin = int(input("Enter the Pin:"))


      if withdraw_amount <= balance:
         balance -= withdraw_amount
         print("Withdraw successful.Remaining balance",balance)
         print("Transaction Completed")
         print("Thank you for using our banking services")

      else:
         print("Insufficient balance.Your current balance is:",balance)
         print("Transaction failed")
         print("Thank you for using our banking services")

   except ValueError:
      print("Invalid input.Please enter a valid amount:")
   
  
   