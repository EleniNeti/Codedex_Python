class BankAccount:
  def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
    self.first_name = first_name
    self.last_name = last_name
    self.account_id = account_id
    self.account_type = account_type
    self.pin = pin
    self.balance = balance
  
  
  def deposit(self, money_added):
    self.money_added = money_added
    self.balance = self.balance + self.money_added
    return self.balance
  
  def withdraw(self, money_withdrawn):
    self.money_withdrawn = money_withdrawn
    self.balance = self.balance - self.money_withdrawn
    return self.balance
  
  def display_balance(self):
    print('You currently have ' + str(self.balance) + '$ in your account.')


alpha_bank = BankAccount('Name', 'Surname', 123456789, 'Expenses', 1234, 300.00)

alpha_bank.deposit(100.89)
alpha_bank.withdraw(25)
alpha_bank.display_balance()