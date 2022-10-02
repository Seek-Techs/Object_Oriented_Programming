import datetime

class Account:
    
    # Define attributes through an Instance
    def __init__(self, name:str, account_num:int):
        self.name = name
        self.account_num = account_num
        self.balance = 0.0
        self.current_local = str(datetime.datetime.now())

    # Methods to perform on the Account are as defined below:
    def show_menu(self):
        msg = 'Welcome to CeayHollertech Bank, %s\n\nYour Current Balance: $%s\nAccount Number: %s\nDate: %s\n' %(
            self.name, self.balance, self.account_num, self.current_local
            )
        return msg
    
    def get_balance(self):
        msg = 'Your Balance is $%s ' %(self.balance)
        return msg

    def deposit(self, amount:float):
        self.balance += amount
        msg = 'Deposited Succesfully!\nYour Account Balance is $%s \n' %(self.balance)
        return msg
    
    def withdraw(self, amount: float):
        if self.balance > amount:
            self.balance -= amount
            msg = 'Withdrawal Successful!\nYour Balance is $%s\n ' %(self.balance)
            return msg
        
        return 'Insufficient Balance'
    
    def transfer(self, account: int, amount: float):
        if self.balance > amount:
            self.balance -= amount
            account.balance += amount
            msg = 'Transfer from %s to %s\nDate: %s\nAvailable Balance: $%s ' %(
                self.name, account.name, self.current_local, self.balance
                )
            return msg
        return 'Insufficient Fund! Your Available Balance: $%s ' %(self.balance)
        
# Define Account Object
yusuff = Account('Sikiru Yusuff', '2345678')

# Display menu
print(yusuff.show_menu())

# Balance of the account
print(yusuff.get_balance())

# Deposit money to the account
print(yusuff.deposit(345.78))

# Withdraw amount 
print(yusuff.withdraw(100))

# Define an account object to transfer with passing the account name and the number
queen = Account('Queen Gatty', 3456782)

# A transfer to the account
print(yusuff.transfer(queen, 44))

# Confirm account transfer
print(queen.get_balance())
