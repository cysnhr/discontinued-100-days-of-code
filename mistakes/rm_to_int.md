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
