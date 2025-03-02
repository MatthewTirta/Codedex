class BankAccount:
    def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return amount
        else:
            print("Insufficient funds!")
            return 0
    
    def display_balance(self):
        print(f"Total Balance: ${self.balance}")

my_account = BankAccount("John", "Doe", 12345, "Checking", 1234, 0)

my_account.deposit(96)
my_account.withdraw(25)
my_account.display_balance()