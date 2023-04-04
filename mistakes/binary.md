#### 20230403

ver 1

```c
int search(int* nums, int numsSize, int target){
    /* nums: array, numSize, target
    output: the index of target if in nums array
    
    binary search: middle, cut half, middle
    loop
    
    [-1,0,3,5,9,12]
    mid = 3
    nums[3] = 5
    5 < 9
    mid = mid + ((numsSize - mid) / 2) = 3 + (3 / 2) = 4
    nums[4] = 9
    
    target = 9
    
    5 > 2
    mid = 3 / 2 + 1
    mid = mid - 
    target = 2
    
    
    
    */
    
    // initialization: middle number, newArray
    int mid = numsSize / 2; 
    
    while (mid > 0) {
        if (target > nums[mid]) {
            mid = mid + ((numsSize - mid) / 2);
        }
        else if (target < nums[mid]) {
            mid = mid - (numsSize / 2);
        }
        else if (target == nums[mid]) {
            return mid;
        }
        else if (target < nums[mid] || target > nums[mid]) {
            return -1;
        }
    }
    
    return 0;
}
```

ver 2

```c
int search(int* nums, int numsSize, int target){
    
    /* nums: array, numSize, target
    output: the index of target if in nums array
    
    binary search: middle, cut half, middle
    loop
    */
    
    int mid = numsSize / 2;
    
    while (numsSize > 1) {
        printf("%i %i\n", mid, numsSize);
        if (target > nums[mid]) {
            numsSize /= 2;
            mid += numsSize;
            if (mid == numsSize * 2) {
                mid -= 1;
            }
        }
        else if (target < nums[mid]) {
            numsSize /= 2;
            mid -= numsSize;
            if (mid == 0) {
                mid += 1;
            }
        }
        else if (target == nums[mid]) {
            return mid;
        }
    }
    
    if (numsSize == 1) {
        return -1;
    }
    else {
        return 0;
    }
    
}
```

ver 3

```c
int search(int* nums, int numsSize, int target){
    
    /* nums: array, numSize, target
    output: the index of target if in nums array
    
    binary search: middle, cut half, middle
    loop
    */
    
    int mid = numsSize / 2;
    int orig = numsSize;
    
    while (numsSize > 1 && mid != orig) {
        printf("%i %i\n", mid, numsSize);
        if (target > nums[mid]) {
            numsSize /= 2;
            mid += numsSize;
            if (mid == orig) {
                mid -= 1;
            }
        }
        else if (target < nums[mid]) {
            numsSize /= 2;
            mid -= numsSize;
            if (mid == 0) {
                mid += 1;
            }
        }
        else if (target == nums[mid]) {
            return mid;
        }
    }
    
    printf("%i %i %i\n", mid, numsSize, orig);
    
    if (mid == 0 && target == nums[mid]) {
        return 0;
    }
    if (mid > 0) {
        if (target == nums[mid-1]) {
            return mid - 1;
        }
        if (mid < orig) {
            if (target == nums[mid]) {
                return mid;
            }
            else if (target == nums[mid+1]) {
                return mid + 1;
            }
        }
    }
    
    
    return -1;
}
```
