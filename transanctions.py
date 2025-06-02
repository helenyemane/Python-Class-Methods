from datetime import datetime
from enum import Enum

class TransactionType(Enum):
    CREDIT = "Credit"
    DEBIT = "Debit"
    LOAN = "Loan"
    LOAN_REPAYMENT = "Loan Repayment"

class Transaction:
    def __init__(self, narration, amount, transaction_type):
        self.date_time = datetime.now()
        self.narration = narration
        self.amount = amount
        self.transaction_type = transaction_type
    def __str__(self):
        formatted_time = self.date_time.strftime("%Y-%m-%d %H:%M:%S")
        return f"{formatted_time}: {self.transaction_type.value} of {self.amount} - {self.narration}"

class Account:
    def __init__(self, owner, account_number, minimum_balance=100):
        self.owner = owner
        self._account_number = account_number
        self.minimum_balance = minimum_balance
        self._balance = 0
        self.loan_amount = 0
        self.transactions = []
        self.is_frozen = False
        self.is_closed = False
       

    def _update_balance(self):
        self._balance = sum(
            transact.amount if transact.transaction_type == TransactionType.CREDIT else -transact.amount
            for transact in self.transactions
        )

    def _check_account_status(self):
        if self.is_closed:
            return "Account is closed."
        if self.is_frozen:
            return "Account is frozen."
        return None

    def deposit(self, amount):
        status = self._check_account_status()
        if status:
            return status
        if amount <= 0:
            return "Deposit amount must be positive."
        transaction = Transaction("Deposit", amount, TransactionType.CREDIT)
        self.transactions.append(transaction)
        self._update_balance()
        return f"Deposited {amount}. New balance: {self.get_balance()}"

    def withdraw(self, amount):
        status = self._check_account_status()
        if status:
            return status
        if amount <= 0:
            return "Withdrawal amount must be positive."
        if self.get_balance() - amount < self.minimum_balance:
            return "Insufficient funds for withdrawal."
        transaction = Transaction("Withdrawal", amount, TransactionType.DEBIT)
        self.transactions.append(transaction)
        self._update_balance()
        return f"Withdrew {amount}. New balance: {self.get_balance()}"

    def transfer_funds(self, amount, target_account):
        status = self._check_account_status()
        if status:
            return status
        if self.withdraw(amount) == "Insufficient funds for withdrawal.":
            return "Transfer failed due to insufficient funds."
        target_account.deposit(amount)
        return f"Transferred {amount} to {target_account.owner}. New balance: {self.get_balance()}"

    def get_balance(self):
        return self._balance

    def request_loan(self, amount):
        status = self._check_account_status()
        if status:
            return status
        self.loan_amount += amount
        transaction = Transaction("Loan Request", amount, TransactionType.LOAN)
        self.transactions.append(transaction)
        self._update_balance()
        return f"Loan of {amount} requested."

    def repay_loan(self, amount):
        status = self._check_account_status()
        if status:
            return status
        if amount > self.loan_amount:
            return "Cannot repay more than the loan amount."
        self.loan_amount -= amount
        transaction = Transaction("Loan Repayment", amount, TransactionType.LOAN_REPAYMENT)
        self.transactions.append(transaction)
        self._update_balance()
        return f"Repaid {amount} towards loan."

    def view_account_details(self):
        return f"Owner: {self.owner}, Balance: {self.get_balance()}, Account Number: {self._account_number}"

    def change_account_owner(self, new_owner):
        self.owner = new_owner
        return f"Account owner changed to {new_owner}."

    def account_statement(self):
        return "\n".join(str(transaction) for transaction in self.transactions)

    def calculate_interest(self):
        interest = self.get_balance() * 0.05
        self.deposit(interest)
        return f"Interest of {interest} applied."

    def freeze_account(self):
        self.is_frozen = True
        return "Account frozen."

    def unfreeze_account(self):
        self.is_frozen = False
        return "Account unfrozen."

    def set_minimum_balance(self, amount):
        self.minimum_balance = amount
        return f"Minimum balance set to {amount}."

    def close_account(self):
        self.is_closed = True
        self._balance = 0
        self.transactions.clear()
        return "Account closed."


acc1 = Account("Belete", "1000221128985")
acc2 = Account("Hellen", "1000294433945")
print(acc1.deposit(5000))
print(acc1.withdraw(100))
print(acc1.transfer_funds(800, acc2))
print(acc1.view_account_details())
print(acc1.account_statement())