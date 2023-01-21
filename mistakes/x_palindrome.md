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
