class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        print(f"Welcome, {self.owner}!\nYour current balance: {self.balance}\n")

    def deposit(self, cash):
        self.balance+=cash
        print(f"The balance have replenished!\nCurrent balance: {self.balance}\n")
    
    def withdraw(self, cashw):
        if(self.balance<cashw):
            print(f"Insufficient funds for withdraw! Your current balance: {self.balance}\n")
        else:
            self.balance-=cashw
            print(f"You've withdrawn: {cashw}\nYour current balance: {self.balance}")
    
newo = Account("Bekzhan", 4555)
newo.deposit(10200)
newo.withdraw(14755)