# 20230109-20230111

n = int(input())
fac = []
i = 2
# find factors first
while i < n:
  if (n % i == 0):
    fac.append(i)
    n //= i
  else:
    i += 1
fac.append(n)

# for later uses when identifying the end
fac.append(0)

# getting overlapped numbers
same = []
for k in fac:
  if k not in same:
    same.append(k)

# getting times of repetition
rep = []
j = 0
count = 1
while j < len(fac) - 1:
  if fac[j] == fac[j+1]:
    count += 1
    j += 1
    continue
  elif fac[j] != fac[j+1]: # the last '0' comes in handy
    if count > 1:
      string = f"{fac[j]}^{count}"
      rep.append(string)
      j += 1
      count = 1 # reset count
    elif count == 1:
      string = f"{fac[j]}"
      rep.append(string)
      j += 1

print(" * ".join(rep))
