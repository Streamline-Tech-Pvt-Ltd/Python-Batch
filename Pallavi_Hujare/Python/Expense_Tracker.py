class Expense:
    def __init__(self, expense_id, date, category, description, amount):
        self.expense_id = expense_id
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount
    def display(self):
        print(f"{self.expense_id:<10}{self.date:<15}{self.category:<15}{self.description:<20}₹{self.amount}")

class ExpenseTracker:
    def __init__(self):
        self.expense_list = []
        self.file_name = "expenses.txt"
        self.load_expenses()

    def load_expenses(self):
        try:
            with open(self.file_name, "r") as file:
                for line in file:
                    data = line.strip().split(",")
                    expense = Expense(
                        int(data[0]),
                        data[1],
                        data[2],
                        data[3],
                        float(data[4])
                    )
                    self.expense_list.append(expense)
        except FileNotFoundError:
            pass

    def save_expenses(self):
        with open(self.file_name, "w") as file:
            for expense in self.expense_list:
                file.write(
                    f"{expense.expense_id},{expense.date},{expense.category},{expense.description},{expense.amount}\n"
                )

    def add_expense(self):
        expense_id = int(input("Enter Expense ID : "))
        date = input("Enter Date : ")
        category = input("Enter Category : ")
        description = input("Enter Description : ")
        amount = float(input("Enter Amount : "))
        expense = Expense(
            expense_id,
            date,
            category,
            description,
            amount
        )
        self.expense_list.append(expense)
        self.save_expenses()
        print("Expense Added Successfully.")

    def view_expense(self):
          if len(self.expense_list) == 0:
            print("\nNo Expense Records Found.")
            return
          print("-" * 80)
          print(f"{'ID':<10}{'Date':<15}{'Category':<15}{'Description':<20}{'Amount'}")
          print("-" * 80)
          for expense in self.expense_list:
                expense.display()
                print("-" * 80)

    def search_expense(self):
        search_id = int(input("Enter Expense ID to Search : "))
        found = False
        for expense in self.expense_list:
            if expense.expense_id == search_id:
                print("-" * 80)
                print("\nExpense Found\n")
                print("-" * 80)
                expense.display()
                print("-" * 80)
                found = True
                break
            if not found:
                print("Expense Not Found.")

    def update_expense(self):
        update_id = int(input("Enter Expense ID to Update : "))
        found = False
        for expense in self.expense_list:
            if expense.expense_id == update_id:
                print("\nCurrent Expense Details")
                print("-" * 80)
                expense.display()
                print("-" * 80)
                print("\nEnter New Details")
                expense.date = input("Enter New Date : ")
                expense.category = input("Enter New Category : ")
                expense.description = input("Enter New Description : ")
                expense.amount = float(input("Enter New Amount : "))
                print("\nExpense Updated Successfully.")
                found = True
                break
        if not found:
            print("Expense Not Found.")

    def delete_expense(self):
        delete_id = int(input("Enter Expense ID to Delete : "))
        found = False
        for expense in self.expense_list:
            if expense.expense_id == delete_id:
                self.expense_list.remove(expense)
                print("Expense Deleted Successfully.")
                found = True
                break
        if not found:
            print("Expense Not Found.")

    def monthly_summary(self):
        if len(self.expense_list) == 0:
            print("No Expense Records Found.")
            return
        total = 0
        print("-" * 70)
        print(f"{'Category':<20}{'Amount'}")
        print("-" * 70)

        for expense in self.expense_list:
            print(f"{expense.category:<20}₹{expense.amount}")
            total += expense.amount

        print("-" * 70)
        print(f"Total Expense : ₹{total}")
        print("-" * 70)

tracker = ExpenseTracker()
while True:

    print("\n========== Monthly Expense Tracker ==========")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Search Expense")
    print("4. Update Expense")
    print("5. Delete Expense")
    print("6. Monthly Summary")
    print("7. Exit")

    choice = int(input("Enter Choice : "))

    if choice == 1:
        tracker.add_expense()

    elif choice == 2:
        tracker.view_expense()

    elif choice == 3:
        tracker.search_expense()

    elif choice == 4:
        tracker.update_expense()

    elif choice == 5:
        tracker.delete_expense()

    elif choice == 6:
        tracker.monthly_summary()

    elif choice == 7:
        print("Thank You")
        break

    else:
        print("Invalid Choice")