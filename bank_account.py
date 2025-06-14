# bank_account.py

class BankAccount:
    def __init__(self, balance=0):
        """Initialize account with an optional starting balance."""
        self.balance = balance

    def deposit(self, amount):
        """Add money to the account."""
        if amount > 0:
            self.balance += amount
        else:
            print("Deposit must be a positive amount.")

    def withdraw(self, amount):
        """Withdraw money if enough balance is available."""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Show the current balance."""
        print(f"Current balance: ${self.balance:.2f}")
