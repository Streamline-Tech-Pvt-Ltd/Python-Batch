print("========= PVR =========")

age = int(input("Enter your Age: "))

if age > 18:
    print("Eligible to watch movie")
else:
    print("Not eligible")

print("""
Select Eligibility:
    1. adult
    2. child
""")

chec = input("Enter your Eligibility: ")

if chec == "adult":
    print("You are eligible")
else:
    print("Not Eligible")

print("""
Select your sitting plan here:
    Sitting Row 1 : 1000
    Sitting Row 2 : 500
    Sitting Last Row : 250
""")

sitting_choice = int(input("Enter Your Choice For Sitting: "))

if sitting_choice == 1:
    print("Your Row 1 Seat is Booked...")
    print("Your Ticket Is Successfully Booked.")
    print("Thank You For Booking Ticket At PVR")
elif sitting_choice == 2:
    print("Your Row 2 Seat is Booked...")
    print("Your Ticket Is Successfully Booked.")
    print("Thank You For Booking Ticket At PVR")
else:
    print("Your Row 3 Seat is Booked...")
    print("Your Ticket Is Successfully Booked.")
    print("Thank You For Booking Ticket At PVR")