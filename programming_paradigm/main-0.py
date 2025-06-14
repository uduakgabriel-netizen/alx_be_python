<<<<<<< HEAD
# main-0.py
# my main-0.py

import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # #Start with $100
=======
import sys
from bank_account import BankAccount

def run(command_line_input):
    account = BankAccount(100)  # Start with $100 initial balance
>>>>>>> faf1441c25376abdc8f84d0edaa05b68db20a47d

    command, *params = command_line_input.split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount:.2f}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command. Use deposit:<amount>, withdraw:<amount>, or display")

def main():
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    run(sys.argv[1])

if __name__ == "__main__":
    main()
