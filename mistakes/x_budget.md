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
