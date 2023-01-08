"""
basically I got every other number right
but the output of s is wrong after looping m twice
(no error)
"""
for m in range(0,q):
  for j in range(0,k):
    print(s)
    new = int(nums[m][j])
    tmp[new-1] = s[j]
    if j == k-1:
      s = tmp

"""
question:
string = apcs
input 3142
the first letter in the string goes to the third place in a new string
I can't remember all of it so I'll have to wait until someone posts it online
"""
