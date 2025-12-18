"""
A. private attribute by convention
"""

class BandAccount:
    def __init__(self,owner,balance = 0):
        self.owner = owner
        # 1. use _(underscore) to mark the balance as a private attribute.
        self._balance = balance

    # 2. Getter: provide safety readable access to private attribute.
    def get_balance(self):
        print("Checking credentials...")
        return self._balance

    #3. Setter: provide a safety writable access.
    def deposit(self,amount):
        """save money into account"""
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount}. New balance: ${self._balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self,amount):
        if amount > self._balance:
            print("Insufficient funds")
        elif amount > 0:
            self._balance -= amount
            print(f"Withdraw ${amount}. New balance: ${self._balance}")
        else:
            print(f"Withdraw amount must be positive.")
