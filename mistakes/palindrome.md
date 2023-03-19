#### 20230114

```python
        x = str(x)
        for i in range(0,len(x)):
            if x[i] == x[len(x) - 1 - i]: # 3 - i
                if i == round(len(x)/2) or x[i] == x[i+1]:
                    return "true"
                else:
                    continue
            else:
                return "false"
```

Harharhar I feel stupid for getting this wrong. And not being able to figure it out.

#### 20230319
```python
class Solution(object):
    
    def isPalindrome(self, x):
        
        if x == 0:
            return True
        elif x < 0 or x % 10 == 0:
            return False
        
        # run half of the integer
        # e.g. x = 12321
        reversed_half = 0
        while reversed_half < x:
            temp = x % 10 # 1, 2, 3
            x /= 10 # 1232, 123, 12
            reversed_half = (reversed_half * 10) + temp # 1, 12, 123
        
        if x == reversed_half or x == reversed_half / 10:
            return True
        else:
            return False
        
        """
        :type x: int
        :rtype: bool
        """
```
Phew. Am I picking it up again?
So I decided to follow tutorials. Try to do the question once, if I can't, watch the tutorial, think it through, close the tab, then do it again. 
Gotta say this solution was genius (tribute to this amazing person [https://www.youtube.com/watch?v=UPdSViixmDs]). I think the lesson I learned was that if they give an integer I should use it instead of turning it into strings.
