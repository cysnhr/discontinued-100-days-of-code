# 20230121-25

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
      des = dict["description"] 
      des += " " * 30 # mindlessly adding spaces for slicing later
      num = '{:.2f}'.format(dict["amount"])
      des = des[0:29-len(num)] # because the spaces
      des += " " + '{:.2f}'.format(dict["amount"])
      output += f"{des}\n"
    output += f"Total: {self.balance}"
    return output
  
  def deposit(self, amount: float, description: str=""):
    depositdict = {"amount": amount, "description": description}
    self.balance += amount
    self.ledger.append(depositdict)

  def check_funds(self, amount):
      if self.balance < amount:
        return False
      else:
        return True

  def withdraw(self, amount:float, description:str=""):
      if self.check_funds(amount): # for calling a method that's in the same class
        withdrawdict = {"amount": 0.00 - amount, "description": description} # because they're supposed to be negative
        self.ledger.append(withdrawdict)
        self.balance -= amount
        return True
      else:
        return False

  
  def get_balance(self):
    return self.balance

  def transfer(self, amount: float, to_ledger):
      if self.check_funds(amount):
        self.balance -= amount
        withdrawdict = {"amount": 0.00 - amount, "description": f"Transfer to {to_ledger.name}"}
        self.ledger.append(withdrawdict)
        to_ledger.ledger.append({"amount": amount, "description": f"Transfer from {self.name}"})
        to_ledger.balance += amount
        return True
      else:
        return False


def create_spend_chart(categories: list):
  # topmost
  output = "Percentage spent by category\n"

  # calculates portions
  # get total withdrawal
  total_spent = 0.00
  # also the name of categories for later purposes
  name_list = []
  for self in categories:
    name_list.append(self.name)
    for item in self.ledger:
      if item["amount"] < 0:
        total_spent += abs(item["amount"]) 

  # have to get total_spent before retrieving each individual total of ledgers
  # this is each total of individual categories
  each_spent = []
  for self in categories:
    category_spent = 0
    for item in self.ledger:
      if item["amount"] < 0:
        category_spent += abs(item["amount"])
    # portion!
    portion = int(round(100 * (category_spent/total_spent)))
    each_spent.append(portion)

  y = [100,90,80,70,60,50,40,30,20,10,0]
  for most in y:
    # spacing
    if most == 100:
      output += f"{most}|"
    elif most == 0:
      output += f"  {most}|"
    else:
      output += f" {most}|"

    # chart
    for each in each_spent:
      if each >= most:
        output += " o "
      else:
        output += "   "
    output += " \n"

  # bottom most

  # find max length to get the correct spacing
  max_len = 0
  for name in name_list:
    if len(name) > max_len:
      max_len = len(name)

  # adding spaces for spacing purposes :)
  new = []
  for name in name_list:
    name += ' ' * (max_len - len(name))
    new.append(name)

  line = "    " + "-" * 3 * len(name_list) + "-\n"
  output += line
  for i in range(0, max_len):
    output += "    "
    for name in new:
      line = f" {name[i]} "
      output += line
    output += " \n"
  
  output = output.rstrip()
  output += "  "
  return output


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
print(auto)
print(create_spend_chart([food, clothing, auto]))

"""
Percentage spent by category
12345012
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o     
 12345678
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     

123456789012
"""
