class FinanceTracker:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, description, amount):
        self.transactions.append({'description': description, 'amount': amount})
        print(f"Added: {description}, Amount: {amount}")

    def view_transactions(self):
        if not self.transactions:
            print("No transactions found.")
            return
        for transaction in self.transactions:
            type = "Income" if transaction['amount'] > 0 else "Expense"
            print(f"{type}: {transaction['description']}, Amount: {transaction['amount']}")

    def summary(self):
        income = sum(t['amount'] for t in self.transactions if t['amount'] > 0)
        expense = sum(t['amount'] for t in self.transactions if t['amount'] < 0)
        balance = income + expense
        print(f"Total Income: {income}")
        print(f"Total Expense: {expense}")
        print(f"Balance: {balance}")

def main():
    tracker = FinanceTracker()
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Income/Expense")
        print("2. View Transactions")
        print("3. Summary")
        print("4. Exit")
        choice = input("Choose an action: ")

        if choice == '1':
            desc = input("Enter description: ")
            amount = float(input("Enter amount (positive for income, negative for expense): "))
            tracker.add_transaction(desc, amount)
        elif choice == '2':
            tracker.view_transactions()
        elif choice == '3':
            tracker.summary()
        elif choice == '4':
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
