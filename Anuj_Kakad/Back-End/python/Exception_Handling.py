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