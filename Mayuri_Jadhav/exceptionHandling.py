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