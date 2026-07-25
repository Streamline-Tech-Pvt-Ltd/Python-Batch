print("=" * 130)
print("  "* 25, "Welcome To Streamline Tech Portal")
print("=" * 130)

def add_intern():
    print("\n======================================= Add Intern ===========================================")
    intern_id =int(input("Enter Intern ID :"))
    name = input("Enter Intern Name :")
    reg_date = input("Enter Registration Date :")
    domain = input("Enter Domain Name :")
    reg_fee = int(input("Enter Registration Fee :"))
    college_name = input("Enter College Name :")
    city = input("Enter City :")    

    with open("Intern.txt","a") as file:
        file.write(f"Intern Id :{intern_id}\n")
        file.write(f"Intern Name :{name}\n")
        file.write(f"Registration Date  :{reg_date}\n")
        file.write(f"Domain Name :{domain}\n")
        file.write(f"Registration Fee :{reg_fee}\n")
        file.write(f"College Name :{college_name}\n")
        file.write(f"City Name  :{city}\n")
        file.write("-" * 80 + "\n")

    print("\n Your Admission Successfully Done!")
    print("\n" + "=" * 130)


def view_intern():
    print("\n====================================== View Intern ===========================================")
    try:
        with open("Intern.txt","r") as file:
            data = file.read()

            if data.strip() =="":
                print("Intern Record Not Found") 
            else:
                print(data)

    except FileNotFoundError:
        print("Intern.txt File Does Not Exist")


def update_intern():
    print("\n====================================== Update Intern ===========================================")

    search_id = input("Enter Intern Id : ")

    try:
        with open("Intern.txt","r") as file:
            data = file.read()
        details = data.split("-" * 80 + "\n")

        updated_details = []
        found = False

        for detail in details:
            if detail.strip() == "":
                continue

            for line in detail.splitlines():
                if line.startswith("Intern Id"):
                    intern_value = line.split(":")[-1].strip()
                    if intern_value == search_id:
                        print("\nIntern Detail Found!")
                        print(detail)

                        print("\n Enter New Updated Details")
                        intern_id = int(input("Enter Intern ID : "))
                        name = input("Enter Intern Name : ")
                        reg_date = input("Enter Registration Date : ")
                        domain = input("Enter Domain Name : ")
                        reg_fee = int(input("Enter Registration Fee : "))
                        college_name = input("Enter College Name : ")
                        city = input("Enter City : ")    

                        new_detail = (
                            f"Intern Id :{intern_id}\n"
                            f"Intern Name :{name}\n"
                            f"Registration Date :{reg_date}\n"
                            f"Domain Name :{domain}\n"
                            f"Registration Fee :{reg_fee}\n"
                            f"College Name :{college_name}\n"
                            f"City Name :{city}\n"
                        )
                        updated_details.append(new_detail)
                        found = True
                        break
            else:
                updated_details.append(detail)

        if found:
            with open("Intern.txt", "w") as file:
                for rec in updated_details:
                    file.write(rec.strip() + "\n")
                    file.write("-" * 80 + "\n")
            print("\nIntern Record Updated Successfully!")
        else:
            print("\nIntern ID Not Found!")

    except FileNotFoundError:
        print("Intern.txt File Does Not Exist.")


def delete_intern():
    print("\n====================================== Delete Intern ===========================================")

    search_id = input("Enter Intern ID : ")

    try:
        with open("Intern.txt", "r") as file:
            f1 = file.read()

        details = f1.split("-" * 80 + "\n")

        updated_details = []
        found = False

        for detail in details:
            if detail.strip() == "":
                continue

            for line in detail.splitlines():
                if line.startswith("Intern Id"):
                    intern_value = line.split(":")[-1].strip()
                    if intern_value == search_id:
                        found = True
                        break

            if found:
                continue 

            updated_details.append(detail)

        with open("Intern.txt", "w") as file:
            for detail in updated_details:
                file.write(detail.strip() + "\n")
                file.write("-" * 80 + "\n")

        if found:
            print("\nIntern Deleted Successfully.")
        else:
            print("\nIntern Record Not Found.")

    except FileNotFoundError:
        print("\nIntern.txt File Does Not Exist")


def search_intern():
    print("\n====================================== Search Intern ===========================================")
    search_id = input("Enter Intern ID : ")

    try:
        with open("Intern.txt", "r") as file:
            data = file.read()

        details = data.split("-" * 80 + "\n")
        found = False

        for detail in details:
            if detail.strip() == "":
                continue

            for line in detail.splitlines():
                if line.startswith("Intern Id"):
                    intern_value = line.split(":")[-1].strip()
                    if intern_value == search_id:
                        print("\nIntern Found Successfully")
                        print("-" * 80)
                        print(detail)
                        found = True
                        break

        if not found:
            print("\nIntern Record Not Found.")

    except FileNotFoundError:
        print("\nIntern.txt File Does Not Exist.")


while True:
    print("1.Add Intern")
    print("2.View Intern")
    print("3.Update Intern")
    print("4.Delete Intern")
    print("5.Search Intern")
    print("6.Exit")

    try:
        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            add_intern()

        elif choice == 2:
            view_intern()

        elif choice == 3:
            update_intern()

        elif choice == 4:
            delete_intern()

        elif choice == 5:
            search_intern()

        elif choice == 6:
            print("Thank You For Visiting Streamline Tech")
            break
        else:
            print("Invalid Choice! Please Try Again.")

    except ValueError:
        print("Please enter a valid choice")

print("=" * 130)



