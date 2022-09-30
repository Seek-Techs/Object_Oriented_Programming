import datetime

class Account:
    account_balance = 3000
    current_local = str(datetime.datetime.now())
    def __init__(self, name: str, account_number: str):
        self.name = name
        self.account = account_number
        #self.current_date = current_date

    def show_menu(self):
        
        msg = {
            'Acount Name': self.name, 'Account balance': Account.account_balance, 
            'Current Date': Account.current_local
            }
            
        return msg

    def get_balance(self):
        available_balance = f'Available Balance: {Account.account_balance}\n'
        return available_balance

    def deposit(self, amount: int):
        Account.account_balance 
        Account.account_balance += amount
        deposited = 'Deposited Successful!' #%(amount) %(Account.account_balance + amount)
        return deposited

    def withdraw(self, amount_withdraw: int):
        available_balance = Account.account_balance
        available_balance = available_balance - amount_withdraw
        if amount_withdraw > available_balance:
            msg = "insufficient funds. Your current balance: %s  " % (Account.account_balance)
            return msg

        msg = "sufficient funds. Amount withdrew: %s  " % (amount_withdraw)
        ad = available_balance - amount_withdraw
        return msg, ad

account = Account('yusuff', 122333333)
print(account.show_menu())

account_balance = account.get_balance()
print(account_balance)

deposit = account.deposit(23000)
print(deposit)

account_balance = account.get_balance()
print('correct', account_balance)

withdraw = account.withdraw(1000000000)
print(withdraw)
