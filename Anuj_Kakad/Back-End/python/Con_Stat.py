# 1. Theater Ticket Booking System:-

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


# 2. Wheather Check:-

temp = int(input("Enter the temperature: "))

if temp >= 35:
    print("It's very hot")
elif temp >= 25:
    print("The weather is warm")
elif temp >= 15:
    print("The weather is cool")
else:
    print("It's cold")


# 3. Program for checking addmision eligibility of a student based on their marks:-

take percentage and entrance marks:-
conditions:-
percentage >= 60 & entrance marks >= 70 :- Addmission is granted
otherwise :- Marks are not sufficient for addmission
percentage < 60 :- not eligible for addmission

per = float(input("Enter your percentage:- "))
entrance_marks = float(input("Enter your entrance marks:-"))


if per >= 60 and entrance_marks >= 70:
    print("Addmisson is granted")
elif per >= 60 and entrance_marks <= 70:
    print("Marks are not sufficient for addmission")
else:
    print("Not eligible for addmission")

