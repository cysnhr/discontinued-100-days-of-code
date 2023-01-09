# 20230109

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



"""

this is the old code
and it's funny
this is me being a genius and trying to run for loop like that
hahaHAHAHA

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

print(rep)
print(times)
print(other)


print("finished running")


" * ".join(b)

okay so
we need to look for repetitions
and all the elements in the thing
then connect them with *
"""
