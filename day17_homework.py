from day16_homework import lucky


class BankAccount:
    def __init__(self,name,balance=0.00):
        self.name = name
        self._balance = balance

    def get_balance(self):
        print(f"The account of {self.name} has {self._balance}")

    def deposit(self,amount):
        if amount > 0:
            self._balance += amount
            print(f"The account of {self.name} has been deposited into ${amount}")
        else:
            print("The amount cannot be negative!")

    def withdraw(self,amount):
        if amount > self._balance:
            print("the balance is not enough!")
        elif amount<=0:
            print("The amount should be positive!")
        else:
            self._balance -= amount
            print(f"You have withdraw ${amount}, the current rest balance is {self._balance}!")

    def exchange_currency(self,amount):
        global currency
        rate = 7
        if amount >self._balance:
            print("The operation is impossible!")
        else:
            currency = f"{amount / rate:.2f}"
            self._balance -= amount
            print(f"You have exchange the currency {currency},and the rest balance is {self._balance}")
        return currency



lulu = BankAccount("Lulu",100000000)
lulu.withdraw(10000)
ex = lulu.exchange_currency(10000)
print(ex)