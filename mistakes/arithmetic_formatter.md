[arithmetic formatter](./codingpractices/arithmetic_formatter.py)

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
