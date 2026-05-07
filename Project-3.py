import json
import os

# --- Configurations ---
FILENAME = "expenses.json"

def load_data():
    """Loads expenses from a JSON file. Interview Tip: Explain how JSON stores data as text."""
    if not os.path.exists(FILENAME):
        return []
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        return []

def save_data(expenses):
    """Saves expenses to a JSON file. Interview Tip: Mention Context Managers ('with' statement) for file safety."""
    try:
        with open(FILENAME, "w") as file:
            json.dump(expenses, file, indent=4)
    except IOError as e:
        print(f"Error saving data: {e}")

def add_expense(expenses):
    print("\n--- Add New Expense ---")
    date = input("Kis date par khrcha kiya tha? (DD-MM-YYYY): ")
    category = input("Kis type ka khrcha kiya? (Food/Travel/Makeup/Books): ")
    description = input("Aur detail dedo (Description): ")
    try:
        amount = float(input("Enter the amount: "))
    except ValueError:
        print("Invalid amount! Please enter a number.")
        return

    expense = {
        "date": date,
        "category": category,
        "description": description,
        "amount": amount
    }
    expenses.append(expense)
    save_data(expenses)
    print("DONE bro. Expense added successfully!")

def view_expenses(expenses):
    print("\n===== Ye Raha Apka Sara Expense ======")
    if not expenses:
        print("No expenses found. Jao pehle khrcha karo!")
        return

    # Interview Tip: Using f-string formatting for a clean table-like view
    print(f"{'No.':<4} | {'Date':<12} | {'Category':<12} | {'Amount':<10} | {'Description'}")
    print("-" * 60)
    for i, exp in enumerate(expenses, 1):
        print(f"{i:<4} | {exp['date']:<12} | {exp['category']:<12} | {exp['amount']:<10.2f} | {exp['description']}")

def delete_expense(expenses):
    view_expenses(expenses)
    if not expenses:
        return
    
    try:
        task_no = int(input("\nDelete karne ke liye 'Kharcha Number' enter kare: "))
        if 1 <= task_no <= len(expenses):
            removed = expenses.pop(task_no - 1)
            save_data(expenses)
            print(f"Removed: {removed['description']} is deleted!")
        else:
            print("Invalid Number!")
    except ValueError:
        print("Please enter a valid number.")

def view_total(expenses):
    total = sum(exp['amount'] for exp in expenses) # Interview Tip: Use list comprehension/sum for cleaner code
    print(f"\n>>> TOTAL KHRCHA = {total:.2f}")

def main():
    expensesList = load_data()
    print("=== Welcome to Expense Tracker PRO ===")

    while True:
        print("\n==== MENU ====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Kharcha")
        print("4. Delete Expense")
        print("5. Exit")

        try:
            choice = input("Please Enter Your Choice (1-5): ")
            
            if choice == "1":
                add_expense(expensesList)
            elif choice == "2":
                view_expenses(expensesList)
            elif choice == "3":
                view_total(expensesList)
            elif choice == "4":
                delete_expense(expensesList)
            elif choice == "5":
                print("Dhanyawad aapne humara system use kiya. Bye!")
                break
            else:
                print("INVALID CHOICE. TRY AGAIN")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()