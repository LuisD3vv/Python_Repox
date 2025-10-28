class BankAccount:
	def __init__(self,first_name,last_name,account_id,account_type,pin,balance):
		self.first_name = first_name
		self.last_name = last_name
		self.account_id = account_id
		self.account_type = account_type
		self.pin = pin
		self.balance = balance

	def deposit(self,deposito):
		balance_nuevo = deposito
		self.balance = self.balance + balance_nuevo
	def withdraw(self,retiro):
		balance_retiro = retiro
		self.balance = self.balance - balance_retiro
	def display_balance(self):
		print(f"Currency {self.balance}")
1
usuario1 = BankAccount("Luis","Aguilar",2004,"credit",2077,96)
usuario1.withdraw(25)
#usuario1.deposit(110)
usuario1.display_balance()