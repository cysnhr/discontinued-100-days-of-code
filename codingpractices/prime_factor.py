# 20230109-20230110

n = 10000 # int(input())
fac = []
i = 2
# find factors first
while i < n:
  if (n % i == 0):
    print(i, n)
    fac.append(i)
    n //= i
  else:
    i += 1
fac.append(n)
print(fac)

# getting overlapped numbers
same = []
for k in fac:
  if k not in same:
    same.append(k)

# getting times of repetition
rep = ""
for e in same:
  c = 0
  if e in fac:
    c += 1
  print(f"{e} occurred {c} times")
