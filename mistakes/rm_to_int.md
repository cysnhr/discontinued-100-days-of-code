#### 20230320

```python
class Solution(object):
    def romanToInt(self, s):
        
        rm = ["I", "V", "X", "L", "C", "D", "M"]
        nm = [1, 5, 10, 50, 100, 500, 1000, 0]
        
        # IV
        # VI
        ans = 0
        for l in s:
            for i in range(0, len(rm)):
                if l == rm[i] and nm[i+1] <= nm[i]:
                    ans += nm[i]
                elif nm[i+1] > nm[i]:
                    ans -= nm[i]
                
        return ans

        
        """
        :type s: str
        :rtype: int
        """
        
```
#### 0321

```python
converted = []
for l in s:
  for i in range(0, len(rm)):
    if l == rm[i]:
      converted.append(rm[i])

converted.append(0)
ans = 0

for n in len(s):
  if converted[n] < converted[n+1]:
    ans -= converted[n])
  else:
    ans += converted[n]
```

#### 0402

```python
class Solution(object):
    def romanToInt(self, s):
        
        rm = ["I", "V", "X", "L", "C", "D", "M"]
        nm = [1, 5, 10, 50, 100, 500, 1000, 0]
        
        # IV
        # VI
        num_list = []
        for l in s:
            for i in range(0, len(rm)):
                if l == rm[i]:
                    num_list.append(nm[i])
                
        num_list.append(0)
        
        # answer variable
        ans=0
        for n in range(0,len(num_list)-1):
            if num_list[n] < num_list[n+1]:
                ans -= num_list[n]
            else:
                ans += num_list[n]
            
        return ans

        
        """
        :type s: str
        :rtype: int
        """
        
```
