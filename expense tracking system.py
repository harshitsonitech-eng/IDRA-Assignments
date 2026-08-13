import csv
from datetime import datetime

FILE_NAME = "expenses.csv"


def create_file():
    try:
        with open(FILE_NAME, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Note"])
    except FileExistsError:
        pass


def add_expense():
    try:
        date = input("Enter date (DD-MM-YYYY): ")

        datetime.strptime(date, "%d-%m-%Y")

        category = input("Enter category: ")
        amount = float(input("Enter amount: "))
        note = input("Enter note (optional): ")

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, category, amount, note])

        print("Expense added successfully!")

    except ValueError:
        print("Invalid input! Please enter a valid date and amount.")


def view_expenses():
    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)

            total = 0
            found = False

            print("\n----- All Expenses -----")

            for expense in reader:
                found = True
                amount = float(expense["Amount"])
                total += amount

                print(
                    f"Date: {expense['Date']} | "
                    f"Category: {expense['Category']} | "
                    f"Amount: ₹{amount:.2f} | "
                    f"Note: {expense['Note']}"
                )

            if not found:
                print("No expenses recorded.")

            print("------------------------------")
            print(f"Total Amount Spent: ₹{total:.2f}")

    except FileNotFoundError:
        print("Expense file not found.")


def category_summary():
    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)

            categories = {}

            for expense in reader:
                category = expense["Category"]
                amount = float(expense["Amount"])

                if category in categories:
                    categories[category] += amount
                else:
                    categories[category] = amount

            print("\n----- Category-wise Spending -----")

            if not categories:
                print("No expenses recorded.")
                return

            for category, amount in categories.items():
                print(f"{category}: ₹{amount:.2f}")

    except FileNotFoundError:
        print("Expense file not found.")


create_file()

while True:
    print("\n----- Expense Tracking System -----")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Category-wise Summary")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        category_summary()

    elif choice == "4":
        print("Thank you for using Expense Tracking System!")
        break

    else:
        print("Invalid choice! Please select 1-4.")