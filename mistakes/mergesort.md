#### 20230416
```py

```

#### 20230415
```py
orig_list = [5, 4, 1, 2, 3]
merge_list = []

# Break it down!
def mergesort(input_list):
    
    # Base case
    if len(input_list) < 2:
        return input_list
    
    mid = int(len(input_list) / 2)
    # Create left, right lists
    left_list = []
    right_list = []
    for i in range(0, mid):
        left_list.append(orig_list[i])
    for j in range(mid, len(orig_list)):
        right_list.append(orig_list[j])

    mergesort(left_list)
    mergesort(right_list)
    
# Seperate function to merge left/right halves
def merge():
    pass

# Main()
mergesort(orig_list)
```
