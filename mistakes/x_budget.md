### 20230125
```python
each_spent = []
for self in categories:
  category_spent = 0
  for item in self.ledger:
    if item["amount"] < 0:
      category_spent += abs(item["amount"])
  # portion!
  portion = int(round(100 * (category_spent/total_spent), -1))
  each_spent.append(portion)
```
I'm not supposed to round up to the tens digit, because charts take the approximate but doing it too soon would make the accuracy go off. Okay my brain is off and so is my language skills but what I mean is that don't do too much approximation in these science stuff.

### 20230121

```python
def __init__(self, name, ledger=[], balance=0.00):
  self.name = name
  self.ledger = []
  self.balance = balance
```

I actually don't know why self.ledger = ledger wouldn't work otherwise.

### 20230124
```python
def check_funds(self, amount):
    if self.balance < amount:
      return False
    else:
      return True
      
def withdraw(self, amount:float, description:str=""):
    self.check_funds(amount) # for calling a method that's in the same class
    withdrawdict = {"amount": 0.00 - amount, "description": description} # because they're supposed to be negative
    self.ledger.append(withdrawdict)
    self.balance -= amount
    return True
```
Because `check_funds()` returns a Boolean value, calling the function won't do anything unless you use conditions.
