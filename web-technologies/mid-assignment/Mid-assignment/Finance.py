from datetime import datetime
import sys

class Transaction:
    def __init__(self, description, amount, date, category):
        self.description = description
        self.amount = amount
        self.date = datetime.strptime(date, '%Y-%m-%d')
        self.category = category

    def __str__(self):
        return f"{self.date.strftime('%Y-%m-%d')} | {self.category} | {self.description}: ${self.amount:.2f}"

class Budget:
    def __init__(self):
        self.category_limits = {}

    def set_budget(self, category, limit):
        self.category_limits[category] = limit

    def get_budget(self, category):
        return self.category_limits.get(category, 0)

class FinanceTracker:
    def __init__(self):
        self.transactions = []
        self.budget = Budget()

    def add_transaction(self, description, amount, date, category):
        self.transactions.append(Transaction(description, float(amount), date, category))
        print("Transaction added successfully.")

    def edit_transaction(self, index, description, amount, date, category):
        try:
            self.transactions[index] = Transaction(description, float(amount), date, category)
            print("Transaction updated.")
        except IndexError:
            print("Invalid transaction index.")

    def delete_transaction(self, index):
        try:
            del self.transactions[index]
            print("Transaction deleted.")
        except IndexError:
            print("Invalid transaction index.")

    def list_transactions(self, category=None, start_date=None, end_date=None):
        print("\nTransactions:")
        filtered = self.transactions
        if category:
            filtered = [t for t in filtered if t.category == category]
        if start_date:
            start = datetime.strptime(start_date, '%Y-%m-%d')
            filtered = [t for t in filtered if t.date >= start]
        if end_date:
            end = datetime.strptime(end_date, '%Y-%m-%d')
            filtered = [t for t in filtered if t.date <= end]
        for i, t in enumerate(filtered):
            print(f"{i}: {t}")
        if not filtered:
            print("No transactions found.")

    def budget_summary(self):
        income = sum(t.amount for t in self.transactions if t.amount > 0)
        expenses = sum(t.amount for t in self.transactions if t.amount < 0)
        balance = income + expenses
        print(f"\nBudget Overview:\nTotal Income: ${income:.2f}\nTotal Expenses: ${-expenses:.2f}\nBalance: ${balance:.2f}")
        for category, limit in self.budget.category_limits.items():
            spent = sum(t.amount for t in self.transactions if t.category == category and t.amount < 0)
            print(f"Category '{category}': Spent ${-spent:.2f} / Limit ${limit:.2f}")

# User Interface
def main():
    tracker = FinanceTracker()

    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add a transaction")
        print("2. Edit a transaction")
        print("3. Delete a transaction")
        print("4. View all transactions")
        print("5. View budget overview")
        print("6. Set category budget")
        print("0. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            desc = input("Description: ")
            amount = input("Amount (positive for income, negative for expense): ")
            date = input("Date (YYYY-MM-DD): ")
            category = input("Category: ")
            tracker.add_transaction(desc, amount, date, category)
        elif choice == '2':
            tracker.list_transactions()
            idx = int(input("Enter the transaction index to edit: "))
            desc = input("New Description: ")
            amount = input("New Amount: ")
            date = input("New Date (YYYY-MM-DD): ")
            category = input("New Category: ")
            tracker.edit_transaction(idx, desc, amount, date, category)
        elif choice == '3':
            tracker.list_transactions()
            idx = int(input("Enter the transaction index to delete: "))
            tracker.delete_transaction(idx)
        elif choice == '4':
            filt_cat = input("Filter by category (press Enter to skip): ")
            start = input("Start date (YYYY-MM-DD, press Enter to skip): ")
            end = input("End date (YYYY-MM-DD, press Enter to skip): ")
            tracker.list_transactions(category=filt_cat or None, start_date=start or None, end_date=end or None)
        elif choice == '5':
            tracker.budget_summary()
        elif choice == '6':
            category = input("Category: ")
            limit = float(input("Budget limit: "))
            tracker.budget.set_budget(category, limit)
            print("Budget set.")
        elif choice == '0':
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
