# Coding Practices Reflection
A lot of times I make the same mistakes, so I figured if I keep track of it, I might start doing better!

### 1. Two Sum
01/01/2023
https://leetcode.com/problems/two-sum
Technical mistakes:
I don't know why I rely on for loops so much, to the extent of implementing a double for loop here. I wish as I go further into these 100 days I'd stop doing it.
what I did:
```
class Solution(object):
    def twoSum(self, num, target):
        total_tests = len(num)
        for i in range(0,total_tests):
            for j in range(i+1,total_tests):
                if num[i] + num[j] == target:
                    return [i,j]```
alternatives (after a sneak peek at solutions):
```
class Solution(object):
  def twoSum(self, num, target):
    
```

Dumb mistakes:
- beware of variable names
- use commas properly
