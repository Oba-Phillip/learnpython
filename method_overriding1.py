# method_overriding/banking_example.py
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        return "Insufficient funds"

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate
    
    # Overriding withdraw method to add minimum balance requirement
    def withdraw(self, amount):
        if self.balance - amount < 100:  # Minimum balance requirement
            return "Withdrawal denied. Must maintain $100 minimum balance."
        return super().withdraw(amount)

class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit
    
    # Overriding withdraw method to allow overdraft
    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        return "Transaction denied. Overdraft limit exceeded"

# Usage
savings = SavingsAccount("SA123", 500, 0.03)
print(savings.withdraw(450))  # Denied - would go below $100
print(savings.withdraw(300))  # Allowed

checking = CheckingAccount("CA456", 200, 100)
print(checking.withdraw(250))  # Allowed with overdraft
print(checking.withdraw(100))  # Denied - exceeds overdraft limit