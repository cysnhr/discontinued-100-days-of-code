[Prime Factor](./codingpractices/prime_factor.py)
completed on 2023 01 11

### 2023 01 11
```
for e in range(0, len(fac)-1):
  count = 1
  print(fac[e], fac[e+1])
  if fac[e] == fac[e+1]:
    count += 1
  if count == 1:
    rep.append(fac[e])
  else:
    string = f"{fac[e]}^{count}"
    rep.append(string)
```
1. Have not considered the last element. What if they are all the same in the list? There'd be no output.
2. Count is not reset.

### 2023 01 10
```python
# getting times of repetition
rep = ""
for e in same:
  c = 0
  if e in fac:
    c += 1
  print(f"{e} occurred {c} times")
```
1. `if` is a conditional, not a loop. The maximum value of `c` will only be 1.

### 2023 01 09

```python
n = int(input())
fac = []
while n > 0:
  for i in range(1,n+1):
    i = int(i)
    if i * i == n:
      print(i, n)
      fac.append(i)
    elif n % (n / i) == 0:
      print(i, n)
      fac.append(i)
      n /= i
```
1. `/=` is going to return floats, which cannot do arithmetic with integers.
2. This is just looking for factors without much accuracy and not all of them are prime numbers.

### who knew how long ago
```python
def prime_fac(a):
  ls = []
  while a != 1:
    for i in range(2,100000000):
      if a % int(i) == 0:
        ls.append(int(i))
        a = a / int(i)
    return ls

rep = []
times = []
other = []

num = prime_fac(100)
print(num)

for j in range(0,len(num)):
  f = 1
  if j < len(num) -2 and num[j] == num[j+1]:
    f += 1
  if f != 1:
    rep.append(num[j])
    times.append(f)
  elif num[j] != num[j-1]:
    other.append(num[j])
```
HAHAHA I don't even know what to say. How much genius did it take for someone to try to run a for loop like that.
Also the list index kept getting out of range :)
