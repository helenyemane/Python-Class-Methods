class Account:
    def __init__(self, name):
        self.name = name
        self.deposits = []
        self.withdrawals = []
        self.transfers = []
        self.loans = []
        self.loan_repayments = []
        self.balance = 0
        self.frozen = False
        self.min_balance = 0
        self.closed = False
    def _is_active(self):
        if self.closed:
            return "Account is closed."
        if self.frozen:
            return "Account is frozen."
        return None
    def deposit(self, amount):
        if self._is_active(): 
            return self._is_active()
        if amount <= 0:
            return "You can't deposit a negative amount."
        self.deposits.append(amount)
        self.balance += amount
        return f"{amount} deposited successfully. New balance: {self.balance}"
    def withdraw(self, amount):
        if self._is_active(): return self._is_active()
        if amount <= 0:
            return "You can't withdraw a negative amount."
        if self.balance - amount < self.min_balance:
            return "Insufficient balance."
        self.withdrawals.append(amount)
        self.balance -= amount
        return f"{amount} withdrawn successfully. New balance: {self.balance}"
    def transfer(self, amount, user_account):
        if self._is_active(): return self._is_active()
        if amount <= 0:
            return "You can't transfer a negative amount."
        if self.balance - amount < self.min_balance:
            return "Minimum balance restriction."
        self.transfers.append(amount)
        self.balance -= amount
        user_account.deposit(amount)
        return f"{amount} transferred to {user_account.name}. New balance: {self.balance}"
    def get_balance(self):
        return f"Current balance: {self.balance}"
    def request_loan(self, amount):
        if self._is_active(): return self._is_active()
        if amount <= 0:
            return "You can't request a negative loan."
        self.loans.append(amount)
        self.balance += amount
        return f"Loan of {amount} granted. New balance: {self.balance}"
    def repay_loan(self, amount):
        if self._is_active(): return self._is_active()
        if amount <= 0:
            return "You can't repay a negative amount."
        if sum(self.loans) == 0:
            return "You have no unpaid loans."
        self.loan_repayments.append(amount)
        self.balance -= amount
        return f"Loan repayment of {amount} successful. Remaining loan: {sum(self.loans) - sum(self.loan_repayments)}"
    def view_account_details(self):
        return f"Account Owner: {self.name}\nBalance: {self.balance}"
    def change_account_owner(self, new_name):
        self.name = new_name
        return f"Account owner updated to {new_name}."
    def get_statement(self):
        print(f"Account Statement for {self.name}")
        print("Deposits:")
        for d in self.deposits:
            print(f" +{d}")
        print("Withdrawals:")
        for w in self.withdrawals:
            print(f" -{w}")
        print("Transfers:")
        for t in self.transfers:
            print(f" -{t}")
        print(f"Current Balance: {self.balance}")
    def get_loan_statement(self):
        print(f"Loan Statement for {self.name}")
        print("Loans Taken:")
        for loan in self.loans:
            print(f" +{loan}")
        print("Loan Repayments:")
        for repayment in self.loan_repayments:
            print(f" -{repayment}")
        print(f"Remaining Loan: {sum(self.loans) - sum(self.loan_repayments)}")
    def apply_interest(self):
        if self._is_active(): return self._is_active()
        interest = self.balance * 0.05
        self.balance += interest
        return f"Interest of {interest} applied. New balance: {self.balance}"
    def freeze_account(self):
        self.frozen = True
        return "Account has been frozen."
    def unfreeze_account(self):
        self.frozen = False
        return "Account has been unfrozen."
    def set_min_balance(self, amount):
        if amount < 0:
            return "Minimum balance cannot be negative."
        self.min_balance = amount
        return f"Minimum balance set to {amount}."
    def close_account(self):
        self.closed = True
        self.deposits.clear()
        self.withdrawals.clear()
        self.transfers.clear()
        self.loans.clear()
        self.loan_repayments.clear()
        self.balance = 0
        return "Account has been closed."
    



# Create two accounts
acc1 = Account("Helen")
acc2 = Account("Berhe")


print(acc1.deposit(500))         
print(acc1.withdraw(200))        
print(acc1.transfer(100, acc2))  
print(acc2.get_balance())  
print(acc1.view_account_details())
print(acc1.request_loan(300))    
print(acc1.repay_loan(100))     
print(acc1.apply_interest())
print(acc1.change_account_owner("Hilari"))
print(acc1.set_min_balance(50))
print(acc1.freeze_account())
print(acc1.deposit(50))         
print(acc1.unfreeze_account())
print(acc1.deposit(50))   

acc1.get_statement()
acc1.get_loan_statement()

print(acc1.close_account())
print(acc1.deposit(10))   
