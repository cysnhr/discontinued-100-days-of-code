[arithmetic formatter](./codingpractices/arithmetic_formatter.py)

### 20230117

I thank that user on the forum so much for catching this mistake I've been mauling over (probably not the right word?) for days. I simply did not read the instructions right, overlooking the part where they're supposed to hide the answer unless otherwise specified.
```python
def arithmetic_arranger(problems, answer = False):
...
  if answer:
    return arranged_problems
  else:
    return f"{one}\n{two}\n{d}"
```


### 20230116

Little stupid mistakes.

```python
if op != "+" or op != "-":
  return "Error: Operator must be '+' or '-'."
```
If the operator is not both of them, it will account to true. Should be using `and` in this case. Argh booleans argh my logic.

```python
form_num1 = (" " * longest - len1) + str(num1)
form_num2 = op + (" " * longest - len2 - 1) + str(num2)
```
Harharhar what you're doing is multiplying strings then trying to subtract them by integers which makes no sense at all.
