# with open("student.txt","x") as file:
print("=" * 120)
print(" " * 30, "Welcome to the Streamline Tech Portal")
print("=" * 120)

def add_details():
    Id = int(input("Enter Your ID :  \n"))
    Name = input("Enter Your Name: \n ")
    Domain_name = input("Enter Your Domain Name :\n")
    Registration_fee = int(input("Enter Your Registration Fee:\n"))
    College_name = input("Enter Your College Name :\n")
    City = input("Enter Your Current City: \n")
    
    with open("student.txt", "a") as file:

        file.write(f"Intern ID : {Id}\n")
        file.write(f"Name : {Name}\n")
        file.write(f"Domain Name : {Domain_name}\n")
        file.write(f"Registration Fee : {Registration_fee}\n")
        file.write(f"College Name : {College_name}\n")
        file.write(f"City : {City}\n")
        file.write("=" * 120 + "\n")

    print("Data Saved Successfully!")


def view_details():
    try:
        with open("student.txt", "r") as file:
            f1 = file.read()
            if f1:
                print("\nStudent Details\n")
                print(f1)
            else:
                print("No Records Found.")
    except FileNotFoundError:
        print("student.txt file not found.")


def update_intern_data():
    try:
        old_name = input("Enter Replacable Data: ")
        new_name = input("Enter new Data: ")
        print("=" * 120)
        with open("student.txt", "r") as file:
            f1 = file.read()
        if old_name in f1:
            f1 = f1.replace(old_name, new_name)
            with open("student.txt", "w") as file:
                file.write(f1)
            print("\nData Updated Successfully!\n")
            with open("student.txt", "r") as file:
                print(file.read())
        else:
            print("Record not found.")
    except FileNotFoundError:
        print("student.txt file not found.")


def search_intern():
    search_id = input("Enter Searching ID: ")
    print("=" * 120)
    with open("student.txt", "r") as file:
        search = False
        for line in file:
            if line.strip() == f"Intern ID : {search_id}":
                search = True
                print(line.strip())          
                print(next(file).strip())    
                print(next(file).strip())    
                print(next(file).strip())    
                print(next(file).strip())    
                print(next(file).strip())    
                break
        if not search:
                print("Record Not Found")


       
def delete_intern():
    delete_id = input("Enter ID to Delete: ")
    print("=" * 120)
    with open("student.txt", "r") as file:
        line = file.readlines()
    new_lines = []
    i = 0
    while i < len(line):
        if line[i].strip() == f"Intern ID : {delete_id}":
            i += 7      
        else:
            new_lines.append(line[i])
            i += 1
    with open("student.txt", "w") as file:
        file.writelines(new_lines)
    print("Record Deleted Successfully!")


while True:
    print("\n1. Add Intern")
    print("2. View Intern Data")
    print("3. Update Intern Data")
    print("4. Delete Intern Data")
    print("5. Search Intern Data")
    print("6. Exit\n")
    print("=" * 120)

    choice = int(input("Enter Your Choice: "))
   
    if choice == 1:
        add_details()
    elif choice == 2:
        view_details()
    elif choice ==3:
        update_intern_data()
    elif choice ==4:
        delete_intern()
    elif choice ==5:
        search_intern()
    elif choice == 6:
        print("Thank You for Visiting !")
        break
    else:
        
        print("Invalid Choice!")
print("=" * 120)