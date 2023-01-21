# 20230121

class Category:
  def __init__(self, name, ledger=[], balance=0.00):
    self.name = name
    self.ledger = []
    self.balance = balance
  # I actually don't know why self.ledger = ledger wouldn't work otherwise but okay
  
  def __repr__(self):
    num = round((30 - len(self.name)) / 2)
    output = ""
    title = f"{'*' * num}{self.name}{'*' * (30-len(self.name)-num)}\n"
    output += title
    for dict in self.ledger:
      # stuff stuff stuff
      pass
    return output
  
  def deposit(self, amount: float, description: str=""):
    depositdict = {"amount": amount, "description": description}
    self.balance += amount
    self.ledger.append(depositdict)

  def check_funds(self, amount):
      if self.balance < amount:
        return False
      else:
        pass

  def withdraw(self, amount:float, description:str=""):
      self.check_funds(amount) # for calling a method that's in the same class
      withdrawdict = {"amount": 0.00 - amount, "description": description} # because they're supposed to be negative
      self.ledger.append(withdrawdict)
      self.balance -= amount
      return True

  def get_balance(self):
    return self.balance

  def transfer(self, amount: float, to_ledger):
      self.check_funds(amount)
      self.balance -= amount
      withdrawdict = {"amount": 0.00 - amount, "description": f"Transfer to {to_ledger.name}"}
      self.ledger.append(withdrawdict)
      to_ledger.ledger.append({"amount": amount, "description": f"Transfer from {self.name}"})
      to_ledger.balance += amount
      return True

def create_spend_chart():
  pass


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)
print(food)
print(clothing)

# print(create_spend_chart([food, clothing, auto]))
